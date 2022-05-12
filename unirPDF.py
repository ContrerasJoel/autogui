from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['./Declaracion.pdf',
'./Declaracion (1).pdf',
'./Declaracion (2).pdf',
'./Declaracion (3).pdf',
'./Declaracion (4).pdf',
'./Declaracion (5).pdf',
'./Declaracion (6).pdf',
'./Declaracion (7).pdf',
'./Declaracion (8).pdf',
'./Declaracion (9).pdf',
'./Declaracion (10).pdf',
'./Declaracion (11).pdf',
'./Declaracion (12).pdf',
'./Declaracion (13).pdf',
'./Declaracion (14).pdf',
'./Declaracion (15).pdf',
'./Declaracion (16).pdf',
'./Declaracion (17).pdf',
'./Declaracion (18).pdf',
'./Declaracion (19).pdf',
'./Declaracion (20).pdf',
'./Declaracion (21).pdf',
'./Declaracion (22).pdf',
'./Declaracion (23).pdf',
'./Declaracion (24).pdf',
'./Declaracion (25).pdf',
'./Declaracion (26).pdf',
'./Declaracion (27).pdf',
'./Declaracion (28).pdf',
'./Declaracion (29).pdf',
'./Declaracion (30).pdf',
'./Declaracion (31).pdf',
'./Declaracion (32).pdf',
'./Declaracion (33).pdf',
'./Declaracion (34).pdf',
'./Declaracion (35).pdf',
'./Declaracion (36).pdf',
'./Declaracion (37).pdf',
'./Declaracion (38).pdf',
'./Declaracion (39).pdf',
'./Declaracion (40).pdf',
'./Declaracion (41).pdf',
'./Declaracion (42).pdf',
'./Declaracion (43).pdf',
'./Declaracion (44).pdf',
'./Declaracion (45).pdf',
'./Declaracion (46).pdf',
'./Declaracion (47).pdf',
'./Declaracion (48).pdf',
'./Declaracion (49).pdf',
'./Declaracion (50).pdf',
'./Declaracion (51).pdf',
'./Declaracion (52).pdf',
'./Declaracion (53).pdf',
'./Declaracion (54).pdf',
'./Declaracion (55).pdf',
'./Declaracion (56).pdf',
'./Declaracion (57).pdf',
'./Declaracion (58).pdf',
'./Declaracion (59).pdf',
'./Declaracion (60).pdf',
'./Declaracion (61).pdf',
'./Declaracion (62).pdf',
'./Declaracion (63).pdf',
'./Declaracion (64).pdf'
]
    merge_pdfs(paths, output='union.pdf')