前端功能

```shell
#安装
pip install git+https://github.com/JoHof/lungmask
#运行6肺叶 INPUT OUTPUT为路径
lungmask INPUT OUTPUT --modelname LTRCLobes --modelpath ./unet_ltrclobes-3a07043d.pth

#6肺叶
lungmask ./ test.mha --modelname LTRCLobes_R231 --modelpath /Users/lee/.cache/torch/checkpoints/unet_ltrclobes-3a07043d.pth                                             

#双肺叶
lungmask ./ test.mha --modelname LTRCLobes --modelpath /Users/lee/.cache/torch/checkpoints/unet_r231-d5d2fc3d.pth

#lungmask -h
usage: lungmask [-h] [--modeltype {unet}]
                [--modelname {R231,LTRCLobes,LTRCLobes_R231,R231CovidWeb}]
                [--modelpath MODELPATH] [--classes CLASSES] [--cpu]
                [--nopostprocess] [--noHU] [--batchsize BATCHSIZE] [--version]
                input output
```

