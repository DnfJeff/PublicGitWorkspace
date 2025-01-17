
# **File Directory CSV Generator**  
*Simple tool for scanning directories and generating CSV file lists.*

---

### **Overview**  
This tool allows you to easily scan any folder on your system, including its subdirectories, and create a CSV file with the names and full paths of all files. It’s packaged as a precompiled executable for Windows, ready for easy use.

---

### **Warning: Please Read Before Running!**  
**Important**: This program scans directories recursively, which can potentially lead to long processing times and very large CSV files if high-level or system directories are selected.  
- **Avoid selecting** the root directory (C:/) or large system folders.
- **Large folders** with thousands of files can lead to a **slow process** or **overwhelming CSV output** that might be hard to open in spreadsheet software.

---

### **Goal**  
- Quickly generate a CSV file listing the full paths and names of all files in a chosen directory.
- Useful for organizing large directories, backing up files, or generating reports on your file structure.

---

### **How to Use**  
1. **Download and Extract**  
   Download the repository from GitHub and extract it to a folder. Inside the `dist/` folder, you'll find the precompiled `.exe` file ready to run.

2. **Run the Program**  
   - Double-click `CSVmaker.exe` to launch the application.

3. **Select the Input Directory**  
   - Click on **"Select Input Directory"** to choose the folder you want to scan.  
   - **Tip**: For optimal performance, avoid scanning large system directories or the root directory.

4. **Select Output Directory**  
   - Click on **"Select Output Directory"** to choose where you want to save the resulting CSV file.

5. **Enter CSV File Name**  
   - In the **"CSV name here"** field, enter a name for your CSV file (e.g., `file_list`). The `.csv` extension will be automatically added.

6. **Generate CSV**  
   - Click on **"Start CSV Creation"** to begin the process. The program will scan the selected directory and generate the CSV file in the output folder.

7. **Review the Output**  
   - Once the process is complete, check the output directory for your CSV file, which will list all file names and their full paths.

---

### **Example CSV Output**  
The generated CSV will look something like this:

```csv
File Name, Full Directory
image1.jpg, C:/path/to/folder/image1.jpg
video1.mp4, C:/path/to/folder/subfolder/video1.mp4
document.txt, C:/path/to/folder/subfolder2/document.txt
```

---

### **Key Features**  
- **No installation required**: Simply run the `.exe` file from the `dist` folder.
- **Easy Directory Selection**: Browse through your directories with the intuitive file picker.
- **Customizable CSV Name**: Specify your own name for the CSV file.

---

### **Considerations**  
- **Avoid Scanning Large Directories**: Directories with many subdirectories and files can take a long time to scan. Consider testing with smaller folders first if you are unsure.
- **File Access**: Ensure you have the necessary permissions to access the selected files. If a file is locked or inaccessible, it will be skipped.
- **Large CSV Files**: The output CSV can grow significantly in size depending on the number of files. Be aware that very large CSV files might be slow to open or manage.

---

### **License**  
This tool is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### **Troubleshooting**  
- **Program Freezes or Takes Too Long**: If the program is taking too long, try using a smaller directory. Large directories (especially those with thousands of files) may slow down the process.
- **Access Denied Errors**: Make sure you have the appropriate permissions to access the directories and files being scanned. Run the program as an administrator if necessary.
- **File Output Issues**: If the CSV file seems empty or incomplete, try running the program on a smaller directory to ensure it’s working properly.

---

**Happy File Organizing!**  
We hope this tool helps you easily manage and organize your files! If you run into any issues or need further assistance, please feel free to open an issue on our [GitHub repository](https://github.com/your-repo).
