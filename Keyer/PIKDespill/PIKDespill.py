# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named PIKDespillExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from PIKDespillExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.PIKDespill"

def getLabel():
    return "PIKDespill"

def getVersion():
    return 2

def getIconPath():
    return "PIKDespill.png"

def getGrouping():
    return "Community/Keyer"

def getPluginDescription():
    return "Despill tool based on the PIK Keyer."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("PIKDespill", "PIKDespill")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.PIKDespill = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createSeparatorParam("line02", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line02 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createDoubleParam("PIK_DespillredWeight", "Red Weight")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.4, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.PIK_DespillredWeight = param
    del param

    param = lastNode.createDoubleParam("PIK_DespillblueGreenWeight", "Blue/Green Weight")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.5, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.PIK_DespillblueGreenWeight = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createSeparatorParam("line04", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line04 = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createColorParam("Gradewhite", "Gain", True)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(4, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(4, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(4, 2)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)
    param.setDisplayMinimum(0, 3)
    param.setDisplayMaximum(4, 3)
    param.setDefaultValue(1, 3)
    param.restoreDefaultValue(3)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Gradewhite = param
    del param

    param = lastNode.createColorParam("Gradegamma", "Gamma", True)
    param.setDisplayMinimum(0.2, 0)
    param.setDisplayMaximum(5, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDisplayMinimum(0.2, 1)
    param.setDisplayMaximum(5, 1)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setDisplayMinimum(0.2, 2)
    param.setDisplayMaximum(5, 2)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)
    param.setDisplayMinimum(0.2, 3)
    param.setDisplayMaximum(5, 3)
    param.setDefaultValue(1, 3)
    param.restoreDefaultValue(3)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Gradegamma = param
    del param

    param = lastNode.createDoubleParam("Saturationsaturation", "Saturation")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(4, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Saturationsaturation = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    param = lastNode.createSeparatorParam("line06", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line06 = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    param = lastNode.createDoubleParam("Dissolve1which", "mix with original")
    param.setMinimum(0, 0)
    param.setMaximum(63, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Dissolve1which = param
    del param

    param = lastNode.createStringParam("sep19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep19 = param
    del param

    param = lastNode.createStringParam("sep20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep20 = param
    del param

    param = lastNode.createSeparatorParam("line05", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line05 = param
    del param

    param = lastNode.createStringParam("seb21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.seb21 = param
    del param

    param = lastNode.createStringParam("sep22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep22 = param
    del param

    param = lastNode.createSeparatorParam("NOTE", "NOTE : despill mask in alpha output")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NOTE = param
    del param

    param = lastNode.createStringParam("sep23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep23 = param
    del param

    param = lastNode.createStringParam("sep24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep24 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createSeparatorParam("line03", "(Fabrice Fernandez - 2016)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Merge"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge")
    lastNode.setLabel("Merge")
    lastNode.setPosition(1000, 392)
    lastNode.setSize(104, 66)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("difference")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("difference")
        del param

    param = lastNode.getParam("AChannelsA")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Merge"

    # Start of node "PIK_Despill"
    lastNode = app.createNode("net.sf.openfx.PIK", 1, group)
    lastNode.setScriptName("PIK_Despill")
    lastNode.setLabel("PIK_Despill")
    lastNode.setPosition(765, 404)
    lastNode.setSize(80, 43)
    lastNode.setColor(0, 1, 0)
    groupPIK_Despill = lastNode

    param = lastNode.getParam("screenType")
    if param is not None:
        param.set("Pick")
        del param

    param = lastNode.getParam("color")
    if param is not None:
        param.setValue(1, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("redWeight")
    if param is not None:
        param.setValue(0.4, 0)
        del param

    del lastNode
    # End of node "PIK_Despill"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(753, 555)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("B.g")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(798, 301)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(1045, 301)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(1045, 569)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Input1")
    lastNode.setPosition(753, 92)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(551, 903)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Grade_despill"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("Grade_despill")
    lastNode.setLabel("Grade_despill")
    lastNode.setPosition(753, 682)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupGrade_despill = lastNode

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Grade_despill"

    # Start of node "Dissolve1"
    lastNode = app.createNode("net.sf.openfx.DissolvePlugin", 1, group)
    lastNode.setScriptName("Dissolve1")
    lastNode.setLabel("Dissolve1")
    lastNode.setPosition(551, 774)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupDissolve1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "Dissolve1"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(596, 301)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Shuffle2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle2")
    lastNode.setLabel("Shuffle2")
    lastNode.setPosition(551, 555)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle2 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue("A.g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue("A.b")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue("B.g")
        del param

    del lastNode
    # End of node "Shuffle2"

    # Start of node "Saturation"
    lastNode = app.createNode("net.sf.openfx.SaturationPlugin", 2, group)
    lastNode.setScriptName("Saturation")
    lastNode.setLabel("Saturation")
    lastNode.setPosition(753, 774)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupSaturation = lastNode

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Saturation"

    # Now that all nodes are created we can connect them together, restore expressions
    groupMerge.connectInput(0, groupPIK_Despill)
    groupMerge.connectInput(1, groupDot2)
    groupPIK_Despill.connectInput(0, groupDot1)
    groupShuffle1.connectInput(0, groupDot3)
    groupShuffle1.connectInput(1, groupPIK_Despill)
    groupDot1.connectInput(0, groupInput1)
    groupDot2.connectInput(0, groupDot1)
    groupDot3.connectInput(0, groupMerge)
    groupOutput1.connectInput(0, groupDissolve1)
    groupGrade_despill.connectInput(0, groupShuffle1)
    groupDissolve1.connectInput(0, groupShuffle2)
    groupDissolve1.connectInput(1, groupSaturation)
    groupDot5.connectInput(0, groupDot1)
    groupShuffle2.connectInput(0, groupDot3)
    groupShuffle2.connectInput(1, groupDot5)
    groupSaturation.connectInput(0, groupGrade_despill)

    param = groupPIK_Despill.getParam("redWeight")
    group.getParam("PIK_DespillredWeight").setAsAlias(param)
    del param
    param = groupPIK_Despill.getParam("blueGreenWeight")
    group.getParam("PIK_DespillblueGreenWeight").setAsAlias(param)
    del param
    param = groupGrade_despill.getParam("white")
    group.getParam("Gradewhite").setAsAlias(param)
    del param
    param = groupGrade_despill.getParam("gamma")
    group.getParam("Gradegamma").setAsAlias(param)
    del param
    param = groupDissolve1.getParam("which")
    group.getParam("Dissolve1which").setAsAlias(param)
    del param
    param = groupSaturation.getParam("saturation")
    group.getParam("Saturationsaturation").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["PIKDespillExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
