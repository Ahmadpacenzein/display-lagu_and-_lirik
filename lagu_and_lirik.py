import tkinter as tk
import time
import threading
from pygame import mixer

mixer.init()

#kalau mau ganti lagu di .load(path nya)
mixer.music.load("C:\\Users\\AtioMacbook\\Music\\mood.mp3")
mixer.music.play()

#ganti lirik disini dict format nya waktu : lirik nya, per-beat
lirik = {
        0.0 : "--------",
        9.0 : "Why you always in a mood?",
        11.0 : "Fuckin' 'round, actin' brand new",
        14.0 : "I ain't tryna tell you what to do",
        16.0 : "But try to play it cool",
        18.0 : "Baby, I ain't playing by your rules",
        20.0 : "Everything look better with a view",
        22.0 : "Why you always in a mood?",
        24.0 : "Fuckin' 'round, actin' brand new",
        26.0 : "I ain't tryna tell you what to do",
        29.0 : "But try to play it cool",
        30.0 : "Baby, I ain't playing by your rules",
        33.0 : "Everything look better with a view, yeah"
}

def tampil_lirik():
    start_time = time.time()
    for start_time_lyric in sorted(lirik.keys()):
        while time.time() - start_time < start_time_lyric:
            time.sleep(0.12)
        lyric_label.config(text=lirik[start_time_lyric])

def start_tampil_lirik():
    lirik_thread = threading.Thread(target=tampil_lirik)
    lirik_thread.start()

root = tk.Tk()
root.title("Programmed by Pacen")
 
root.geometry("540x135+300+400")

root.config(bg="#2B2B2B")

title_frame = tk.Frame(root, bg="#181818")
title_frame.pack(fill="both")

title_label = tk.Label(title_frame, text="== Foot Fungus x Mood == ", font=("Harlow Solid Italic", 12), bg="#181818", fg="white")
title_label.pack(pady=10)

lyric_label = tk.Label(root, text="hello pacen", font=("Eras Demi ITC", 12), bg="#5C5C5C", fg="white", wraplength=500)
lyric_label.pack(pady=20)

start_tampil_lirik()

root.mainloop()

while mixer.music.get_busy():
    time.sleep(0)
