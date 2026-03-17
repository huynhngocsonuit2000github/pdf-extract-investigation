from docstrange import DocumentExtractor
import time

start_time = time.time()
            
extractor = DocumentExtractor(cpu=True)

result = extractor.extract("sample-1 1.docx") 

text = result.extract_data(specified_fields=[
    "Heading 2",
])
 

print(text)
elapsed_time = time.time() - start_time
print(f"✅ SUCCESS: Elapsed: {elapsed_time:.3f}s") 