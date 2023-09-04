import os
import re
from textanalyzer.constants import ToolsConstant


class Tools():
    """An object to analyse your text.

    **Tools** - This class uses your inputs and some variables and changes them into your desired result.


    .. warning::
        Do not subclass this class if you are a beginner. This is for an experimental app with django.
    
    ::
    
    """

    def __init__(self, raw_text: str = None, removepunc: str = None, removenum: str = None, removealpha: str = None, removespecialchar: str = None, newlineremover: str = None, extraspaceremover: str = None, extractUrls: str = None, fullcaps: str = None, lowercaps: str = None, charcount: str = None, alphacount: str = None, alphanumericcount: str = None):

        # THINGS TO ANALYZE
        self.raw_text = raw_text

        # CHARACTER COUNT
        self.count = 0
        self._count = 0

        # IMPORTANT VARS
        self.operations = []
        self.output = ''

        # OPTIONS
        self.removepunc = removepunc
        self.removenum = removenum
        self.removealpha = removealpha
        self.removespecialchar = removespecialchar

        self.newlineremover = newlineremover
        self.extraspaceremover = extraspaceremover

        self.extractUrls = extractUrls

        self.fullcaps = fullcaps
        self.lowercaps = lowercaps

        self.charcount = charcount
        self.alphacount = alphacount
        self.alphanumericcount = alphanumericcount

        # CONSTANTS
        self.alphabets = ToolsConstant.alphabets
        self.numbers = ToolsConstant.numbers
        self.punctuations = ToolsConstant.punctuations
        self.specialcharacters = ToolsConstant.specialcharacters

    async def removeAlphabets(self):
        """|coro|

        Removes alphabets from the given string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = ''.join(char for char in self.raw_text if char not in set(self.alphabets))

        await self.set_results(output=output, operation="Removed Alphabets")


    async def removeNumbers(self):
        """|coro|

        Removes numbers from the given string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = ''.join(char for char in self.raw_text if char not in set(self.numbers))

        await self.set_results(output=output, operation="Removed Numbers")

    async def removePunctuations(self):
        """|coro|

        Removes punctuations from the given string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = ''.join(char for char in self.raw_text if char not in set(self.punctuations))

        await self.set_results(output=output, operation="Removed Punctuations")

    async def removeSpecialCharacters(self):
        """|coro|

        Removes special characters from the given string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = ''.join(char for char in self.raw_text if char not in set(self.specialcharacters))

        await self.set_results(output=output, operation="Removed Special Characters")

    async def extraSpaceRemover(self):
        """|coro|

        Removes extra spaces from the given string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = re.sub(' +', ' ', self.raw_text)

        await self.set_results(output=output, operation="Removed Extra Spaces")

    async def newLineRemover(self):
        """|coro|

        Removes new line characters from the given string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = os.linesep.join([line for line in self.raw_text.splitlines() if line.strip() != '' ])

        await self.set_results(output=output, operation="Removed New Line Characters")

    async def extractURL(self):
        """|coro|

        Extracts urls from the given string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = ', '.join(re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.raw_text))

        await self.set_results(output=output, operation="Extracted URLs")

    async def toFullUppercase(self):
        """|coro|

        Changes text's case to upper.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = self.raw_text.upper()

        await self.set_results(output=output, operation="Changes to uppercase.")


    async def toFullLowercase(self):
        """|coro|

        Changes text's case to lower.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = self.raw_text.lower()

        await self.set_results(output=output, operation="Changes to lowercase.")


    async def countCharacters(self):
        """|coro|

        Counts the no. of characters in a string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = sum(not char.isspace() for char in self.raw_text.rstrip())

        await self.set_results(count=output, operation="Counted the no. of characters.")

    async def countAlphas(self):
        """|coro|

        Counts the no. of alphabets in a string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = 0
        for char in self.raw_text:
            if char.isalpha():
                output += 1

        await self.set_results(count=output, operation="Counted the no. of alphabets.")


    async def countAlphaNumeric(self):
        """|coro|

        Counts the no. of alphabets and numbers in a string.

        Parameters
        ----------

        :class:`Parametreless` - No parametre is required.  

        ----------

        """

        output = 0
        _output = 0

        for char in self.raw_text:
            if char.isalpha():
                output += 1

            if  char.isnumeric():
                _output += 1 

        await self.set_results(count=output, _count =_output, operation="Counted the no. of alphabets and numbers.")


    async def set_results(self, output: str = None, count: int = None, _count: int = None, operation: str = None) -> None:
        """|coro|

        Sets the values of the args.

        Parameters
        ----------
        
        `output` - [Optional: ```type: str```] Output achieved from analysing related functions `e,g: removeAlphabets, etc.`.

        `count` -  [Optional: ```type: int```] If using counting actions then can pass the result.
        
        `__count` -  [Optional: ```type: int```] If using `countAlphaNumeric()` function.

        `operation` - [Optional: ```type: str```] The name of the action performed.

        ----------

        """
 
        if output:
           self.raw_text = output
           self.output = self.raw_text

        else:  
            self.count = count 
            self._count = _count

            self.output = self.count            

        self.operations.append(operation)

        return None


    async def get_results(self):
     """|coro|
 
         Sends the values of the args.
 
     """
     
     __params =  {"purpose": ' , '.join(self.operations), "output": self.output}

     return __params
 

    async def main(self):
        if self.removepunc == "on":
          await self.removePunctuations()

        if(self.removenum == "on"):
            await self.removeNumbers()

        if(self.removealpha == "on") :
            await self.removeAlphabets()

        if(self.removespecialchar == "on"):
           await self.removeSpecialCharacters()

        if(self.fullcaps == "on"):
           await self.toFullUppercase()

        if(self.lowercaps == "on"):
           await self.toFullLowercase()

        if(self.extraspaceremover == "on"):
           await self.extraSpaceRemover()

        if(self.newlineremover == "on"):
           await self.newLineRemover()

        if(self.charcount == "on"):
           await self.countCharacters()

        if(self.alphacount == "on"):
           await self.countAlphas()

        if(self.extractUrls == "on"):
           await self.extractURL()

        __result  = await self.get_results()   

        if(self.alphanumericcount == "on"):
            await self.countAlphaNumeric()
            __result['count'] = self.count
            __result['output'] = 'alphanumeric'
            __result['num_count'] = self._count   


        if(self.removepunc != "on" and self.newlineremover != "on" and self.extraspaceremover != "on" and self.fullcaps != "on" and self.lowercaps != "on" and self.charcount != "on" and self.removenum != "on" and self.removealpha != "on" and self.removespecialchar != "on" and self.alphanumericcount != "on" and self.alphacount != "on" and self.extractUrls != "on") :
            __result = {'purpose': "Error Occurred", 'output': 'No Output.'} 



        return __result    

