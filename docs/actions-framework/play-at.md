# Play video or audio segment

The play behavior causes the `.ve-media` viewer to play a video or audio clip starting at a specified time.  A second time value may optionally be used to define a stop time.  If a stop time is not provided the clip will play from the start time to the end.  The values for the start and end times are specified in **hh:mm:ss** notation.  The **hh** and **mm** values are optional.  For example:

- **30**: `==start playing 30 seconds into clip=={30}`
- **1:30**: `==start playing 90 seconds into clip=={1:30}`
- **15:00**: `==start playing 15 minutes into clip=={15:00}`
- **1:10:00**: `==start playing 1 hour and 10 minutes into clip=={1:10:00}`
- **5:30,6:00**: `==play from 5:30 to 6:00=={5:30,6:00}`
