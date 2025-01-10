#pokemon - pikachu
#init - liam white
import time
import random
#functions

def print_pikachu_stage_baby():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠒⠊⠉⠀⢀⠴⠊⠉⠋⠙⢿⡖⠦⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠊⠁⠀⠀⠀⠀⡠⠚⠁⠀⠀⠀⠀⠀⠀⠹⡄⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢀⣾⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⡇⠀⠀⠀⢀⣴⢿⠁⠀⠈⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⢸⣿⠀⢀⡴⠋⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢾⣧⣘⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⢸⣿⠖⠁⠀⠀⠀⢣⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣇⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀
⠀⠀⠀⣀⣤⣶⠟⠋⠓⠦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣶⣿⠤⠖⠚⠉⠙⡆⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀
⠀⢠⣾⣟⠁⠃⠀⠀⠀⠀⠀⠈⠉⠉⠓⠒⠒⠒⠒⠒⠒⠒⣶⡶⢿⠉⠉⠀⠈⢆⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀
⠀⠀⠙⣿⢿⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⡖⣻⡟⠀⢸⠀⠀⠀⠀⠈⡆⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣨⠇
⠀⠀⠀⢹⡀⠀⠉⠉⡿⠲⣶⠒⠒⠒⣿⡏⠉⠁⠀⠀⠉⢉⡴⠒⢺⠀⠀⠀⠀⠀⢹⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⣬⠃⠀
⠀⠀⠀⠀⠳⡀⠀⠀⢧⠀⡾⠀⠀⣀⣠⡀⠀⠀⠀⠀⠀⠸⣦⣀⣸⡇⠀⠀⠀⠀⠈⡆⠀⣰⣿⡇⠀⠀⠀⠀⢀⡴⠁⠀⠀
⠀⠀⠀⠀⠀⠱⡀⠀⠈⢯⡀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠉⠛⠛⢳⠀⠀⠀⠀⠀⣷⣴⣿⣿⡇⠀⠀⠀⢀⡟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣱⡀⠀⠀⠑⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⣿⠛⠿⣿⡇⠀⠀⢠⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⢦⡀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⣹⠀⠀⠈⠁⠀⢠⠎⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠁⠀⢙⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⢦⡀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⡀⠀⠀⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣴⣿⣷⠾⠃⠀⠀⠀⠀⠀⠀⠀
⡼⠟⠳⣀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⠋⢁⣀⡀⢀⣀⡀⠀⠀⠀⠀
⡇⠀⡀⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠿⠟⠳⡀⠀⠀⠀⠀⠀⠀⢸⣤⡞⠉⠀⠀⠰⡟⠙⠳⣄⠀⠀
⢹⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⢳⠀⠀⠀⠀⠀⢀⣼⣿⡿⠀⠀⠀⠀⠹⣄⠀⢹⣇⠀
⠘⡆⢰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⡇⠀⠀⠀⣠⣾⣿⣿⠇⠀⠀⠀⠀⢀⠈⠙⣿⣿⠀
⠀⠸⡄⢹⠆⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⠀⠤⠊⢁⠟⣿⢿⣦⣀⣀⣾⣿⠟⣧⣴⠿⡯⠀
⠀⠀⠉⠉⠳⢄⡙⠢⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢆⠀⠀⢸⠀⢀⡠⠊⠀⠘⢦⣢⡈⠉⠻⢿⠿⠋⢀⠔⠁⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠒⠒⠶⠒⠒⠒⠈⠉⠉⠉⠉⠉⠉⠒⠒⠪⠷⠒⠛⠊⠉⠀⠠⠄⠀⠤⣌⠛⠳⠦⠤⠴⠒⠁⠀⠀⠀""")
def print_pikachu_stage_medium():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠿⠟⠛⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠁⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠤⠶⠶⠒⠛⢻⣿⣿⣿⣿⣿⡿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠴⠖⠚⠉⠁⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠟⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⢀⣀⡤⠿⠶⠒⠒⠒⠒⠒⠲⠶⠶⠶⢤⣀⣀⠀⠀⣀⣠⠶⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣀⡴⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣽⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠶⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⣠⡤⠶⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⣠⣶⡶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⠤⠶⠶⠶⠶⠒⠒⡷
⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⢸⣿⣿⣀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡏⠉⣿⣶⡄⠀⠀⠀⠀⣿⠀⠀⠀⠀⣀⣠⠤⠶⠖⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇
⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠘⣿⣿⣿⡿⠏⠀⠀⢠⣤⡄⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⢿⣠⡴⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀
⠀⠀⠀⠀⠀⠀⢀⣼⠁⠀⠀⠀⠉⠉⠀⠀⠀⢀⣤⣍⣀⠀⠀⠀⠀⠀⠀⠉⠻⠿⠛⠉⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀
⠀⠀⠀⠀⠀⠀⣸⡏⠉⠳⣆⠀⠀⠘⢷⡶⣶⠛⠉⠈⠉⠳⠦⣄⣀⣤⠖⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣹⡄⠀⠀⠀⣿⠋⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⣶⠋⠁⠈⠙⢶⡀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣇⣀⣴⡟⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠐⣇⠀⠀⠀⠀⢠⣏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣏⠁⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⣴⠃⠀⠀⠀⠀⠀⠙⠦⣄⣀⡴⠟⢰⠇⠀⠀⠀⠀⣶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⢳⣄⠀⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣦⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢦⣀⠀⠀⠀⠀⠀⠙⠳⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⡇⠘⢷⡀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠉⠳⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡴⠞⠁⠀⣿⠀⠀⠻⣄⠀⠀⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠉⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢹⣦⠴⠞⠋⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠀⣀⣠⠶⠖⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣀⠀⠀⠀⠀⠀⢰⡏⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠘⣾⠋⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⡄⢀⣴⠶⠛⠓⠶⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⣠⠶⠿⠷⠶⣄⣠⣾⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡿⡟⣯⢻⡏⠁⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠁⠀⠀⠀⠀⣼⢧⣿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣧⠛⠛⠉⣧⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⣼⠋⠈⠈⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢿⡆⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠁⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣧⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣇⠀⢰⣆⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⣀⡾⠁⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠓⠛⠉⠉⠉⠉⠓⠒⠒⠒⠲⠿⣽⣼⣤⣦⡴⣾⡯⣄⣰⣀⣤⣠⣹⣶⠶⠶⠶⠦⠤⠤⠤⠶⠾⠷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠀⠀⠀⠈⠉⠉⠉⠉⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
def print_pikachu_stage_max():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡿⠿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠏⠀⠀⠀⠉⠛⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠐⣄⠀⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠈⣆⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠈⢣⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⠀⠀⠀⠈⠱⡀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀⠀⠀⡈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣘⣷⣅⣀⡀⠀⠀⠙⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠉⠉⠉⠉⠉⠉⠀⠒⠒⠒⠲⠦⢤⣄⣀⡀⠀⠀⣀⡴⠖⠋⠉⠁⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠉⠒⠂⠀⠀⢀⡀⠀⠀⠀⠈⠙⠳⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠿⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⠦⢤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⡘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠒⠒⠒⠒⢲⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⣿⣆⠹⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⣾⠀⠀⠀⠀⠀⠀⣴⣿⡿⢶⡀⠀⠀⠀⠀⠀⠀⢻⣾⠿⣿⡆⠙⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⠓⠒⠶⠦⢤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠁⠀⠀⠀⠀⢸⣿⣿⣧⣼⣷⠀⠀⠀⠀⠀⠀⠀⠻⠶⠟⠀⡼⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠈⡉⠙⠓⠲⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠘⢿⣅⣈⣿⠏⠀⠀⠀⠀⠶⠂⠀⠀⠀⠀⢠⡇⢨⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣶⣷⣿⣿⣿⣿
⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠈⠉⠛⠲⢤⣄⡀⠀⠀⢹⡄⢀⡶⠛⠙⠳⣦⠉⠉⠁⠀⠀⠀⡀⠀⣀⣤⣤⠇⠀⠀⢸⣡⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⣿⣯⣽⣳⣿⣿⡿⣹
⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢦⣀⢻⣼⡰⢄⠀⠀⠈⣧⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⠿⠛⢉⡿⠉⠀
⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠇⠹⣷⣀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣰⣿⣿⣿⣀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣷⣿⣿⣿⣿⠿⢋⣁⣤⠾⠋⠀⠀⠀
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⢈⣿⠉⠉⠉⠀⠀⠀⣀⣀⣰⣦⣶⣾⡿⣻⣿⣿⣿⡟⠈⠙⢓⣦⣴⣾⣿⣿⣿⣿⣿⣿⠟⠛⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⢀⣴⣿⡇⠀⠀⠀⠀⢰⡿⢛⣛⣳⢽⣦⢀⣴⣿⣿⣿⠟⣀⣴⣞⣯⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠛⠁⠀⠀⠀⠀⠠⠤⠤⠤⠤⠤⠤⠤⣄⡀⠀⠀⠀⢠⡞⢀⣴⣿⣿⣿⡇⠀⠀⠀⠀⠘⡏⠉⠀⠈⠉⢻⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⡟⠋⠉⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⠃⠀⠀⠀⢈⣹⣿⣿⣿⣿⣿⣇⡂⠀⠀⠀⠀⣯⠀⠀⠀⣀⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣛⣁⣀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⣀⣴⣿⣿⣿⣿⡿⠷⠷⣿⡘⠀⠀⠀⠀⣿⣦⣷⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⡍⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠇⠀⢀⡾⠛⠉⠁⠀⠀⠀⠀⠀⣾⣿⣧⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠠⡽⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⢀⢤⠞⡱⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⣄⣀⣤⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢼⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⣿⢠⠇⠀⠀⠀⠀⠀⠀⢀⣴⣶⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⡤⣄⠀⠀⠀⠀⠀⠀⠲⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⠀⠀⠀⠀⠀⠀⠀⠸⣄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡸⡄⠀⠀⠀⠀⠀⠀⠀⠙⢧⣨⠟⠁⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⢣⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⢀⣤⣿⣿⣿⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⢧⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⠟⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢯⡳⡄⠀⠀⠀⣠⣾⣿⣽⡿⠛⢡⣾⠏⠀⠀⠀⢀⣀⣠⣤⠤⠤⠤⢤⢤⣀⠀⢀⣤⠾⣟⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠾⣶⣤⣀⡙⠾⠋⠁⢀⣠⡿⢃⣀⣤⠶⠛⠋⠉⠀⠀⠀⠀⠀⠙⢦⣀⠀⠀⢀⢀⣀⡻⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠷⣶⣶⢿⣟⠋⣀⢄⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠲⠶⠦⠿⠷⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡋⣱⣏⣡⠽⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

def battle_easy():
    global exp
    global win
    global loss
    easy_battle = random.randint(1,2)
    if easy_battle == 1:
        print(str(pokemon_name) + " won the battle! Congratulations! He will be rewarded for his efforts")
        exp += 2
        win += 1
    else:
        print(str(pokemon_name) + " lost, unfortunately. Dinged up, he returns defeated.")
        exp -= 1
        loss += 1
def battle_medium():
    global exp
    global win
    global loss
    easy_battle = random.randint(1,4)
    if easy_battle == 1:
        print(str(pokemon_name) + " won the battle! Congratulations! He will be rewarded greatly for his efforts")
        exp += 5
        win += 1
    else:
        print(str(pokemon_name) + " lost, unfortunately. Dinged up, he returns defeated.")
        exp -= 2
        loss += 1
def battle_hard():
    global exp
    global win
    global loss
    easy_battle = random.randint(1,6)
    if easy_battle == 1:
        print(str(pokemon_name) + " won the battle! Congratulations! He will be rewarded very handsomely for his efforts")
        exp += 8
        win += 1
    else:
        print(str(pokemon_name) + " lost, unfortunately. Dinged up, he returns defeated.")
        exp -= 3
        loss += 1
#main

pokemon_level = 0
day = 0
exp = 0
win = 0
loss = 0

print("Welcome to Pokemon Evolution 2024")
print("Create a name for your pokemon: ")
pokemon_name = str(input("Enter a name for your pokemon: "))

while True:
    global day
    global exp
    global pokemon_name
    global pokemon_level
    global win
    global loss
    if pokemon_level < 2:
        print("""Select an activity for the day:
        A) Train
        B) Gym Battle
        C) Rest (Display Info)
        D) Level Up
        E) Quit
        """)
        activity = str(input("Select an activity (See console for info): 'A', 'B', 'C', 'D', 'E'"))
        if activity == "A" or activity == "a":
            day += 1
            print("You selected 'Train'. Your pokemon is training...")
            print("Day: " + str(day))
            time.sleep(1)
            exp_gain = random.randint(1,3)
            exp += exp_gain
            print("Your pokemon had a successful day at the gym. He gained " + str(exp_gain) + " xp.")
            print("Your pokemon now has " + str(exp) + " xp. ")
            print(" ")
        elif activity == "B" or activity == "b":
            day += 1
            print("You selected 'Gym Battle'. Finding an opponent...")
            print("Day: " + str(day))
            opp = str(input("Would you like an: A. Easy, B. Medium, or C. Hard opponent?"))
            if opp == 'a' or opp == 'A':
                battle_easy()
            elif opp == 'b' or opp == 'B':
                battle_medium()
            elif opp == 'c' or opp == 'C':
                battle_hard()
            else:
                print("Wrong input. Skipping day...")
        elif activity == "C" or activity == "c":
            day += 1
            print("""You selected: 'Rest'. Displaying info...
                """)
            print("Day: " + str(day))
            print("Your pokemon's name is " + str(pokemon_name))
            print("Your pokemon's level is " + str(pokemon_level))
            print("Pokemon XP: " + str(exp))
            print("Wins: " + str(win) + " | Losses: " + str(loss))
            print("Here is your pokemon: ")
            print(" ")
            if pokemon_level == 0:
                print_pikachu_stage_baby()
                print(" ")
            elif pokemon_level == 1:
                print_pikachu_stage_medium()
                print(" ")
            elif pokemon_level == 2:
                print_pikachu_stage_max()
                print(" ")
        elif activity == "D" or activity == "d":
            day += 1
            if pokemon_level == 0:
                if exp >= 5:
                    print("Look, your pokemon is evolving!")
                    exp -= 5
                    print_pikachu_stage_medium()
                    pokemon_name = str(pokemon_name) + " Master"
                    pokemon_level += 1
                else:
                    print("Your pokemon doesn't have enough xp to level up. Try again later.")
                    print(" ")
            elif pokemon_level == 1:
                if exp >= 10:
                    print("Wow, look over there! Your pokemon is evolving!")
                    exp -= 10
                    print_pikachu_stage_max()
                    pokemon_name = str(pokemon_name) + " Lord"
                    pokemon_level += 1
                else:
                    print("Your pokemon doesn't have enough xp to level up. Try again later.")
                    print(" ")
            elif pokemon_level == 2:
                if exp >= 25:
                    print("Your pokemon is too big! It cannot evolve currently. Maybe later though...")
                else:
                    print("Your pokemon doesn't have enough xp to level up. Try again later.")
                    print(" ")
        elif activity == "E" or activity == "e":
            day += 1
            print("""You selected: 'Quit'. Terminating...
                """)
            break
        elif activity == "cheatcode":
            exp += 1000
        else:
            print("""You selected: 'Wrong Input'. Try again...
            """)
    elif pokemon_level >= 2:
        print("""Select an activity for the day:
        A) Train
        B) Gym Battle
        C) Rest (Display Info)
        D) Level Up
        E) Boss Battle
        F) Quit
        """)
        activity = str(input("Select an activity (See console for info): 'A', 'B', 'C', 'D', 'E', 'F'"))
        if activity == "A" or activity == "a":
            day += 1
            print("You selected 'Train'. Your pokemon is training...")
            print("Day: " + str(day))
            time.sleep(1)
            exp_gain = random.randint(1,3)
            exp += exp_gain
            print("Your pokemon had a successful day at the gym. He gained " + str(exp_gain) + " xp.")
            print("Your pokemon now has " + str(exp) + " xp. ")
            print(" ")
        elif activity == "B" or activity == "b":
            day += 1
            print("You selected 'Gym Battle'. Finding an opponent...")
            print("Day: " + str(day))
            opp = str(input("Would you like an: A. Easy, B. Medium, or C. Hard opponent?"))
            if opp == 'a' or opp == 'A':
                battle_easy()
            elif opp == 'b' or opp == 'B':
                battle_medium()
            elif opp == 'c' or opp == 'C':
                battle_hard()
            else:
                print("Wrong input. Skipping day...")
        elif activity == "C" or activity == "c":
            day += 1
            print("""You selected: 'Rest'. Displaying info...
                """)
            print("Day: " + str(day))
            print("Your pokemon's name is " + str(pokemon_name))
            print("Your pokemon's level is " + str(pokemon_level))
            print("Pokemon XP: " + str(exp))
            print("Wins: " + str(win) + " | Losses: " + str(loss))
            print("Here is your pokemon: ")
            print(" ")
            if pokemon_level == 0:
                print_pikachu_stage_baby()
                print(" ")
            elif pokemon_level == 1:
                print_pikachu_stage_medium()
                print(" ")
            elif pokemon_level == 2:
                print_pikachu_stage_max()
                print(" ")
        elif activity == "D" or activity == "d":
            day += 1
            if pokemon_level == 0:
                if exp >= 5:
                    print("Look, your pokemon is evolving!")
                    exp -= 5
                    print_pikachu_stage_medium()
                    pokemon_name = str(pokemon_name) + " Master"
                    pokemon_level += 1
                else:
                    print("Your pokemon doesn't have enough xp to level up. Try again later.")
                    print(" ")
            elif pokemon_level == 1:
                if exp >= 10:
                    print("Wow, look over there! Your pokemon is evolving!")
                    exp -= 10
                    print_pikachu_stage_max()
                    pokemon_name = str(pokemon_name) + " Lord"
                    pokemon_level += 1
                else:
                    print("Your pokemon doesn't have enough xp to level up. Try again later.")
                    print(" ")
            elif pokemon_level == 2:
                if exp >= 25:
                    print("Your pokemon is too big! It cannot evolve currently. Maybe later though...")
                else:
                    print("Your pokemon doesn't have enough xp to level up. Try again later.")
                    print(" ")
        elif activity == "E" or activity == "e":
            day += 1
            print("""You selected: 'Boss Battle'. Your pokemon is taken into the boss room...
                  """)
            print("""⣏⠉⠉⠉⠉⠉⠉⠉⣩⣭⡽⢏⠯⡹⢫⢟⠻⠿⢿⣿⣯⣍⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢉⣩⣭⣭⣭⣭⣭⣍⣉⠙⢫⠍⢉⠉⠍⡉⠍⡙⠉⠛⡙⠻⢽⡯⠉⠉⠉⠉⠉⠉⠉⠉⠉
