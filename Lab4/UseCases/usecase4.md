**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Drawing on Canvas with Mouse Press

**Primary Actor**: User

**Goal in Context**: The user aims to draw on the canvas in real-time by pressing and dragging the left mouse button, simulating the action of a pencil drawing on paper.

**Preconditions**: The application is successfully launched and is in drawing mode.
The canvas or drawing area is active and ready to accept inputs.
A color has been previously selected or the default color is set.

**Trigger**: The user presses (and possibly holds) the left mouse button over the canvas.
  
**Scenario**: User positions the mouse cursor over the desired starting point on the canvas.
User presses the left mouse button (without releasing it).
The system detects the mouse press event.
The system changes the pixel color where the mouse cursor is located to the currently selected color.
As the user drags the mouse (while keeping the button pressed), the system continues to change the pixel colors along the path of the cursor to the selected color.
The user releases the left mouse button to stop drawing.
The user observes the drawn path on the canvas.
 
**Exceptions**: If the system fails to detect the mouse press or doesn't draw on the canvas, it provides feedback (like a sound or message) indicating the error. The user may try the action again.
If there's an issue with tracking the continuous movement of the mouse while drawing, the drawn line might appear broken or jagged.

**Priority**: High

**When available**: Version 1.0

**Channel to actor**: GUI and Mouse Input

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: How will the system handle rapid and erratic mouse movements while drawing?
Should there be a feature that adjusts the thickness or opacity of the drawn line?
How to ensure smooth drawing, especially on systems or devices with limited resources?

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
