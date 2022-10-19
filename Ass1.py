import cv2
import time
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Dhanesh.avi', fourcc, 20.0, (640,480))
start=0
br=False
st=None
def mouse_click(event,x,y,flags,params):
    global br
    if event==cv2.EVENT_RBUTTONDOWN:
        l = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH )/2)
        r = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT )/2)
        pa={'w1':l-40,'w2':l+40,'h1':r-20,'h2':r+20}
        if (y>=pa['h1'] and y<=pa['h2']) and (x>=pa['w1'] and x<=pa['w2']):
            br=True

while True:
    ret,frame=cap.read()
    if(st and time.time()-st>=5):
        x = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH )/2)
        y = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT )/2)
        frame=cv2.rectangle(frame, pt1=(x-40, y+20), pt2=(x+40, y-20), color=(0, 0,255 ), thickness=-1)
        font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        frame= cv2.putText(frame, 'Dhanesh',(x-28,y+5), font, 
                   0.5, (255,255,255),1, cv2.LINE_AA)
    cv2.imshow("Your Face",frame)
    cv2.setMouseCallback('Your Face',mouse_click)
    if br:
        break
    if cv2.waitKey(1)==ord('d'):
        st=time.time()
        start=1
    if(start):
        out.write(frame)
out.release()
cap.release()
cv2.destroyAllWindows()