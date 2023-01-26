# Stanford Research Computing Center and the Humanities

## What is High-Performance Computing?

### About Stanford Research Computing Center

Stanford Research Computing Center ([SRCC](https://srcc.stanford.edu/) builds, manages, and supports Stanford's High-Performance Computing ([HPC](https://en.wikipedia.org/wiki/High-performance_computing) resources. For researchers in H&S, these resources primarily consist of [Sherlock](https://srcc.stanford.edu/sherlock-high-performance-computing-cluster), a computing cluster made up of nearly 50,000 CPU cores, provided both by Stanford centrally and researchers who contribute hardware to the cluster. These resources are free to use for Stanford researchers.

While we work a lot with the folks in the S of H&S, we've had limited engagement with you H's. It's my hope to change that.

### Why use High-Performance Computing?

The simple answer is, you may not need to. If you don't do computational research, obviously, you don't need to compute in a high-performance environment. If you do comptutational research, but your personal machine works for you what you do, you may not need HPC either, though there may be some other reasons to get on HPC beyond pure compute power. You definitely should think about moving to HPC if you're doing computational research and working at a scale that your personal computer struggles or fails to handle it. A typical Sherlock node has about 250x the CPUs and RAM of the average Macbook Pro, and even more can be accessed in special circumstances. In short, you can do things on HPC that you simply cannot do on a personal computer.

But there are other reasons to get on Sherlock, even if you're not a power user. If you do computational research with students or a team, Sherlock offers 1 TB of free, shared storage to teams: this can be really convenient if folks need to be working on the same files and it's proving a pain to pass them back and forth, coordinate usage, etc. [It's also a good learning environment?????] [OTHER REASONS?]

### Key Differences from Personal Computing

If you do computational research currently, you probably use a high-level language like R or Python, in an Integrated Development Environment (IDE) like RStudio or Jupyter Labs, and work with your data interactively, executing individual lines, seeing what comes back, adjusting your code, executing the line again, etc. One of the great things about Sherlock is that you can still work in this way, just with more firepower on the backend. Sherlock's OnDemand interface offers a browser-based, interactive environment where you can work in RStudio or Jupyter Notebooks, send your inputs to Sherlock's clusters and get outputs interactively to your screen in real time. This is a great way to learn about and use HPC without having to learn a new research workflow.

That said, HPC resources are primarily designed around the idea of the batch, where an entire script (not just a line in R or a cell in Jupyter) is submitted to a scheduler, [SLURM](https://slurm.schedmd.com/overview.html) in this case, via another script that you write to tell it what resources to devote to the job (how many cores, how much memory, etc.). Because the whole university can use these resources, the scheduler then puts your job in a queue, and it gets sent to the computer in as fair a manner as possible (small jobs can usually jump in front of big ones, users who haven't been hogging resources recently get priority, etc.). What this means in a practical sense is that, if you use this method, you aren't able to do much exploratory visualization, code tinkering, and the like. But if you have code that works and you just need finished outputs, especially from computationally intensive processes (tokenizing texts, geocoding locations, tagging entities, building word vectors), HPC can be great.

## How to do HPC research at Stanford

### Code

If you're an old pro, you probably have code that you can run directly in OnDemand's RStudio or Jupyter, or adapt to run through the SLURM queue. It's my (and the rest of SRC's) job to help you do these things, too, so if you run into any issues, you can reach out to [me](mailto:bcritt@stanford.edu), or submit a ticket [here](mailto:srcc-support@stanford.edu). For the non-experts (or those wisely looking for a shortcut, I have also been assembling a library of scripts both for scheduling jobs on Sherlock and for executing common digital humanities tasks [here](NEEED AN HTTPS). They don't work out of the box as they need to be adapted to point to your data, accounts, etc., but they're pretty clear about what you need to complete and where, and thus pretty easy Mad Libs (a rarity in technical documentation, I've found).
