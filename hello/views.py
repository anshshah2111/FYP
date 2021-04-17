from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import matplotlib.image as mpimg 
import re
import requests
import base64


# Create your views here.
def fyp(request):
    return render(request,'./fyp.html')
def index(request):
    return render(request,'./index.html')
def workspace(request):
    return render(request,'./workspace.html')
def navigation(request):
    return render(request,'./navigation.html')
def nlpdemo(request):
    return render(request,'./nlpdemo.html')
def objdetect(request):
    return render(request,'./objdetect.html')
import networkx as nx 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
#import cv2
# from collections import defaultdict
# import pandas as pd
def kansara(destination):

    G = nx.Graph()

    
    #img1 = mpimg.imread('hello/static/images/5.jpg')
    img1=mpimg.imread('hello/static/images/E.png')
    img2=mpimg.imread('hello/static/images/G.png')
    

    G.add_nodes_from(['entrance', 'master bedroom door', 'master bed', 'nightstand','frontyard window', 'master bedroom lamp', 'bathroom door', 'weighing scale', 'toiletries', 'bathroom sink', 'shoe rack', 
                    'washroom door', 'wash basin', 'commode', 'shower', 'hallway-1', 'study', 'wardrobe', 'whiteboard', 'study table', 'study chair', 
                    'study sofa', 'library', 'hallway-2', 'bedroom door', 'left twin bed', 'right twin bed', 'bedroom nightstand', 'hat stand', 'hallway-3', 'laundry room',
                    'press', 'washing machine', 'backyard window', 'folding station', 'stairs', 'chopping board', 'induction', 'kitchen cabinet', 'kitchen sink', 
                    'kitchen counter', 'computer table', 'living room window', 'dining chair', 'dining table', 'thermostat', 'backyard door', 'plug points', 'sofa', 'couch',
                    'leg rest', 'round table', 'television', 'speakers', 'living room closet'])

    G.add_edge('entrance', 'master bedroom door', weight=3)
    G.add_edge('entrance', 'shoe rack', weight=6)
    G.add_edge('entrance', 'washroom door', weight=8)
    G.add_edge('entrance', 'hallway-1', weight=12)
    G.add_edge('master bedroom door', 'frontyard window', weight=6 )
    G.add_edge('master bedroom door', 'master bed', weight= 7)
    G.add_edge('master bedroom door', 'nightstand', weight= 8)
    G.add_edge('frontyard window', 'nightstand', weight= 4)
    G.add_edge('frontyard window', 'master bed', weight= 6)
    G.add_edge('master bed', 'master bedroom lamp', weight=3 )
    G.add_edge('master bed', 'bathroom door', weight= 4)
    G.add_edge('master bedroom lamp', 'bathroom door', weight= 2)
    G.add_edge('bathroom door', 'weighing scale', weight=6)
    G.add_edge('bathroom door', 'toiletries', weight=2 )
    G.add_edge('bathroom door', 'bathroom sink', weight=7 )
    G.add_edge('weighing scale', 'bathroom sink', weight=2 )
    G.add_edge('weighing scale', 'toiletries', weight=6 )
    G.add_edge('shoe rack', 'washroom door', weight= 3 )
    G.add_edge('shoe rack', 'hallway-1', weight=8 )
    G.add_edge('washroom door', 'shower', weight=9 )
    G.add_edge('washroom door', 'commode', weight=5 )
    G.add_edge('washroom door', 'wash basin', weight=7 )
    G.add_edge('shower', 'commode', weight= 7)
    G.add_edge('shower', 'wash basin', weight= 5)
    G.add_edge('wash basin', 'commode', weight=2 )
    G.add_edge('washroom door', 'hallway-1', weight=6)
    G.add_edge('hallway-1', 'study', weight=7 )
    G.add_edge('hallway-1', 'hallway-2', weight=11 )
    G.add_edge('study', 'wardrobe', weight=2 )
    G.add_edge('study', 'whiteboard', weight=5 )
    G.add_edge('study', 'study table', weight=9 )
    G.add_edge('study', 'study chair', weight=8 )
    G.add_edge('study', 'study sofa', weight=8 )
    G.add_edge('study', 'library', weight=6 )
    G.add_edge('study sofa', 'library', weight=2)
    G.add_edge('study sofa', 'whiteboard', weight=4 )
    G.add_edge('study chair', 'study table', weight=2 )
    G.add_edge('study table', 'whiteboard', weight= 3)
    G.add_edge('study', 'hallway-2', weight=7)
    G.add_edge('hallway-2', 'bedroom door', weight=5 )
    G.add_edge('hallway-2', 'hallway-3', weight=7)
    G.add_edge('bedroom door', 'hat stand', weight=2)
    G.add_edge('bedroom door', 'left twin bed', weight=4)
    G.add_edge('bedroom door', 'right twin bed', weight=4 )
    G.add_edge('bedroom door', 'bedroom nightstand', weight=6 )
    G.add_edge('bedroom door', 'hallway-2', weight=4 )
    G.add_edge('hallway-3', 'laundry room', weight=6 )
    G.add_edge('hallway-3', 'stairs', weight=8 )
    G.add_edge('laundry room', 'press', weight=2 )
    G.add_edge('laundry room', 'washing machine', weight= 5)
    G.add_edge('washing machine', 'backyard window', weight=3 )
    G.add_edge('washing machine', 'folding station', weight=2)
    G.add_edge('laundry room', 'stairs', weight=4 )
    G.add_edge('stairs', 'chopping board', weight=3 )
    G.add_edge('stairs', 'kitchen sink', weight=6 )
    G.add_edge('chopping board', 'kitchen sink', weight=4 )
    G.add_edge('chopping board', 'induction', weight=6)
    G.add_edge('chopping board', 'kitchen counter', weight=8)
    G.add_edge('kitchen sink', 'induction', weight=3 )
    G.add_edge('kitchen sink', 'kitchen counter', weight= 2)
    G.add_edge('induction', 'kitchen counter', weight=3)
    G.add_edge('induction', 'kitchen cabinet', weight=4 )
    G.add_edge('kitchen counter', 'kitchen cabinet', weight=3 )
    G.add_edge('kitchen counter', 'computer table', weight=7)
    G.add_edge('kitchen counter', 'dining table', weight=12)
    G.add_edge('computer table', 'living room window', weight=3)
    G.add_edge('living room window', 'dining chair', weight=5 )
    G.add_edge('living room window', 'thermostat', weight=7 )
    G.add_edge('dining chair', 'dining table', weight=1)
    G.add_edge('dining table', 'thermostat', weight=4)
    G.add_edge('dining table', 'backyard door', weight= 3)
    G.add_edge('dining table', 'couch', weight=4 )
    G.add_edge('dining table', 'leg rest', weight=4)
    G.add_edge('thermostat', 'backyard door', weight=3 )
    G.add_edge('backyard door', 'plug points', weight=4 )
    G.add_edge('backyard door', 'sofa', weight=6)
    G.add_edge('backyard door', 'couch', weight=5)
    G.add_edge('plug points', 'sofa', weight=3)
    G.add_edge('plug points', 'speakers', weight=3)
    G.add_edge('sofa', 'round table', weight=2)
    G.add_edge('couch', 'round table', weight=2)
    G.add_edge('round table', 'leg rest', weight=2)
    G.add_edge('couch', 'leg rest', weight=1)
    G.add_edge('couch', 'television', weight=5 )
    G.add_edge('couch', 'living room closet', weight=6 )
    G.add_edge('round table', 'speakers', weight=4 )
    G.add_edge('speakers', 'television', weight=2)
    G.add_edge('television', 'living room closet', weight=2)


    # destination = 'round table'
    short = nx.shortest_path(G,'entrance',destination)
    print(short)

    all_nodes = G.nodes()
    alll = list(all_nodes)

    # print(type(alll))
    # print(type(short))

    color_map = []
    for i in alll:
        if i in short:
            color_map.append('#00ff00')
        else:
            color_map.append('#87ceff')

    pos = {'entrance' : [65,9] , 'master bedroom door' : [63,12] , 'master bed' : [61,30] , 'nightstand' : [64,39] ,'frontyard window' : [68,27] ,
        'master bedroom lamp' : [59,39] , 'bathroom door' : [57,36] , 'weighing scale' : [53,39] , 'toiletries' : [58,30] , 'bathroom sink' : [53,30] , 'shoe rack' : [57,6] , 
        'washroom door' : [55,12] , 'wash basin' : [53,21] , 'commode' : [56,21] , 'shower' : [50,15] , 'hallway-1' : [52,6] , 'study' : [48,12] , 'wardrobe' : [46,15] , 'whiteboard' : [43,18] ,
        'study table' : [41,27] , 'study chair' : [43,24] , 
        'study sofa' : [48,33] , 'library' : [45,33] , 'hallway-2' : [43,6] , 'bedroom door' : [36,12] , 'left twin bed' : [34,30] , 'right twin bed' : [38,30] ,
        'bedroom nightstand' : [36,36] , 'hat stand' : [33,15] , 'hallway-3' : [33,6] , 'laundry room' : [29,12] ,
        'press' : [34,15] , 'washing machine' : [34,30] , 'backyard window' : [33,36] , 'folding station' : [31,27] , 'stairs' : [30,9] ,
        'chopping board' : [29,15] , 'induction' : [29,24] , 'kitchen cabinet' : [29,33] , 'kitchen sink' : [24,15] , 
        'kitchen counter' : [24,30] , 'computer table' : [21,42] , 'living room window' : [19,45] , 'dining chair' : [17,36] , 'dining table' : [16,33] ,
        'thermostat' : [13,42] , 'backyard door' : [8,36] , 'plug points' : [8,24] , 'sofa' : [10,21] , 'couch' : [14,30] ,
        'leg rest' : [16,21] , 'round table' : [14,15] , 'television' : [12,9] , 'speakers' : [9,9] , 'living room closet' : [16,9] }
    fig = plt.figure()
    # nx.draw(G , pos, with_labels = False, node_color = color_map,  
    #         node_size = 200, font_size = 9, font_family = 'calibri', 
    #         font_weight = 100, linewidths = 5, edge_color = 'white', 
    #         font_color = 'white')

    nx.draw(G , pos, with_labels = False, node_color = color_map,  
            node_size = 30, node_shape="o", alpha=0.5, font_size = 9, font_family = 'calibri', 
            font_weight = 100, linewidths = 5, edge_color = 'white', 
            font_color = 'black')

    ax=plt.gca()
    fig=plt.gcf()
    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform
    imsize = 0.1 
    (x,y) = pos['entrance']
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize ])
    a.imshow(img1)
    a.set_aspect('equal')
    a.axis('off')


    (a,b) = pos[destination]
    aa,bb = trans((a,b)) # figure coordinates
    ax,bx = trans2((aa,bb)) # axes coordinates
    b = plt.axes([ax-imsize/2.0,bx-imsize/2.0, imsize, imsize ])
    b.imshow(img2)
    b.set_aspect('equal')
    b.axis('off')

       fig.set_facecolor('black')
    #plt.savefig("simple_graph.png")
    # img = plt.imread('env.jpeg')
    # fig, ax = plt.subplots()
    # ax.imshow(img)
    plt.grid('on')
    #plt.show()
    plt.savefig("simple_graph.png")
    img = mpimg.imread('simple_graph.png')
 
    # img = plt.imread('bg1.png')
    # fig, ax = plt.subplots()
    # ax.imshow(img)
    # plt.grid('on')
    #plt.show()
    return img

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        myDict = request.data.dict()
        #print(myDict['instruction'])
        instruction=myDict['instruction']
        print("INS IS",instruction)
        locations = ['entrance', 'master bedroom door', 'master bed', 'nightstand','frontyard window', 'master bedroom lamp', 'bathroom door', 'weighing scale', 'toiletries', 'bathroom sink', 'shoe rack', 
                    'washroom door', 'wash basin', 'commode', 'shower', 'hallway-1', 'study', 'wardrobe', 'whiteboard', 'study table', 'study chair', 
                    'study sofa', 'library', 'hallway-2', 'bedroom door', 'left twin bed', 'right twin bed', 'bedroom nightstand', 'hat stand', 'hallway-3', 'laundry room',
                    'press', 'washing machine', 'backyard window', 'folding station', 'stairs', 'chopping board', 'induction', 'kitchen cabinet', 'kitchen sink', 
                    'kitchen counter', 'computer table', 'living room window', 'dining chair', 'dining table', 'thermostat', 'backyard door', 'plug points', 'sofa', 'couch',
                    'leg rest', 'round table', 'television', 'speakers', 'living room closet']
        instruction_list = instruction.split(" ")
        # re.split("\s+", instruction)
        goal_location = ''

        found_word=False

        img=None
        for location in locations:
            if instruction.find(location)!= -1:
                goal_location=location
                found_word=True
                img=kansara(goal_location)
                print("Goal Loation is ",goal_location)
                break
        if not found_word:
             print("Wrong location, try again")

        # for word in instruction_list:
        #      if word in locations:
        #         goal_location = word 
        #         print("Goal Loation is ",goal_location)
                
        #      elif word not in locations:
        #         print("Wrong location, try again")
        # kansara(goal_location)
        return Response({"message": goal_location, "data": request.data,"img":img})
    return Response({"message": "Hello, world!"})
    


# def main():
#     return render_template('index.html')
#     def workspace(request):
#     return render(request,'./workspace.html')


@api_view(['GET','POST'])
def img_response(request):
    with open(
        "./simple_graph.png", "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    return Response({"image":image_data})

