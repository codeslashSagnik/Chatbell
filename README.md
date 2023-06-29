# Chatbell

Chatbell

I am excited to share my recent project, ChatBell, an innovative voice assistant designed for conducting interviews.

Architecture:
ChatBell follows a client-server architecture, with a frontend built using React for the interactive user interface and a backend powered by FastAPI to handle the server-side logic and communication with OpenAI services.

Process:
During the development of ChatBell, I focused on creating a seamless interview experience. The process involved leveraging OpenAI's Whisper for accurate voice-to-text conversion and ElevenLabs for generating lifelike voice responses. Users can engage in natural and interactive conversations with the virtual assistant, enhancing the efficiency and engagement of interviews.

Technologies:

Frontend: The frontend of ChatBell is built with React, providing a user-friendly and intuitive interface for interview sessions. It allows candidates to easily navigate through the conversation and interact with the voice assistant.

Backend: The backend is developed using FastAPI, a modern web framework for building robust and scalable server-side applications. FastAPI enables efficient communication with OpenAI services, handling voice-to-text conversion and generating voice responses in real-time.

OpenAI Services: ChatBell utilizes OpenAI's advanced technologies, including Whisper for accurate voice recognition and ElevenLabs for generating natural and realistic voice responses. These technologies contribute to the seamless and lifelike conversation experience. 

If you have any questions or would like to learn more about ChatBell, please don't hesitate to reach out. I would be delighted to share my insights and experiences during the development process.


## Acknowledgements



I would also like to acknowledge the open-source community and the vast array of resources available online. The development of ChatBell would not have been possible without the collective knowledge and support provided by the community.

Lastly, I would like to thank the GitHub platform for providing a robust and collaborative environment for version control and project management. It has been instrumental in organizing and sharing the progress of ChatBell with the developer community.

I am truly grateful for the support, guidance, and contributions from all those involved in this project. Together, we have created a valuable resource that showcases the power of voice-based virtual assistants in the interview process.## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |

## API Reference
Reset Conversation
Resets the conversation to its initial state.

http

GET /reset-
Response
A successful request will return a response with a status code of 200.

Post Audio
Posts an audio file for processing.

http

POST /post-audio
Request 
The request body should contain the audio file to be processed.

Response
A successful request will return a response with a status code of 200.



