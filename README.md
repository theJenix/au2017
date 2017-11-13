# au2017
Project files for SD125713 - Testing strategies for python add-ins, presented at Autodesk University 2017

Platform: If you are running Windows, you must set this up in cygwin or Bash on Windows or another, similar shell.  This should work as described on Mac OS.


To set up:

    Clone into an empty folder, and cd into that folder

    run `git submodule init`
    run `git submodule update`

    cd to test/lib (you may have to create this folder)
    run `ln -s ../../submodules/f360mock`

    cd back to root of project

    cd to AU2017AddInTests/lib (you may have to create this folder)
    run `ln -s ../../submodules/sodium`


To set up test add-ins in Fusion 360:

    open Fusion 360

    open the Scripts and Add-Ins command
    select Add-Ins, and press the + button

    navigate to the root of the project, and then, AU2017AddIn.  click Open

    repeat the process for AU2017AddInTests (also in the root of the project)


To run unit tests:

    open a terminal window, and navigate to the root of this project
    execute test.sh.  the output will be printed to the console.


To run UI integration tests:

    open Fusion 360
    open the Scripts and Add-Ins command
    select Add-Ins, and click on AU2017AddInTests.  click "edit"

    in Spyder, make sure AU2017AddInTests.py is open, and press the run file button

    the output will be printed in the Spyder console (you may need to press enter a couple times to get it to show up)
