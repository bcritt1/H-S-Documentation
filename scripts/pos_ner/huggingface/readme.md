# Usage

1. Upload all files from this directory to your Home on Sherlock. For more on files transfer, see [here](https://www.sherlock.stanford.edu/docs/storage/data-transfer/#ssh-based-protocols).
2. Input the lines from [packages.txt](/scripts/pos_ner/huggingface/packages.txt) into the terminal.
3. Change the value of corpusdir in [huggingface.py](/scripts/pos_ner/huggingface/huggingface.py) to the file path of your corpus.
4. Run [huggingface.sh](/scripts/pos_ner/huggingface/huggingface.sh) with ```sbatch huggingface.sh```.