# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:42:41 2022

@author: vigne
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('D:/tcs madhu/trained_model.sav','rb'))

def prediction(input_data):
    
    input_array=np.array(input_data)
    input_reshape=input_array.reshape(1,-1)
    prediction=loaded_model.predict(input_reshape)
    if (prediction[0]==0):
      return "Ranking : 4"
    elif (prediction[0]==1):
      return "Ranking : 3"
    elif (prediction[0]==2):
      return "Ranking : 2"
    else:
      return "Ranking : 1"

def main():
    st.title('Rank features of smartphone app')
    battery_power=st.text_input('Battery Power')
    blue=st.text_input('Bluetooth')
    clock_speed=st.text_input('Clock Speed')
    dual_sim=st.text_input('Dual Sim')
    four_g=st.text_input('4G')
    fc=st.text_input('Front Camera')
    int_memory=st.text_input('Internal Memory')
    m_dep=st.text_input('Mobile depth')
    mobile_wt=st.text_input('Mobile Width')
    n_cores=st.text_input('Number of cores of a processor')
    pc=st.text_input('Primary Camera')
    px_height=st.text_input('Pixel Resolution Height')
    px_width=st.text_input('Pixel Resolution Width')
    ram=st.text_input('RAM')
    sc_h=st.text_input('Screen Height')
    sc_w=st.text_input('Screen Width')
    talk_time=st.text_input('Talk Time')
    three_g=st.text_input('3G')
    touch_screen=st.text_input('Touch Screen')
    wifi=st.text_input('WIFI')
    
    
    Rank=''
    
    if st.button('Find'):
        Rank=prediction([battery_power,blue,clock_speed,dual_sim,four_g,fc,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi])
        
    st.success(Rank)

if __name__=='__main__':
    main()