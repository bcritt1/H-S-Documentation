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

That said, HPC resources are primarily designed around the idea of the batch, where you submit an entire script (not just a line in R or a cell in Jupyter) to a scheduler, [SLURM](https://slurm.schedmd.com/overview.html) in this case, via another script that you write to tell it what resources to devote to the job (how many cores, how much memory, etc.). Because the whole university can use these resources, the scheduler then puts your job in a queue, and it gets sent to the computer in as fair a manner as possible (small jobs can usually jump in front of big ones, users who haven't been hogging resources recently get priority, etc.). What this means in a practical sense is that, if you use this method, you aren't able to do much exploratory visualization, code tinkering, and the like. But if you have code that works and you just need finished outputs, especially from computationally intensive processes (tokenizing texts, geocoding locations, tagging entities, building word vectors), HPC can be great.

## How to do HPC research at Stanford (in the Humanities)

### Code

If you're an old pro, you probably have code that you can run directly in OnDemand's RStudio or Jupyter, or adapt to run through the SLURM queue. It's my (and the rest of SRC's) job to help you do these things, too, so if you run into any issues, you can reach out to [me](mailto:bcritt@stanford.edu), or submit a ticket [here](mailto:srcc-support@stanford.edu). If you're looking to optimize that code to run on the batch system, I'm happy to help, or you can check out the resource in the next paragraph.

For the non-experts (or those wisely looking for a shortcut), I have also been assembling a library of scripts both for scheduling jobs on Sherlock and for executing common digital humanities tasks [here](NEEED AN HTTPS). They don't work out of the box as they need to be adapted to point to your data, accounts, etc., but they're pretty clear about what you need to complete and where, and thus pretty easy Mad Libs (a rarity in technical documentation, I've found). This is a good option for those of you who can generally read code, but may not be comfortable writing it from scratch. 

For those who are new to coding in general, there are also lots of options that I hope to support and make more central to HPC research at Stanford. The library offers tons of great [courses](https://library.stanford.edu/workshops) on a broad range of subjects specific to computational humanities research. There are also Carpentry [workshops](https://library.stanford.edu/research/carpentries-stanford), but these seem to have gone into hibernation during COVID, and also can tend to focus more on science data and methods that can be hard for beginners to apply to humanities research.

### Actually Running Code: An Interactive Adventure

Before you leave today, you will have run code on a supercomputer. [NO OPEN ONDEMAND ON FARMSHARE RIGHT?]

For this exercise, we're going to be using [Farmshare](https://srcc.stanford.edu/more-about-farmshare), an educational cluster, rather than Sherlock. If you're just learning, you'll probably want to use Farmshare too. Conveniently, you don't even have to request an account: anyone with a Stanford ID can just log-on (we'll cover this in a second). Once you switch to running "real" jobs, though, you'll want to make the switch to Sherlock. An added benefit of switching to Sherlock is that you can take advantage of the OnDemand interface, which I mentioned before allows you to work in RStudio and/or Jupyter. Farmshare, however, will give us a taste of the real, stripped-down HPC experience.

### Computer Interfaces

Most of you only or primarily have experience with Graphical User Interfaces (GUIs), which have dominated the personal computing landscape since (arguably) Windows 95. GUIs largely overtook command-line interfaces (CLIs), at least in consumer markets, though some of you may remember CLIs like MS-DOS, which were still relatively commonplace in the 90s. High-powered computing environments still, however, largely use CLIs due to their simplicity, low resource demands, and their power in the hands of experienced users (like many HPC users). That's all to say that, in order to complete today's exercise, we'll need to learn to use a CLI just a bit.

### SSH and Connecting to Another Machine

You may be surprised to learn that the Mac in front of you is not the supercomputer we're going to be using today. So we need a way to communicate with that supercomputer (Farmshare) to tell it what code we want to run and how to run it. For this, we'll use a small but very useful computer program called Secure Shell Protocol (SSH) that you probably already have installed on your personal computer. The easiest way to use SSH is through the Terminal, another program likely already on your personal computer and, just as likely you've never used (for many of you, it may even still be in your Dock). If we click on the Terminal icon, you will see a command-line interface, which you can think of as just another way of interacting with your computer that doesn't involve visual interfaces like windows, and icons, and docks. 

Here, we pretty much exclusively use text. To demonstrate the Terminal's connection to your machine, though, type the following command:
```
pwd
```
This is another small Terminal program which stands for "Print Working Directory". When you run it, it will print the directory where you are currently located. In my case, it says something like
```
/Users/bcritt
```
and in yours it will say something similar. Because we ran pwd as soon as we opened the terminal, this is also our "Home" directory, which you can always get back to by using the program "cd" and giving it the option "~", as in:
```
cd ~
```
If you type "pwd" again, you'll see you're in the same place, but only because we were already in "Home". If we were elsewhere, we would have been moved here. When you log onto Farmshare, you will be opening a Terminal session on that machine, and where it opens will be your Home directory, and you can always get back there with the above cd command. 

But what if you want to go somewhere else? Well first we'd want to know where we want to go, and I think very few of us even know what the options are at this point. To start figuring that out, let's use another program called "ls", short for "list". If you type "ls" into the Terminal, you'll get a list of everything (more or less) in your current directory (Home). "ls", like many Terminal programs, has different options or flags you can add to it to modify its behavior. If I typed

```
ls -lha
```
I'd get a list of the directory's contents in (l) long form, (h) human-readable format, and (a) all files, even hidden ones, would be listed. For me, that looks like this:
![ls -lha](/images/lsLHA.png)
Say we wanted to move into our Documents folder, how would we do that?

That's right!
 ```
 cd Documents
 ```
 A really nice thing about the terminal is it will autocomplete entries when it can, so if we type "cd Doc" and then press "Tab", it will complete to "Documents"[^1]. Once we're there, we can "ls" again to see what documents are on our systems. Because these are public computers, you'll likely have none, which is a bit of a sad affair. Let's fix that:
 ```
 touch myFile.txt
 ```
 If we now go into our GUI "Finder", we'll see that even though we made the file in the CLI Terminal, it exists in the GUI. And vice-versa: anything you make in the GUI MacOS will show up and be manipulable in the Terminal. They're just different ways of interacting with the same underlying system!
 
 There are a ton more things you can do in the terminal: it can be very powerful and even do a lot of things higher-level languages that R and Python might struggle with, but now that we have some basics down, let's connect to that supercomputer. For that, we will type
 ```
 ssh SUNetid@rice.stanford.edu
 ```
 You'll be asked to approve some sort of authentication through the terminal (type "yes" and "Enter"), enter your Stanford password, and complete 2fa (type "1" and "Enter"), at which point you should see a semi-grpahical welcome screen to Farmshare:
 ![Farmshare](/images/farmshare.png)
 
 [^1]: This autocomplete feature needs at least 3 characters, and will give you options if there are competing answers to your input: "Documents" and "Docker", for instance. To use autocomplete, you'll need to type enough so that there are no alternatives.

