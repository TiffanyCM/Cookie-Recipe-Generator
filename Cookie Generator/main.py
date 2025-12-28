import sys
import random
import itertools
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,QWidget, QPushButton, QStackedWidget,QTextBrowser
from PyQt6.QtGui import QIcon, QPixmap, QFont, QFontDatabase
from PyQt6.QtCore import QSize, Qt, QUrl
from cookie_links import *
from cookie_images_paths import *

cookie_list_file = "read files\CookieList.txt"
cookie_description_file = "read files\CookieDescription.txt"
cookies_generated = []


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.load_font()

        self.setWindowTitle("Cookie Generator")
        self.setGeometry(300,100,500,800)

        self.central = QWidget(self)
        self.setCentralWidget(self.central)

        self.page1 = self.main_menu()
        self.page2 = self.cookie_generated()
        self.page3 = self.view_all_cookies()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)

        self.setCentralWidget(self.stack)
        
        self.cookie_gen_num = 0
        self.last_cookie_gen = None

    def load_font(self):
        
        font_id = QFontDatabase.addApplicationFont(
            "SugarFlareDemoRegular-4nGED.otf"
        )

        self.font_family = QFontDatabase.applicationFontFamilies(font_id)[0]


    def main_menu(self):

        page = QWidget()

        background = QLabel(page)
        background.setGeometry(0,0,500,800)
        background_pic = QPixmap("images\Pink_background_circle.png")
        background.setPixmap(background_pic)
        background.setScaledContents(True)
        background.lower()

        main_cookie = QLabel(page)
        main_cookie.setGeometry(100,120,300,300)
        main_cookie_pic = QPixmap("images\Cookie_image.png")
        main_cookie.setPixmap(main_cookie_pic)
        main_cookie.setScaledContents(True)

        cookie_title = QLabel("Cookie Recipe Generator", page)
        cookie_title.setGeometry(10,0,500,100)
        cookie_title.setStyleSheet("color: #6D4E56")
        cookie_title.setFont(QFont(self.font_family, 34))

        self.cookie_gen_button = QPushButton("Generate a cookie recipe!",page)
        self.cookie_gen_button.setGeometry(10,500,480,100)
        self.cookie_gen_button.setFont(QFont(self.font_family,28))
        self.cookie_gen_button.setStyleSheet("color: #FFFFFF;" 
                                            "background-color: #6D4E56;"
                                            "border-radius: 20px;"
                                            "padding: 8px;")
                                            
        self.view_all_cookie_types_button = QPushButton("View all cookie types", page)
        self.view_all_cookie_types_button.setGeometry(10,630,480,100)
        self.view_all_cookie_types_button.setFont(QFont(self.font_family,28))
        self.view_all_cookie_types_button.setStyleSheet("color: #FFFFFF;" 
                                            "background-color: #6D4E56;"
                                            "border-radius: 20px;"
                                            "padding: 8px;")
                                            
        self.cookie_gen_button.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.view_all_cookie_types_button.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        

        self.cookie_gen_button.clicked.connect(self.generated_cookie)
        self.view_all_cookie_types_button.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        return page
    
    def generated_cookie(self, cookie_id = None):

        if cookie_id is not None:

            self.cookie_id = cookie_id

        else:
            self.cookie_id = random.randint(1, 29)

        if self.cookie_id < 1:
            self.cookie_id = 1

            if self.cookie_gen_num > 0 and self.cookie_id == self.last_cookie_gen:

                self.cookie_id = random.randint(1, 29)

        self.cookie_gen_num += 1

        if self.cookie_gen_num > 1 and self.cookie_id == self.last_cookie_gen:

            self.cookie_id = random.randint(1,29)

            self.cookie_gen_num = 0

        self.last_cookie_gen = self.cookie_id

        self.cookie_id_image = cookie_img_path_list[self.cookie_id - 1]
        self.cookie_id_image = QPixmap(self.cookie_id_image)

        self.cookie_image.setPixmap(self.cookie_id_image)

        recipe = cookie_recipe[self.cookie_id - 1]
        cookie_hyperlink_list = []
        cookie_hyperlink_recipe_name = []


        with open (cookie_list_file, "r") as file:
            
            for line in itertools.islice(file, self.cookie_id - 1, self.cookie_id):

                cookie_name_string = line.strip().split(".", 1)[1]

                break

        for cookie,hyperlink in recipe.items():

            cookie_hyperlink_list.append(hyperlink)
            cookie_hyperlink_recipe_name.append(cookie)
        
        self.cookie_chosen = cookie_name_string
        self.cookie_name_label.setText(self.cookie_chosen)

        self.cookie_hyperlink_display_list = cookie_hyperlink_list

        if len(self.cookie_hyperlink_display_list) == 1:

            self.recipe_link1.setText(f'<a href="{cookie_hyperlink_list[0]}" style=color:{"#6D4E56"}>'f'{"1. " + cookie_hyperlink_recipe_name[0]}</a>')

        elif len(self.cookie_hyperlink_display_list) == 2:

            self.recipe_link1.setText(f'<a href="{cookie_hyperlink_list[0]}" style=color:{"#6D4E56"}>'f'{"1. " + cookie_hyperlink_recipe_name[0]}</a>')

            self.recipe_link2.setText(f'<a href="{cookie_hyperlink_list[1]}" style=color:{"#6D4E56"}>'f'{"2. " + cookie_hyperlink_recipe_name[1]}</a>')

        elif len(self.cookie_hyperlink_display_list) == 3:

            self.recipe_link1.setText(f'<a href="{cookie_hyperlink_list[0]}" style=color:{"#6D4E56"}>'f'{"1. " + cookie_hyperlink_recipe_name[0]}</a>')

            self.recipe_link2.setText(f'<a href="{cookie_hyperlink_list[1]}" style=color:{"#6D4E56"}>'f'{"2. " + cookie_hyperlink_recipe_name[1]}</a>')


            self.recipe_link3.setText(f'<a href="{cookie_hyperlink_list[2]}" style=color:{"#6D4E56"}>'f'{"3. " + cookie_hyperlink_recipe_name[2]}</a>')



    def cookie_generated(self):

        page = QWidget()
        browser = QTextBrowser()

        background = QLabel(page)
        background.setGeometry(0,0,500,800)
        background_pic = QPixmap("images\pink_background.jpg")
        background.setPixmap(background_pic)
        background.setScaledContents(True)
        background.lower()

        pixmap = QPixmap("images\Back_arrow.png")
        back_button_image = QIcon(pixmap)
        self.back_button = QPushButton("",page)
        self.back_button.setIcon(back_button_image)
        self.back_button.setIconSize(QSize(75, 75))
        self.back_button.setGeometry(0,90,75,100)

        self.back_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        self.cookie_name_label = QLabel("",page)
        self.cookie_name_label.setWordWrap(True)
        self.cookie_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        self.cookie_name_label.setGeometry(10,0,500,110)
        self.cookie_name_label.setStyleSheet("color: #6D4E56")
        self.cookie_name_label.setFont(QFont(self.font_family, 34))

        self.cookie_image = QLabel(page)
        self.cookie_image.setGeometry(100,120,300,300)
        self.cookie_image.setScaledContents(True)



        self.cookie_id = random.randint(1, 29)
        self.cookie_id_image = QPixmap(cookie_img_path_list[self.cookie_id - 1])

        self.recipe_links_box = QLabel("",page)
        self.recipe_links_box.setGeometry(10,450,480,230)
        self.recipe_links_box.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.recipe_links_box.setStyleSheet("background-color : #FFFFFF;"
                                            "color: black;"
                                            "border: 10px solid #6D4E56;"
                                            "border-radius: 20px;")
        
        self.recipes_title = QLabel("Recipe Links", page)
        self.recipes_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.recipes_title.setGeometry(150,430,200,100)
        self.recipes_title.setFont(QFont(self.font_family,24))
        self.recipes_title.setStyleSheet("color: #6D4E56;")
        
        
        self.recipe_link1 = QLabel("", page)
        self.recipe_link1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.recipe_link1.setWordWrap(True)
        self.recipe_link1.setGeometry(30,500,460,100)
        self.recipe_link1.setFont(QFont(self.font_family,16))
        self.recipe_link1.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.recipe_link1.setOpenExternalLinks(True)
        self.recipe_link1.raise_()

        self.recipe_link2 = QLabel("", page)
        self.recipe_link2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.recipe_link2.setWordWrap(True)
        self.recipe_link2.setGeometry(30,560,460,100)
        self.recipe_link2.setFont(QFont(self.font_family,16))
        self.recipe_link2.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.recipe_link2.setOpenExternalLinks(True)
        self.recipe_link2.raise_()

        self.recipe_link3 = QLabel("", page)
        self.recipe_link3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.recipe_link3.setWordWrap(True)
        self.recipe_link3.setGeometry(30,620,460,100)
        self.recipe_link3.setFont(QFont(self.font_family,16))
        self.recipe_link3.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.recipe_link3.setOpenExternalLinks(True) 
        self.recipe_link3.raise_()       

        self.new_cookie_gen_button = QPushButton("Generate a new cookie recipe!",page)
        self.new_cookie_gen_button.setGeometry(10,700,480,80)
        self.new_cookie_gen_button.setFont(QFont(self.font_family,26))
        self.new_cookie_gen_button.setStyleSheet("color: #FFFFFF;" 
                                            "background-color: #6D4E56;"
                                            "border-radius: 20px;"
                                            "padding: 8px;")
        

        self.new_cookie_gen_button.clicked.connect(self.generated_a_new_cookie)
                                        
        return page
    
    def generated_a_new_cookie(self):

        self.generated_cookie()


    def form_button_for_view_all(self,name,cookie_id,x_axis,y_axis,page):


        self.cookie_button = QPushButton(name,page)
        self.cookie_button.setGeometry(x_axis,y_axis,250,30)
        self.cookie_button.setStyleSheet("color: #6D4E56") 
        self.cookie_button.setFont(QFont(self.font_family, 18))
        

        self.cookie_id = cookie_id


        self.cookie_button.clicked.connect(lambda _, cid=cookie_id: (
            self.stack.setCurrentIndex(1),
            self.generated_cookie(cid)
        ))


    def view_all_cookies(self):

        page = QWidget()

        background = QLabel(page)
        background.setGeometry(0,0,500,800)
        background_pic = QPixmap("images\pink_background.jpg")
        background.setPixmap(background_pic)
        background.setScaledContents(True)
        background.lower()

        self.all_cookies_label = QLabel("All Cookie Types",page)

        self.all_cookies_label.setWordWrap(True)
        self.all_cookies_label.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        self.all_cookies_label.setGeometry(10,-10,500,110)
        self.all_cookies_label.setStyleSheet("color: #6D4E56")
        self.all_cookies_label.setFont(QFont(self.font_family, 34))

        self.all_cookies_directions_label = QLabel("Click the type of cookie to view the recipes",page)

        self.all_cookies_directions_label.setWordWrap(True)
        self.all_cookies_directions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)        
        self.all_cookies_directions_label.setGeometry(10,60,500,110)
        self.all_cookies_directions_label.setStyleSheet("color: #6D4E56")
        self.all_cookies_directions_label.setFont(QFont(self.font_family, 20))

        pixmap = QPixmap("images\Back_arrow.png")
        back_button_image = QIcon(pixmap)
        self.back_button = QPushButton("",page)
        self.back_button.setIcon(back_button_image)
        self.back_button.setIconSize(QSize(75, 75))
        self.back_button.setGeometry(0,90,75,100)
        self.back_button.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        self.form_button_for_view_all("Biscotti",11,20,200, page)
        self.form_button_for_view_all("Black and White", 27,20, 230, page)
        self.form_button_for_view_all("Butter", 12, 20,260, page)
        self.form_button_for_view_all("Chocolate Chip", 2, 20, 290, page)
        self.form_button_for_view_all("Crinkle", 21, 20, 320, page)
        self.form_button_for_view_all("Crescent", 29, 20, 350, page)
        self.form_button_for_view_all("Drop", 15, 20, 380, page)
        self.form_button_for_view_all("Fortune", 20, 20, 410, page)
        self.form_button_for_view_all("Gingerbread", 23, 20, 440, page)
        self.form_button_for_view_all("Gingersnap", 4, 20, 470, page)
        self.form_button_for_view_all("Icebox", 22, 20, 500, page)
        self.form_button_for_view_all("Kiss", 10, 20, 530, page)
        self.form_button_for_view_all("Lebkuchen", 25, 20, 560, page)
        self.form_button_for_view_all("Macadamia Nut", 28, 20, 590, page)  

        self.form_button_for_view_all("Macaron", 26, 270, 200, page)
        self.form_button_for_view_all("Macaroon", 19, 270, 230, page)
        self.form_button_for_view_all("Molasses", 9, 270,260, page)
        self.form_button_for_view_all("Oatmeal Raisin", 3, 270, 290, page)
        self.form_button_for_view_all("Peanut Butter", 6, 270, 320, page)
        self.form_button_for_view_all("Pinwheel", 17, 270, 350, page)
        self.form_button_for_view_all("Shortbread", 5, 270, 380, page)
        self.form_button_for_view_all("Snowball", 14, 270, 410, page)
        self.form_button_for_view_all("Snickerdoodle", 1, 270, 440, page)
        self.form_button_for_view_all("Spritz", 13, 270, 470, page)
        self.form_button_for_view_all("Sugar", 8, 270, 500, page)
        self.form_button_for_view_all("Tassie", 24, 270, 530, page)
        self.form_button_for_view_all("Thumbprint", 16, 270, 560, page)
        self.form_button_for_view_all("Wafer", 18, 270, 590, page)
        self.form_button_for_view_all("Whoopie Pie", 7, 125, 620, page)          
                                


        return page





def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":

    main()    