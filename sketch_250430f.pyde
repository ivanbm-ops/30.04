x=30
y=30
def setup():
    size(800,800)
def draw():
    global x,y
    background(0)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(400,400,x,y)
    if mouseButton==LEFT:
        x=x+1
        y=y+1
    elif mouseButton==RIGHT:
        x=x-1
        y=y-1
        
