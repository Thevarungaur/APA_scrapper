import os
import google.auth
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import scholarly
import time

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def read_titles_from_google_docs(doc_id):
    creds = authenticate()
    service = build('docs', 'v1', credentials=creds)
    document = service.documents().get(documentId=doc_id).execute()
    titles = []
    for element in document.get('body').get('content'):
        if 'paragraph' in element:
            for run in element['paragraph']['elements']:
                if 'textRun' in run and 'content' in run['textRun']:
                    text = run['textRun']['content'].strip()
                    if text:  # Avoid empty paragraphs
                        titles.append(text)
    return titles

def search_google_scholar(title):
    try:
        search_query = scholarly.search_pubs(title)
        result = next(search_query, None)
        return result
    except Exception as e:
        print(f"Error searching for title '{title}': {e}")
        return None

def format_apa_citation(scholar_article):
    if not scholar_article:
        return "No result found"
    
    authors = scholar_article.bib.get('author', 'No author').replace(',', '')
    year = scholar_article.bib.get('year', 'n.d.')
    title = scholar_article.bib.get('title', 'No title')
    journal = scholar_article.bib.get('journal', 'No journal')
    volume = scholar_article.bib.get('volume', '')
    pages = scholar_article.bib.get('pages', '')
    doi = scholar_article.bib.get('doi', '')

    apa_citation = f"{authors} ({year}). {title}. {journal}, {volume}, {pages}. {doi}"
    return apa_citation

def append_to_file(file_path, citations):
    with open(file_path, 'a') as f:
        for citation in citations:
            f.write(citation + '\n')

def main(doc_id, output_file):
    titles = read_titles_from_google_docs(doc_id)
    citations = []

    for title in titles:
        article = search_google_scholar(title)
        if article:
            apa_citation = format_apa_citation(article)
        else:
            apa_citation = f"Error: No result found for '{title}'"
        citations.append(apa_citation)
        time.sleep(1)  # To avoid rate limiting

    append_to_file(output_file, citations)

if __name__ == "__main__":
    doc_id = "YOUR_GOOGLE_DOC_ID"  # Replace with your actual Google Docs ID
    output_file = "apa_citations.txt"
    main(doc_id, output_file)
