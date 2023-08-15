#programa que busca las etiquetas de un html
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

parser = MyHTMLParser()
for _ in range(int(input("Introduce el numero de lineas y las etiquetas separasdas por un enter: "))):
    parser.feed(input())

"""9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>"""