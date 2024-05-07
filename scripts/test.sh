dataDir=

python test.py \
    --name default \
    --dataroot ./PhotoSketch/dataset/ \
    --phase val \
    --how_many 100 \
    --checkpoints_dir./PhotoSketch/Checkpoints/ \
    --results_dir ./PhotoSketch/TestResults/ \
    --model pix2pix \
    --which_direction AtoB \
    --dataset_mode 1_to_n \
    --norm batch \
    --input_nc 3 \
    --output_nc 1 \
    --which_model_netG resnet_9blocks \
    --which_model_netD global_np \
    --aug_folder width-5 \
    --no_dropout \
