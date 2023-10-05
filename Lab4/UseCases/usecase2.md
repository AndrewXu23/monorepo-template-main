**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: Change Drawing Color via Number Keys

**Primary Actor**: User

**Goal in Context**: The user aims to quickly change the drawing color on the canvas by pressing number keys between 1 and 8.

**Preconditions**: The application is successfully launched and is in drawing mode. The canvas or drawing area is active and ready to accept inputs.

**Trigger**: The user presses a number key between 1 and 8.
  
**Scenario**: User is interacting with the canvas, drawing or preparing to draw.
User decides to change the drawing color.
User presses a specific number key (for example, 4).
The system detects the keypress event.
The system maps the keypress to the corresponding color (in this example, Green).
The drawing color is changed to the selected color.
The user continues drawing in the newly selected color.
 
**Exceptions**: If the system fails to detect a keypress or maps it to the wrong color, it provides feedback (like a sound or message) indicating the error. The user may try pressing the key again.
If a number outside the range 1-8 is pressed, the system might ignore the input or provide feedback that it's an invalid color selection.

**Priority**: Medium

**When available**: Version 1.1 

**Channel to actor**: GUI and Keyboard Input

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: Should there be a visual indicator or palette showing which number corresponds to which color? How will the system behave if multiple number keys are pressed rapidly in succession?


<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
