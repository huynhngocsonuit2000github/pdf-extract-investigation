from docstrange import DocumentExtractor

extractor = DocumentExtractor(cpu=True)

result = extractor.extract("sample-data/sample-1.pdf")

text = result.extract_text()

print(text)