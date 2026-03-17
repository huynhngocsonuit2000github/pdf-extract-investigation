from docstrange import DocumentExtractor
import time

start_time = time.time()
            
extractor = DocumentExtractor(cpu=True)

result = extractor.extract("sample-123.pdf")

# EXTRACT TEXT LOCAL MODE.... 1 PAGE
text = result.extract_data() 

elapsed_time = time.time() - start_time
print(f"✅ SUCCESS: Elapsed: {elapsed_time:.3f}s") 