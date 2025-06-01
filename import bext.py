import bext
import time

# Clear the screen
bext.clear()

# Move the cursor to row 5, column 10
bext.goto(10, 5)
bext.fg('red')  # Set foreground color
print("Hello from bext!")

# Wait for 1 second
time.sleep(1)

# Change the text color and move again
bext.fg('green')
bext.goto(10, 7)
print("Now in green!")

# Reset colors
bext.fg('reset')
bext.goto(0, 10)
print("All done.")
