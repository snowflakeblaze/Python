##Create pseudocode for a program that asks for the length and width of two rectangles, 
##then calculates the area of each and displays which rectangle has the greatest area or 
## if the areas are the same.

Display "Enter the length of rectangle 1"
Input rectangle_1_length

Display "Enter the width of rectangle 1"
Input rectangle_1_width

Display "Enter the length of rectangle 2"
Input rectangle_2_length

Display "Enter the width of rectangle 2"
Input rectangle_2_width

set rectangle_1_area = rectangle_1_length * rectangle_1_width
set rectangle_2_area = rectangle_2_length * rectangle_2_width

 if rectangle_1_area > rectangle_2_area
 Display "Rectangle 1 has a greater area"

 if rectangle_2_area > rectangle_1_area
 Display "Rectangle 2 has a greater area"

 if rectangle_1_area = rectangle_2_area
 Display "The areas are the same for both rectangles"