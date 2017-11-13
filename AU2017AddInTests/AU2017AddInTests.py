#Author-
#Description-

import adsk.core
import traceback

from .lib import sodium


class InputCreatedTestCase(sodium.CommandTestCase):
    def __init__(self):
        super().__init__('Input Created')
        self._document = None

    def setUp(self):
        app = adsk.core.Application.get()
        cmddef = app.userInterface.commandDefinitions.itemById('AU2017AddInCommand')
        return cmddef

    def testCommand(self, command, inputs):
        command.isAutoExecute = False
        command.isExecutedWhenPreEmpted = False

        assert 'name2' in inputs

    def tearDown(self):
        app = adsk.core.Application.get()
        app.userInterface.commandDefinitions.itemById('SelectCommand').execute()

class ComponentCreatedTestCase(sodium.CommandTestCase):
    def __init__(self):
        super().__init__('Create Command')
        self._document = None

    def setUp(self):
        app = adsk.core.Application.get()
        cmddef = app.userInterface.commandDefinitions.itemById('AU2017AddInCommand')
        if cmddef is None:
            return None
        self._document = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType, True)
        return cmddef

    def testCommand(self, command, inputs):
        inputs['name'].value = 'Automated'

        command.doExecute(False)

        app = adsk.core.Application.get()
        comp = next((c for c in app.activeProduct.allComponents if c.name == 'DEMO: Automated'), None)
        assert comp is not None

    def tearDown(self):
        app = adsk.core.Application.get()
        app.userInterface.commandDefinitions.itemById('SelectCommand').execute()
        self._document.close(False)

runner = sodium.SodiumTestRunner()
def run(context):
    try:
        global runner
        runner.add(InputCreatedTestCase())
        runner.add(ComponentCreatedTestCase())
        runner.add_complete_handler(sodium.SodiumTestRunner.print_results)
        runner.run()
    except:
        traceback.print_exc()


def stop(context):
    pass
