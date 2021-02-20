#!/bin/bash

sbatch --gres=gpu:4 --partition=Teach-LongJobs --overcommit --mail-type=END,FAIL --mail-user=jdyer.garrison@gmail.com example.sh

