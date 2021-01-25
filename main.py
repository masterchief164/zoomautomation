import webbrowser
import schedule
import time


def usual():
    webbrowser.open('https://zoom.us/j/92454298426?pwd=cWQrT3k2OXZISVlsbXFsMjZsNFZ0dz09')


schedule.every().monday.at("9:00").do(usual())


