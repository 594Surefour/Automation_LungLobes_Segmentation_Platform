import nibabel as nib
import numpy as np
import imageio
import os

#读取nii文件
def read_niifile(niifile):  # 读取niifile文件
    img = nib.load(niifile)  # 下载niifile文件（其实是提取文件）
    img_fdata = img.get_fdata()  # 获取niifile数据
    img90 = np.rot90(img_fdata) #旋转90度
    #return img_fdata
    return img90

#保存jpg文件并输出
def save_fig(file):  # 保存为图片
    fdata = read_niifile(file)  # 调用上面的函数，获得数据
    (y, x, z) = fdata.shape  # 获得数据shape信息：（长，宽，维度-即切片数量）
    for k in range(z):
        silce = fdata[:, :, k]
        #silce = fdata[k, :, :]  # 三个位置表示三个不同角度的切片
        imageio.imwrite(os.path.join(output, '{}.jpg'.format(os.path.splitext(os.path.splitext(i)[0])[0]+'_'+str(k))), silce)
        # 将切片信息保存为jpg格式
        #i表示获取到的nii文件名（不含路径）
        #os.path.splitext(i)[0]表示去除文件名后缀
        #用两次splitext是因为图像原格式为.nii.gz，需要去两次后缀，如果是.nii形式的文件只用去除一次后缀即可
        #str(k)代表每层切片单独命名，避免重名，以_0,_1,...的形式命名

#读取文件
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

#设置文件路径
base ='./res' # nii文件的路径
output = './jpgs' # 保存png的路径
for i in findAllFile(base):
    dir = os.path.join(base,i)
    savepicdir = (os.path.join(output,i))
    #os.mkdir(savepicdir) #新建文件夹，重命名为nii文件名称,无需子文件夹，注释掉
    save_fig(dir)
