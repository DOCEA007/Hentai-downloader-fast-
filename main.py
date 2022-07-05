from requests import get
from io import BytesIO
color="#252626"
from tkinter import RIGHT, Button, Label, Entry, Frame, LEFT, Tk
from PIL import Image
from time import sleep, perf_counter
from random import randint
from threading import Thread
from random import randint
from pathlib import Path
import os.path
class image_downloader:
    def __init__(self, master):
        self.master = master
        master.configure(bg=color)
        master.geometry('270x75')
        master.title("Sauce downloader")
        self.label = Label(master, text="Downloader by ~your mother", bg=color, fg="white")
        self.label.pack()
        frame1 = Frame(master,bg=color)
        frame1.pack()
        Label(frame1,text='Query:', bg=color, fg="white").pack(side=LEFT)
        self.querysearch = Entry(frame1,width=10, bg=color, fg="white")
        self.querysearch.pack(side=LEFT)
        Label(frame1,text=' Amount:', bg=color, fg="white").pack(side=LEFT)
        self.number_of_images = Entry(frame1,width=4, bg=color, fg="white")
        self.number_of_images.pack()

        self.close_button = Button(master, text="Download!", command=self.download, bg=color, fg="white")
        self.close_button.place(y=43, x=85)
    def convert_bytes(size):
        """ Convert bytes to KB, or MB or GB"""
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0  
    def download(self):
        try:
            number = int(self.number_of_images.get())
        except:
            self.number_of_images.delete(0, 'end')
            self.number_of_images.insert(10, "Enter valid number")
            return
        try:
            tags=self.querysearch.get().replace('/', '%20')
        except:
            tags="ass%20boobs"
        url = f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit=1&tags={tags}%20sort:random"
        self.master.withdraw()
        sizes=[]
        def thread_func():
            while True:
                try:
                    response = get(url).json()
                    img_url = response['post'][0]['file_url']
                    sleep(0.1)
                    data = BytesIO(get(img_url).content)
                    sleep(0.1)
                    img = Image.open(data)
                    print(f"{Path(__file__).parent.resolve()}\Image{randint(0,1000)}.png")
                    try:
                        img.save(f"{Path(__file__).parent.resolve()}\Image{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}.png")
                        break
                    except:
                        print("Error saving")        
                except:
                    print("Error, trying again")
        def main():
            # create threads
            threads = []
            for i in range(number):
                threads.append(Thread(target=thread_func, args=()))

            # start the threads
            for thread in threads:
                thread.start()

            # wait for the threads to complete
            for thread in threads:
                thread.join()


        if __name__ == "__main__":
            start_time = perf_counter()

            main()

            end_time = perf_counter()
            print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
        self.master.deiconify()
        self.master.deiconify()
            
root = Tk() 
downloader = image_downloader(root)
root.mainloop()