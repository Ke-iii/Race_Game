
#-----Project Description----------------------------------#
#
#  This project task tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.
#
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately.
from email.mime import image
from operator import truediv
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile
import turtle


# Import the functions for setting up the drawing canvas
if isfile('data_visualisation_configuration.py'):
    print('\nConfiguration module found ...\n')
    from data_visualisation_configuration import *
else:
    print("\nCannot find file 'data_visualisation_configuration.py', aborting!\n")
    abort()

# Define the function for generating data sets, using the
# imported raw data generation function if available, but
# otherwise creating a dummy function that just returns an
# empty list
if isfile('data_visualisation_data_source.py'):
    print('Data generation module found ...\n')
    from data_visualisation_data_source import raw_data
    def data_set(new_seed = randint(0, 99999)):
        print('Using random number seed', new_seed, '...\n')
        seed(new_seed) # set the seed
        return raw_data() # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Solution---------------------------------------------#

# All codes goes in, or is called from, this function
def visualise_data(datas, numbers):

    #drawing the characters (Mordecai & Rigby)
    #misc setup
    speed('fastest')
    title('Mordecai and Rigby (Regular Show)')
    tracer(False)


    #going to Mordecai's energized state
    penup()
    home()
    setheading(130)
    forward(400)
    
    # writing who it is
    setheading(90)
    forward(40)
    setheading(180)
    forward(150)
    style = ('Arial', 15, 'bold')
    write('Mordecai: energized', font = style)

    # going back to mordecai's energized area
    setheading(0)
    forward(150)
    setheading(270)
    forward(40)

    def mordecai_energized():
        #drawing mordecai (energized)
        #drawing the rectangle
        fillcolor('light green')
        angle = [90, 0, 270, 180]

        pendown()
        begin_fill()
        for rectangle in range(len(angle)):
            setheading(angle[rectangle])
            forward(80)
        end_fill()
        mordecai_energized_pos = turtle.pos()
        penup()

        # drawing mordecai (energized)
        fillcolor('light blue')
        setheading(90)
        forward(40)
        setheading(10)
        forward(8)
        pendown()
        forward(17)

        #drawing top half
        setheading(120)
        begin_fill()
        circle(-4, extent = 190)
        circle(4, 190)
        setheading(0)
        forward(7)
        circle(-4, extent = 100)
        setheading(0)
        forward(7)
        setheading(105)
        forward(7)
        setheading(80)
        forward(7)
        setheading(240)
        forward(10)
        setheading(80)
        forward(20)
        setheading(190)
        circle(40, extent = 52)
        end_fill()
        penup()
        circle(15, extent = 25)

        #drawing the eyes  
        setheading(90)
        pendown()
        begin_fill()
        circle(-3, extent = 90)
        dot(2.5)
        circle(-3, extent = 70)
        setheading(190)
        forward(5)
        end_fill()
        setheading(10)
        forward(7)
        setheading(90)
        begin_fill()
        circle(-4, extent = 70)
        dot(2.5)
        circle(-4, extent = 60)
        setheading(270)
        circle(-4, extent = 140)
        end_fill()
        penup()

        # filling the eyes
        fillcolor('white')
        setheading(90)
        pendown()
        begin_fill()
        circle(-4, extent = 60)
        dot(2.5)
        circle(-4, extent = 70)
        setheading(90)
        circle(4, extent = 215)
        end_fill()
        setheading(90)
        begin_fill()
        circle(4, extent = 215)
        setheading(90)
        circle(-3, extent = 90)
        dot(2.3)
        circle(-3, extent = 60)
        end_fill()

        #drawing Mordecai's beak
        setheading(10)
        penup()
        fillcolor('grey')
        forward(7)
        pendown()
        begin_fill()
        forward(1)
        circle(-4, extent = 180)
        forward(30)
        setheading(18)
        forward(22)
        setheading(180)
        forward(25)
        setheading(10)
        forward(32)
        end_fill()

        #drawing bottom half
        penup()
        fillcolor('white')
        pendown()
        forward(3.5)
        begin_fill()
        setheading(90)
        forward(3.5)
        setheading(0)
        forward(7)
        circle(-4, extent = 100)
        setheading(0)
        forward(7)
        setheading(270)
        circle(-17, extent = 150)
        setheading(10)
        forward(12)
        circle(4, extent = 120)
        setheading(90)
        forward(4.5)
        end_fill()

        #torso area
        penup()
        setheading(270)
        forward(21)
        begin_fill()
        setheading(180)
        forward(4)
        pendown()
        setheading(260)
        forward(10)
        setheading(270)
        forward(20)
        setheading(0)
        forward(15)
        setheading(90)
        forward(32)
        setheading(180)
        forward(15)
        end_fill()
        penup()
        #going back to starting corner
        goto(mordecai_energized_pos)
    mordecai_energized()





    
    #Going to Mordecai exhausted state
    home()
    setheading(65)
    forward(340)

    # writing who it is
    setheading(90)
    forward(40)
    setheading(0)
    forward(100)
    style = ('Arial', 15, 'bold')
    write('Mordecai: exhausted', font = style)

    # going back
    setheading(180)
    forward(100)
    setheading(270)
    forward(40)




    def mordecai_exhausted():
        #drawing mordecai (exhausted)
        #drawing the square
        fillcolor('light green')
        angle = [90, 0, 270, 180]

        pendown()
        begin_fill()
        for rectangle in range(len(angle)):
            setheading(angle[rectangle])
            forward(80)
        end_fill()
        penup()

        #drawing mordecai's beak
        setheading(90)
        forward(40)
        fillcolor('grey')
        setheading(0)
        forward(40)
        pendown()
        begin_fill()
        setheading(180)
        circle(60, extent = 30)
        setheading(10)
        forward(25)
        setheading(190)
        forward(22)
        setheading(4)
        forward(30)
        circle(2.8, extent = 220)
        end_fill()

        #drawing mordecai's eyes
        penup()
        fillcolor('light blue')
        setheading(180)
        circle(60, extent = 12)
        setheading(90)
        forward(5)
        for mordecai_eyes in range(2):
            pendown()
            circle(-4)
            begin_fill()
            circle(-4, extent = 180)
            setheading(180)
            forward(8)
            end_fill()
            penup()
            setheading(90)
            circle(-4, extent = 90)
            setheading(270)
            forward(6)
            dot(2.5)
            setheading(90)
            forward(2)
            setheading(0)
            forward(4)
            setheading(90)
            penup()

        #drawing mordecai's top half
        setheading(0)
        pendown()
        begin_fill()
        forward(7)
        circle(-4, extent = 100)
        setheading(0)
        forward(7)
        setheading(105)
        forward(7)
        setheading(80)
        forward(7)
        setheading(240)
        forward(10)
        setheading(80)
        forward(20)
        setheading(190)
        circle(50, extent = 45)
        for mordecai_eye_lids in range(2):
            setheading(90)
            circle(-4, extent = 180)
            setheading(90)
        end_fill()
        penup()

        #drawing mordecai's bottom half
        fillcolor('white')
        setheading(0)
        forward(7)
        circle(-4, extent = 100)
        setheading(0)
        forward(7)
        setheading(270)
        begin_fill()
        pendown()
        circle(-16, extent = 165)
        setheading(5)
        forward(15)
        setheading(90)
        forward(8)
        setheading(0)
        forward(7)
        circle(-4, extent = 100)
        setheading(0)
        forward(7)
        end_fill()

        #torso area
        penup()
        setheading(270)
        circle(-16, extent = 90)
        setheading(290)
        pendown()
        begin_fill()
        forward(24)
        setheading(0)
        forward(20)
        setheading(120)
        forward(35)
        end_fill()
        penup()
    mordecai_exhausted()





    
    #going to rigby energized state
    home()
    setheading(235)
    forward(460)

    # writing who it is
    setheading(90)
    forward(40)
    setheading(180)
    forward(130)
    style = ('Arial', 15, 'bold')
    write('Rigby: energized', font = style)

    # going back to rigby's energized area
    setheading(0)
    forward(130)
    setheading(270)
    forward(40)

    def rigby_energized():
        #start drawing rigby (energized)
        #drawing the square
        fillcolor('antique white')
        angle = [90, 0, 270, 180]

        pendown()
        begin_fill()
        for rectangle in range(len(angle)):
            setheading(angle[rectangle])
            forward(80)
        end_fill()
        rigby_energized_pos = turtle.pos()
        penup()

        #drawing the nose
        fillcolor('chocolate')
        setheading(0)
        forward(30)
        setheading(90)
        pendown()
        begin_fill()
        forward(30)
        setheading(180)
        circle(-20, extent = 50)
        dot(5)
        setheading(0)
        circle(40, extent = 22)
        setheading(90)
        forward(3)

        #drawing the hair
        hair_coords = [170, 150, 130]
        for rigby_hair in range(len(hair_coords)):
            setheading(hair_coords[rigby_hair])
            circle(-7, extent = 90)
            setheading(350)
            circle(-9, extent = 60)
            
        #drawing the ears
        forward(7)
        setheading(90)
        circle(-7, extent = 90)
        setheading(270)
        circle(-9, extent = 60)

        #filling the body
        setheading(300)
        forward(7)
        setheading(270)
        forward(40)
        setheading(180)
        forward(23)
        end_fill()
        penup()

        #drawing the eyes
        setheading(90)
        forward(30)
        setheading(180)
        circle(-20, extent = 50)
        setheading(0)
        circle(40, extent = 22)
        setheading(90)
        forward(3)
        fillcolor('saddle brown')
        pendown()
        for rigby_eyes in range(2):
            begin_fill()
            circle(-5)
            end_fill()
            penup()
            setheading(0)
            forward(10)
            setheading(90)
            pendown()

        #drawing the pupils and eyelids
        penup()
        fillcolor('white')
        for rigby_eye_lids in range(2):
            setheading(180)
            forward(10)
            setheading(270)
            forward(3)
            setheading(90)
            pendown()
            begin_fill()
            circle(-5, extent = 170)
            setheading(180)
            forward(6)
            setheading(90)
            forward(1)
            dot(3)
            setheading(270)
            forward(1)
            setheading(180)
            forward(4)
            end_fill()
            penup()
            setheading(90)
            forward(3)

        #drawing the mouth
        setheading(0)
        forward(8)
        setheading(270)
        forward(15)
        pendown()
        setheading(0)
        circle(5, extent = 80)
        setheading(180)
        circle(-8, extent = 40)
        penup()

        #going back to starting corner
        goto(rigby_energized_pos)
    rigby_energized()
    





    
    #going to rigby exhausted state
    home()
    setheading(290)
    forward(400)
        
    # writing who it is
    setheading(90)
    forward(40)
    setheading(0)
    forward(100)
    style = ('Arial', 15, 'bold')
    write('Rigby: exhausted', font = style)

    # going back
    setheading(180)
    forward(100)
    setheading(270)
    forward(40)

    def rigby_exhausted():
        #start drawing rigby (exhausted)
        #drawing the square
        fillcolor('antique white')
        angle = [90, 0, 270, 180]

        pendown()
        begin_fill()
        for rectangle in range(len(angle)):
            setheading(angle[rectangle])
            forward(80)
        end_fill()
        penup()

        #drawing the nose
        fillcolor('chocolate')
        setheading(0)
        forward(40)
        setheading(115)
        pendown()
        begin_fill()
        forward(30)
        setheading(180)
        circle(-20, extent = 50)
        dot(5)
        setheading(0)
        circle(40, extent = 22)
        setheading(90)
        forward(3)

        #drawing the hair
        hair_coords = [170, 150, 130, 120]
        for rigby_hair in range(len(hair_coords)):
            setheading(hair_coords[rigby_hair])
            circle(-7, extent = 90)
            setheading(350)
            circle(-9, extent = 60)

        #drawing the ears
        forward(7)
        setheading(90)
        circle(-7, extent = 90)
        setheading(270)
        circle(-9, extent = 60)

        #filling the body
        setheading(285)
        forward(48)
        setheading(180)
        forward(27)
        end_fill()
        penup()

        #drawing the eyes
        setheading(115)
        forward(30)
        setheading(180)
        circle(-20, extent = 50)
        setheading(0)
        circle(40, extent = 22)
        setheading(90)
        forward(3)
        fillcolor('saddle brown')
        pendown()
        for rigby_eyes in range(2):
            begin_fill()
            circle(-5)
            end_fill()
            penup()
            setheading(0)
            forward(10)
            setheading(90)
            pendown()

        #drawing the pupil and eyelids
        penup()
        fillcolor('white')

        for rigby_eyelids in range(2):
            begin_fill()
            setheading(180)
            forward(2)
            pendown()
            setheading(90)
            circle(3)
            end_fill()
            penup()
            setheading(210)
            forward(3)
            dot(2)
            setheading(160)
            forward(6)
            pendown()

        #drawing tears
        fillcolor('pale turquoise')
        for rigby_tears in range(2):
            penup()
            setheading(270)
            forward(4)
            pendown()
            begin_fill()
            forward(3)
            setheading(270)
            circle(2, extent = 180)
            setheading(270)
            forward(4)
            circle(2, extent = 180)
            setheading(80)
            forward(10)
            setheading(270)
            circle(-5, extent = 150)
            end_fill()
            penup()
            setheading(90)
            forward(4)
            setheading(0)
            forward(10)

        #drawing mouth
        penup()
        fillcolor('indian red')
        setheading(180)
        forward(14)
        setheading(270)
        forward(20)
        setheading(90)
        pendown()
        begin_fill()
        circle(-7, extent = 180)
        setheading(180)
        forward(14)
        end_fill()
        penup()
    rigby_exhausted()
    

