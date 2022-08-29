from django.shortcuts import render, redirect
from django.contrib import messages

from asgiref.sync import async_to_sync

from tools.tools import *

from textanalyzer.captcha import check_recpatcha, captchaVerificationFailedHandler
# Create your views here.


def index(request):
  return render(request, 'tools/index.html')



@async_to_sync
async def analyser(request):
   # THE TEXT WHICH IS GOING TO BE ANALYZED
   raw_text = request.POST.get('text', None) 

   # SOME IPORTANT VARS
   removepunc = request.POST.get('removepunc', "off")
   removenum = request.POST.get('removenum', "off")
   removealpha = request.POST.get('removealpha', "off")
   removespecialchar = request.POST.get('removespecialchar', "off")
   newlineremover = request.POST.get('newlineremover', "off")
   extraspaceremover = request.POST.get('extraspaceremover', "off")
   extractUrls = request.POST.get('extracturls', "off")

   fullcaps = request.POST.get('fullcaps', "off")
   lowercaps = request.POST.get('lowercaps', "off")

   charcount = request.POST.get('charcount', "off")
   alphacount = request.POST.get('alphacount', "off")
   alphanumericcount = request.POST.get('alphanumericcount', "off")

   res = check_recpatcha(request)

   if res != True:
      captchaVerificationFailedHandler(request, res)
      return redirect("/tools/analyser")
   
   __analyser__engine = Tools(raw_text=raw_text, removepunc=removepunc, removenum=removenum, removealpha=removealpha, removespecialchar=removespecialchar, newlineremover=newlineremover, extraspaceremover=extraspaceremover, fullcaps=fullcaps, lowercaps=lowercaps, charcount=charcount, alphacount=alphacount, alphanumericcount=alphanumericcount, extractUrls=extractUrls)

   result = await __analyser__engine.main()

   if result['output'] == "No Output.":
      messages.error(request, "Some Error Occurred.")

   else:
     messages.success(request, 'Successfully analysed the text.')

   return render(request, 'tools/output.html', result)

def editor(request):
   return render(request, 'tools/editor.html')
      
def styler(request):
   return render(request, 'tools/styler.html')