import threading
from live_calculations import*
from animation import *

def start():
   
    create_database()
    root = create_window()
    plot_properties = create_multiplot_figure(root)
    create_buttons(root, plot_properties)
    print("Init threads")
    thread1 = threading.Thread(target=update_live_data, daemon=True)
    thread2 = threading.Thread(target=animate_live_graph, args=(plot_properties,), daemon=True)
    
    print("Starting threads...")
    thread1.start()
    thread2.start()
    print("Threads started.")
    thread1.join()
    thread2.join()
    print("Threads finished.")
    root.mainloop()


start()
