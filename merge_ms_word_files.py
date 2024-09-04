import os
from docx import Document


def insert_page_break(doc):
    """Insert a page break in the document."""
    doc.add_page_break()


def combine_word_documents(output_path, input_files):
    # Create a new Document object for the combined document
    combined_doc = Document()

    for index, file in enumerate(input_files):
        sub_doc = Document(file)

        # Add a page break before each new document, except the first one
        if index != 0:
            insert_page_break(combined_doc)

        # Iterate through elements in the document and add them to the combined document
        for element in sub_doc.element.body:
            combined_doc.element.body.append(element)

    # Save the combined document to the specified path
    combined_doc.save(output_path)


def get_word_files_from_directory(directory):
    """Get a list of all Word files in the given directory."""
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.docx')]
    return sorted(files)  # Sort the files alphabetically


# Usage
directory_path = '/Users/patescalona/Library/CloudStorage/OneDrive-Personal/Marketing Reports/CCR Reports/Centerpoint Energy/CNP Outage Tracker In Depth Interviews/Original/CNP Outage Tracker IDI Transcripts'  # Replace with the path to your directory
output_file = 'combined_document.docx'

# Get the list of Word files in the directory
word_files = get_word_files_from_directory(directory_path)

# Combine the documents
combine_word_documents(output_file, word_files)
