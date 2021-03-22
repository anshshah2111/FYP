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
import networkx as nx 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
#import cv2
# from collections import defaultdict
# import pandas as pd
def kansara(dest):

    G = nx.Graph()

    
    #img1 = mpimg.imread('hello/static/images/5.jpg')
    img1=mpimg.imread('hello/static/images/5.jpg')
    img2=mpimg.imread('hello/static/images/7.jpg')
    

    G.add_nodes_from(['lounge','television','speaker','hallway-1','stairs-1','stairs-2','stairs-3','stairs-4','railing','entrance table',
                    'entrance-vase','door hinge','entrance door','entrance closet','master bedroom chair','master bedroom closet',
                    'master bedroom nightstand','master bedroom bed','master bedroom lamp','washroom door','shower','tap','washroom mirror',
                    'toiletries','kitchen door','kitchen cabinet','kitchen counter','induction cooker','grill','kitchen table','dining room door',
                    'trophy mantle','dining room table','coffee table','dining room hallway-1','coffee room chair','bookshelf','dining room sofa',
                    'living room door','living room chair','living room sofa','living room curtains','telephone','living room chair','dining room hallway-2',
                    'study table','wash basin','study room closet','study room bed','study room nightstand'])

    G.add_edge('lounge','television', weight=2, length=40, X=-0.6, Y=1, image=img1)
    G.add_edge('television','speaker', weight=1, length=40)
    G.add_edge('speaker','hallway-1', weight=2, length=40)
    G.add_edge('hallway-1','stairs-1', weight=1, length=40)
    G.add_edge('stairs-1','stairs-2', weight=1, length=40)
    G.add_edge('stairs-2','stairs-3', weight=1, length=40)
    G.add_edge('stairs-3','stairs-4', weight=1, length=40)
    G.add_edge('stairs-4','railing', weight=1, length=40)
    G.add_edge('stairs-4','master bedroom chair', weight=3, length=40)
    G.add_edge('railing','entrance table', weight=2, length=40)
    G.add_edge('entrance table','entrance-vase', weight=1, length=40)
    G.add_edge('entrance table','door hinge', weight=1, length=40)
    G.add_edge('door hinge','entrance door', weight=1, length=40)
    G.add_edge('entrance door','entrance closet', weight=2, length=40)
    G.add_edge('entrance door','entrance mirror', weight=2.5, length=40)
    G.add_edge('entrance closet','entrance mirror', weight=1.5, length=40)
    G.add_edge('master bedroom chair','master bedroom closet', weight=1, length=40)
    G.add_edge('master bedroom closet','master bedroom nightstand', weight=1.5, length=40)
    G.add_edge('master bedroom nightstand','master bedroom bed', weight=1, length=40)
    G.add_edge('master bedroom bed','master bedroom lamp', weight=2, length=40)
    G.add_edge('master bedroom lamp','washroom door', weight=3, length=40)
    G.add_edge('washroom door','shower', weight=1.5, length=40)
    G.add_edge('shower','tap', weight=1, length=40)
    G.add_edge('tap','washroom mirror', weight=1, length=40)
    G.add_edge('washroom door','toiletries', weight=2, length=40)
    G.add_edge('toiletries','kitchen door', weight=4, length=40)
    G.add_edge('kitchen door','kitchen cabinet', weight=2, length=40)
    G.add_edge('washroom mirror','kitchen door', weight=7, length=40)
    G.add_edge('kitchen cabinet','kitchen counter', weight=2, length=40)
    G.add_edge('kitchen counter','induction cooker', weight=1, length=40)
    G.add_edge('kitchen counter','kitchen table', weight=2, length=40)
    G.add_edge('induction cooker','grill', weight=1, length=40)
    G.add_edge('grill','kitchen table', weight=4, length=40)
    G.add_edge('kitchen table','dining room door', weight=3, length=40)
    G.add_edge('dining room door','trophy mantle', weight=3, length=40)
    G.add_edge('trophy mantle','dining room table', weight=4, length=40)
    G.add_edge('trophy mantle','coffee table', weight=2, length=50)
    G.add_edge('dining room table','dining room hallway-1', weight=7, length=50)
    G.add_edge('dining room table','coffee table', weight=4, length=50)
    G.add_edge('dining room table','living room chair', weight=8, length=50)
    G.add_edge('coffee table','coffee room chair', weight=1, length=50)
    G.add_edge('coffee table','bookshelf', weight=4, length=50)
    G.add_edge('dining room hallway-1','dining room hallway-2', weight=1, length=50)
    G.add_edge('coffee room chair','bookshelf', weight=2, length=50)
    G.add_edge('bookshelf','living room chair', weight=5, length=50)
    G.add_edge('bookshelf','dining room sofa', weight=2, length=50)
    G.add_edge('dining room sofa','living room door', weight=3, length=50)
    G.add_edge('living room door','living room chair', weight=2, length=50)
    G.add_edge('living room door','living room sofa', weight=4, length=50)
    G.add_edge('living room door','living room curtains', weight=8, length=50)
    G.add_edge('living room chair','living room sofa', weight=8, length=50)
    G.add_edge('living room sofa','living room curtains', weight=4, length=50)
    G.add_edge('living room sofa','living room curtains', weight=2, length=50)
    G.add_edge('living room sofa','telephone', weight=2, length=50)
    G.add_edge('living room curtains','telephone', weight=2, length=50)
    G.add_edge('dining room hallway-2','study table', weight=4, length=50)
    G.add_edge('study table','wash basin', weight=2, length=50)
    G.add_edge('wash basin','study room closet', weight=3, length=50)
    G.add_edge('study room closet','study room bed', weight=2, length=50)
    G.add_edge('study room bed','study room nightstand', weight=3, length=50)

    # self.x=x
    #x = 'living room sofa'
    short = nx.shortest_path(G,'lounge',dest)
    print(short)

    all_nodes = G.nodes()
    alll = list(all_nodes)

    # print(type(alll))
    # print(type(short))

    color_map = []
    for i in alll:
        if i in short:
            color_map.append('green')
        else:
            color_map.append('red')
    
    pos = {'lounge' : [1,1] ,'television' : [8,1] ,'speaker' : [13,1] ,'hallway-1' : [18,1] ,'stairs-1' : [23,2] ,'stairs-2' : [28,3] ,'stairs-3' : [33,4] ,'stairs-4' : [38,5] ,'railing' : [50,5] ,'entrance table' : [60,5] ,
       'entrance-vase' : [65,4] , 'entrance mirror' : [70,4],'door hinge' : [72,5] ,'entrance door' : [77,5] ,'entrance closet' : [82,4] ,'master bedroom chair' : [18,7] ,'master bedroom closet' : [13,8] ,
       'master bedroom nightstand' : [19,6] ,'master bedroom bed' : [21,6] ,'master bedroom lamp' : [14,5] ,'washroom door' : [12,6] ,'shower' : [8,7] ,'tap' : [8,8] ,'washroom mirror' : [2,10] ,
       'toiletries' : [2,10] ,'kitchen door' : [-5,13] ,'kitchen cabinet' : [-10,15] ,'kitchen counter' : [-20,18] ,'induction cooker' : [-25,23] ,'grill' : [-20,27],'kitchen table' : [-8,27] ,'dining room door' : [0,40] ,
       'trophy mantle' : [10,38] ,'dining room table' : [20,43] ,'coffee table' : [23,40] ,'dining room hallway-1' : [20,47] ,'coffee room chair' : [23,37] ,'bookshelf' : [32,40] ,'dining room sofa' : [37,45] ,
       'living room door' : [40,48] ,'living room chair' : [47,48] ,'living room sofa' : [47,50] ,'living room curtains' : [70,43] ,'telephone' : [75,43] ,'living room chair' : [40,43] ,'dining room hallway-2' : [23,54] ,
       'study table' : [24,54] ,'wash basin' : [27,54] ,'study room closet' : [30,54] ,'study room bed' : [32,54] ,'study room nightstand'  : [37,57] }
    
    fig = plt.figure()
    # nx.draw(G, pos, with_labels = False, node_color = color_map,  
    #         node_size = 200, font_size = 9, font_family = 'calibri', 
    #         font_weight = 100, linewidths = 5, edge_color = 'white', 
    #         font_color = 'white')
    # nx.draw(G, with_labels=False, node_size=150, node_color = color_map, node_shape="o", alpha=0.5, linewidths=4,  
    #         font_color="grey", font_weight="bold", width=2,edge_color='white' )

    nx.draw(G , pos, with_labels = False, node_color = color_map,  
        node_size = 200, font_size = 9, font_family = 'calibri', 
        font_weight = 100, linewidths = 5, edge_color = 'black', 
        font_color = 'black')

    #to add images to the nodes
    ax=plt.gca()
    fig=plt.gcf()
    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform
    imsize = 0.1 # this is the image size
    #for n in G.nodes():
    #for lounge
    (x,y) = pos['lounge']
    xx,yy = trans((x,y)) # figure coordinates
    xa,ya = trans2((xx,yy)) # axes coordinates
    a = plt.axes([xa-imsize/2.0,ya-imsize/2.0, imsize, imsize ])
    a.imshow(img1)
    a.set_aspect('equal')
    a.axis('off')

    #for destination
    (a,b) = pos[dest]
    aa,bb = trans((a,b)) # figure coordinates
    ax,bx = trans2((aa,bb)) # axes coordinates
    b = plt.axes([ax-imsize/2.0,bx-imsize/2.0, imsize, imsize ])
    b.imshow(img2)
    b.set_aspect('equal')
    b.axis('off')


    
    fig.set_facecolor('#87ceff')
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
        locations = ['lounge','television','speaker','hallway-1','stairs-1','stairs-2','stairs-3','stairs-4','railing','entrance table',
                  'entrance-vase','door hinge','entrance door','entrance closet','master bedroom chair','master bedroom closet',
                  'master bedroom nightstand','master bedroom bed','master bedroom lamp','washroom door','shower','tap','washroom mirror',
                  'toiletries','kitchen door','kitchen cabinet','kitchen counter','induction cooker','grill','kitchen table','dining room door',
                  'trophy mantle','dining room table','coffee table','dining room hallway-1','coffee room chair','bookshelf','dining room sofa',
                  'living room door','living room chair','living room sofa','living room curtains','telephone','living room chair','dining room hallway-2',
                  'study table','wash basin','study room closet','study room bed','study room nightstand']
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

