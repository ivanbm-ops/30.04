def setup():
    size(800,600)
def draw():
    ellipse(random(0,800),random(0,800),40,40)
    if mousePressed:
        background(0)
