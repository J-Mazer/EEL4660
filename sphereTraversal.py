from matplotlib import pyplot as plt
import numpy as np

# Draw loop for the animation.
fig = plt.figure()

linkLength = 10
pixelCount = 100
length = 0
theta1 = 0
theta2 = 0
theta3 = 0
theta4 = 0
theta5 = 0
theta6 = 0
theta7 = 0

frames = 200
startRev = 40
end = startRev + frames
for i in range(end):
    plt.clf()
    #fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.view_init(vertical_axis='x')
    # Setting the axes properties
    ax.set_xlim3d([-0.7, 0.7])
    ax.set_xlabel('X')

    ax.set_ylim3d([-0.7, 0.7])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-0.7, 0.7])
    ax.set_zlabel('Z')


    # Animation code
    if (i > startRev and i < end):
        theta1 = (theta1 % (2 * np.pi)) + 0.03
        theta2 = (theta2 % (2 * np.pi)) + 0.02
        theta3 = (theta3 % (2 * np.pi)) + 0.03
        theta4 = (theta4 % (2 * np.pi)) + 0.02
        theta5 = (theta5 % (2 * np.pi)) + 0.03
        theta6 = (theta6 % (2 * np.pi)) + 0.02
        theta7 = (theta7 % (2 * np.pi)) + 0.03

    # Updating the matrices
    A1 = np.asarray([
        [np.cos(theta1), -np.cos(-np.pi/2)*np.sin(theta1),
         np.sin(-np.pi/2)*np.sin(theta1), 0.069*np.cos(theta1)],
        [np.sin(theta1), np.cos(-np.pi/2)*np.cos(theta1),
         -np.sin(-np.pi/2)*np.cos(theta1), 0.069*np.sin(theta1)],
        [0, np.sin(-np.pi/2), np.cos(-np.pi/2), 0.27035],
        [0, 0, 0, 1]])
    A2 = np.asarray([
        [np.cos(theta2 + np.pi/2), -np.cos(np.pi/2)*np.sin(theta2 + np.pi/2),
         np.sin(np.pi/2)*np.sin(theta2 + np.pi/2), 0],
        [np.sin(theta2 + np.pi/2), np.cos(np.pi/2)*np.cos(theta2 + np.pi/2),
         -np.sin(np.pi/2)*np.cos(theta2 + np.pi/2), 0],
        [0, np.sin(np.pi/2), np.cos(np.pi/2), 0.025], # 0.025 for visuals
        [0, 0, 0, 1]])
    A3 = np.asarray([
        [np.cos(theta3), -np.cos(-np.pi/2)*np.sin(theta3),
         np.sin(-np.pi/2)*np.sin(theta3), 0.069*np.cos(theta3)],
        [np.sin(theta3), np.cos(-np.pi/2)*np.cos(theta3),
         -np.sin(-np.pi/2)*np.cos(theta3), 0.069*np.sin(theta3)],
        [0, np.sin(-np.pi/2), np.cos(-np.pi/2), 0.36435],
        [0, 0, 0, 1]])
    A4 = np.asarray([
        [np.cos(theta4), -np.cos(np.pi/2)*np.sin(theta4),
         np.sin(np.pi/2)*np.sin(theta4), 0],
        [np.sin(theta4), np.cos(np.pi/2)*np.cos(theta4),
         -np.sin(np.pi/2)*np.cos(theta4), 0],
        [0, np.sin(np.pi/2), np.cos(np.pi/2), -0.025], # -0.025 for visuals
        [0, 0, 0, 1]])
    A5 = np.asarray([
        [np.cos(theta5), -np.cos(-np.pi/2)*np.sin(theta5),
         np.sin(-np.pi/2)*np.sin(theta5), 0.010*np.cos(theta5)],
        [np.sin(theta5), np.cos(-np.pi/2)*np.cos(theta5),
         -np.sin(-np.pi/2)*np.cos(theta5), 0.010*np.sin(theta5)],
        [0, np.sin(-np.pi/2), np.cos(-np.pi/2), 0.37429],
        [0, 0, 0, 1]])
    A6 = np.asarray([
        [np.cos(theta6), -np.cos(np.pi/2)*np.sin(theta6),
         np.sin(np.pi/2)*np.sin(theta6), 0],
        [np.sin(theta6), np.cos(np.pi/2)*np.cos(theta6),
         -np.sin(np.pi/2)*np.cos(theta6), 0],
        [0, np.sin(np.pi/2), np.cos(np.pi/2), 0.025], # 0.025 for visuals
        [0, 0, 0, 1]])
    A7 = np.asarray([
        [np.cos(theta7), -np.cos(0)*np.sin(theta7),
         np.sin(0)*np.sin(theta7), 0],
        [np.sin(theta7), np.cos(0)*np.cos(theta7),
         -np.sin(0)*np.cos(theta7), 0],
        [0, np.sin(0), np.cos(0), 0.3945],
        [0, 0, 0, 1]])
    # Alternate version of A7 with d=0 to mark the base of the end effector
    # for the sake of rendering it.
    A7Zero = np.asarray([
        [np.cos(theta7), -np.cos(0)*np.sin(theta7),
         np.sin(0)*np.sin(theta7), 0],
        [np.sin(theta7), np.cos(0)*np.cos(theta7),
         -np.sin(0)*np.cos(theta7), 0],
        [0, np.sin(0), np.cos(0), 0],
        [0, 0, 0, 1]])

    # Frame 0 (Origin)
    fullFrame0 = np.asarray([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    frame0 = [fullFrame0[0][3], fullFrame0[1][3],
              fullFrame0[2][3], fullFrame0[3][3]]
    # Colored joint head
    origin = np.asarray([
         [frame0[0]] * pixelCount,
         [frame0[1]] * pixelCount,
         np.linspace(frame0[2] - .05, frame0[2] + .05, pixelCount)
    ])

    # Frame 1
    fullFrame1 = np.dot(A1, fullFrame0)
    frame1 = [fullFrame1[0][3], fullFrame1[1][3],
              fullFrame1[2][3], fullFrame1[3][3]]
    # Colored joint head
    f1 = np.asarray([
        np.linspace(frame0[0], frame1[0], pixelCount),
        np.linspace(frame0[1], frame1[1], pixelCount),
        np.linspace(frame0[2], frame1[2], pixelCount)
    ])

    # Frame 2
    fullFrame2 = np.dot(np.dot(A1, A2), fullFrame0)
    frame2 = [fullFrame2[0][3], fullFrame2[1][3],
              fullFrame2[2][3], fullFrame2[3][3]]
    # Colored joint head
    f2 = np.asarray([
        np.linspace(frame1[0], frame2[0], pixelCount),
        np.linspace(frame1[1], frame2[1], pixelCount),
        np.linspace(frame1[2], frame2[2], pixelCount)
    ])

    # Frame 3
    fullFrame3 = np.dot(np.dot(np.dot(A1, A2), A3), fullFrame0)
    frame3 = [fullFrame3[0][3], fullFrame3[1][3],
              fullFrame3[2][3], fullFrame3[3][3]]
    # Colored joint head
    f3 = np.asarray([
        np.linspace(frame2[0], frame3[0], pixelCount),
        np.linspace(frame2[1], frame3[1], pixelCount),
        np.linspace(frame2[2], frame3[2], pixelCount)
    ])

    # Frame 4
    fullFrame4 = np.dot(np.dot(np.dot(np.dot(A1, A2), A3), A4), fullFrame0)
    frame4 = [fullFrame4[0][3], fullFrame4[1][3],
              fullFrame4[2][3], fullFrame4[3][3]]
    # Colored joint head
    f4 = np.asarray([
        np.linspace(frame3[0], frame4[0], pixelCount),
        np.linspace(frame3[1], frame4[1], pixelCount),
        np.linspace(frame3[2], frame4[2], pixelCount)
    ])

    # Frame 5
    fullFrame5 = np.dot(np.dot(np.dot(np.dot(np.dot(A1, A2), A3), A4), A5),
                        fullFrame0)
    frame5 = [fullFrame5[0][3], fullFrame5[1][3],
              fullFrame5[2][3], fullFrame5[3][3]]
    # Colored joint head
    f5 = np.asarray([
        np.linspace(frame4[0], frame5[0], pixelCount),
        np.linspace(frame4[1], frame5[1], pixelCount),
        np.linspace(frame4[2], frame5[2], pixelCount)
    ])

    # Frame 6
    fullFrame6 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(
                            A1, A2), A3), A4), A5), A6), fullFrame0)
    frame6 = [fullFrame6[0][3], fullFrame6[1][3],
              fullFrame6[2][3], fullFrame6[3][3]]
    # Colored joint head
    f6 = np.asarray([
        np.linspace(frame5[0], frame6[0], pixelCount),
        np.linspace(frame5[1], frame6[1], pixelCount),
        np.linspace(frame5[2], frame6[2], pixelCount)
    ])

    # Frame 7 (End Effector)
    fullFrame7 = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(
        A1, A2), A3), A4), A5), A6), A7), fullFrame0)
    frame7 = [fullFrame7[0][3], fullFrame7[1][3],
              fullFrame7[2][3], fullFrame7[3][3]]
    fullFrame7Zero = np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(np.dot(
        A1, A2), A3), A4), A5), A6), A7Zero), fullFrame0)
    frame7Zero = [fullFrame7Zero[0][3], fullFrame7Zero[1][3],
                  fullFrame7Zero[2][3], fullFrame7Zero[3][3]]

    # Colored end effector
    f7 = np.asarray([
        np.linspace(frame7[0], frame7Zero[0], pixelCount),
        np.linspace(frame7[1], frame7Zero[1], pixelCount),
        np.linspace(frame7[2], frame7Zero[2], pixelCount)
    ])

    # Plotting
    # Plotting frame 0
    ax.plot(origin[0], origin[1], origin[2], color='pink')
    # Plotting frame 1
    ax.plot(f1[0], f1[1], f1[2], color='red')
    # Plotting frame 2
    ax.plot(f2[0], f2[1], f2[2], color='orange')
    # Plotting frame 3
    ax.plot(f3[0], f3[1], f3[2], color='yellow')
    # Plotting frame 4
    ax.plot(f4[0], f4[1], f4[2], color='green')
    # Plotting frame 5
    ax.plot(f5[0], f5[1], f5[2], color='blue')
    # Plotting frame 6
    ax.plot(f6[0], f6[1], f6[2], color='purple')
    # Plotting frame 7 (end effector)
    ax.plot(f7[0], f7[1], f7[2], color='black')

    plt.pause(0.001)
