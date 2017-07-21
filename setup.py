from sourcekitd import request
text = "struct MyStruct {}"
resp = request.syntax_annotate_text(text)
print(resp)

