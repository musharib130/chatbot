from ingestion.pipeline import ingest_pdf  # make sure your structure matches
import os


loc = "C:\personal\Study\Books\Marcus-Aurelius-Meditations.pdf"


if not loc:
    # Ask user for PDF file path
    loc = input("Enter the file path to be added: ").strip()

# Check if path exists and is a file
if not os.path.exists(loc):
    print(f"Error: File '{loc}' does not exist.")
elif not os.path.isfile(loc):
    print(f"Error: '{loc}' is not a file.")
elif not loc.lower().endswith(".pdf"):
    print(f"Error: '{loc}' is not a PDF file.")
else:
    # Ingest the PDF
    vectordb = ingest_pdf(loc)
    print("PDF ingested successfully!")


