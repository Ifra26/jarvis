Libraries Used:
pyttsx3: Handles text-to-speech conversion, allowing Jarvis to speak.
speech_recognition: Enables Jarvis to recognize speech input from the user.
datetime: Retrieves the current time for responding to time-related queries.
wikipedia: Fetches information from Wikipedia based on user queries.
webbrowser: Opens specified web pages (like YouTube or Google) based on user commands.
pywhatkit: Specifically used for interacting with YouTube (playing videos).
os: Provides functions for interacting with the operating system (e.g., opening files or applications).
random: Used for selecting random elements, such as random music files.
tkinter: Implements the graphical user interface (GUI) for user interaction
2. Functionality Breakdown:
Initialization and Setup:
pyttsx3 Initialization: Initializes the text-to-speech engine (pyttsx3.init('sapi5')) and sets the voice to a male or female option (engine.setProperty('voice', voices[1].id)).
GUI Setup: Uses tkinter to create a GUI with a logo, status area, text area for displaying interactions, and buttons for starting and stopping Jarvis.
User Interaction:
wishMe(): Greets the user based on the current time of day (Morning, Afternoon, Evening) using the datetime library.
speak(text): Utilizes pyttsx3 to convert text to speech and speak out responses to the user.
Speech Recognition:
takeCommand(): Activates the microphone (sr.Microphone()) and listens for user speech. It adjusts for ambient noise (recognizer.adjust_for_ambient_noise(source, duration=1)) and captures audio (recognizer.listen(source)). It then uses Google's Web Speech API (recognize_google) to convert the captured audio into text.
Command Execution:
executeCommand(query): Processes user commands based on recognized keywords:
Opens specified websites (open youtube, open google).
Searches and plays videos on YouTube (open youtube with pywhatkit).
Searches and retrieves information from Wikipedia (what is, who is).
Opens various applications (open vs code, open excel) using os.startfile.
Plays random music from a specified directory (play music).
Retrieves the current time (the time).
GUI Interaction:
Text Area (text_area): Displays both user queries and Jarvis's responses in a scrolled text widget (scrolledtext.ScrolledText). This provides a history of interactions for the user.
Status Updates (status_text): Displays real-time updates on the GUI about the current status of Jarvis (e.g., Listening, Recognizing, Assistant Stopped).
3. Additional Details:
Error Handling: Includes handling cases where speech recognition fails to understand the user (sr.UnknownValueError). In such cases, Jarvis informs the user and prompts for a repeat of the command.
Continuous Interaction: Utilizes a while True loop in startAssistant() to continuously listen for and respond to user commands until instructed to stop.
Modular Design: Commands are structured based on keywords (if and elif statements in executeCommand(query)) to efficiently handle specific tasks, ensuring clarity and maintainability of the code.
Voice and Visual Interaction: Offers a seamless interaction experience where users can speak commands naturally, and Jarvis responds both vocally (through pyttsx3) and visually (through tkinter GUI).
