from fpdf import FPDF    # 1. Importing the 'Blueprint' tool
import os                # 2. Importing the 'System' tool

def create_diary_pdf(title, content): # 3. Defining your custom machine
    pdf = FPDF()         # 4. Creating the blank page object
    pdf.add_page()       # 5. Adding the page to the PDF
    
    # Setting the Header (The Title)
    pdf.set_font("Arial", 'B', 16) # 6. Setting font style to BOLD
    pdf.cell(200, 10, txt=title, ln=True, align='C') # 7. Placing the title
    pdf.ln(10)           # 8. Adding some empty space (a line break)
    
    # Setting the Body (Your thoughts)
    pdf.set_font("Arial", size=12) # 9. Setting font size to 12
    pdf.multi_cell(0, 10, txt=content) # 10. Placing the big text block
    
    # Folder Logic
    folder = "diary_vault"
    if not os.path.exists(folder): # 11. Does the vault exist?
        os.makedirs(folder)        # 12. If not, build the vault!
    
    # Saving the File
    filepath = os.path.join(folder, f"{title}.pdf") # 13. Naming the file
    pdf.output(filepath) # 14. Saving the file to your phone
    print(f"✅ Diary entry saved: {filepath}") # 15. The 'Success' message

# The Interface
t = input("Enter Title: ") # 16. Ask you for a title
c = input("Enter Content: ") # 17. Ask you for the content
create_diary_pdf(t, c) # 18. Fire up the machine
