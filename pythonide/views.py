from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "index.html", {"result": []})

@csrf_exempt
def submit(request):
    # Load Data
    import json
    data = json.loads(request.body)

    codes = data['code']
    stdin = data['input']

    f = open("in.txt", "w")
    f.write(stdin)
    f.close()

    # Make Python File
    #codes = "import sys\nsys.stdin = open('in.txt', 'r')\nsys.stdout = open('out.txt','w')\n" + codes

    code_start = "import sys\nsys.stdin = open('in.txt', 'r')\nsys.stdout = open('out.txt','w')\ntry:\n"
    
    f = open("codeFile.txt", "w")
    f.write(codes)
    f.close()

    f = open("codeFile.txt", "r")
    for i in f.readlines():
        code_start += "\t" + i + "\n"
    f.close()

    code_start += "\nexcept Exception as e:\n\tprint('Error Message: {}'.format(e))"

    code_start = code_start.replace("input", "sys.stdin.readline")

    print(code_start)

    f = open("compile.py", "w")
    f.write(code_start)
    f.close()

    import os
    os.system("python3 compile.py")

    # Processing Output
    f = open("out.txt", "r").read()

    f = f.replace("\n", "<br>")

    return JsonResponse({ 'result': f })
    #return render(request, "index.html", {"result": f.split("\n")})

    