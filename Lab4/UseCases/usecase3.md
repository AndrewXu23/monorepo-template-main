**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Clear Canvas with Space Key

**Primary Actor**: User

**Goal in Context**: The user wants to quickly clear the current content on the canvas and fill it entirely with the last selected color by pressing the space key.

**Preconditions**: The application is successfully launched and is in drawing mode. The canvas or drawing area is active and ready to accept inputs. A color has been previously selected or the default color is set.

**Trigger**: User presses the space key.
  
**Scenario**: User is interacting with the canvas, either drawing or observing current content.
User decides to clear the canvas.
User presses the space key.
The system detects the space keypress event.
The canvas content is cleared.
The system fills the entire canvas with the last selected color.
The user now sees a canvas filled entirely with that color and can continue their interaction.
 
**Exceptions**: If the system fails to detect the space keypress or doesn't clear the canvas, it provides feedback (like a sound or message) indicating the error. The user may try pressing the key again. If the system can't remember the last selected color, it might default to a pre-determined color (e.g., white) and inform the user.

**Priority**: High

**When available**: Version 1.1 

**Channel to actor**: GUI and Keyboard Input

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: What should happen if the user presses the space key accidentally? Should there be an undo option or a confirmation prompt before clearing? How to ensure the 'last selected color' is always stored and retrieved correctly?

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
