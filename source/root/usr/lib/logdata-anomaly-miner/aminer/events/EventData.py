from aminer.input.LogAtom import LogAtom
from datetime import datetime
from aminer.analysis import CONFIG_KEY_LOG_LINE_PREFIX

class EventData(object):

    def __init__(self, eventType, eventMessage, sortedLogLines, eventData, eventSource, analysisContext):
      self.eventType = eventType
      self.eventMessage = eventMessage
      self.sortedLogLines = sortedLogLines
      self.eventSource = eventSource
      self.analysisContext = analysisContext
      if analysisContext is not None:
        self.description = '"%s"' % analysisContext.getNameByComponent(eventSource)
      else:
        self.description = ''
      if isinstance(eventData, LogAtom):
        self.logAtom = eventData
      elif isinstance(eventData, list):
        self.eventData = eventData
#         self.dataList = None
#       elif isinstance(eventData, list) and len(eventData) == 2:
#         if isinstance(eventData[0], LogAtom):
#           self.logAtom = eventData[0]
#         if isinstance(eventData[1], tuple):
#           self.dataList = list(eventData[1])
#         elif isinstance(eventData[1], list):
#           self.dataList = eventData[1]
      elif eventData is None:
        return
      else:
        raise(Exception("wrong eventData type!"))
    
    def receiveEventString(self):
      message = ''
      if hasattr(self, "logAtom"):
        if self.logAtom.getTimestamp() is None:
          self.logAtom.atomTime = datetime.now()
        if not isinstance(self.logAtom.getTimestamp(), datetime):
          atomTime = datetime.fromtimestamp(self.logAtom.getTimestamp())
        else:
          atomTime = self.logAtom.getTimestamp()
        message += '%s ' % atomTime.strftime("%Y-%m-%d %H:%M:%S")
        message += '%s\n' % (self.eventMessage)
        size = 0
        line = None
        for line in self.sortedLogLines:
          if isinstance(line, bytes):
            line = repr(line)
          size += line.count("\n")
        if size is 0:
          size = len(self.sortedLogLines)
        elif not line.endswith("\n"):
          size += 1
        message += '%s: %s (%d lines)\n' % (self.logAtom.source.__class__.__name__, self.description, size)
      elif hasattr(self, "eventData"):
        for line in self.eventData:
          if isinstance(line, bytes):
            if line is not b'':
              message += '  '+line.decode("utf-8")+'\n'
            else:
              if line is not '':
                message += '  '+line+'\n'
      else:
        size = 0
        line = None
        for line in self.sortedLogLines:
          if isinstance(line, bytes):
            line = repr(line)
          size += line.count("\n")
        if size is 0:
          size = len(self.sortedLogLines)
        elif not line.endswith("\n"):
          size += 1
        message += '%s (%d lines)\n' % (self.eventMessage, size)
      #if self.logAtom.parserMatch is not None:
      #  message += '  '+self.logAtom.parserMatch.matchElement.annotateMatch('')+'\n'
      for line in self.sortedLogLines:
        if isinstance(line, bytes):
          if line is not b'':
            message += '  '+line.decode("utf-8")+'\n'
        else:
          if line.startswith(self.analysisContext.aminerConfig.configProperties.get(CONFIG_KEY_LOG_LINE_PREFIX)):
            message+= line+'\n'
          elif line is not '':
            message += '  '+line+'\n'
      #if self.dataList is not None:
      #  for line in self.dataList:
      #    message += '  '+line+'\n'
      
      #print("%s" % message)
      return message
        