import sys


run = (len(sys.argv)) -1

while(run>=1):
    try:
        with open(sys.argv[run]) as f:   
            data = f.read()
            data = data.replace('%','')
            f.close()
            run = (run - 1)
    except IndexError:
        print('no file dropped...')
        input('press enter')


     
    with open('Bundled.nc','a') as f:
        f.close()
        
    with open('Bundled.nc') as f:
        bData = f.read()
        bData = bData.replace('%','') 
        f.close()      

    with open('Bundled.nc','w') as f:
        startEnd = "%"   
        f.write(startEnd + bData + data + startEnd) 
        f.close()
        