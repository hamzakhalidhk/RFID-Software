# RFID Python Based Software

## Note: This tutorial is available on my [Hackster](https://www.hackster.io/hamzakhalidonline/python-software-for-arduino-rfid-415a91) profile 

HK RFID Monitor is a Python-based software for RFID. It reads the data coming to COM port and displays it on your laptop screen. The data used in this project is IDs, names and roll numbers of students, coming from a micro-controller (AVR or simply Arduino). The software reads the values with the 'Serial' module of Python and displays it using 'Tkinker.'

![Screenshot](https://hackster.imgix.net/uploads/attachments/499136/whatsapp-image-2017-12-23-at-2-31-38-am-e1514208856685_rGfbGjmtZ3.jpeg?auto=compress%2Cformat&w=900&h=675&fit=min)

# How is the data coming to COM port?
In this project, Arduino is used to sending data to the COM port, so it is easier to understand that how the data is coming to COM port for those who have worked with Arduino or AVR microcontroller.

Let us assume that our microcontroller board (arduino UNO) is connected to COM port 4 of our PC and take the following dummy arduino code:

    void setup() {
      Serial.begin(9600);
      }
    void loop() {
        Serial.print("id=1000; name=Hamza Khalid; rollnumber=115;");
        Serial.print("\n ");
        delay(3000);
        Serial.print("id=1001; name=Ahmed Arif; rollnumber=120;");
        Serial.print("\n ");
        delay(3000);
        Serial.print("id=1002; name=Ammar Ahmed; rollnumber=142;");
        Serial.print("\n ");
        delay(3000);
    }

So, the output on Arduino's serial monitor will be:

    id=1000; name=Hamza Khalid; rollnumber=115;
    id=1001; name=Ahmed Arif; rollnumber=120;
    id=1002; name=Ammar Ahmed; rollnumber=142; (... continue)

# How is the software processing data?
The following line (Line 121) in our Python file allows you to type the port name on which the data is coming. As our arduino is connected to the port No. 4 so we write 'COM4' in the input box:

    Labelh=Label(root,text='Enter port Name. E.g: COM4',font=("Arial","14")).place(x=120,y=40)

The python program now starts reading 'COM4' and saves every line in a string with the help of following lines (Line 55,56):

    thing = self.ser.readline().decode('ascii')
            string = str(thing)
        
The program now does string parsing to separate the values of id, name and roll number of a student with the help of following lines (Line 72-83):

       for i in range(2, len(string)):
           if string[i] == ';':
               break
       v = string[3:i]
       for j in range(10, len(string)):
           if string[j] == ';':
               break
       c = string[i + 7:j]
        or k in range(20, len(string)):
           if string[k] == len(string):
               break
        p = string[j + 13:k-1]
        
# Storing in the database
The values of id, name and roll number are stored in variables v,c an p respectively. The values are then stored in sqlite3 database and are displayed on the software screen with the help of following lines:

    call.execute("INSERT INTO rfid (datestamp, id, name, rollnumber) VALUES (?,?,?,?)", (date, v, c, p))
                    conn.commit()
    call.execute('SELECT * FROM rfid ORDER BY datestamp DESC LIMIT 5')
    for row in call.fetchall():
        print(row)
    self.tree.insert("", 0, text="FETCHED --- >", values=(date, v, c, p))

# How to make changings for your own data?
It would be best if you made the following changes for your data:
1. You need to change the Arduino code, which is sending data to COM port. *Note that your source of sending data to the COM port can be anything, so make changes accordingly.*
2. Make changes in lines (61-72) of Python program, which are used for string-parsing to separate values from the string (in our case, alphanumeric values if the id, name, and roll number).
3. Change the names of columns in the database.
4. Change the tree used in the python code.

