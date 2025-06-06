import pandas as pd
from fpdf import FPDF

class ReportGenerator:
    def generate_pdf(self, data, period):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Reporte de Nómina ({period})", ln=1, align='C')
        
        for item in data:
            pdf.cell(200, 10, 
                    txt=f"{item['employee']}: ${item['total']} ({item['events']} eventos)", 
                    ln=1)
        
        pdf.cell(200, 10, txt=f"Total periodo: ${sum(i['total'] for i in data)}", ln=1)
        return pdf.output(dest='S').encode('latin-1')

    def generate_excel(self, data):
        df = pd.DataFrame(data)
        return df.to_excel("report.xlsx", index=False)