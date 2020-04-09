import os
import random

config_names = ["Hisilicon","Apple","Realtek","Samsung","Falcon","SMIC","TSMC","GF","SM","TPE", "LPE"]
product_names= ["usb30","usb20","usb30_u2only","usb3_dev","usb3_drd","npi","host","host_crit","dev_npi"]
mode = ["axi","ahb","native","pipe","utmi","u2_only","suspended","absolete"]
ref_file = open('spyglass.html','r')
html = ref_file.read()

try:
    os.mkdir('lib')
    for i in range(70):
        # Create target Directory
        cfg_name = 'lib/'+random.choice(config_names)+'_'+random.choice(product_names)+'_'+random.choice(mode)
        os.mkdir(cfg_name)
        os.mkdir(cfg_name + "/docs")
        os.mkdir(cfg_name + "/custom")
        os.mkdir(cfg_name + "/examples")
        os.mkdir(cfg_name + "/simulations")
        os.mkdir(cfg_name + "/tcl")
        os.mkdir(cfg_name + "/spyglass")
        print("./"+cfg_name + "/spyglass/spyglass.html")
        if i % 5 != 0:
         html_file =open("./"+cfg_name + "/spyglass/spyglass.html",'w+')
         html_file.write(html)
         html_file.close()

        print("Directory " , cfg_name,  " Created ")
except FileExistsError:
    print("Directory " , cfg_name,  " already exists")

