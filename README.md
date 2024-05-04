# sd-status-indicator  
**Stable Diffusion Status Indicator Utility**  
**SD Status Indicator**  
  
**About**  
The SD Status Indicator is a Python utility that monitors CPU and GPU usage to notify the user when Stable Diffusion is ready to be used. The program displays a graphical window with a circle that turns red when GPU usage exceeds 70%.  
  
**Features**  
Monitors CPU and GPU usage, and creates a window that stays on top  
Displays a graphical window with a circle that turns red when GPU usage exceeds 70%  
Provides a simple and intuitive interface for users to monitor Stable Diffusion status  

**2 Flavors**  
SD Status Indicator now comes in two flavors.
- Windows
- Linux (Python Script)
  
**System Requirements**  
- Nvidia GPU

**Linux/Python Requirements**  
Python 3.x  
Tkinter library  
psutil library  
GPUtil library  
  
  
**Known Issues**  
- The CPU reading may not be extremely accurate.  
- The program has been tested to work best when run through native Linux or the Windows Command Prompt, as the "stay on top" function may not work correctly in virtual environments.  
- Testing without a GPU has resulted in an error.
  
**Usage**  
Clone this repository to your local machine.  
Install the required libraries by running pip to install the requirements.  
Run the script by executing python sd-status-indicator.py.  
The graphical window will appear, displaying the CPU and GPU usage.  
  
**License**  
**Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use the Software solely for the purpose of developing, testing, and using with artificial intelligence (AI) and machine learning (ML) applications.**  
**Restrictions**  
The Software shall not be used for any purpose other than developing, testing, and using with AI and ML applications.  
The Software shall not be modified, reverse-engineered, or distributed without the express written permission of the copyright holder.  
The Software shall not be used for commercial purposes without the express written permission of the copyright holder.  
**Warranty Disclaimer**  
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
  
**Copyright**  
Copyright (C) 2024 alby13. All rights reserved.  
  
**Author**  
alby13  
  
**Version**  
v1.0 - April 24, 2024  
Readme Updated May 03, 2024
