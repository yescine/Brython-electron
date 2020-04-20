from browser import document,console ,alert
 
def echo(event):
   alert(document["zone"].value)

def show(e):
   console.log('hello')


document['mybutton'].bind('click', show)
# document['mybutton'].bind('click', echo)
