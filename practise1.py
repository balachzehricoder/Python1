# # print('''Twinkle, twinkle, little star,
# # How I wonder what you are!
# # Up above the world so high,
# # Like a diamond in the sky.

# # When the blazing sun is gone,
# # When he nothing shines upon,
# # Then you show your little light,
# # Twinkle, twinkle, all the night.

# # Then the trav'ller in the dark,
# # Thanks you for your tiny spark,
# # He could not see which way to go,
# # If you did not twinkle so.

# # In the dark blue sky you keep,
# # And often thro' my curtains peep,
# # For you never shut your eye,
# # Till the sun is in the sky.

# # 'Tis your bright and tiny spark,
# # Lights the trav'ller in the dark:
# # Tho' I know not what you are,
# # Twinkle, twinkle, little star.''')


# import pyttsx3
# engine = pyttsx3.init()
# engine.say('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.''')
# engine.runAndWait()





import os

def list_directories(path='/users/'):
    # Get the list of all files and directories
    entries = os.listdir(path)
    
    # Filter out only directories
    directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
    
    # Print the list of directories
    print(f"Directories in '{path}':")
    for directory in directories:
        print(directory)

# Call the function to list directories in the current working directory
list_directories()
