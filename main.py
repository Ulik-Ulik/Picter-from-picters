import os
from PIL import Image
import math


class PfP:
    def __init__(self, main_img, size):

        self.main_img = Image.open(main_img)
        self.width, self.height = self.main_img.size

        self.size = size
        self.main_img = self.main_img.resize(self.pic_up_size())

        self.perm_width, self.perm_height = size, size
        # print(self.perm_width, self.perm_height)

        self.adr = r".\pct"
        self.names = os.listdir(self.adr)

        self.photos = []
        self.pruning()
        self.colors = self.colorization(self.photos)

        self.components = []
        self.compilation()
        self.components_colors = self.colorization(self.components)


        self.result_img = Image.new('RGB', self.pic_up_size())



    def pic_up_size(self):
        h = 0
        w = 0
        while h < self.height:
            h += self.size
        h -= self.size
        while w < self.width:
            w += self.size
        w -= self.size
        return w, h

    def pruning(self):
        for i in self.names:
            self.photos.append(Image.open(os.path.join(self.adr, i)).resize((self.size, self.size)))
        # print(self.photos)

    def colorization(self, par):
        res = []
        for i in par:
            res.append(i.resize((1, 1)).getpixel((0, 0)))
        return res

    def compilation(self):
        for y in range(0, self.height-self.perm_height, self.perm_height):
            for x in range(0, self.width-self.perm_height, self.perm_width):
                self.components.append(self.main_img.crop((x, y, x + self.perm_width, y + self.perm_width)), )

    def make_picter(self):

        step_x = 0
        step_y = 0
        for um in self.components_colors:
            appr_img = self.photos[0]
            temp = 765.0
            for i, img in zip(self.colors, self.photos):
                res = ((um[0] - i[0]) ** 2 + (um[1] - i[1]) ** 2 + (um[2] - i[2]) ** 2) ** (1 / 2)
                if res < temp:
                    appr_img = img
                    temp = res

            for y in range(self.size):
                for x in range(self.size):
                    try:
                        self.result_img.putpixel((x + step_x * self.size, y + step_y * self.size),
                                                 appr_img.getpixel((x, y)))
                    except:
                        pass
                        # print('пытается поставить пиксель на', (x + step_x * self.size, y + step_y* self.size))
                        # print(self.result_img.size)
                        # print('ДА КАКОГО ХУЯ РАЗМЕР ГОТОВОГО ИЗОБРАЖЕНИЯ ИЗМЕНЯЕТСЯ Я НЕ ПОНИМААААЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮ, ТАК ЖЕ НЕ РАБОТАЕТ ПУТПИКСЕЛЬААААААААААААААААААААААААА')
            step_x += 1
            if step_x == self.result_img.width // self.size:
                #print(self.result_img.width)
                #print(step_x)
                step_x = 0
                step_y += 1
    def save_result(self):
        self.result_img.save('result.jpg')
        self.result_img.show()



if __name__ == '__main__':
    p = PfP("original.jpg", 10)

    p.make_picter()
    p.save_result()
