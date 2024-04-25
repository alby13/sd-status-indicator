# sd-status-indicator  
**Stable Diffusion Status Indicator Utility**  
**SD Status Indicator**  
<br>
**About**<br>
The SD Status Indicator is a Python utility that monitors CPU and GPU usage to notify the user when Stable Diffusion is ready to be used. The program displays a graphical window with a circle that turns red when GPU usage exceeds 70%.<br>
<br>
**Features**<br>
Monitors CPU and GPU usage, and creates a window that stays on top<br>
Displays a graphical window with a circle that turns red when GPU usage exceeds 70%<br>
Provides a simple and intuitive interface for users to monitor Stable Diffusion status<br>
<br>
**Requirements**<br>
Python 3.x<br>
Tkinter library<br>
psutil library<br>
GPUtil library<br>
<br>
**System Requirements**<br>
- Nvidia GPU<br>
<br>
**Known Issues**<br>
<br>
**Known Issues**<br>
- The CPU reading may not be extremely accurate.<br>
- The program has been tested to work best when run through native Linux or the Windows Command Prompt, as the "stay on top" function may not work correctly in virtual environments.<br>
- Testing without a GPU has resulted in an error.<br>
**Usage**<br>
Clone this repository to your local machine.<br>
Install the required libraries by running pip install -r requirements.txt.<br>
Run the script by executing python sd-status-indicator.py.<br>
The graphical window will appear, displaying the CPU and GPU usage.<br>
<br>
**License**<br>
**Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use the Software solely for the purpose of developing, testing, and using with artificial intelligence (AI) and machine learning (ML) applications.**<br>
**Restrictions**<br>
The Software shall not be used for any purpose other than developing, testing, and using with AI and ML applications.<br>
The Software shall not be modified, reverse-engineered, or distributed without the express written permission of the copyright holder.<br>
The Software shall not be used for commercial purposes without the express written permission of the copyright holder.<br>
**Warranty Disclaimer**<br>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.<br>
<br>
**Copyright**<br>
Copyright (C) 2024 alby13. All rights reserved.<br>
<br>
**Author**<br>
alby13<br>
<br>
**Version**<br>
v1.0 - April 24, 2024<br>
