<h1> LockInAI </h1>

## 📝 Overview 📝

LockInAI is an application that uses machine learning to help users maintain focus when working. LockInAI uses a neural network on a video of the user to determine whether they are currently focused or unfocused on their task, using binary classification. What makes this project special is that it's able to determine focus or unfocus when the user is working on tasks off of their computer, like on paper. LockInAI also uses machine learning and advanced AR technology to allow for in-air gesture controls. Since getting on the computer can be a gateway for many distractions, by allowing the user to scroll or click just by swiping the air, it helps ensure that the user will stay on task.

## How we built it
We trained a pre-trained model (ResNet152v2) on our own data created during the hackathon in Google Colab notebooks. The CNN binary classifier was trained on individual frames from the training videos, and we obtained high accuracy. In the app, this model was called every few frames to analyze the user. If the user is detected as unfocused multiple times in a row, the app gives a warning to the user.


For the gesture controls, we used OpenCV's media pipe pose estimation, which tracks 22 points on the hand. Through computing the relationships between different points, we developed three highly accurate gesture controls: left-click, scrolling up, and and scrolling down.

## Focus Mode Demonstration

https://github.com/user-attachments/assets/5aa119b8-43d7-49a8-b0a8-4d2059c5bbb5



## Hand Gesture Demonstration

![Alt Text](./output.gif)

## Built with

- [opencv](https://opencv.org)
- [mediapipe](https://github.com/google/mediapipe)
- [ResNet152v2](https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet_v2/ResNet152V2)
- [tkinter](https://docs.python.org/3/library/tkinter.html)

## 🧑‍💻 Authors 🧑‍💻

Alexander S. Du / [@Mantlemoose](https://github.com/Mantlemoose "Mantlemoose's github page") \
Prarthan Ghosh / [@coder2003lucky](https://github.com/coder2003lucky "coder2003lucky's github page") \
Eashan Chatterjee / [@EashanC23](https://github.com/EashanC23 "EashanC23's github page") \
Nicholas Kann / [@nick-kann](https://github.com/nick-kann "nick-kann's github page")
