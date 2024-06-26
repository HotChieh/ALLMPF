import os
import numpy as np
import torch

from config import cfg

#------------prepare enviroment------------
seed = cfg.SEED
if seed is not None:
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)

gpus = cfg.GPU_ID
if len(gpus)>=1:
    torch.cuda.set_device(cfg.MAIN_GPU[0])

torch.backends.cudnn.benchmark = True


#------------prepare data loader------------
data_mode = cfg.DATASET
if data_mode == 'SHHA':
    from datasets.SHHA.loading_data import loading_data 
    from datasets.SHHA.loading_data import drlloading_data
    from datasets.SHHA.setting import cfg_data 
elif data_mode == 'SHHB':
    from datasets.SHHB.loading_data import loading_data 
    from datasets.SHHB.loading_data import drlloading_data
    from datasets.SHHB.setting import cfg_data 
elif data_mode == 'QNRF':
    from datasets.QNRF.loading_data import loading_data 
    from datasets.QNRF.setting import cfg_data 
elif data_mode == 'UCF50':
    from datasets.UCF50.loading_data import loading_data 
    from datasets.UCF50.setting import cfg_data 
elif data_mode == 'WE':
    from datasets.WE.loading_data import loading_data 
    from datasets.WE.setting import cfg_data 
elif data_mode == 'GCC':
    from datasets.GCC.loading_data import loading_data
    from datasets.GCC.setting import cfg_data
elif data_mode == 'Mall':
    from datasets.Mall.loading_data import loading_data
    from datasets.Mall.setting import cfg_data
elif data_mode == 'UCSD':
    from datasets.UCSD.loading_data import loading_data
    from datasets.UCSD.setting import cfg_data
elif data_mode == 'SHTRGBD':
    from datasets.SHTRGBD.loading_data import loading_data
    from datasets.SHTRGBD.setting import cfg_data
elif data_mode == 'CARPK':
    from datasets.CARPK.loading_data import loading_data
    from datasets.CARPK.loading_data import drlloading_data
    from datasets.CARPK.setting import cfg_data
elif data_mode == 'PUCPR':
    from datasets.PUCPR.loading_data import loading_data
    from datasets.PUCPR.loading_data import drlloading_data
    from datasets.PUCPR.setting import cfg_data
elif data_mode == 'RSOC':
    from datasets.RSOC.loading_data import loading_data
    from datasets.RSOC.setting import cfg_data
elif data_mode == 'VISDRONE':
    from datasets.VISDRONE.loading_data import loading_data
    from datasets.VISDRONE.setting import cfg_data
elif data_mode == 'RSOCLARGEVEHICLE':
    from datasets.RSOCLARGEVEHICLE.loading_data import loading_data
    from datasets.RSOCLARGEVEHICLE.setting import cfg_data
elif data_mode == 'RSOCSMALLVEHICLE':
    from datasets.RSOCSMALLVEHICLE.loading_data import loading_data
    from datasets.RSOCSMALLVEHICLE.setting import cfg_data
elif data_mode == 'RSOCSHIP':
    from datasets.RSOCSHIP.loading_data import loading_data
    from datasets.RSOCSHIP.setting import cfg_data
elif data_mode == 'RSOCSHIPORG':
    from datasets.RSOCSHIPORG.loading_data import loading_data
    from datasets.RSOCSHIPORG.setting import cfg_data
#------------Prepare Trainer------------
net = cfg.NET
if net in ['MCNN', 'AlexNet', 'VGG', 'VGG_DECODER', 'Res50', 'Res101', 'CSRNet','Res101_SFCN', 'DDIPMN', 'OANet', 'ALLMPF']:
    from trainer import Trainer
elif net in ['SANet']: 
    from trainer_for_M2TCC import Trainer # double losses but signle output
elif net in ['CMTL']: 
    from trainer_for_CMTL import Trainer # double losses and double outputs
elif net in ['PCCNet']:
    from trainer_for_M3T3OCC import Trainer

#------------Start Training------------
gpu_env = ",".join(str(x) for x in gpus)
os.environ['CUDA_VISIBLE_DEVICES'] = gpu_env

pwd = os.path.split(os.path.realpath(__file__))[0]
cc_trainer = Trainer(drlloading_data, loading_data,cfg_data,pwd)
cc_trainer.forward()
