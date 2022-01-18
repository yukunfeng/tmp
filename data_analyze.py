import argparse
import random


def main(args):
  # Read tweet text.
  id2text = {}  # hash dict, data structure for storing key-value.
  with open(args.tweet_text_path, 'r') as fh: # file handle
    next(fh) # Skip the head line.
    for line in fh:
      line = line.strip() # remove spaces on both ends.
      if line == "":
        continue
      # "id", "text"
      tokens = line.split(',')
      tweet_id = tokens[0] # id contains "
      tweet_id = tweet_id.strip('"')
      tweet_text = " ".join(tokens[1:])
      id2text[tweet_id] = tweet_text
  # text = id2text["your_id"]

  # Read image.
  train_path = f"{args.tweet_image_path}/b-t4sa_train.txt"

  id2image = {}
  with open(train_path, 'r') as fh:
    for line in fh:
      line = line.strip()
      if line == "":
        continue
      image_path, label = line.split(' ')
      # data/75801/758014713804587008-1.jpg
      # 758014713804587008-1
      image_id = image_path.split('.')[0].split('/')[-1].split('-')[0]

      # ./CHIN/research/image/  image_path="data/23432/sf"
      image_path = f"{args.tweet_image_path}/{image_path}"
      if image_id not in id2image:
        id2image[image_id] = [label]
      if id2image[image_id][0] != label:
        raise Exeption("label not the same given same image id!")
      id2image[image_id].append(image_path)

  ids = list(id2image.keys())
  # in-place operation
  random.shuffle(ids)

  for i in range(args.n):
    image_id = ids[i]
    label = id2image[image_id][0]
    images = id2image[image_id][1:]
    text = id2text[image_id]
    print(f"id: {image_id}")
    print(f"label: {label}")
    print(text)
    print(images)
    print("")
    print("-------------------")


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )
  parser.add_argument('--tweet_text_path', required=True, type=str)
  parser.add_argument('--tweet_image_path', required=True, type=str)
  parser.add_argument('-n', required=True, type=int)
  args = parser.parse_args()
  main(args)