⡧⠀⠀⠀⠀⢀⡴⠟⣫⣱⣼⣾⣿⣷⣿⣾⣷⣾⣤⣀⡈⠛⢿⣶⣤⡀⢀⣤⣶⣶⣿⢿⣿⣿⣿⣿⣿⣿⣧⣭⣛⠛⠛⠿⣦⣌⠐⡀⠆⠱⡈⠔⡠⠁⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡷⠀⠀⠀⠠⢏⣰⣳⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣶⡄⠈⠻⣿⣿⣿⠿⣉⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠈⠙⢷⣤⠈⠄⡱⢈⠔⠡⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣷⠀⠀⠄⡁⣶⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣧⠀⠈⠻⣧⣃⣿⣿⣿⠏⠉⠈⠀⠀⠈⠈⠙⠿⣿⣿⣿⣷⡄⠀⠻⣷⡐⢀⠣⡘⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠌⢂⣱⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣷⡄⠀⢢⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⡆⠀⢹⣷⡀⠢⡐⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠠⢼⣿⣿⣿⡟⠀⠀⢀⣀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠉⢻⣿⡷⠀⣸⣿⡿⠉⠀⢀⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⠙⠻⣿⣿⠀⠀⣿⣧⠁⡔⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⢺⣿⣿⣿⠃⠀⣰⣾⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⢈⣿⣿⠀⢼⣿⣇⢀⣾⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⣀⣴⣿⣿⠀⠀⣿⣿⣎⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⠀⠀⠩⣿⣿⣿⣄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢼⣿⣿⠀⢸⣿⣇⣸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣿⣿⣟⣿⠀⠀⣿⣿⣿⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⡀⠀⢠⣿⣿⣿⣿⡸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣠⣿⡿⠀⠀⢿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⢠⣿⣿⣿⡿⠀⢸⣿⣿⣿⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠀⢄⠀⠀⠻⣿⣿⣿⣷⣟⠻⠿⠿⡿⠿⠿⠿⠟⠁⠀⢀⣼⣿⡿⠁⠀⠀⠘⢿⣷⣄⠈⠉⠉⠛⠛⠛⠋⠀⠀⣠⣾⣿⣿⡟⠁⢀⣾⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠈⠄⢡⢀⡀⠙⢿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⣀⣴⣿⣿⡿⠃⠀⣠⡄⠀⠈⢻⣿⣷⣤⡀⠀⠀⠀⢀⣠⣾⢿⣿⡿⠋⠀⢠⣿⠟⣙⠻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠈⢂⠄⠂⠐⠲⣮⡙⡙⠻⣿⣿⣿⣿⣿⣿⣿⢿⣿⠿⠟⠉⠀⣠⣾⣿⣷⣤⡀⠀⠈⠛⠿⢿⣷⣶⣿⣿⣵⡾⠟⠋⠀⣠⣴⠿⢃⡜⠤⢣⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢦
⣿⠀⠡⡈⠄⠈⠀⠈⠻⢷⣶⣤⣍⠛⠛⡛⢛⠛⠛⠁⣀⣤⣴⡿⠟⠿⢿⣿⣿⣿⣦⣤⣀⠀⠀⠀⠀⠉⠁⢀⣀⣠⡴⠾⢿⣧⠘⡆⠼⣈⣷⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣌⡳
⣿⠈⡐⠄⡀⠁⠀⠀⠀⠀⠈⠉⠙⠻⠿⠿⣿⣿⣿⠿⠿⠛⠉⠀⠀⠀⠀⠈⠙⠛⠿⠿⢿⣿⡿⠿⠿⠿⠟⠛⠋⠉⠀⠀⣾⣇⠣⡜⣑⢲⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢳⣎⠷
⣿⠀⡐⢂⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⡓⡜⢤⢋⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⣹⢎⡟
⣿⠀⢄⠃⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣿⢢⠱⣘⠦⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⢦⣹⢏⣞
⣿⠐⡠⠌⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢂⡓⢬⢒⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠐⣈⠶⣹⣞⡼
⣿⠀⡔⢡⠐⠤⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⢢⡑⢎⠲⣼⡇⠀⠀⠀⠀⠀⠀⠀⠠⠐⡌⢾⣱⢯⣟
⣿⠐⡌⢆⣉⠒⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⠣⡜⡌⢧⣿⠃⠀⠀⠀⠀⠀⠀⠀⠐⠬⣜⣣⢾⣛⣾
⣿⠘⡜⠬⡄⢳⡐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢣⠳⡜⣽⡿⠀⠀⠀⠀⠀⠀⠀⢀⢉⠲⣍⣞⣳⢻⡾
⣿⠘⣌⠳⡌⢣⠜⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣌⣳⣿⣿⡇⠀⠀⠀⠀⠀⠀⡀⠂⣌⢲⡹⣜⣳⣯⣿
⣿⠘⡤⢓⠬⡱⠌⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣼⣿⠳⢿⡄⠀⠀⠀⠀⠀⠐⠀⢢⠰⣣⢞⣵⣯⣿⣾
⣿⠱⣌⠳⢎⡱⡍⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣏⠷⣙⣾⣿⣶⣶⣶⣾⣷⣻⣾⣷⣿⣿⣿⣿⣿⣿⣿
⣿⣵⣮⣽⣮⣵⣾⣽⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣀⣀⣄⣠⣀⢠⣀⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠙⢸⡍⡞⢡⠋⠘⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⢻⣭⡟⣿⢻⡟⣿⣿⣿⣿⣿⣿⣯⣿⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⡁⢂⠔⣠⢡⢌⡐⣠⢀⠄⡠⢀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠹⣿⣯⣷⣻⣽⣿⣻⣗⢯⡿⣹⢯⣟⣾⣭⣟⡾⣽⢯⡿⣿
⣿⣿⣿⣿⣿⣿⡟⠀⣀⢽⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠌⠂⠍⠂⠡⠁⠊⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠇⢩⢛⣿⣿⣿⣽⣾⢷⣯⣟⡾⣯⣟⣾⣳⡟⣾⣻⣭⣟⣽⣻
⣿⣿⣿⣿⣿⣿⠃⡀⢾⡌⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡏⢸⠄⢻⣿⣿⣿⣯⡿⣟⣾⢾⣽⣳⣯⣞⡷⣽⣶⣛⣮⡽⣞⣳
⣿⣿⣿⣟⣿⣿⠁⠐⣺⣿⡀⠹⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⢘⣿⡇⢌⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⣽⣻⡼
⣿⣿⣿⣞⣿⣿⠂⠡⣜⣿⡅⠀⢹⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⡯⣼⣿⣿⡀⠾⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⢿⣻⣞⡷⣿
⣿⣿⢷⣻⢾⣿⠂⠱⣸⣿⣧⠀⢸⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣄⣀⣀⣀⣀⣄⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣌⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣟⣯⢿⣿⡇⢬⣽⣿⣿⣷⡄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣯⣿⣽⣿⣿⣿⣿
                                      (VS)
                  """)
            print_pikachu_stage_max()
            print("You must fight the boss. Choose an option:")
            print("A) Hit with guitar")
            print("B) Approach cautiously")
            print("C) Run away")
            boss_option = str(input("Choose an option (A, B, C): "))
            if boss_option == "A" or boss_option == "a":
                print("Your pokemon doesn't wait for any movement from the minion, he slams him with his guitar instead.")
                print("The minion is caught off guard and falls over, now unconscious.")
                print("After toppling such a tough opponent, your pokemon now has a lot of newfound experience under his belt.")
                exp += 100
            elif boss_option == "B" or boss_option == "b":
                print("You approach cautiously, trying to see what the minion wants. Impatient, he sucker punches you and you fall to the ground.")
                print("Embarrassed by the fight, your pokemon goes into experience debt.")
                exp -= 300
            if boss_option == "C" or boss_option == "c":
                print("You try to run away, but the minion grabs you and slams you against the ground.")
                print("Embarrassed by trying to run away, your pokemon reverts to baby form.")
                pokemon_level -= 2
        elif activity == "cheatcode":
            exp += 1000
        elif activity == "F" or activity == "f":
            day += 1
            print("""You selected: 'Quit'. Terminating...
                """)
            break
        else:
            print("""You selected: 'Wrong Input'. Try again...
            """)
