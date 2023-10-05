**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 1

<hr>

**Use Case**: Set Canvas Dimensions

**Primary Actor**: Random User

**Goal in Context**: The user aims to view or create graphical content within a window and drawable canvas of specific dimensions (600x400 pixels).

**Preconditions**: The application is successfully launched. The graphical user interface (GUI) toolkit or library supports customizable canvas dimensions.

**Trigger**: The user starts the application or requests to set/reset canvas dimensions.
  
**Scenario**: User launches the graphic application.
The application initializes the GUI components.
The system sets the default canvas size.
The system detects the requirement for a canvas size of 600x400 pixels.
The system adjusts the canvas to the specified dimensions.
The system displays the canvas to the user with the set dimensions.
 
**Exceptions**: If the system fails to adjust to the required dimensions, an error message is displayed. The user may try again or check their system settings.
If the user's display resolution is less than the required dimensions, the system adjusts to the maximum available size and informs the user.

**Priority**: High

**When available**: Version 1.0

**Channel to actor**: GUI

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: How should the system behave if the requested dimensions are larger than the user's display resolution? Is there a need for a user interface element that allows users to manually adjust canvas dimensions

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
