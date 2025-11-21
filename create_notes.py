import os
import shutil
import re
from PyPDF2 import PdfReader, PdfMerger

#------------------------------------------------------------------------------------------------------------------
# Function to collect all PDFs from "notes/pdf" subfolders into "NOTES" folder
#------------------------------------------------------------------------------------------------------------------
def collect_pdfs(base_folder, ):
    # Folder where all PDFs will be collected
    allnotes_folder = os.path.join(base_folder, "NOTES")
    os.makedirs(allnotes_folder, exist_ok=True)

    # Walk through all subfolders and Check if current path ends with "notes/pdf"
    for root, dirs, files in os.walk(base_folder):
        if os.path.basename(root).lower() == "pdfs" and os.path.basename(os.path.dirname(root)).lower() == "notes":
            for file in files:
                if file.lower().endswith(".pdf"):
                    src = os.path.join(root, file)
                    dest = os.path.join(allnotes_folder, file)

                    # Handle duplicate file names by renaming
                    if os.path.exists(dest):
                        name, ext = os.path.splitext(file)
                        counter = 1
                        while os.path.exists(dest):
                            dest = os.path.join(allnotes_folder, f"{name}_{counter}{ext}")
                            counter += 1

                    shutil.copy2(src, dest)  # copy with metadata
                    print(f"Copied: {src} -> {dest}")

    print(f"\n✅ All PDFs collected in: {allnotes_folder}")


#------------------------------------------------------------------------------------------------------------------
# Function to extract chapter numbers
#------------------------------------------------------------------------------------------------------------------
def extract_chapter_number(pdf_path):
    """
    Extract chapter number like 3.1 from the first page of a PDF.
    Returns float('inf') if not found to sort at the end.
    """
    try:
        reader = PdfReader(pdf_path)
        first_page = reader.pages[0]
        text = first_page.extract_text()

        if text:
            # Regex to match "Chapter X.Y"
            match = re.search(r"Chapter\s+(\d+(?:\.\d+)?)", text)
            if match:
                return float(match.group(1))  # convert to number for sorting
    except Exception as e:
        print(f"⚠️ Could not read {pdf_path}: {e}")
    return float("inf")  # put unreadable PDFs at end


#------------------------------------------------------------------------------------------------------------------
# Function to combine PDFs in order of chapter numbers
#------------------------------------------------------------------------------------------------------------------
def combine_pdfs(allnotes_folder, output_file="1_Python_Notes.pdf"):
    pdf_files = [
        os.path.join(allnotes_folder, f)
        for f in os.listdir(allnotes_folder)
        if f.lower().endswith(".pdf")
    ]

    # Extract chapter numbers and sort
    pdfs_with_chapters = [(f, extract_chapter_number(f)) for f in pdf_files]
    pdfs_with_chapters.sort(key=lambda x: x[1])

    # Merge PDFs
    merger = PdfMerger()
    for pdf, chap in pdfs_with_chapters:
        merger.append(pdf)
        print(f"Added {os.path.basename(pdf)} (Chapter {chap})")

    output_path = os.path.join(allnotes_folder, output_file)
    merger.write(output_path)
    merger.close()

    print(f"\n✅ Combined PDF saved as: {output_path}")

# Example usage
if __name__ == "__main__":
    base_path = r"topics"  # adjust path
    print("Collecting PDFs...")
    collect_pdfs(base_path)
    print("\nCombining PDFs...")
    combine_pdfs(os.path.join(base_path, "NOTES"))
    
