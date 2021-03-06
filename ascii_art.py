import logging

logging.basicConfig(level=logging.INFO)


class CoffeeDrinksAscii:

    def print_coffee_machine(self):
        logging.info("    /~~~~~~~~~~~~~~~~~~~/|          .----.-----.'  _|.-----.-----. .--------.---.-.----.|  |--.|__|.-----.-----.")
        logging.info("   /              /######/ / |      |  __|  _  |   _||  -__|  -__| |        |  _  |  __||     ||  ||     |  -__|")
        logging.info("  /              /______/ /  |      |____|_____|__|  |_____|_____| |__|__|__|___._|____||__|__||__||__|__|_____|")
        logging.info(" ========================= /||                                                                                  ")
        logging.info(" |_______________________|/ ||       __                              __        ")
        logging.info("  |  \****/     \__,,__/    ||      |__|.-----. .----.-----.---.-.--|  |.--.--.")
        logging.info("  |===\**/       __,,__     ||      |  ||__ --| |   _|  -__|  _  |  _  ||  |  |")
        logging.info("  |______________\====/%____||      |__||_____| |__| |_____|___._|_____||___  |")
        logging.info("  |   ___        /~~~~\ %  / |                                          |_____|")
        logging.info(" _|  |===|===   /      \%_/  |")
        logging.info("| |  |###|     |########| | /")
        logging.info("|____\###/______\######/__|/")
        logging.info("~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def print_coffee_beans(self):
        logging.info("    o8Oo./")
        logging.info("._o8o8o8Oo_.")
        logging.info(" \========/")
        logging.info("  `------'")

    def print_water(self):
        logging.info("    .----."),
        logging.info("    |~~~~|"),
        logging.info("    |    |"),
        logging.info("    |____|"),

    def print_milk(self):
        logging.info("      _____"),
        logging.info("     j_____j"),
        logging.info("    /_____/_\\"),
        logging.info("    |_(~)_| |"),
        logging.info("    | )\"( | |"),
        logging.info("    |(@_@)| |"),
        logging.info("    |_____|,'"),

    def print_trashcan(self):
        logging.info("    ==^=="),
        logging.info("    |[[[|"),
        logging.info("    |[[[|"),
        logging.info("    '---'"),

    def print_espresso(self):
        logging.info("                     .                              __  "),
        logging.info("                      `:.             .-----.-----.|__|.-----.--.--.   .--.--.-----.--.--.----."),
        logging.info("                        `:.           |  -__|     ||  ||  _  |  |  |   |  |  |  _  |  |  |   _|"),
        logging.info("                .:'     ,::           |_____|__|__||  ||_____|___  |   |___  |_____|_____|__|  "),
        logging.info("               .:'      ;:'                       |___|      |_____|   |_____|                 "),
        logging.info("               ::      ;:'            .-----.-----.-----.----.-----.-----.-----.-----."),
        logging.info("                :    .:'              |  -__|__ --|  _  |   _|  -__|__ --|__ --|  _  |"),
        logging.info("                 `.  :.               |_____|_____|   __|__| |_____|_____|_____|_____|"),
        logging.info("        _________________________                 |__|   "),
        logging.info("       : _ _ _ _ _ _ _ _ _ _ _ _ :"),
        logging.info('   ,---:".".".".".".".".".".".".":'),
        logging.info("  : ,'\"`::.:.:.:.:.:.:.:.:.:.:.::'"),
        logging.info("  `.`.  `:-===-===-===-===-===-:'"),
        logging.info("    `.`-._:                   :"),
        logging.info("      `-.__`.               ,' "),
        logging.info("  ,--------`\"`-------------'--------."),
        logging.info("   `\"--.__                   __.--\"'"),
        logging.info("          `""-------------""'"),

    def print_cappuccino(self):
        logging.info("                        ("),
        logging.info("                          )     ("),
        logging.info("                   ___...(-------)-....___"),
        logging.info("               .-""       )    (          ""-.               __    "),
        logging.info("         .-'``'|-._             )         _.-| .-----.-----.|__|.-----.--.--.   .--.--.-----.--.--.----."),
        logging.info("        /  .--.|   `""---...........---""`       | |  -__|     ||  ||  _  |  |  |   |  |  |  _  |  |  |   _|"),
        logging.info("       /  /    |                             | |_____|__|__||  ||_____|___  |   |___  |_____|_____|__|  "),
        logging.info("       |  |    |                             |             |___|      |_____|   |_____|                 "),
        logging.info("        \  \   |                             | .----.---.-.-----.-----.--.--.----.|__|.-----.-----."),
        logging.info("         `\ `\ |                             ||  __|  _  |  _  |  _  |  |  |  __||  ||     |  _  |"),
        logging.info("           `\ `|                             ||____|___._|   __|   __|_____|____||__||__|__|_____|"),
        logging.info("           _/ /;                             ;           |__|  |__|  "),
        logging.info("          (__/  \                           /"),
        logging.info("       _..---""` \                         /`""---.._"),
        logging.info("    .-'           \                       /          '-."),
        logging.info("   :               `-.__             __.-'              :"),
        logging.info("   :                  ) ""---...---"" (                 :"),
        logging.info("    '._               `\"--...___...--\"`              _.'"),
        logging.info("      \"\"--..__                              __..--""/"),
        logging.info("       '._     \"\"\"----.....______.....----\"\"\"     _.'"),
        logging.info("          `""--..,,_____            _____,,..--""`"),
        logging.info("                        `\"\"\"----\"\"\"`"),

    def print_latte_macchiato(self):
        logging.info("          ..     .,;                       __                                         "),
        logging.info("          ` ;,.;`            .-----.-----.|__|.-----.--.--.   .--.--.-----.--.--.----."),
        logging.info("          ;'` ; ,.;  0       |  -__|     ||  ||  _  |  |  |   |  |  |  _  |  |  |   _|"),
        logging.info("           .;'` . . /        |_____|__|__||  ||_____|___  |   |___  |_____|_____|__|  "),
        logging.info("           `,.;'.  /                     |___|      |_____|   |_____|                 "),
        logging.info("                  /           __         __   __         "),
        logging.info("       |`'-.......-'`| ___   |  |.---.-.|  |_|  |_.-----."),
        logging.info("       |             |/__ \\  |  ||  _  ||   _|   _|  -__|"),
        logging.info("       |             |/  \ \\ |__||___._||____|____|_____|"),
        logging.info("       |             |    | |                            "),
        logging.info("       |             |    | |                           __     __         __         "),
        logging.info("       |             |\__/ / .--------.---.-.----.----.|  |--.|__|.---.-.|  |_.-----."),
        logging.info("       |             |\___/  |        |  _  |  __|  __||     ||  ||  _  ||   _|  _  |"),
        logging.info("    ,--|             |--.    |__|__|__|___._|____|____||__|__||__||___._||____|_____|"),
        logging.info(" ,-'  ,|             |.  `-. "),
        logging.info("(    (  \           /  )    ) "),
        logging.info(" `-.  `---------------'  ,-' "),
        logging.info("    `-._______________,-'  ")
