from PyQt6.QtWidgets import *
from gui import *
import math

class Logic(QMainWindow, Ui_MainWindow):
    """
    Class used to use the calculator application.
    Houses some class variables.
    """
    nums_in_box = ['~']
    math_function = ''
    nums_for_calculation = []

    def __init__(self) -> None:
        """
        Checks for the buttons the user clicks
        """
        super().__init__()
        self.setupUi(self)

        self.radio_equilateral_cone.setText('Equilateral Tri.')

        self.button_0.clicked.connect(lambda: self.push_0())
        self.button_1.clicked.connect(lambda: self.push_1())
        self.button_2.clicked.connect(lambda: self.push_2())
        self.button_3.clicked.connect(lambda: self.push_3())
        self.button_4.clicked.connect(lambda: self.push_4())
        self.button_5.clicked.connect(lambda: self.push_5())
        self.button_6.clicked.connect(lambda: self.push_6())
        self.button_7.clicked.connect(lambda: self.push_7())
        self.button_8.clicked.connect(lambda: self.push_8())
        self.button_9.clicked.connect(lambda: self.push_9())
        self.button_plus.clicked.connect(lambda: self.plus())
        self.button_subtract.clicked.connect(lambda: self.subtract())
        self.button_multiply.clicked.connect(lambda: self.multiply())
        self.button_divide.clicked.connect(lambda: self.divide())
        self.button_equal.clicked.connect(lambda: self.equal())
        self.radio_area.clicked.connect(lambda: self.area())
        self.radio_volume.clicked.connect(lambda: self.volume())
        self.radio_square_cube.clicked.connect(lambda: self.square_cube())
        self.radio_rectangle_cuboid.clicked.connect(lambda: self.rectangle_cuboid())
        self.radio_circle_sphere.clicked.connect(lambda: self.circle_sphere())
        self.radio_triangle_pyramid.clicked.connect(lambda: self.triangle_pyramid())
        self.radio_equilateral_cone.clicked.connect(lambda: self.equilateral_cone())
        self.radio_hypotenuse_cylinder.clicked.connect(lambda: self.hypotenuse_cylinder())
        self.pushButton_submit.clicked.connect(lambda: self.submit())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_del.clicked.connect(lambda: self.delete())
        self.button_decimal.clicked.connect(lambda: self.decimal())
        self.button_negative.clicked.connect(lambda: self.negative())

# -----------------------------------------------------------------------------
# Checks
    def length_check(self) -> bool:
        """
        Checks the length of the number the user input so that it is not too long
        :return: Boolean value; True if length of number is less than or equal to 26, False if greater than 26
        """
        if len(Logic.nums_in_box) <= 26:
            return True
        else:
            return False

    def box_empty_check(self) -> bool:
        """
        Checks if the spot is empty
        :return: Boolean value; True if the spot is empty, False if the spot is not empty
        """
        if Logic.nums_in_box[0] == '~':
            return True
        else:
            return False

    def area_or_volume_check(self) -> None:
        """
        Checks which of the six area/volume buttons is pressed
        """
        if self.radio_square_cube.isChecked():
            self.square_cube()
        elif self.radio_rectangle_cuboid.isChecked():
            self.rectangle_cuboid()
        elif self.radio_circle_sphere.isChecked():
            self.circle_sphere()
        elif self.radio_triangle_pyramid.isChecked():
            self.triangle_pyramid()
        elif self.radio_equilateral_cone.isChecked():
            self.equilateral_cone()
        elif self.radio_hypotenuse_cylinder.isChecked():
            self.hypotenuse_cylinder()

