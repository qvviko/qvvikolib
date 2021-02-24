import os

from PIL import Image
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm


class LazyParallelResize(Dataset):
    def __init__(self, path, new_path, size, show_progress=True):
        self.show_progress = show_progress
        self.path = path
        self.new_path = new_path
        self.dirs = os.listdir(path)
        self.size = size
        os.makedirs(new_path, exist_ok=True)

    def __getitem__(self, idx):
        item = self.dirs[idx]
        in_path = os.path.join(self.path, item)
        out_path = os.path.join(self.new_path, item)
        if os.path.isfile(in_path) and not os.path.exists(out_path):
            im = Image.open(in_path)
            imResize = im.resize(self.size, Image.CUBIC)
            imResize.save(out_path)
        return 0

    def __len__(self):
        return len(self.dirs)

    def process(self, num_workers):

        loader = DataLoader(
            self,
            batch_size=1,
            num_workers=num_workers
        )

        pbar = tqdm(loader) if self.show_progress else loader
        for item in pbar:
            pass
