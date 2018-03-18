# RFID Python Based Software
HK RFID Monitor is basically a Python based software for RFID. It reads the COM port and displays the data on a laptop screen. The data used in this project is id, name and roll number of a student coming from a micro-controller (AVR or simply arduino). The software reads the values with serial module of Python and displays it using tkinker.

# How is the data coming to COM port?
In this project arduino is used to send data on the COM port so it is easier to understand that how the data is coming to COM port for those who have worked with arduino or AVR. 

Let's assume that our microcontroller board (arduino UNO) is connected on COM port 4 of our PC and take the following dummy code of arduino:

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

So, the output on the Serial monitor will be:

    id=1000; name=Hamza Khalid; rollnumber=115;
    id=1001; name=Ahmed Arif; rollnumber=120;
    id=1002; name=Ammar Ahmed; rollnumber=142; (... continue)

# How is the software processing data?
The following line (Line 121) in our Python file allows you to type the port name on which the data is coming. As our arduino is connected to the port No. 4 so we will write 'COM4' in the input box:

Labelh=Label(root,text='Enter port Name. E.g: COM4',font=("Arial","14")).place(x=120,y=40)

The python program now starts reading COM4 and saves every line in a string with the help of following lines (Line 55,56):

thing = self.ser.readline().decode('ascii')
        string = str(thing)
        
The program now does string parsing to separate the values of id, name and roll number of a student with the help of follwing lines (Line 72-83):

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

# How to make changings for your customized data?
You need to make the following changes for your own data:

1. You need to change the Arduino code which is sending data to COM port. 
*Note that your source of sending data to the COM port can be anything so make changes accordingly.

2. Make changes in the lines (61-72) of python program which are used for string parsing to separate values from the string (in our case numeric values if id, name and roll number).

3. Change names of columns in the database and of tree used in the python code.

