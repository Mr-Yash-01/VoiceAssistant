import pyttsx3.engine
import speech_recognition as sr
import datetime
import wikipedia
import AppOpener as ao
import os
import setuptools
import geocoder
from geopy.geocoders import Nominatim
import time
from threading import Thread
from tkinter import messagebox

class Func_Jarvis():

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(self,audio):

        self.engine.say(audio)
        self.engine.runAndWait()


    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\n\tListening...")
            r.pause_threshold = 1
            r.energy_threshold = 4000
            audio = r.listen(source)
        try:
            print("\tRecognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"\tUser said: {query}\n")
        except Exception as e:
            print("\tSay that again please...")
            return None
        return query

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("Good Morning!")
        elif hour >= 12 and hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("I am Jarvis 2.0 Sir. Please tell me how may I help you")


    def Listing_File(self):
        self.dir_Files = {}
        self.file_fetching = False
        for d in ['C','D','E','F']:
            try:
                for (root, dirs, files) in os.walk(f'{d}:\\', topdown=True):
                    for i in files:
                        self.dir_Files[i] = root
                    for i in dirs:
                        self.dir_Files[i] = root
                    for i in root:
                        self.dir_Files[i] = root
            except Exception as e:
                pass
        self.file_fetching = True
        messagebox.showinfo("JARVIS 2.0","File fetching is done!!")

if __name__ == '__main__':

    # LISTS
    user_manual = "\n\tCOMMANDS:\n\tto open the user manual(open the user manual)\n\tto open the wikipedia(__object__ wikipedia)" \
                  "\n\tto open the app(open the __app_name__)\n\tto open saved files(open the files then say file name)\n\tto close the app(close the __app_name__)\n\tto play music(play __song_name__)\n\tto restart pc or shutdown or close the JARVIS 2.0 or location(admin commands)\n\tto convert objects(obj1 convert obj2 )\n\tto do basic calculations(Let's do some calculations ,\tthen enter calculations example say : three plus five) \n\tfor google search(search obj))"
    user_info = "\n\t_______  ______  _____  _    _  _______  _______    _______      _________" \
                "\n\t   |     |    |  |   |  |    |     |     |                |      |       |\n\t   |     |____|  |___|  |    |     |     |______    ______|      |       |\n\t   |     |    |  |\\     |    |     |           |    |            |       |\n\t|__|     |    |  | \\     \\__/   ___|___  ______|    |______ |__| |_______|\n\t\n\tUSER INFO:\n\thello guys!!\n\tI am JARVIS 2.0\n\tI can make your work easier.\n\tI took 30 sec afer running the app to load the all files in your device.\n\tI can open your apps,your files(for this version only files which are saved in C: drive),\n\tI can search on google,also play music,also work in offline mode(some specific commands),\n\thistory,wikipedia,shutdown restart close the JARVIS 2.0(via commanding admin commands)and etc.\n\tTHANK YOU FOR CALLING"

    positiveacknowledgement = ['yes','ha', 'han', 'yahh', 'yess', 'yes', 'right', 'obviously', 'ha ha', 'yes yes', 'yupp',
                               'always', 'sure']
    negativeacknowledgement = ['noooo','Nahin','nope', 'no', 'no no', 'na', 'nahi', 'not', 'nothing', 'na na', 'nhi', 'none', 'None',
                               'never', 'obviously not', 'not sure']
    errorextentionlist = [' dot apk', ' dot bat', ' dot mp3', ' dot pdf', ' dot doc', ' dot docx',
                          ' dot css', ' dot htm', ' dot html', ' dot js', ' dot jsp', ' dot part', ' dot php',
                          ' dot rss', ' dot xhtml', ' dot ai', ' dot bmp', ' dot gif', ' dot ico', ' dot jpeg',
                          ' dot jpg', ' dot max', ' dot obj', ' dot png', ' dot txt', ' dot bin', ' dot mp4',
                          ' dot cgi', ' dot com', ' dot exe', ' dot jar', ' dot py', ' dot wsf', ' dot aif',
                          ' dot cda', ' dot iff', ' dot mid', ' dot midi', ' dot mpa', ' dot wav', ' dot wma',
                          ' dot wpl', ' dot avi', ' dot flv', ' dot h264', ' dot m4v', ' dot mkv', ' dot mov',
                          ' dot mpg', ' dot mpeg', ' dot rm', ' dot swf', ' dot vob', ' dot wmv', ' dot 3g2',
                          ' dot 3gp', ' dot odt', ' dot msg', ' dot rtf', ' dot tex', ' dot wks', ' dot wps',
                          ' dot wpd', ' dot ods', ' dot xlr', ' dot xls', ' dot xlsx', ' dot key', ' dot odp',
                          ' dot pptx', ' dot accdb', ' dot csv', ' dot dat', ' dot db', ' dot dbf', ' dot log',
                          ' dot mdb', ' dot pdb', ' dot sav', ' dot sql', ' dot tar', ' dot bak', ' dot cab',
                          ' dot cfg', ' dot cpl', ' dot cur', ' dot dll', ' dot dmp', ' dot drv', ' dot icns',
                          ' dot ico', ' dot ini', ' dot lnk', ' dot msi', ' dot sys', ' dot tmp', ' dot asp',
                          ' dot aspx', ' dot cer', ' dot cfm', ' dot cgi', ' dot pl', ' dot ps', ' dot psd',
                          ' dot svg', ' dot tif ', ' dot tiff', ' dot 3ds', ' dot 3dm', ' dot APK', ' dot 3DM',
                          ' dot BAT', ' dot MP3', ' dot PDF', ' dot DOC', ' dot DOCX', ' dot CSS', ' dot HTM',
                          ' dot HTML', ' dot JS', ' dot JSP', ' dot PART', ' dot PHP', ' dot RSS', ' dot XHTML',
                          ' dot AI', ' dot BMP', ' dot GIF', ' dot ICO', ' dot JPEG', ' dot JPG', ' dot MAX',
                          ' dot OBJ', ' dot PNG', ' dot TXT', ' dot BIN', ' dot MP4', ' dot CGI', ' dot COM',
                          ' dot EXE', ' dot JAR', ' dot PY', ' dot WSF', ' dot AIF', ' dot CDA', ' dot IFF',
                          ' dot MID', ' dot MIDI', ' dot MPA', ' dot WAV', ' dot WMA', ' dot WPL', ' dot AVI',
                          ' dot FLV', ' dot H264', ' dot M4V', ' dot MKV', ' dot MOV', ' dot MPG', ' dot MPEG',
                          ' dot RM', ' dot SWF', ' dot VOB', ' dot WMV', ' dot 3G2', ' dot 3GP', ' dot ODT',
                          ' dot MSG', ' dot RTF', ' dot TEX', ' dot WKS', ' dot WPS', ' dot WPD', ' dot ODS',
                          ' dot XLR', ' dot XLS', ' dot XLSX', ' dot KEY', ' dot ODP', ' dot PPTX', ' dot 3DS',
                          ' dot ACCDB', ' dot CSV', ' dot DAT', ' dot DB', ' dot DBF', ' dot LOG', ' dot MDB',
                          ' dot PDB', ' dot SAV', ' dot SQL', ' dot TAR', ' dot BAK', ' dot CAB', ' dot CFG',
                          ' dot CPL', ' dot CUR', ' dot DLL', ' dot DMP', ' dot DRV', ' dot ICNS', ' dot ICO',
                          ' dot INI', ' dot LNK', ' dot MSI', ' dot SYS', ' dot TMP', ' dot ASP', ' dot ASPX',
                          ' dot CER', ' dot CFM', ' dot CGI', ' dot PL', ' dot PS', ' dot PSD', ' dot SVG',
                          ' apk', ' bat', ' mp3', ' pdf', ' doc', ' docx', ' css', ' htm', ' dot TIF dot ',
                          ' html', ' js', ' jsp', ' part', ' php', ' rss', ' xhtml', ' ai', ' bmp', ' gif',
                          ' ico', ' jpeg', ' jpg', ' max', ' obj', ' png', ' txt', ' bin', ' mp4', ' cgi',
                          ' com', ' exe', ' jar', ' py', ' wsf', ' aif', ' cda', ' iff', ' mid', ' midi',
                          ' mpa', ' wav', ' wma', ' wpl', ' avi', ' flv', ' h264', ' m4v', ' mkv', ' mov',
                          ' mpg', ' mpeg', ' rm', ' swf', ' vob', ' wmv', ' 3g2', ' 3gp', ' odt', ' msg',
                          ' rtf', ' tex', ' wks', ' wps', ' wpd', ' ods', ' xlr', ' xls', ' xlsx', ' key',
                          ' odp', ' pptx', ' accdb', ' csv', ' dat', ' db', ' dbf', ' log', ' mdb', ' pdb',
                          ' sav', ' sql', ' tar', ' bak', ' cab', ' cfg', ' cpl', ' cur', ' dll', ' dmp',
                          ' drv', ' icns', ' ico', ' ini', ' lnk', ' msi', ' sys', ' tmp', ' asp', ' aspx',
                          ' cer', ' cfm', ' cgi', ' pl', ' ps', ' psd', ' svg', ' tif ', ' tiff', ' 3ds',
                          ' 3dm', ' APK'' 3DM', ' BAT', ' MP3', ' PDF', ' DOC', ' DOCX', ' CSS', ' HTM', ' HTML', ' JS',
                          ' JSP', ' PART', ' PHP', ' RSS', ' XHTML', ' AI', ' BMP', ' GIF', ' ICO', ' JPEG', ' JPG',
                          ' MAX', ' OBJ', ' PNG', ' TXT', ' BIN', ' MP4', ' CGI', ' COM', ' EXE', ' JAR', ' PY', ' WSF',
                          ' AIF', ' CDA', ' IFF', ' MID', ' MIDI', ' MPA', ' WAV', ' WMA', ' WPL', ' AVI', ' FLV',
                          ' H264', ' M4V', ' MKV', ' MOV', ' MPG', ' MPEG', ' RM', ' SWF', ' VOB', ' WMV', ' 3G2',
                          ' 3GP', ' ODT', ' MSG', ' RTF', ' TEX', ' WKS', ' WPS', ' WPD', ' ODS', ' XLR', ' XLS',
                          ' XLSX', ' KEY', ' ODP', ' PPTX', ' 3DS', ' ACCDB', ' CSV', ' DAT', ' DB', ' DBF', ' LOG',
                          ' MDB', ' PDB', ' SAV', ' SQL', ' TAR', ' BAK', ' CAB', ' CFG', ' CPL', ' CUR', ' DLL',
                          ' DMP', ' DRV', ' ICNS', ' ICO', ' INI', ' LNK', ' MSI', ' SYS', ' TMP', ' ASP', ' ASPX',
                          ' CER', ' CFM', ' CGI', ' PL', ' PS', ' PSD', ' SVG', ' dot TIFF', ]

    extentionlist = ['.apk', '.bat', '.mp3', '.pdf', '.doc', '.docx', '.css', '.htm', '.html', '.js',
                     '.jsp', '.part', '.php', '.rss', '.xhtml', '.ai', '.bmp', '.gif', '.ico', '.jpeg',
                     '.jpg', '.max', '.obj', '.png', '.txt', '.bin', '.mp4', '.cgi', '.com', '.exe',
                     '.jar', '.py', '.wsf', '.aif', '.cda', '.iff', '.mid', '.midi', '.mpa', '.wav',
                     '.wma', '.wpl', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg',
                     '.rm', '.swf', '.vob', '.wmv', '.3g2', '.3gp', '.odt', '.msg', '.rtf', '.tex',
                     '.wks', '.wps', '.wpd', '.ods', '.xlr', '.xls', '.xlsx', '.key', '.odp', '.pptx',
                     '.accdb', '.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.pdb', '.sav', '.sql',
                     '.tar', '.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns',
                     '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp', '.asp', '.aspx', '.cer', '.cfm',
                     '.cgi', '.pl', '.ps', '.psd', '.svg', '.tif ', '.tiff', '.3ds', '.3dm']

    sillyquetions = {"how are you": "I am fine", "who are you": "I am JARVIS 2.0", "what is your name": "JARVIS 2.0",
                     "I love u": "sorry I have no access for emotions.",
                     "are you tired": "no i am machine so not", "what did you eat": "electricity",
                     "i am very happy with u": "ohh its my pleasure"}

    command_history = []

    root = Func_Jarvis()


    # MAIN
    print(user_info)
    print(user_manual)
    daemon = Thread(target=root.Listing_File, daemon=True, name='Monitor')
    daemon.start()
    root.wishMe()

    try:
        import pywhatkit as kt
        while True:
            query = root.takeCommand()


            if query == None:
                pass

            elif 'open the history' == query.lower():
                try:
                    no = 1
                    root.speak("opening history")
                    print("\tHISTORY:")
                    for i in command_history:
                        print("\t" + str(no) + "." + i)
                        no += 1
                except Exception as e:
                    root.speak("error plz speak again")

            elif 'open the user manual' in query.lower() or 'open user manual' in query.lower():
                try:
                    root.speak("opening user manual")
                    print(user_manual)
                    command_history.append(str(query))
                except Exception as e:
                    root.speak("error plz speak again")

            elif 'wikipedia' in query.casefold():
                command_history.append(str(query))
                try:
                    root.speak('Searching Wikipedia...')
                    results = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
                    root.speak("According to Wikipedia")
                    print("\t"+results)
                    root.speak(results)
                except Exception as e:
                    root.speak("error plz speak again")

            elif query.lower() in sillyquetions.keys():
                linetospeak = sillyquetions[query.lower()]
                root.speak(linetospeak)
                command_history.append(str(query))

            elif 'open the youtube' in query.casefold():
                try:
                    root.speak("opening youtube")
                    kt.search("https://www.youtube.com/")
                    command_history.append(str(query))
                except Exception as e:
                    root.speak("error plz speak again")

            elif 'open the google' in query.casefold():
                try:
                    root.speak("Its time to search ??")
                    kt.search("https://www.google.com/")
                    command_history.append(str(query))
                except Exception as e:
                    root.speak("error plz speak again")

            elif 'open the file' in query.casefold():
                if root.file_fetching == False:
                    root.speak("File fetching is not yet completed plz try after couple of mintues")
                else:
                    try:
                        root.speak("ok, what is the name of file?")
                        onlinefilename = root.takeCommand()
                        while onlinefilename== None:
                            root.speak("Sorry I cant get it plz speak again")
                            onlinefilename = root.takeCommand()
                        root.speak("Is it right?")
                        while True:
                            response = root.takeCommand()
                            fileopencode = False
                            if response in positiveacknowledgement:
                                root.speak("Searching!")
                                try:
                                    # perfect name
                                    for i in extentionlist:
                                        if i in onlinefilename:
                                            for i in root.dir_Files.keys():
                                                if onlinefilename == i.casefold():
                                                    os.startfile(root.dir_Files[i]+ "\\" + onlinefilename)
                                                    command_history.append(str(query) + "--" + root.dir_Files[i]+ "\\" + onlinefilename)
                                                    fileopencode = True
                                                    break
                                            break
                                    if fileopencode == True:
                                        break

                                    # errorfilename
                                    expectederrorfiles = {}
                                    errornameaccess = False
                                    for i in errorextentionlist:
                                        if i in onlinefilename:
                                            if " dot " in i:
                                                onlinefilename = onlinefilename.replace(i,"")
                                                i = i.replace(" dot ",".")
                                                onlinefilename = onlinefilename + i.lower()
                                            elif " " in i:
                                                onlinefilename = onlinefilename.replace(i,"")
                                                i = i.replace(" ",".")
                                                onlinefilename = onlinefilename+i.lower()
                                            errornameaccess = True
                                            break
                                    if errornameaccess == True:
                                        for j in root.dir_Files.keys():
                                            if onlinefilename.casefold() == j.casefold():
                                                tempaddress = root.dir_Files[j]
                                                fileaddress = tempaddress + "\\" + onlinefilename
                                                expectederrorfiles[j] = fileaddress
                                        if len(expectederrorfiles)>0:
                                            index = 1
                                            for i in expectederrorfiles.keys():
                                                print("\t"+str(index) + "." + i)
                                                index = index + 1
                                            userindex = input("\tEnter your choice: ")
                                            choiceindex = 1
                                            fileopencode = 0
                                            for i in expectederrorfiles.keys():
                                                if int(choiceindex) == int(userindex):
                                                    tobeopenfile = str(i)
                                                    os.startfile(expectederrorfiles[tobeopenfile])
                                                    command_history.append(str(query) + "--" + expectederrorfiles[tobeopenfile])
                                                    fileopencode = fileopencode + 1
                                                    break
                                                else:
                                                    choiceindex = choiceindex + 1
                                        else:
                                            root.speak("File doesnt exist")
                                            command_history.append(str(query) + "-- file doesnt exist")
                                        if fileopencode == 1 :
                                            break

                                    # filename
                                    expectedfiles = {}
                                    for i in extentionlist:
                                        filename = onlinefilename + i
                                        for j in root.dir_Files.keys():
                                            if filename.casefold() == j.casefold():
                                                tempaddress = root.dir_Files[j]
                                                fileaddress = tempaddress + "\\" + filename
                                                expectedfiles[j] = fileaddress
                                    if len(expectedfiles)>0:
                                        index = 1
                                        for i in expectedfiles.keys():
                                            print("\t"+str(index) + "." + i)
                                            index = index + 1

                                        userindex = input("\tEnter your choice: ")
                                        choiceindex = 1
                                        for i in expectedfiles.keys():
                                            if int(choiceindex) == int(userindex):
                                                tobeopenfile = str(i)
                                                os.startfile(expectedfiles[tobeopenfile])
                                                command_history.append(str(query) + "--" + expectedfiles[tobeopenfile])
                                                break
                                            else:
                                                choiceindex = choiceindex + 1
                                    else:
                                        root.speak("File doesnt exist")
                                        command_history.append(str(query) + "-- file doesnt exist")
                                except Exception as e:
                                    root.speak("File doesnt exist")
                                    command_history.append(str(query) + "-- file doesnt exist")
                                break
                            elif response in negativeacknowledgement:
                                root.speak("sorry sir, I apologize! plz,manually enter the file name.")
                                manualfilename = input("\tEnter the file name here: ")
                                root.speak("Searching!")
                                try:
                                    expectedfiles = {}
                                    # perfect name
                                    for i in extentionlist:
                                        if i or i.upper() in manualfilename:
                                            for i in root.dir_Files.keys():
                                                if manualfilename == i:
                                                    tempaddress = root.dir_Files[i]
                                                    fileaddress = tempaddress + "\\" + manualfilename
                                                    os.startfile(fileaddress)
                                                    command_history.append(str(query) + "--" + str(fileaddress))
                                                    fileopencode = True
                                                    break
                                            break
                                    if fileopencode == True:
                                        break

                                    # filename
                                    for i in extentionlist:
                                        filename = manualfilename + i

                                        for j in root.dir_Files.keys():
                                            tempfilename = str(j)
                                            if filename.casefold() == tempfilename.casefold():
                                                tempaddress = root.dir_Files[tempfilename]
                                                fileaddress = tempaddress + "\\" + filename
                                                expectedfiles[j] = fileaddress
                                    if len(expectedfiles) > 0:
                                        index = 1
                                        for i in expectedfiles.keys():
                                            print("\t"+str(index) + "." + i)
                                            index = index + 1

                                        userindex = input("\tEnter your choice: ")
                                        choiceindex = 1
                                        for i in expectedfiles.keys():
                                            if int(choiceindex) == int(userindex):
                                                tobeopenfile = str(i)
                                                os.startfile(expectedfiles[tobeopenfile])
                                                command_history.append(str(query) + "--" + str(expectedfiles[tobeopenfile]))
                                                break
                                            else:
                                                choiceindex = choiceindex + 1
                                    else:
                                        root.speak("File doesnt exist")
                                        command_history.append(str(query) + "-- file doesnt exist")
                                        break

                                except Exception as e:
                                    root.speak("File doesnt exist")
                                break
                            else:
                                root.speak("plz answer in positive or negative acknowledgment")
                    except Exception as e:
                        root.speak("error plz speak again")

            elif 'open' in query.casefold():
                querynull = query
                try:
                    if 'open the' in query:
                        query = query.replace("open the ","",5)
                    else:
                        query = query.replace("open ","",5)
                    root.speak("opening "+query)
                    ao.run(query)
                    command_history.append(str(querynull))
                except Exception as e:
                    root.speak("Application name unmatch")
                    command_history.append(str(query) + "-- file doesnt match")

            elif 'play' in query.casefold():
                try:
                    query = query.replace("play ", "", 5)
                    query = query.replace(" ", "+", 50)
                    query = "https://www.youtube.com/results?search_query="+query
                    print("\t"+query+"\n")
                    kt.search(query)
                    command_history.append("song--"+str(query))
                except Exception as e:
                    root.speak("error plz speak again")
                    command_history.append(query + "-- error")

            elif 'admin commands' == query.casefold().strip():
                root.speak("Add 2 spaces to enter in admin mode")
                while (input("\tEnter double spaces to proceed:")!= "  "):
                    pass
                try:
                    powercommand = {1:"shutdown /s /t 10",2:"shutdown /r /t 10",3:"taskkill /f /im JARVIS_2.0.exe"}
                    maincommand = None
                    print("\t1.Shutdown\n\t2.Restart\n\t3.close JARVIS 2.0\n\t4.Location\n\t5.Exit")
                    while True:
                        usercommand = int(input("\tEnter the command here: "))
                        if usercommand == 1:
                            maincommand = powercommand[usercommand]
                            root.speak("laptop is going to be shutdown in 10 seconds")
                            os.system(maincommand)
                            break
                        elif usercommand == 2:
                            maincommand = powercommand[usercommand]
                            root.speak("laptop is going to be restart in 10 seconds")
                            os.system(maincommand)
                            break
                        elif usercommand == 3:
                            maincommand = powercommand[usercommand]
                            root.speak("ok then good bye sir and have a nice day")
                            os.system(maincommand)
                            break
                        elif usercommand == 4:
                            try:
                                geolocator = Nominatim(user_agent="MyApp")
                                g = geocoder.ip('me')
                                coordinates = f"{g.latlng[0]} , {g.latlng[1]}"
                                location = geolocator.reverse(coordinates)
                                address = location.raw['address']
                                city = address.get('city', '')
                                state = address.get('state', '')
                                print(f"\tNear by {city} in {state}")
                                root.speak(f"I am not sure but, I think your near by {city} in {state}")
                                command_history.append(query)
                                break
                            except Exception as e:
                                root.speak("error plz speak again")
                                command_history.append(query + "-- error")
                        elif usercommand == 5:
                            break
                        else:
                            print("\tplzz enter valid command number.")

                except Exception as e:
                    root.speak("error plz speak again")
                    command_history.append(query + "-- error")

            elif 'convert' in query.casefold():
                try:
                    kt.search(query)
                    command_history.append(query)
                except Exception as e:
                    root.speak("error plz speak again")
                    command_history.append(query + "-- error")

            elif 'close the' in query.casefold():
                try:
                    querynull= query
                    query = query.replace("close the ","")
                    command = "taskkill /f /im "+query.lower()+".exe"
                    os.system(command)
                    command_history.append(querynull )
                    querynull = None
                except Exception as e:
                    root.speak("Application name doesnt match")
                    command_history.append(query + "-- error")

            elif 'do some calculation' in query.casefold():
                root.speak("Okay lets start")
                try:
                    while True:
                        try:
                            query = root.takeCommand()
                            if 'finish' in query.lower():
                                break
                            query = query.replace('x', '*')
                            query = query.replace('into','*')
                            query = query.replace('raised to','**')
                            query = query.replace('raise to','**')
                            query = query.replace('to the power','**')
                            query = query.replace('in bracket','(')
                            query = query.replace('bracket close',')')
                            query = query.replace('close bracket',')')
                            root.speak("It's "+str(eval(query)))
                            print(f"\tAnswer is: {eval (query)}")
                            command_history.append(query +"="+ str(eval(query)))
                        except Exception as e:
                            root.speak("I can't understand plz speak again")
                    root.speak("It was amazing")
                except Exception as e:
                    root.speak("error plz speak again")
                    command_history.append(query + "-- error")

            elif query[:6] == 'search':
                try:
                    query = query[6:].strip()
                    kt.search(query)
                    command_history.append("Searched "+query)
                except Exception as e:
                    root.speak("error plz speak again")
                    command_history.append("error in searching "+query)

    except Exception as e:
        root.speak("checking the status...")
        time.sleep(0.5)
        root.speak("You are offline")
        root.speak("you can do some specific commands in offline mode")
        while True:
            print("\n\tCOMMANDS:\n\t\t1.admin commands-shutdown/restart\t\t2.to open the application write -- open the App_name\n\t\t3.to open the saved files\t\t\t\t4.History\n\t\t5.User Manual\n\t(to use enter the digit of command)")
            query = int(input("\tEnter the command:").strip())
            if query == None:
                pass

            elif 5 == query:
                try:
                    print(user_manual)
                    command_history.append(query)
                except Exception as e:
                    root.speak("error plz speak again")



            elif 4 == query:
                try:
                    root.speak("opening history")
                    no = 1
                    print("\tHISTORY:")
                    for i in command_history:
                        print("\t" + str(no) + "." + i)
                        no += 1
                except Exception as e:
                    root.speak("error plz speak again")

            elif 3 == query:
                if root.file_fetching == False:
                    root.speak("File fetching is not yet completed plz try after couple of mintues")
                else:
                    try:
                        root.speak("ok, what is the name of file?")
                        offlinefilename = str(input("\tEnter the file name:"))
                        root.speak("Searching!")
                        fileopencode = 0
                        expectederrorfiles = {}
                        expectedfiles = {}

                        while True:

                            # perfect name
                            for i in extentionlist:
                                if i in offlinefilename.lower():
                                    for j in root.dir_Files.keys():
                                        if offlinefilename == j:
                                            tempaddress = root.dir_Files[j]
                                            fileaddress = tempaddress + "\\" + offlinefilename
                                            os.startfile(fileaddress)
                                            fileopencode += 1
                                            command_history.append("open the file-- " + str(fileaddress))
                                            break
                                    break
                            if fileopencode == 1:
                                fileopencode = 0
                                break

                            # error name
                            fileopencode = 0
                            errornameaccess = 0
                            no = 1
                            for i in errorextentionlist:
                                if i in offlinefilename:
                                    if " dot " in i:
                                        offlinefilename = offlinefilename.replace(i, "")
                                        i = i.replace(" dot ", ".")
                                        offlinefilename = offlinefilename + i.lower()
                                    elif " " in i:
                                        offlinefilename = offlinefilename.replace(i, "")
                                        i = i.replace(" ", ".")
                                        offlinefilename = offlinefilename + i.lower()
                                    errornameaccess += 1
                            if errornameaccess > 0:
                                for i in root.dir_Files.keys():
                                    if offlinefilename.casefold() == i.casefold():
                                        tempaddress = root.dir_Files[i]
                                        fileaddress = tempaddress + "\\" + offlinefilename
                                        expectederrorfiles[i] = fileaddress
                                if len(expectederrorfiles) > 0:
                                    print("\tchoose the file:")
                                    for i in expectederrorfiles.keys():
                                        print("\t" + str(no) + "." + i)
                                        print(expectederrorfiles[i])
                                        no += 1
                                    root.speak("enter the code to open:")
                                    userindex = int(input("\tenter the code:"))
                                    choiceindex = 1
                                    for i in expectederrorfiles.keys():
                                        if int(choiceindex) == int(userindex):
                                            fileaddress = expectederrorfiles[i]
                                            os.startfile(fileaddress)
                                            fileopencode += 1
                                            command_history.append("open the file-- " + str(fileaddress))
                                            break
                                        else:
                                            choiceindex += 1
                                    if fileopencode == 1:
                                        fileopencode = 0
                                        break
                                else:
                                    root.speak("file doesnt exist")
                                    break

                            # perfectname
                            no = 1
                            for i in extentionlist:
                                filename = offlinefilename + i
                                for j in root.dir_Files.keys():
                                    if filename.casefold() == j.casefold():
                                        tempaddress = root.dir_Files[j]
                                        fileaddress = tempaddress + "\\" + filename
                                        expectedfiles[filename] = fileaddress
                            if len(expectedfiles) > 0:
                                print("\tchoose the file:")
                                for i in expectedfiles:
                                    print("\t" + str(no) + "." + i)
                                    no += 1
                                root.speak("enter the code to open:")
                                userindex = int(input("\tenter the code:"))
                                choiceindex = 1
                                for i in expectedfiles:
                                    if int(choiceindex) == int(userindex):
                                        fileaddress = expectedfiles[i]
                                        os.startfile(fileaddress)
                                        fileopencode += 1
                                        command_history.append("open the file-- " + str(fileaddress))
                                        break
                                    else:
                                        choiceindex += 1
                            else:
                                root.speak("file doesnt exist")
                                break
                            break
                    except Exception as e:
                        root.speak("error plz speak again")


            elif 2 == query:
                try:
                    root.speak("what is the name of application?")
                    query = str(input("Enter the name of Application:"))
                    root.speak("opening " + query)
                    ao.run(query)
                    command_history.append(str(query))
                except Exception as e:
                    root.speak("error plz speak again")
                    command_history.append(str(query) + str("-- error"))

            elif 1 == query:
                try:
                    powercommand = {1: "shutdown /s /t 10", 2: "shutdown /r /t 10", 3: "taskkill /f /im JARVIS_2.0.exe"}
                    print("\t1.Shutdown\n\t2.Restart\n\t3.close the JARVIS 2.0")
                    while True:
                        usercommand = int(input("\tEnter the command here: "))
                        if usercommand == 1:
                            maincommand = powercommand[usercommand]
                            root.speak("laptop is going to be shutdown in 10 seconds")
                            break
                        elif usercommand == 2:
                            maincommand = powercommand[usercommand]
                            root.speak("laptop is going to be restart in 10 seconds")
                            break
                        elif usercommand == 3:
                            maincommand = powercommand[usercommand]
                            root.speak("ok then good bye sir and have a nice day")
                            break
                        else:
                            root.speak("plzz enter valid command number.")
                    os.system(maincommand)
                except Exception as e:
                    root.speak("error plz speak again")
            else:
                root.speak("plzz enter the valid commands")