# -----------------------------------------------------------------
# Calculator Buttons
# ------------------
# Numbers
    def push_0(self) -> None:
        """
        Enters 0 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('0')
            Logic.nums_in_box[0] = '0'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}0')
                Logic.nums_in_box.append('0')

    def push_1(self) -> None:
        """
        Enters 1 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('1')
            Logic.nums_in_box[0] = '1'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}1')
                Logic.nums_in_box.append('1')

    def push_2(self) -> None:
        """
        Enters 2 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('2')
            Logic.nums_in_box[0] = '2'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}2')
                Logic.nums_in_box.append('2')

    def push_3(self) -> None:
        """
        Enters 3 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('3')
            Logic.nums_in_box[0] = '3'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}3')
                Logic.nums_in_box.append('3')

    def push_4(self) -> None:
        """
        Enters 4 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('4')
            Logic.nums_in_box[0] = '4'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}4')
                Logic.nums_in_box.append('4')

    def push_5(self) -> None:
        """
        Enters 5 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('5')
            Logic.nums_in_box[0] = '5'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}5')
                Logic.nums_in_box.append('5')

    def push_6(self) -> None:
        """
        Enters 6 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('6')
            Logic.nums_in_box[0] = '6'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}6')
                Logic.nums_in_box.append('6')

    def push_7(self) -> None:
        """
        Enters 7 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('7')
            Logic.nums_in_box[0] = '7'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}7')
                Logic.nums_in_box.append('7')

    def push_8(self) -> None:
        """
        Enters 8 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('8')
            Logic.nums_in_box[0] = '8'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}8')
                Logic.nums_in_box.append('8')

    def push_9(self) -> None:
        """
        Enters 9 into the calculator
        """
        if self.box_empty_check() == True:
            self.label_calculations.setText('9')
            Logic.nums_in_box[0] = '9'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}9')
                Logic.nums_in_box.append('9')

# ------------------
# Math Functions
    def plus(self) -> None:
        """
        Adds the numbers that the user input
        """
        Logic.math_function = ''
        Logic.nums_for_calculation.append(''.join(Logic.nums_in_box))
        Logic.nums_in_box = ['~']
        if len(Logic.nums_for_calculation) > 1:
            for x in range(0, len(Logic.nums_for_calculation)):
                if Logic.nums_for_calculation[x] == '~':
                    Logic.nums_for_calculation[x] = 0
            Logic.nums_for_calculation = [float(x) for x in Logic.nums_for_calculation]
            Logic.nums_for_calculation[0] = Logic.nums_for_calculation[0] + Logic.nums_for_calculation[1]
            Logic.nums_for_calculation = Logic.nums_for_calculation[:1:]
        Logic.math_function = 'plus'

    def subtract(self) -> None:
        """
        Subtracts the numbers that the user input
        """
        Logic.math_function = ''
        Logic.nums_for_calculation.append(''.join(Logic.nums_in_box))
        Logic.nums_in_box = ['~']
        if len(Logic.nums_for_calculation) > 1:
            for x in range(0, len(Logic.nums_for_calculation)):
                if Logic.nums_for_calculation[x] == '~':
                    Logic.nums_for_calculation[x] = 0
            Logic.nums_for_calculation = [float(x) for x in Logic.nums_for_calculation]
            Logic.nums_for_calculation[0] = Logic.nums_for_calculation[0] - Logic.nums_for_calculation[1]
            Logic.nums_for_calculation = Logic.nums_for_calculation[:1:]
        Logic.math_function = 'subtract'

    def multiply(self) -> None:
        """
        Multiplies the numbers that the user input
        """
        Logic.math_function = ''
        Logic.nums_for_calculation.append(''.join(Logic.nums_in_box))
        Logic.nums_in_box = ['~']
        if len(Logic.nums_for_calculation) > 1:
            for x in range(0, len(Logic.nums_for_calculation)):
                if Logic.nums_for_calculation[x] == '~':
                    Logic.nums_for_calculation[x] = 1
            Logic.nums_for_calculation = [float(x) for x in Logic.nums_for_calculation]
            Logic.nums_for_calculation[0] = Logic.nums_for_calculation[0] * Logic.nums_for_calculation[1]
            Logic.nums_for_calculation = Logic.nums_for_calculation[:1:]
        Logic.math_function = 'multiply'

    def divide(self) -> None:
        """
        Divides the numbers that the user input
        """
        Logic.math_function = ''
        Logic.nums_for_calculation.append(''.join(Logic.nums_in_box))
        Logic.nums_in_box = ['~']
        if len(Logic.nums_for_calculation) > 1:
            for x in range(0, len(Logic.nums_for_calculation)):
                if Logic.nums_for_calculation[x] == '~':
                    Logic.nums_for_calculation[x] = 1
            Logic.nums_for_calculation = [float(x) for x in Logic.nums_for_calculation]
            try:
                Logic.nums_for_calculation[0] = Logic.nums_for_calculation[0] / Logic.nums_for_calculation[1]
            except:
                Logic.nums_for_calculation = ['DBV']
            Logic.nums_for_calculation = Logic.nums_for_calculation[:1:]
        Logic.math_function = 'divide'

    def equal(self) -> None:
        """
        Gives the total
        """
        try:
            if Logic.math_function == 'plus':
                self.plus()
            elif Logic.math_function == 'subtract':
                self.subtract()
            elif Logic.math_function == 'multiply':
                self.multiply()
            elif Logic.math_function == 'divide':
                self.divide()
            if Logic.nums_for_calculation == ['DBV']:
                self.clear()
                self.label_calculations.setText('Cannot Divide by Zero')
            else:
                self.label_calculations.setText(f'= {Logic.nums_for_calculation[0]}')
        except:
            self.clear()

# ------------------
# Additional Buttons

    def clear(self) -> None:
        """
        Clears the calculator
        """
        Logic.nums_in_box = ['~']
        Logic.nums_for_calculation = []
        Logic.math_function = ''
        self.label_calculations.setText('')

    def delete(self) -> None:
        """
        Deletes one number from the calculator
        """
        try:
            if Logic.nums_in_box[0] == '~':
                self.clear()
            else:
                Logic.nums_in_box.pop(-1)
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}')
        except:
            self.clear()

    def decimal(self) -> None:
        """
        Adds a maximum of one decimal in the user's number
        """
        if '.' not in ''.join(Logic.nums_in_box):
            if self.box_empty_check() == True:
                self.label_calculations.setText('0.')
                Logic.nums_in_box[0] = '0.'
            else:
                if self.length_check() == True:
                    self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}.')
                    Logic.nums_in_box.append('.')

    def negative(self) -> None:
        """
        Adds a maximum of one negative in the user's number
        """
        if '-' not in ''.join(Logic.nums_in_box):
            if self.box_empty_check() == True:
                self.label_calculations.setText('-')
                Logic.nums_in_box[0] = '-'
            else:
                if self.length_check() == True:
                    self.label_calculations.setText(f'-{''.join(Logic.nums_in_box)}')
                    Logic.nums_in_box.insert(0, '-')

# ------------------
# Area and Volume
    '''
    s = side, b = base, h = height, w = width, l = length, r = radius, p = pi
    Areas:
        Square: s * s
        Rectangle: b * h
        Circle: p * r^2
        Triangle: (b * h) / 2
        Equilateral Triangle: (sqrt(3) / 4) * s^2
        Hypotenuse: sqrt(b^2 + h^2)
    Volumes:
        Cube: s^3
        Cuboid: l * b * h
        Sphere: (4 / 3) * p * r^3
        Pyramid: (l * w * h) / 3
        Cone: (1 / 3) * p * r^2 * h
        Cylinder: p * r^2 * h
    '''
    def area(self) -> None:
        """
        Sets the text for the 6 buttons when the area button is pushed
        """
        self.radio_square_cube.setText('Square')
        self.radio_rectangle_cuboid.setText('Rectangle')
        self.radio_circle_sphere.setText('Circle')
        self.radio_triangle_pyramid.setText('Triangle')
        self.radio_equilateral_cone.setText('Equilateral Tri.')
        self.radio_hypotenuse_cylinder.setText('Hypotenuse')
        self.area_or_volume_check()

    def volume(self) -> None:
        """
        Sets the text for the 6 buttons when the volume button is pushed
        """
        self.radio_square_cube.setText('Cube')
        self.radio_rectangle_cuboid.setText('Cuboid')
        self.radio_circle_sphere.setText('Sphere')
        self.radio_triangle_pyramid.setText('Pyramid')
        self.radio_equilateral_cone.setText('Cone')
        self.radio_hypotenuse_cylinder.setText('Cylinder')
        self.area_or_volume_check()

    def square_cube(self) -> None:
        """
        Checks if the proper parameters are input for the square or cube formula
        """
        if self.radio_area.isChecked():
            self.label_top.setText('Side')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')
        elif self.radio_volume.isChecked():
            self.label_top.setText('Side')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')

    def rectangle_cuboid(self) -> None:
        """
        Checks if the proper parameters are input for the rectangle or cuboid formula
        """
        if self.radio_area.isChecked():
            self.label_top.setText('Base')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')
        elif self.radio_volume.isChecked():
            self.label_top.setText('Length')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('Base')
            self.lineEdit_middle.setEnabled(True)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('Height')
            self.lineEdit_bottom.setEnabled(True)
            self.lineEdit_bottom.setText('')

    def circle_sphere(self) -> None:
        """
        Checks if the proper parameters are input for the circle or sphere formula
        """
        if self.radio_area.isChecked():
            self.label_top.setText('Radius')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')
        elif self.radio_volume.isChecked():
            self.label_top.setText('Radius')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')

    def triangle_pyramid(self) -> None:
        """
        Checks if the proper parameters are input for the triangle or pyramid formula
        """
        if self.radio_area.isChecked():
            self.label_top.setText('Base')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')
        elif self.radio_volume.isChecked():
            self.label_top.setText('Length')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('Width')
            self.lineEdit_middle.setEnabled(True)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('Height')
            self.lineEdit_bottom.setEnabled(True)
            self.lineEdit_bottom.setText('')

    def equilateral_cone(self) -> None:
        """
        Checks if the proper parameters are input for the equilateral triangle or cone formula
        """
        if self.radio_area.isChecked():
            self.label_top.setText('Side')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')
        elif self.radio_volume.isChecked():
            self.label_top.setText('Radius')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')

    def hypotenuse_cylinder(self) -> None:
        """
        Checks if the proper parameters are input for the hypotenuse of a triangle or cylinder formula
        """
        if self.radio_area.isChecked():
            self.label_top.setText('Side One')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('Side Two')
            self.lineEdit_middle.setEnabled(True)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')
        elif self.radio_volume.isChecked():
            self.label_top.setText('Radius')
            self.lineEdit_top.setEnabled(True)
            self.lineEdit_top.setText('')
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.lineEdit_middle.setText('')
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
            self.lineEdit_bottom.setText('')

    def submit(self) -> None:
        """
        Does the calculations for the area or volume
        """
        if self.radio_square_cube.isChecked():
            if self.radio_area.isChecked():
                side = self.lineEdit_top.text()
                try:
                    side = float(side)
                except:
                    if side == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {side ** 2}')
            elif self.radio_volume.isChecked():
                side = self.lineEdit_top.text()
                try:
                    side = float(side)
                except:
                    if side == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {side ** 3}')

        elif self.radio_rectangle_cuboid.isChecked():
            if self.radio_area.isChecked():
                base = self.lineEdit_top.text()
                height = self.lineEdit_middle.text()
                try:
                    base = float(base)
                    height = float(height)
                except:
                    if base == '' or height == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {base * height}')
            elif self.radio_volume.isChecked():
                length = self.lineEdit_top.text()
                base = self.lineEdit_middle.text()
                height = self.lineEdit_bottom.text()
                try:
                    length = float(length)
                    base = float(base)
                    height = float(height)
                except:
                    if length == '' or base == '' or height == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {length * base * height}')

        elif self.radio_circle_sphere.isChecked():
            if self.radio_area.isChecked():
                radius = self.lineEdit_top.text()
                try:
                    radius = float(radius)
                except:
                    if radius == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {math.pi * (radius ** 2)}')
            elif self.radio_volume.isChecked():
                radius = self.lineEdit_top.text()
                try:
                    radius = float(radius)
                except:
                    if radius == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {(4 / 3) * math.pi * (radius ** 3)}')

        elif self.radio_triangle_pyramid.isChecked():
            if self.radio_area.isChecked():
                base = self.lineEdit_top.text()
                height = self.lineEdit_middle.text()
                try:
                    base = float(base)
                    height = float(height)
                except:
                    if base == '' or height == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {(base * height) / 2}')
            elif self.radio_volume.isChecked():
                length = self.lineEdit_top.text()
                width = self.lineEdit_middle.text()
                height = self.lineEdit_bottom.text()
                try:
                    length = float(length)
                    width = float(width)
                    height = float(height)
                except:
                    if length == '' or width == '' or height == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {(length * width * height) / 3}')

        elif self.radio_equilateral_cone.isChecked():
            if self.radio_area.isChecked():
                side = self.lineEdit_top.text()
                try:
                    side = float(side)
                except:
                    if side == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {(math.sqrt(3) / 4) * (side ** 2)}')
            elif self.radio_volume.isChecked():
                radius = self.lineEdit_top.text()
                height = self.lineEdit_middle.text()
                try:
                    radius = float(radius)
                    height = float(height)
                except:
                    if radius == '' or height == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {(1 / 3) * math.pi * (radius ** 2) * height}')

        elif self.radio_hypotenuse_cylinder.isChecked():
            if self.radio_area.isChecked():
                side1 = self.lineEdit_top.text()
                side2 = self.lineEdit_middle.text()
                try:
                    side1 = float(side1)
                    side2 = float(side2)
                except:
                    if side1 == '' or side2 == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {math.sqrt((side1 ** 2) + (side2 ** 2))}')
            elif self.radio_volume.isChecked():
                radius = self.lineEdit_top.text()
                height = self.lineEdit_middle.text()
                try:
                    radius = float(radius)
                    height = float(height)
                except:
                    if radius == '' or height == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    self.label_calculations.setText(f'Area = {math.pi * (radius ** 2) * height}')