#!/bin/python3

import cgi

page = """<!DOCTYPE html>
<html>
    <body>
    <h1>Calculatrice</h1>
    <form action="calc.py" method="post">
        <input type="text" name="formule" value="" />
        <input type="submit" name="calc" value="Calculer">
    </form>
    </body>
</html>"""

print("Content-Type: text/html; charset=utf-8\n")
print(page)

data = cgi.FieldStorage()

calc = data.getvalue('formule')
if calc:
    print("the answer is : ", eval(calc))