#first dictionary - so I suppose dictionaries like a list, but using {} instead of []
# and we can store variables with values using : to store value
alien_0 = {'color': 'green', 'points': 7}
#and here I see that we can call separatelly variables using dicitionary name and ['variable-key']
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"Your reward is {new_points} points")
#to add key-variable I need simply write dictionary name and new key in [] with = value
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f"I added new key-variables {alien_0}")
#example of how objects could be programmed on the screen using simple logic
print("\nExample:")
cat = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {cat['x_position']}")
#basically we assign position
#next logic is for predicting movements
if cat['speed'] == 'slow':
    x_increment = 1
elif cat['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
#so new position is old pos + number from new variable increment which we will get
# based on what type of speed we put
cat['x_position'] = cat['x_position'] + x_increment
print(f"New position: {cat['x_position']}")
# to delete value I can use del
del cat['speed']
print(cat)
cat['speed'] = 'fast'
print(cat)