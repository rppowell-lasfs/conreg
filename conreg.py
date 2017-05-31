import curses
import logging


"""
conreg - proof of concept / mock-up
"""

main_app=None

class State(object):
    """Base state.  This is to share functionality"""

    def print_status(self):
        self.app.stdscr.clear()
        self.app.stdscr.addstr(0, 0, "Current state:" + str(self.__class__), curses.A_REVERSE)
        logger.info(str(self.__class__))
        self.app.stdscr.refresh()


class MainState(State):
    def __init__(self, app):
        #logger.info(str(self.__class__))
        self.app = app

    def do_loop(self):
        c = self.app.stdscr.getch()
        if c == ord('q'):
            self.app.done = True
        elif c == ord('1'):
            self.app.state = State1(self.app)
        elif c == ord('2'):
            self.app.state = State2(self.app)

class State1(State):
    def __init__(self, app):
        self.app = app

    def do_loop(self):
        c = self.app.stdscr.getch()
        if c == ord('m'):
            self.app.state = MainState(self.app)

class State2(State):
    def __init__(self, app):
        self.app = app

    def do_loop(self):
        c = self.app.stdscr.getch()
        if c == ord('m'):
            self.app.state = MainState(self.app)

class App(object):
    """The app"""
    def __init__(self):

        #logger = logging.getLogger(__file__)
        #hdlr = logging.FileHandler(__file__ + ".log")
        #formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        #hdlr.setFormatter(formatter)
        #logger.addHandler(hdlr)
        #logger.setLevel(logging.DEBUG)
        #
        logger.info("App")

        self.done = False
        self.stdscr = curses.initscr()
        print self.stdscr.getmaxyx()

        self.state = MainState(self)

    def do_loop(self):
        self.state.print_status()
        self.state.do_loop()

def main_loop(stdscr):
    global main_app
    while main_app and not main_app.done:
        main_app.do_loop()



if __name__ == '__main__':
    
    logger = logging.getLogger(__file__)
    hdlr = logging.FileHandler(__file__ + ".log")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    
    logger.info("begin")

    ## turn off automatic echoing of characters
    #curses.noecho()
    ## react to keys without waiting for ENTER
    #curses.cbreak()
    ## set to return special keys / num_pad, page_up/page_down, etc
    #stdscr.keypad(1)
    #main_loop(stdscr)
    #stdscr.keypad(0); 
    #curses.nocbreak(); 
    #curses.echo()
    #curses.endwin()
    
    main_app=App()
    curses.wrapper(main_loop)
