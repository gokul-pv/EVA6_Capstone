# EVA6_Capstone
## Objective

The aim of this project is to train [DETR](https://github.com/facebookresearch/detr) on a custom dataset consisting of objects from construction domain (around 48 classes) for Object Detection and Panoptic Segmentation.

Let us now understand how DETR works and try to answer few questions.

- [Understanding DETR](./Part1/DetrExplanation.md)
- [Few questions to consider for Panoptic segmenation training](./Part1/README.md)



## Data preparation

[Click here](./Dataset/README.md)

## Training

First the object detection model was trained for 200 epochs using pre-trained weights. Then a panoptic head was added on top of this and trained for another 50 epochs. This time the object detection model was freezed and only panoptic head was trained.  

We train DETR with AdamW setting learning rate in the transformer to 1e-4 and 1e-5 in the backbone. Horizontal flips, scales and crops are used for augmentation. Images are rescaled to have min size 800 and max size 1333. The transformer is trained with dropout of 0.1, and the whole model is trained with grad clip of 0.1.



## Results

Bounding box detection evaluation results for the construction dataset after training for 200 epochs

```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.753
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.864
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.801
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.387
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.609
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.782
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.716
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.857
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.871
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.505
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.728
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.899
```

Segmentation Metric: (Panoptic, Segmentation, Recognition Quality) after training panoptic head for 50 epochs

```
          |    PQ     SQ     RQ     N
--------------------------------------
All       |  53.1   80.0   60.7    61
Things    |  61.6   82.9   69.6    46
Stuff     |  27.0   71.2   33.5    15
```




## References
1. [DETR Paper](https://arxiv.org/abs/2005.12872)
2. [https://www.youtube.com/watch?v=utxbUlo9CyY](https://www.youtube.com/watch?v=utxbUlo9CyY)
3. [https://wandb.ai/veri/detr/reports/DETR-Panoptic-segmentation-on-Cityscapes-dataset--Vmlldzo2ODg3NjE](https://wandb.ai/veri/detr/reports/DETR-Panoptic-segmentation-on-Cityscapes-dataset--Vmlldzo2ODg3NjE)
4. [https://opensourcelibs.com/lib/finetune-detr](https://opensourcelibs.com/lib/finetune-detr)
5. [https://www.youtube.com/watch?v=RkhXoj_Vvr4](https://www.youtube.com/watch?v=RkhXoj_Vvr4)
6. Explanation on Paper by [Yanic](https://www.youtube.com/watch?v=T35ba_VXkMY) , [AI Epiphany](https://www.youtube.com/watch?v=BNx-wno-0-g)

