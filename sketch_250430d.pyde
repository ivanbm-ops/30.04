def setup():
    size(800,800)
def draw():
    background(0)
    if mouseButton==LEFT:
      fill(255,173,72)
      ellipse(400,400,300,280)
      ellipse(360,380,40,40)
      ellipse(450,380,40,40)
      ellipse(380,450,60,30)
    elif mouseButton==RIGHT:
        ellipse(500,500,250,260)
        ellipse(480,480,50,50)
        ellipse(430,480,50,50)
