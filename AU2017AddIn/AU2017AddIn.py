#Author-Jesse Rosalia
#Description-Demo add-in for AU 2017 class

import adsk.core, adsk.fusion, adsk.cam, traceback

from .demo_component import make_demo_component_name

handler = None


class AU2017AddInExecuteHandler(adsk.core.CommandEventHandler):

    def notify(self, args):

        app = adsk.core.Application.get()
        ui = app.userInterface
        try:
            command = args.command
            inputs = command.commandInputs
            nameInput = inputs.itemById('name')

            design = app.activeProduct
            rootComp = design.rootComponent
            # Create a new occurrence.
            trans = adsk.core.Matrix3D.create()
            occ = rootComp.occurrences.addNewComponent(trans)
            comp = occ.component
            comp.name = make_demo_component_name(nameInput)
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class AU2017AddInCommandCreatedEventHandler(adsk.core.CommandCreatedEventHandler):

    def __init__(self):
        super().__init__()
        self._execute = None

    def notify(self, args):
        command = args.command
        inputs = command.commandInputs
        inputs.addStringValueInput('name', 'Name', '')

        self._execute = AU2017AddInExecuteHandler()
        command.execute.add(self._execute)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Hello addin')

        # Add a command that displays the panel.
        workspace = ui.workspaces.itemById('FusionSolidEnvironment')
        tpanel = workspace.toolbarPanels.itemById('AU2017AddInPanel')
        if tpanel and tpanel.isValid:
            tpanel.deleteMe()

        tpanel = workspace.toolbarPanels.add('AU2017AddInPanel', 'AU 2017 Demo', 'InsertPanel', False)
        cmddef = ui.commandDefinitions.addButtonDefinition('AU2017AddInCommand', 'Demo Command', '', '')

        cmdCreated = AU2017AddInCommandCreatedEventHandler()
        global handler
        handler = cmdCreated
        cmddef.commandCreated.add(handler)
        tpanel.controls.addCommand(cmddef, '', False)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Stop addin')

        cmddef = ui.commandDefinitions.itemById('AU2017AddInCommand')
        cmddef.deleteMe()
        workspace = ui.workspaces.itemById('FusionSolidEnvironment')
        tpanel = workspace.toolbarPanels.itemById('AU2017AddInPanel')
        tpanel.deleteMe()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
