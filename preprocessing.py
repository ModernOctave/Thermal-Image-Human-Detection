import numpy as np
from pycocotools.coco import COCO
from tqdm import tqdm
from tensorflow.keras.utils import Sequence, load_img, img_to_array


def label_dataset(dataset_path):
	# Load the annotations
	coco_annotation_file_path = dataset_path+"coco.json"
	coco_annotation = COCO(annotation_file=coco_annotation_file_path)

	# Get all images
	img_ids = coco_annotation.getImgIds()

	# Get category info
	cat_ids = coco_annotation.getCatIds()
	cat = dict(zip(cat_ids,[cat['name'] for cat in coco_annotation.loadCats(cat_ids)]))

	# Label the images
	print("labeling the dataset...")

	labeled_dataset = []

	for i, img_id in enumerate(tqdm(img_ids)):
		# Get file paths
		img_info = coco_annotation.loadImgs([img_id])[0]
		img_file_name = img_info["file_name"]
		img_path = dataset_path+img_file_name

		# Get all the annotations for the specified image.
		ann_ids = coco_annotation.getAnnIds(imgIds=[img_id], iscrowd=None)
		anns = coco_annotation.loadAnns(ann_ids)

		if 'person' in [cat[ann['category_id']] for ann in anns]:
			labeled_dataset.append((img_path, 1))
		else:
			labeled_dataset.append((img_path, 0))

	return labeled_dataset

def split_dataset(dataset, split, shuffle=True, seed=None):
    if shuffle:
        if seed is not None:
            np.random.seed(seed)
        np.random.shuffle(dataset)

    left_size = int(len(dataset) * split)

    left_dataset = dataset[:left_size]
    right_dataset = dataset[left_size:]

    return left_dataset, right_dataset

class DataGen(Sequence):
    def __init__(self, dataset, batch_size):
        self.dataset = dataset
        self.batch_size = batch_size

    def __len__(self):
        return int(np.ceil(len(self.dataset) / float(self.batch_size)))

    def __getitem__(self, idx):
        batch = self.dataset[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_x, batch_y = zip(*batch)
        batch_x = np.array([img_to_array(load_img(path)) for path in batch_x])
        batch_y = np.array(batch_y)
        return batch_x, batch_y