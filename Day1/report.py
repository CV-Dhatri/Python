import os
import subprocess
from docx import Document
from docx.shared import Pt

# Create a new Word document
doc = Document()

# Root folder containing your tasks
root_folder = r"D:\Dhatri\Python\Python Tasks 1"

# Walk through all subfolders
for folder, _, files in os.walk(root_folder):
    for file in files:
        if file.endswith(".py") and file != "report.py":  # skip this script itself
            file_path = os.path.join(folder, file)

            # Add heading for the file
            doc.add_heading(file, level=1)

            # Read and add code
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
            doc.add_paragraph("Program Code:")
            code_para = doc.add_paragraph(code)
            code_para.style.font.name = "Courier New"  # monospaced font
            code_para.style.font.size = Pt(10)

            # Run the file and capture output
            try:
                result = subprocess.run(
                    ["c:\\python314\\python.exe", file_path],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output = result.stdout.strip() if result.stdout else "No output"
            except Exception as e:
                output = f"Error running file: {e}"

            # Add output to document
            doc.add_paragraph("Program Output:")
            output_para = doc.add_paragraph(output)
            output_para.style.font.name = "Courier New"
            output_para.style.font.size = Pt(10)

# Save the Word document
doc.save("All_Tasks_Report.docx")
print("Report created successfully!")