#----------------------------------------------------------------------------------------------------#

    #Coding the game's rule



    #noting the competitor's energy level
    #Competitor A's energy level
    mordecai_energy = datas[0][1]
    print('mordecai energy level is', mordecai_energy)

    #Competitor B's energy level
    rigby_energy = datas[0][2]
    print('rigby energy level is', rigby_energy)



    #noting the number for each image (Competitor A)
    mordecai_image_number = 0

    #draw competitors in starting area
    #mordecai energized (start area)
    goto(-640, 80)
    mordecai_energized()
    mordecai_coords = turtle.pos()
    mordecai_xpos = round(xcor())
    mordecai_ypos = round(ycor())
    print('mordecai starting position is', mordecai_coords)

    #drawing the number on image
    if numbers == True:
        goto (mordecai_coords)
        setheading(45)
        forward(10)
        mordecai_image_number = mordecai_image_number + 1
        write(mordecai_image_number, font = style)
    else:
        pass



    #noting the number for each image (Competitor B)
    rigby_image_number = 0
    
    #rigby energized (start area)
    goto(-640, -160)
    rigby_energized()
    rigby_coords = turtle.pos()
    rigby_xpos = round(xcor())
    rigby_ypos = round(ycor())
    print('rigby starting position is', rigby_coords)

    #drawing the number on image
    if numbers == True:
        goto (rigby_coords)
        setheading(45)
        forward(10)
        rigby_image_number = rigby_image_number + 1
        write(rigby_image_number, font = style)
    else:
        pass




    #create a loop to go through all the competitor's moves
    for competitor_movement in datas[1:]:

        #checking if Competitor A (aka mordecai) is at the finish line (used grid coordinates to determine finish line)
        if competitor_movement[0:][1] == 'Competitor A' and mordecai_xpos == 560 and mordecai_energy > 0 and competitor_movement[0:][2] == 'Forward':
            gold_star(640, (mordecai_ypos + 70))
            break


        #checking if Competitor A can move forward
        elif competitor_movement[0:][1] == 'Competitor A' and mordecai_energy > 0 and competitor_movement[0:][2] == 'Forward':

            #going forward on the grid
            goto(mordecai_coords)
            setheading(0)
            forward(80)
            mordecai_energized()
            mordecai_coords = turtle.pos()
            mordecai_xpos = round(xcor())
            mordecai_ypos = round(ycor())
            mordecai_energy = mordecai_energy - 1

             #drawing the number on image 
            if numbers == True:
                goto (mordecai_coords)
                setheading(45)
                forward(10)
                mordecai_image_number = mordecai_image_number + 1
                write(mordecai_image_number, font = style)
            else:
                pass


        #checking if Competitor A can move one lane down
        elif competitor_movement[0:][1] == 'Competitor A' and mordecai_energy > 0 and competitor_movement[0:][2] == 'Lane down':
            #checking if the competitor is going out of bound
            if mordecai_ypos == (-240.00):
                goto(mordecai_coords)
                mordecai_exhausted()
                mordecai_energy = mordecai_energy - 1

                #drawing the number on image
                if numbers == True:
                    goto (mordecai_coords)
                    setheading(45)
                    forward(10)
                    mordecai_image_number = mordecai_image_number + 1
                    write(mordecai_image_number, font = style)
                else:
                    pass

            #if competitor is not out of bound
            else:
                goto(mordecai_coords)
                setheading(270)
                forward(80)
                mordecai_energized()
                mordecai_coords = turtle.pos()
                mordecai_xpos = round(xcor())
                mordecai_ypos = round(ycor())
                mordecai_energy = mordecai_energy - 1

                #drawing the number on image
                if numbers == True:
                    goto (mordecai_coords)
                    setheading(45)
                    forward(10)
                    mordecai_image_number = mordecai_image_number + 1
                    write(mordecai_image_number, font = style)
                else:
                    pass



        #checking if Competitor A can move one lane up
        elif competitor_movement[0:][1] == 'Competitor A' and mordecai_energy > 0 and competitor_movement[0:][2] == 'Lane up':
            #checking if the competitor is going out of bound
            if mordecai_ypos == 160:
                goto(mordecai_coords)
                mordecai_exhausted()
                mordecai_energy = mordecai_energy - 1

                #drawing the number on image
                if numbers == True:
                    goto (mordecai_coords)
                    setheading(45)
                    forward(10)
                    mordecai_image_number = mordecai_image_number + 1
                    write(mordecai_image_number, font = style)
                else:
                    pass

            #if competitor is not out of bound
            else:
                goto(mordecai_coords)
                setheading(90)
                forward(80)
                mordecai_energized()
                mordecai_coords = turtle.pos()
                mordecai_xpos = round(xcor())
                mordecai_ypos = round(ycor())
                mordecai_energy = mordecai_energy - 1

                #drawing the number on image
                if numbers == True:
                    goto (mordecai_coords)
                    setheading(45)
                    forward(10)
                    mordecai_image_number = mordecai_image_number + 1
                    write(mordecai_image_number, font = style)
                else:
                    pass



        #if Competitor A (mordecai) energy is at 0, draw Competitor A exhausted
        elif competitor_movement[0:][1] == 'Competitor A' and mordecai_energy == 0:
            goto(mordecai_coords)
            mordecai_exhausted()

            #drawing the number on image
            if numbers == True:
                goto (mordecai_coords)
                setheading(45)
                forward(10)
                write(mordecai_image_number, font = style)
            else:
                pass



        #checking if Competitor B (aka rigby) is at the finish line (used grid coordinates to determine finish line)
        elif competitor_movement[0:][1] == 'Competitor B' and rigby_xpos == 560 and rigby_energy > 0 and competitor_movement[0:][2] == 'Forward':
            gold_star(640, (rigby_ypos + 70))
            break


        #checking if Competitor B can move forward
        elif competitor_movement[0:][1] == 'Competitor B' and rigby_energy > 0 and competitor_movement[0:][2] == 'Forward':
            goto(rigby_coords)
            setheading(0)
            forward(80)
            rigby_energized()
            rigby_coords = turtle.pos()
            rigby_xpos = round(xcor())
            rigby_ypos = round(ycor())
            rigby_energy = rigby_energy - 1

            #drawing the number on image
            if numbers == True:
                goto (rigby_coords)
                setheading(45)
                forward(10)
                rigby_image_number = rigby_image_number + 1
                write(rigby_image_number, font = style)
            else:
                pass



        #checking if Competitor B can move one lane down
        elif competitor_movement[0:][1] == 'Competitor B' and rigby_energy > 0 and competitor_movement[0:][2] == 'Lane down':
            #checking if the competitor is going out of bound
            if rigby_ypos == (-240.00):
                goto(rigby_coords)
                rigby_exhausted()
                rigby_energy = rigby_energy - 1

                #drawing the number on image
                if numbers == True:
                    goto (rigby_coords)
                    setheading(45)
                    forward(10)
                    rigby_image_number = rigby_image_number + 1
                    write(rigby_image_number, font = style)
                else:
                    pass

            # if competitor is not out of bound
            else:
                goto(rigby_coords)
                setheading(270)
                forward(80)
                rigby_energized()
                rigby_coords = turtle.pos()
                rigby_xpos = round(xcor())
                rigby_ypos = round(ycor())
                rigby_energy = rigby_energy - 1

                #drawing the number on image
                if numbers == True:
                    goto (rigby_coords)
                    setheading(45)
                    forward(10)
                    rigby_image_number = rigby_image_number + 1
                    write(rigby_image_number, font = style)
                else:
                    pass



        #checking if Competitor A can move one lane up
        elif competitor_movement[0:][1] == 'Competitor B' and rigby_energy > 0 and competitor_movement[0:][2] == 'Lane up':
            #checking if the competitor is going out of bound
            if rigby_ypos == 160.00:
                goto(rigby_coords)
                rigby_exhausted()
                rigby_energy = rigby_energy - 1

                #drawing the number on image
                if numbers == True:
                    goto (rigby_coords)
                    setheading(45)
                    forward(10)
                    rigby_image_number = rigby_image_number + 1
                    write(rigby_image_number, font = style)
                else:
                    pass

            #if competitor is not out of bound
            else:
                goto(rigby_coords)
                setheading(90)
                forward(80)
                rigby_energized()
                rigby_coords = turtle.pos()
                rigby_xpos = round(xcor())
                rigby_ypos = round(ycor())
                rigby_energy = rigby_energy - 1

                #drawing the number on image
                if numbers == True:
                    goto (rigby_coords)
                    setheading(45)
                    forward(10)
                    rigby_image_number = rigby_image_number + 1
                    write(rigby_image_number, font = style)
                else:
                    pass



        #if Competitor B (rigby) energy is at 0, draw Competitor B exhausted
        elif competitor_movement[0:][1] == 'Competitor B' and rigby_energy == 0:
            goto(rigby_coords)
            rigby_exhausted()
            
            #drawing the number on image
            if numbers == True:
                goto (rigby_coords)
                setheading(45)
                forward(10)
                write(rigby_image_number, font = style)
            else:
                pass


        #if both competitors energy are at 0, the race is stopped
        elif rigby_energy == 0 and mordecai_energy == 0:
            print('Both competitors have ran out of energy, the race is concluded.')
            break

        else:
            break



    #exiting
    hideturtle()
    done()
    
    pass
#
#--------------------------------------------------------------------#



#-----Main Program to Run Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
create_drawing_canvas(write_instructions = False)

# Call the function to process the data set
# ***** While developing your program you can call the
# ***** "data_set" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set(), True) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Do not change this function call
release_drawing_canvas()

#
#--------------------------------------------------------------------#
