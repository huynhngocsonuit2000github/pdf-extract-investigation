from docstrange import DocumentExtractor
import time

start_time = time.time()
            
extractor = DocumentExtractor(cpu=True)

# result = extractor.extract("test-docx1/sample-1.docx") 
result = extractor.extract("sample.docx") 

# case 1
# text = result.extract_data()

# case 2
text = result.extract_data()


print(text)
elapsed_time = time.time() - start_time
print(f"✅ SUCCESS: Elapsed: {elapsed_time:.3f}s") 