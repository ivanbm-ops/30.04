x=100
def setup():
    size(800,800)
def draw():
    global x
    background(0)
    ellipse(x,400,50,50)
    if mouseButton == LEFT:
        x=x+1
