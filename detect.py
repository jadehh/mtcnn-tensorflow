#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 作者：2019/9/2 by jade
# 邮箱：jadehh@live.com
# 描述：TODO
# 最近修改：2019/9/2  下午4:32 modify by jade
from detection import get_faces
import cv2
from jade import *
img = cv2.imread("images/office4.jpg")
bboxes,label_texts,labels,scores,face_img = get_faces(img, 0.6)
result_img = CVShowBoxes(img,bboxes,label_texts,labels,scores,waitkey=-1)
image = CutImageWithBoxes(img,bboxes)
cv2.imshow("result",result_img)
cv2.imshow("no_alignment",image[0])
cv2.imshow("alignment",face_img)
cv2.waitKey(0)