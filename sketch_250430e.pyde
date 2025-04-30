x=360
def setup():
    size(800,800)
    rectMode(CENTER)
def draw():
    global x
    background(0)
    translate(400,400)
    rotate(radians(x))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(0,0,400,470)
    fill(random(0,255),random(0,255),random(0,255))
    rect(0,0,250,250)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(0,0,125,155)
    frameRate(30)
    if mouseButton==LEFT:
        x=x+1
    elif mouseButton==RIGHT:
        x=x-1
    
    
    
