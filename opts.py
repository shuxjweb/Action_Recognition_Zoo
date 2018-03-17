# @Author  : Sky chen
# @Email   : dzhchxk@126.com
# @Personal homepage  : https://coderskychen.cn

import argparse
parser = argparse.ArgumentParser(description="PyTorch implementation of TwoStream")
parser.add_argument('model', type=str, choices=['TwoStream', 'TSN', 'C3D'])
parser.add_argument('modality', type=str, choices=['RGB', 'Flow'])
parser.add_argument('train_id', type=str)
parser.add_argument('--num_segments', type=int, default=3)
parser.add_argument('--train_list', type=str,default="")
parser.add_argument('--val_list', type=str, default="")
parser.add_argument('--root_path', type=str, default="")
parser.add_argument('--store_name', type=str, default="")
# ========================= Model Configs ==========================
parser.add_argument('--arch', type=str, default="BNInception")
parser.add_argument('--dropout', '--do', default=0.8, type=float, metavar='DO', help='dropout ratio (default: 0.8)')
# ========================= Learning Configs ==========================
parser.add_argument('--epochs', default=120, type=int, metavar='N',
                    help='number of total epochs to run')
parser.add_argument('-b', '--batch_size', default=16, type=int,
                    metavar='N', help='mini-batch size (default: 256)')
parser.add_argument('--lr', '--learning-rate', default=0.005, type=float,
                    metavar='LR', help='initial learning rate')
parser.add_argument('--factor', '--factor', default=0.1, type=float,
                    help='decay factor')
parser.add_argument('--lr_steps', default=[30, 55], type=float, nargs="+",
                    metavar='LRSteps', help='epochs to decay learning rate by factor')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='momentum')
parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                    metavar='W', help='weight decay (default: 5e-4)')
parser.add_argument('--clip-gradient', '--gd', default=20, type=float,
                    metavar='W', help='gradient norm clipping (default: disabled)')
parser.add_argument('--no_partialbn', '--npb', default=False, action="store_true")
# ========================= Monitor Configs ==========================
parser.add_argument('--print-freq', '-p', default=5, type=int,
                    metavar='N', help='print frequency (default: 10)')
parser.add_argument('--eval-freq', '-ef', default=1, type=int,
                    metavar='N', help='evaluation frequency (default: 5)')
# ========================= Runtime Configs ==========================
parser.add_argument('-j', '--workers', default=30, type=int, metavar='N',
                    help='number of data loading workers (default: 4)')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')
parser.add_argument('--snapshot_pref', type=str, default="")
parser.add_argument('--start_epoch', default=0, type=int, metavar='N',
                    help='manual epoch number (useful on restarts)')
parser.add_argument('--gpus', nargs='+', type=int, default=None)
parser.add_argument('--root_log',type=str, default='log')
parser.add_argument('--root_model', type=str, default='model')
parser.add_argument('--root_output',type=str, default='output')



