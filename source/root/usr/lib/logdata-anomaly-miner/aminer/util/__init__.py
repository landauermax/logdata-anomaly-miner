"""This module contains various methods and class definitions
useful for various components from parsing, analysis and event
handling. Larger separate blocks of code should be split into
own subfiles or submodules, e.g. persistency."""

import random

from aminer.input import AtomHandlerInterface

def getLogInt(maxBits):
  """Get a log-distributed random integer integer in range 0 to
  maxBits-1."""
  randBits = random.randint(0, (1<<maxBits)-1)
  result = 0
  while (randBits&1) != 0:
    result += 1
    randBits >>= 1
  return result


class ObjectHistory(object):
  """This is the superinterface of all object histories. The idea
  behind that is to use that type of history best suited for a
  purpose considering amount of data, possibility for history
  size limits to be reached, priorization which elements should
  be dropped first."""

  def addObject(self, newObject):
    """Add an object to this history. This method call may evict
    other objects from the history."""
    raise Exception('Interface method called')

  def getHistory(self):
    """Get the whole history list. Make sure to clone the list
    before modification when influences on this object are not
    intended."""
    raise Exception('Interface method called')

  def clearHistory(self):
    """Clean the whole history."""
    raise Exception('Interface method called')


class LogarithmicBackoffHistory(ObjectHistory):
  """This class keeps a history list of items with logarithmic
  storage characteristics. When adding objects, the list will
  be filled to the maximum size with the newest items at the end.
  When filled, adding a new element will move with probability
  1/2 the last element to the next lower position before putting
  the new item to the end position. With a chance of 1/4, the
  last 2 elements are moved, with 1/8 the last 3, ... Thus the
  list will in average span a time range of 2^maxItems items with
  growing size of holes towards the earliest element."""

  def __init__(self, maxItems, initialList=None):
    self.maxItems = maxItems
    if initialList is None:
      initialList = []
    else: initialList = initialList[:maxItems]
    self.history = initialList

  def addObject(self, newObject):
    """Add a new object to the list according to the rules described
    in the class docstring."""
    if len(self.history) < self.maxItems:
      self.history.append(newObject)
    else:
      movePos = getLogInt(self.maxItems)
      if movePos != 0:
        self.history = self.history[:self.maxItems-movePos]+ \
            self.history[self.maxItems+1-movePos:]+[newObject]
      else:
        self.history[-1] = newObject

  def getHistory(self):
    """Get the whole history list. Make sure to clone the list
    before modification when influences on this object are not
    intended."""
    return self.history

  def clearHistory(self):
    """Clean the whole history."""
    self.history[:] = []


class TimeTriggeredComponentInterface(object):
  """This is the common interface of all components that can be
  registered to receive timer interrupts. There might be different
  timelines for triggering, real time and normalized log data
  time scale for forensic analysis. For forensic analyis different
  timers might be available to register a component. Therefore
  the component should state, which type of triggering it would
  require."""

  def getTimeTriggerClass(self):
    """Get the trigger class this component can be registered
    for. See AnalysisContext class for different trigger classes
    available."""
    raise Exception('Interface method called')

  def doTimer(self, triggerTime):
    """This method is called to perform trigger actions and to
    determine the time for next invocation. The caller may decide
    to invoke this method earlier than requested during the previous
    call. Classes implementing this method have to handle such
    cases. Each class should try to limit the time spent in this
    method as it might delay trigger signals to other components.
    For extensive compuational work or IO, a separate thread should
    be used.
    @param triggerTime the time this trigger is invoked. This
    might be the current real time when invoked from real time
    timers or the forensic log timescale time value.
    @return the number of seconds when next invocation of this
    trigger is required."""
    raise Exception('Interface method called')


class VolatileLogarithmicBackoffAtomHistory(AtomHandlerInterface, LogarithmicBackoffHistory):
  """This class is a volatile filter to keep a history of log
  atoms, e.g. for analysis by other components or for external
  access via remote control interface."""

  def __init__(self, maxItems):
    """Initialize the history component."""
    LogarithmicBackoffHistory.__init__(self, maxItems)

  def receiveAtom(self, logAtom):
    """Receive an atom and add it to the history log."""
    self.addObject(logAtom)
    return True
