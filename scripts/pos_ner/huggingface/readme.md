# Usage

1. Clone this repo to your Home directory on Sherlock with ```git clone git://https://github.com/bcritt1/H-S-Documentation/edit/main/scripts/pos_ner/huggingface/```
2. Upload your corpus to a directory within your Home directory. For more on files transfer, see [here](https://www.sherlock.stanford.edu/docs/storage/data-transfer/#ssh-based-protocols).
3. Input the lines from [packages.txt](/scripts/pos_ner/huggingface/packages.txt) into the terminal.
4. Change the value of corpusdir in [huggingface.py](/scripts/pos_ner/huggingface/huggingface.py) to the file path of your corpus.
5. Run [huggingface.sh](/scripts/pos_ner/huggingface/huggingface.sh) with ```sbatch huggingface.sh```.
