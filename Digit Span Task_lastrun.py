﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Mart 15, 2023, at 17:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Digit Span Task'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\İndirilenler\\backwarddigitspan-master\\backwarddigitspan-master\\Digit Span Task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "hello" ---
text_hello = visual.TextStim(win=win, name='text_hello',
    text='Bellek dizisi testlerine hoş geldiniz.\n\nLÜTFEN AÇIKLAMALARI OKUMADAN TESTLERE BAŞLAMAYIN.\n\nBu çalışmada arka arkaya iki test bulunmaktadır. Her testin açıklaması başlamadan önce ekrana gelecektir.\n\nLütfen iki testte de olabildiğince hızlı ve doğru yanıt vermeye çalışın.\n\nTESTLER SIRASINDA KAĞIT KALEM KULLANMAYIN. \nRAKAMLARI SADECE AKLINIZDA TUTUN!\n\nDevam etmek için hazır olduğunuzda SPACE (BOŞLUK) tuşuna basın.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_hello = keyboard.Keyboard()

# --- Initialize components for Routine "Instructions" ---
instr_bwd = visual.TextStim(win=win, name='instr_bwd',
    text='GERİ SAYI DİZİSİ TESTİ\n\nBu testte ekranınıza birtakım sayı dizileri gelecektir. Sizden istenen sayı dizilerini hatırlayıp "ters sırada" yazmanızdır. Örneğin ekrana sırasıyla 1-2-3 geldiğinde sizden istenen hatırlama ekranında 3-2-1 yazmanızdır.\n\nTest 3 rakamlı dizilerle başlayacaktır (1-2-3 gibi). Eğer 3 rakamlı dizileri doğru hatırlarsanız dizi bir rakam uzayacaktır (1-2-3-4 gibi). Üç kez arka arkaya hata yaparsanız test sona erecektir.\n\nYanıtınızı yazmak için klavyenizin üstündeki rakam tuşlarını kullanın. Hata yaparsanız BACKSPACE (GERİ) tuşu ile hatanızı düzeltebilirsiniz. Rakamları girdikten sonra yanıtınızı göndermek için ENTER tuşuna basın. Her yanıttan sonra geribildirim alacaksınız.\n\nRakamları girerken arada boşluk bırakmayın.  Rakam dışında başka bir karakter (+, - vb.) girmeyin.\n\nAçıklamaları anladıysanız hazır olunca deneye başlamak için SPACE (BOŞLUK) tuşuna basın.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_bwd = keyboard.Keyboard()

# --- Initialize components for Routine "Presentation" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pres_text = visual.TextStim(win=win, name='pres_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Recall" ---
recall_txt = visual.TextStim(win=win, name='recall_txt',
    text='Rakamları ters sırada yazın',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox',
     autoLog=True,
)
# Run 'Begin Experiment' code from code
# Store responses
allResponses = []
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "End" ---
thank_you = visual.TextStim(win=win, name='thank_you',
    text='Geri sayı dizisi testi sona ermiştir.\nBirazdan ileri sayı dizisi başlayacaktır.\nLütfen bekleyin...',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Instructions_Forward" ---
instr_fwd = visual.TextStim(win=win, name='instr_fwd',
    text='İLERİ SAYI DİZİSİ TESTİ\n\nBu testte ekranınıza birtakım sayı dizileri gelecektir. Sizden istenen sayı dizilerini hatırlayıp "ters sırada" yazmanızdır. Örneğin ekrana sırasıyla 1-2-3 geldiğinde sizden istenen hatırlama ekranında 3-2-1 yazmanızdır.\n\nTest 3 rakamlı dizilerle başlayacaktır (1-2-3 gibi). Eğer 3 rakamlı dizileri doğru hatırlarsanız dizi bir rakam uzayacaktır (1-2-3-4 gibi). Üç kez arka arkaya hata yaparsanız test sona erecektir.\n\nYanıtınızı yazmak için klavyenizin üstündeki rakam tuşlarını kullanın. Hata yaparsanız BACKSPACE (GERİ) tuşu ile hatanızı düzeltebilirsiniz. Rakamları girdikten sonra yanıtınızı göndermek için ENTER tuşuna basın. Her yanıttan sonra geribildirim alacaksınız.\n\nRakamları girerken arada boşluk bırakmayın.  Rakam dışında başka bir karakter (+, - vb.) girmeyin.\n\nAçıklamaları anladıysanız hazır olunca deneye başlamak için SPACE (BOŞLUK) tuşuna basın.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_fwd = keyboard.Keyboard()

# --- Initialize components for Routine "Presentation_Forward" ---
fixation_fwd = visual.TextStim(win=win, name='fixation_fwd',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pres_text_fwd = visual.TextStim(win=win, name='pres_text_fwd',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Recall_Forward" ---
recall_txt_fwd = visual.TextStim(win=win, name='recall_txt_fwd',
    text='Rakamları aynı sırada yazın',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
textbox_fwd = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='textbox_fwd',
     autoLog=True,
)
# Run 'Begin Experiment' code from code_fwd
# Store responses
allResponsesfwd = []
key_resp_fwd = keyboard.Keyboard()

# --- Initialize components for Routine "Feedback_Forward" ---
feedback_text_fwd = visual.TextStim(win=win, name='feedback_text_fwd',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "End_Fwd" ---
thank_you_fwd = visual.TextStim(win=win, name='thank_you_fwd',
    text='İleri sayı dizisi testi sona ermiştir.\n\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "goodbye" ---
text_goodbye = visual.TextStim(win=win, name='text_goodbye',
    text='Çalışma sona ermiştir.\nKatılımınız için teşekkürler.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "hello" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_hello.keys = []
key_resp_hello.rt = []
_key_resp_hello_allKeys = []
# keep track of which components have finished
helloComponents = [text_hello, key_resp_hello]
for thisComponent in helloComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "hello" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_hello* updates
    if text_hello.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_hello.frameNStart = frameN  # exact frame index
        text_hello.tStart = t  # local t and not account for scr refresh
        text_hello.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_hello, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_hello.started')
        text_hello.setAutoDraw(True)
    
    # *key_resp_hello* updates
    waitOnFlip = False
    if key_resp_hello.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_hello.frameNStart = frameN  # exact frame index
        key_resp_hello.tStart = t  # local t and not account for scr refresh
        key_resp_hello.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_hello, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_hello.started')
        key_resp_hello.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_hello.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_hello.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_hello.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_hello.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_hello_allKeys.extend(theseKeys)
        if len(_key_resp_hello_allKeys):
            key_resp_hello.keys = _key_resp_hello_allKeys[-1].name  # just the last key pressed
            key_resp_hello.rt = _key_resp_hello_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in helloComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "hello" ---
for thisComponent in helloComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_hello.keys in ['', [], None]:  # No response was made
    key_resp_hello.keys = None
thisExp.addData('key_resp_hello.keys',key_resp_hello.keys)
if key_resp_hello.keys != None:  # we had a response
    thisExp.addData('key_resp_hello.rt', key_resp_hello.rt)
thisExp.nextEntry()
# the Routine "hello" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
start_bwd.keys = []
start_bwd.rt = []
_start_bwd_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instr_bwd, start_bwd]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_bwd* updates
    if instr_bwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_bwd.frameNStart = frameN  # exact frame index
        instr_bwd.tStart = t  # local t and not account for scr refresh
        instr_bwd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_bwd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_bwd.started')
        instr_bwd.setAutoDraw(True)
    
    # *start_bwd* updates
    waitOnFlip = False
    if start_bwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_bwd.frameNStart = frameN  # exact frame index
        start_bwd.tStart = t  # local t and not account for scr refresh
        start_bwd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_bwd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_bwd.started')
        start_bwd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_bwd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_bwd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_bwd.status == STARTED and not waitOnFlip:
        theseKeys = start_bwd.getKeys(keyList=['space'], waitRelease=False)
        _start_bwd_allKeys.extend(theseKeys)
        if len(_start_bwd_allKeys):
            start_bwd.keys = _start_bwd_allKeys[-1].name  # just the last key pressed
            start_bwd.rt = _start_bwd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_bwd.keys in ['', [], None]:  # No response was made
    start_bwd.keys = None
thisExp.addData('start_bwd.keys',start_bwd.keys)
if start_bwd.keys != None:  # we had a response
    thisExp.addData('start_bwd.rt', start_bwd.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('choose_digitSpan.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condition_file),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        digitLoop = data.TrialHandler(nReps=digitSpan, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='digitLoop')
        thisExp.addLoop(digitLoop)  # add the loop to the experiment
        thisDigitLoop = digitLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
        if thisDigitLoop != None:
            for paramName in thisDigitLoop:
                exec('{} = thisDigitLoop[paramName]'.format(paramName))
        
        for thisDigitLoop in digitLoop:
            currentLoop = digitLoop
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop.rgb)
            if thisDigitLoop != None:
                for paramName in thisDigitLoop:
                    exec('{} = thisDigitLoop[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Presentation" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            pres_text.setText(str(digits)[digitLoop.thisN])
            # keep track of which components have finished
            PresentationComponents = [fixation, pres_text]
            for thisComponent in PresentationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Presentation" ---
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.tStart = t  # local t and not account for scr refresh
                    fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.started')
                    fixation.setAutoDraw(True)
                if fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation.tStop = t  # not accounting for scr refresh
                        fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation.stopped')
                        fixation.setAutoDraw(False)
                
                # *pres_text* updates
                if pres_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    pres_text.frameNStart = frameN  # exact frame index
                    pres_text.tStart = t  # local t and not account for scr refresh
                    pres_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pres_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text.started')
                    pres_text.setAutoDraw(True)
                if pres_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pres_text.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        pres_text.tStop = t  # not accounting for scr refresh
                        pres_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'pres_text.stopped')
                        pres_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in PresentationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Presentation" ---
            for thisComponent in PresentationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
        # completed digitSpan repeats of 'digitLoop'
        
        
        # --- Prepare to start Routine "Recall" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        textbox.reset()
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        RecallComponents = [recall_txt, textbox, key_resp]
        for thisComponent in RecallComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Recall" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_txt* updates
            if recall_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recall_txt.frameNStart = frameN  # exact frame index
                recall_txt.tStart = t  # local t and not account for scr refresh
                recall_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_txt.started')
                recall_txt.setAutoDraw(True)
            
            # *textbox* updates
            if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox.frameNStart = frameN  # exact frame index
                textbox.tStart = t  # local t and not account for scr refresh
                textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.started')
                textbox.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RecallComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Recall" ---
        for thisComponent in RecallComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('textbox.text',textbox.text)
        # Run 'End Routine' code from code
        if textbox.text == str(response):
            correct = 1
            fbTxt = 'Correct!'
        else:
            correct = 0
            fbTxt = 'Incorrect'
        thisExp.addData('correct', correct)
        
        # Store each response in list
        allResponses.append(correct)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        # the Routine "Recall" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        feedback_text.setText(fbTxt)
        # keep track of which components have finished
        FeedbackComponents = [feedback_text]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Feedback" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.started')
                feedback_text.setAutoDraw(True)
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback" ---
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from feedback_code
        # for incorrect, check that two responses exist
        # and that their sum of last two responses is zero
        if len(allResponses) >= 3 and sum(allResponses[-3:]) == 0:
            trials.finished = True
            blocks.finished = True
        # If sum of last two responses is 2, move to next sequence
        elif sum(allResponses[-2:]) == 2:
            trials.finished = True
            allResponses = []
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
# completed 5.0 repeats of 'blocks'


# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [thank_you]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thank_you.started')
        thank_you.setAutoDraw(True)
    if thank_you.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            thank_you.tStop = t  # not accounting for scr refresh
            thank_you.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thank_you.stopped')
            thank_you.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Instructions_Forward" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
start_fwd.keys = []
start_fwd.rt = []
_start_fwd_allKeys = []
# keep track of which components have finished
Instructions_ForwardComponents = [instr_fwd, start_fwd]
for thisComponent in Instructions_ForwardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions_Forward" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_fwd* updates
    if instr_fwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_fwd.frameNStart = frameN  # exact frame index
        instr_fwd.tStart = t  # local t and not account for scr refresh
        instr_fwd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_fwd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_fwd.started')
        instr_fwd.setAutoDraw(True)
    
    # *start_fwd* updates
    waitOnFlip = False
    if start_fwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_fwd.frameNStart = frameN  # exact frame index
        start_fwd.tStart = t  # local t and not account for scr refresh
        start_fwd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_fwd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_fwd.started')
        start_fwd.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_fwd.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_fwd.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_fwd.status == STARTED and not waitOnFlip:
        theseKeys = start_fwd.getKeys(keyList=['space'], waitRelease=False)
        _start_fwd_allKeys.extend(theseKeys)
        if len(_start_fwd_allKeys):
            start_fwd.keys = _start_fwd_allKeys[-1].name  # just the last key pressed
            start_fwd.rt = _start_fwd_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_ForwardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions_Forward" ---
for thisComponent in Instructions_ForwardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_fwd.keys in ['', [], None]:  # No response was made
    start_fwd.keys = None
thisExp.addData('start_fwd.keys',start_fwd.keys)
if start_fwd.keys != None:  # we had a response
    thisExp.addData('start_fwd.rt', start_fwd.rt)
thisExp.nextEntry()
# the Routine "Instructions_Forward" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks_fwd = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('choose_digitSpan_fwd.xlsx'),
    seed=None, name='blocks_fwd')
thisExp.addLoop(blocks_fwd)  # add the loop to the experiment
thisBlocks_fwd = blocks_fwd.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_fwd.rgb)
if thisBlocks_fwd != None:
    for paramName in thisBlocks_fwd:
        exec('{} = thisBlocks_fwd[paramName]'.format(paramName))

for thisBlocks_fwd in blocks_fwd:
    currentLoop = blocks_fwd
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_fwd.rgb)
    if thisBlocks_fwd != None:
        for paramName in thisBlocks_fwd:
            exec('{} = thisBlocks_fwd[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_fwd = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condition_file_fwd),
        seed=None, name='trials_fwd')
    thisExp.addLoop(trials_fwd)  # add the loop to the experiment
    thisTrials_fwd = trials_fwd.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_fwd.rgb)
    if thisTrials_fwd != None:
        for paramName in thisTrials_fwd:
            exec('{} = thisTrials_fwd[paramName]'.format(paramName))
    
    for thisTrials_fwd in trials_fwd:
        currentLoop = trials_fwd
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_fwd.rgb)
        if thisTrials_fwd != None:
            for paramName in thisTrials_fwd:
                exec('{} = thisTrials_fwd[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        digitLoop_fwd = data.TrialHandler(nReps=digitSpan_fwd, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='digitLoop_fwd')
        thisExp.addLoop(digitLoop_fwd)  # add the loop to the experiment
        thisDigitLoop_fwd = digitLoop_fwd.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_fwd.rgb)
        if thisDigitLoop_fwd != None:
            for paramName in thisDigitLoop_fwd:
                exec('{} = thisDigitLoop_fwd[paramName]'.format(paramName))
        
        for thisDigitLoop_fwd in digitLoop_fwd:
            currentLoop = digitLoop_fwd
            # abbreviate parameter names if possible (e.g. rgb = thisDigitLoop_fwd.rgb)
            if thisDigitLoop_fwd != None:
                for paramName in thisDigitLoop_fwd:
                    exec('{} = thisDigitLoop_fwd[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "Presentation_Forward" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            pres_text_fwd.setText(str(digits_fwd)[digitLoop_fwd.thisN])
            # keep track of which components have finished
            Presentation_ForwardComponents = [fixation_fwd, pres_text_fwd]
            for thisComponent in Presentation_ForwardComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Presentation_Forward" ---
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_fwd* updates
                if fixation_fwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_fwd.frameNStart = frameN  # exact frame index
                    fixation_fwd.tStart = t  # local t and not account for scr refresh
                    fixation_fwd.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_fwd, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_fwd.started')
                    fixation_fwd.setAutoDraw(True)
                if fixation_fwd.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_fwd.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_fwd.tStop = t  # not accounting for scr refresh
                        fixation_fwd.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_fwd.stopped')
                        fixation_fwd.setAutoDraw(False)
                
                # *pres_text_fwd* updates
                if pres_text_fwd.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    pres_text_fwd.frameNStart = frameN  # exact frame index
                    pres_text_fwd.tStart = t  # local t and not account for scr refresh
                    pres_text_fwd.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(pres_text_fwd, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pres_text_fwd.started')
                    pres_text_fwd.setAutoDraw(True)
                if pres_text_fwd.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > pres_text_fwd.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        pres_text_fwd.tStop = t  # not accounting for scr refresh
                        pres_text_fwd.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'pres_text_fwd.stopped')
                        pres_text_fwd.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Presentation_ForwardComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Presentation_Forward" ---
            for thisComponent in Presentation_ForwardComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
        # completed digitSpan_fwd repeats of 'digitLoop_fwd'
        
        
        # --- Prepare to start Routine "Recall_Forward" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        textbox_fwd.reset()
        key_resp_fwd.keys = []
        key_resp_fwd.rt = []
        _key_resp_fwd_allKeys = []
        # keep track of which components have finished
        Recall_ForwardComponents = [recall_txt_fwd, textbox_fwd, key_resp_fwd]
        for thisComponent in Recall_ForwardComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Recall_Forward" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recall_txt_fwd* updates
            if recall_txt_fwd.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recall_txt_fwd.frameNStart = frameN  # exact frame index
                recall_txt_fwd.tStart = t  # local t and not account for scr refresh
                recall_txt_fwd.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recall_txt_fwd, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recall_txt_fwd.started')
                recall_txt_fwd.setAutoDraw(True)
            
            # *textbox_fwd* updates
            if textbox_fwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_fwd.frameNStart = frameN  # exact frame index
                textbox_fwd.tStart = t  # local t and not account for scr refresh
                textbox_fwd.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_fwd, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_fwd.started')
                textbox_fwd.setAutoDraw(True)
            
            # *key_resp_fwd* updates
            waitOnFlip = False
            if key_resp_fwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_fwd.frameNStart = frameN  # exact frame index
                key_resp_fwd.tStart = t  # local t and not account for scr refresh
                key_resp_fwd.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_fwd, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_fwd.started')
                key_resp_fwd.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_fwd.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_fwd.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_fwd.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_fwd.getKeys(keyList=['return'], waitRelease=False)
                _key_resp_fwd_allKeys.extend(theseKeys)
                if len(_key_resp_fwd_allKeys):
                    key_resp_fwd.keys = _key_resp_fwd_allKeys[-1].name  # just the last key pressed
                    key_resp_fwd.rt = _key_resp_fwd_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Recall_ForwardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Recall_Forward" ---
        for thisComponent in Recall_ForwardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_fwd.addData('textbox_fwd.text',textbox_fwd.text)
        # Run 'End Routine' code from code_fwd
        if textbox_fwd.text == str(digits_fwd):
            correct = 1
            fbTxtFwd = 'Correct!'
        else:
            correct = 0
            fbTxtFwd = 'Incorrect'
        thisExp.addData('correct', correct)
        
        # Store each response in list
        allResponsesfwd.append(correct)
        # check responses
        if key_resp_fwd.keys in ['', [], None]:  # No response was made
            key_resp_fwd.keys = None
        trials_fwd.addData('key_resp_fwd.keys',key_resp_fwd.keys)
        if key_resp_fwd.keys != None:  # we had a response
            trials_fwd.addData('key_resp_fwd.rt', key_resp_fwd.rt)
        # the Routine "Recall_Forward" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Feedback_Forward" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        feedback_text_fwd.setText(fbTxtFwd)
        # keep track of which components have finished
        Feedback_ForwardComponents = [feedback_text_fwd]
        for thisComponent in Feedback_ForwardComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Feedback_Forward" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text_fwd* updates
            if feedback_text_fwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text_fwd.frameNStart = frameN  # exact frame index
                feedback_text_fwd.tStart = t  # local t and not account for scr refresh
                feedback_text_fwd.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text_fwd, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text_fwd.started')
                feedback_text_fwd.setAutoDraw(True)
            if feedback_text_fwd.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text_fwd.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text_fwd.tStop = t  # not accounting for scr refresh
                    feedback_text_fwd.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_fwd.stopped')
                    feedback_text_fwd.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback_ForwardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Feedback_Forward" ---
        for thisComponent in Feedback_ForwardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from feedback_code_fwd
        # for incorrect, check that two responses exist
        # and that their sum of last two responses is zero
        if len(allResponsesfwd) >= 3 and sum(allResponsesfwd[-3:]) == 0:
            trials_fwd.finished = True
            blocks_fwd.finished = True
        # If sum of last two responses is 2, move to next sequence
        elif sum(allResponsesfwd[-2:]) == 2:
            trials_fwd.finished = True
            allResponsesfwd = []
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_fwd'
    
# completed 5.0 repeats of 'blocks_fwd'


# --- Prepare to start Routine "End_Fwd" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
End_FwdComponents = [thank_you_fwd]
for thisComponent in End_FwdComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End_Fwd" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you_fwd* updates
    if thank_you_fwd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you_fwd.frameNStart = frameN  # exact frame index
        thank_you_fwd.tStart = t  # local t and not account for scr refresh
        thank_you_fwd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you_fwd, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thank_you_fwd.started')
        thank_you_fwd.setAutoDraw(True)
    if thank_you_fwd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you_fwd.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            thank_you_fwd.tStop = t  # not accounting for scr refresh
            thank_you_fwd.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thank_you_fwd.stopped')
            thank_you_fwd.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_FwdComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End_Fwd" ---
for thisComponent in End_FwdComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- Prepare to start Routine "goodbye" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
goodbyeComponents = [text_goodbye]
for thisComponent in goodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "goodbye" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_goodbye* updates
    if text_goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_goodbye.frameNStart = frameN  # exact frame index
        text_goodbye.tStart = t  # local t and not account for scr refresh
        text_goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_goodbye, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_goodbye.started')
        text_goodbye.setAutoDraw(True)
    if text_goodbye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_goodbye.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_goodbye.tStop = t  # not accounting for scr refresh
            text_goodbye.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_goodbye.stopped')
            text_goodbye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "goodbye" ---
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
