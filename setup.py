from sourcekitd.request import syntax_annotate_text
text = "struct MyStruct {}"
resp = syntax_annotate_text(text)
print(resp)

