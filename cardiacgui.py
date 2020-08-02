from PIL import Image


class CardiacDisplay:
    slider1=[-25,-45]
    slider2=[-34,-58,-78,-100,-124,-148,-172,-195,-216,-240]
    slider3=[109,85,61,38,14,-9,-32,-53,-76,-99]
    slider4=[108,87,63,40,18,-4,-28,-51,-75,-96]
    
    def __init__(self):
        self.im=Image.open("cardiac2top.png")
        self.im1=Image.open("slider1a.png")
        self.im2=Image.open("slider2.png")
        self.im3=Image.open("slider3.png")
        self.im4=Image.open("slider4.png")
        self.displayed_image = self.im

    def show(self,s1,s2,s3,s4):
        s1v=self.slider1[s1]
        s2v=self.slider2[s2]
        s3v=self.slider3[s3]
        s4v=self.slider4[s4]
        im1t=self.im1.transform(self.im1.size,Image.AFFINE,(1,0,50,0,1,s1v))
        im2t=self.im2.transform(self.im2.size,Image.AFFINE,(1,0,-356,0,1,s2v))
        im3t=self.im3.transform(self.im3.size,Image.AFFINE,(1,0,-155,0,1,s3v))
        self.displayed_image=self.im4.transform(self.im4.size,Image.AFFINE,(1,0,-280,0,1,s4v))
        self.displayed_image.paste(im3t,(0,0),im3t)
        self.displayed_image.paste(im1t,(0,0),im1t)
        self.displayed_image.paste(im2t,(0,0),im2t)
        self.displayed_image.paste(self.im,(0,0),self.im)
        self.displayed_image.show()

    def get_image(self, s1, s2, s3, s4) -> Image:
        s1v=self.slider1[s1]
        s2v=self.slider2[s2]
        s3v=self.slider3[s3]
        s4v=self.slider4[s4]
        im1t=self.im1.transform(self.im1.size,Image.AFFINE,(1,0,50,0,1,s1v))
        im2t=self.im2.transform(self.im2.size,Image.AFFINE,(1,0,-356,0,1,s2v))
        im3t=self.im3.transform(self.im3.size,Image.AFFINE,(1,0,-155,0,1,s3v))
        self.displayed_image=self.im4.transform(self.im4.size,Image.AFFINE,(1,0,-280,0,1,s4v))
        self.displayed_image.paste(im3t,(0,0),im3t)
        self.displayed_image.paste(im1t,(0,0),im1t)
        self.displayed_image.paste(im2t,(0,0),im2t)
        self.displayed_image.paste(self.im,(0,0),self.im)
        return self.displayed_image

if __name__ == "__main__":
    cd=CardiacDisplay()
    instr=input("Enter 4 values: ")
    values=tuple(map(int,instr.split(',')))
    while (values[0]!=9):
        cd.show(values[0],values[1],values[2],values[3])
        instr=input("Enter 4 values: ")
        values=tuple(map(int,instr.split(',')))


