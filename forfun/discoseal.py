import time
from colorama import Fore, init

# Your additional ASCII art
extra_ascii = r'''
           /!
          / !              ,/!  
 ..-~~~~~/  `````~~~~,__,,/ ,!
(     @         ) ) )       {
 \ vvvv     ,,   ,,,,,,---,,`\, 
  ``````````\,,,\          `\,!
'''

# The main ASCII art
ascii_art = r'''
                                             oo
                                            o"  $
                                          " o   $
                                         "      $
                                        $      $$ 
                                        o"     "$o 
   $oo                                  $     "$$$
   $"$oo                               "      "o$$ 
  "$$o$"o"o                          o"      $"$$$
     """o"$o"""""""" """ oo ooooooo"""     o""o$$$
          "$$ o                            o""$$$
    oooo$$$$$$$$oo"o o                 o "o "o ""oo
  "$$$$$$$$$$""""$$$$o"o$ o o o  "o " $"$o$$oo"o  $"o
   "$$$$$$"         ""$$o$o$ $ "ooo$o$o$$$$$$"$o$o $"$o
   "$""                 """"$$$$$o$$$$$$$$$     "$o$$$$o
   "                           " "" "  "$$$$       " $$$o
                                         "$$$         """
                                           ""$
'''

# Function to print the ASCII art with colors
def print_colorful_ascii(ascii, colors, duration):
    init(autoreset=True)
    for _ in range(int(2 * duration)):
        for color in colors:
            print(color + ascii, end='\r')
            time.sleep(0.5)
            print("\033[H\033[J")

# Define the colors (you can choose the ones you prefer)
colors = [Fore.RED, Fore.BLUE, Fore.YELLOW, Fore.GREEN]

# Call the function to display the colorful ASCII art
print_colorful_ascii(extra_ascii + ascii_art, colors, 5)

