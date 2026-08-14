from pathlib import Path
from pypdf import PdfReader

pdf_path = Path(r'Q:\nckh\COTVD\COTVD- A function-level vulnerability detection framework using chain-of-thought reasoning with LLMs.pdf')
out_path = Path(r'Q:\nckh\COTVD\paper_extract.txt')

print('pdf_exists=', pdf_path.exists())
if not pdf_path.exists():
    raise FileNotFoundError(pdf_path)

reader = PdfReader(str(pdf_path))
print('pages=', len(reader.pages))
chunks = []
for i in range(min(20, len(reader.pages))):
    txt = reader.pages[i].extract_text() or ''
    chunks.append(f'--- PAGE {i+1} ---\n{txt}')

out_path.write_text('\n\n'.join(chunks), encoding='utf-8')
print('written=', out_path)
