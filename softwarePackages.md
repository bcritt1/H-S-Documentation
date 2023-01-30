# Software Packages

## Python
### Introduction

[Python][url_python] is an interpreted high-level programming language for
general-purpose programming. Its design philosophy emphasizes code readability,
notably using significant whitespace. It provides constructs that enable clear
programming on both small and large scales, which makes it both easy to learn
and very well-suited for rapid prototyping.

### More documentation

The following documentation is specifically intended for using Python on
Sherlock. For more complete documentation about Python in general, please see
the [Python documentation](https://www.python.org/doc/).


## Python on Sherlock [[NEED TO UPDATE THIS FOR CURRENT VERSIONS]]

Sherlock features multiple versions of Python (currently `2.7` and `3.6`).

Some applications only work with legacy features of version 2.x, while more
recent code will require specific version 3.x features.  [Modules on
Sherlock][url_modules] may only be available in a single flavor (as denoted by
their suffix: `_py27` or `_py36`, because the application only supports one or
the other.

You can load either version on Sherlock by doing the following commands:

```shell
$ ml python/2.7.13
```

or

```shell
$ ml python/3.6.1
```

!!! warning "The Python3 interpreter is `python3`"

    The Python3 executable is named `python3`, not `python`. So, once you have
    the "python/3.6.1" module loaded on Sherlock, you will need to use
    `python3` to invoke the proper interpreter. `python` will still refer to
    the default, older system-level Python installation, and may result in
    errors when trying to run Python3 code.

    This is an upstream decision detailled in [PEP-394][url_pep394], not
    something specific to Sherlock.


### Using Python

Once your environment is configured (ie. when the Python module is loaded),
Python can be started by simply typing `python` at the shell prompt:

``` shell
$ python
Python 2.7.13 (default, Apr 27 2017, 14:19:21)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


### Python in batch jobs

!!! info "Python output is buffered by default"

    By default, Python buffers console output. It means that when running
    Python in a batch job through Slurm, you may see output less often than you
    would when running interactively.

When output is being buffered, the `print` statements are aggregated until
there is a enough data to print, and then the messages are all printed at once.
And as a consequence, job output files (as specified with the `--output` and
`--error` job submission options) will be refeshed less often and may give the
impression that the job is not running.

For debugging or checking that a Python script is producing the correct output,
you may want to switch off buffering.

#### Switching  off buffering

For a single python script you can use the `-u` option, as in `python -u
my_script.py`. The `-u` option stands for "unbuffered".

For instance:

```shell
#!/bin/bash
#SBATCH -n 1

python -u my_script.py
```

!!! tip

    You can also use the environment variable `PYTHONUNBUFFERED` to set
    unbuffered I/O for your whole batch script.
    ```shell
    #!/bin/bash
    #SBATCH -n 1

    export PYTHONUNBUFFERED=True
    python my_script.py
    ```

NB: There is some performance penalty for having unbuffered print statements, so
you may want to reduce the number of print statements, or run buffered for
production runs.

### Python packages

The capabilities of Python can be extended with packages developed by third
parties. In general, to simplify operations, it is left up to individual users
and groups to install these third-party packages in their own directories.
However, Sherlock provides tools to help you install the third-party packages
that you need.

Among [many others][url_modules], the following common Python packages are
provided on Sherlock:

* [NumPy][url_numpy]
* [SciPy][url_scipy]
* [TensorFlow][url_tensorflow]

Python modules on Sherlock generally follow the naming scheme below:

``` shell
py-<package_name>/version_py<python_version>
```

For instance, NumPy modules are:

* [`py-numpy/1.14.3_py27`][url_module_numpy]
* [`py-numpy/1.14.3_py36`][url_module_numpy]


You can list all available module versions for a package with `ml spider
<package_name>`. For instance:

``` shell
$ ml spider tensorflow
-------------------------------------------------------------------------------
  py-tensorflow:
-------------------------------------------------------------------------------
    Description:
      TensorFlow™ is an open source software library for numerical computation using data flow graphs.

     Versions:
        py-tensorflow/1.6.0_py27
        py-tensorflow/1.6.0_py36
        py-tensorflow/1.7.0_py27
        py-tensorflow/1.9.0_py27
        py-tensorflow/1.9.0_py36
```


!!! tip "Dependencies are handled automatically"

    When you decide to use NumPy on Sherlock, you just need to load the
    `py-numpy` module of your choice, and the correct Python interpreter will
    be loaded automatically. No need to load a `python` module explicitly.


#### Installing packages

If you need to use a Python package that is not already provided as a module on
Sherlock, you can use the [`pip`][url_pip] command. This command takes care of
compiling and installing most of Python packages and their dependencies. All of
`pip`'s commands and options are explained in detail in the [Pip user
guide][url_pip_docs].

A comprehensive index of Python packages can be found at [PyPI][url_pypi].


To install Python packages with `pip`, you'll need to use the `--user` option.
This will make sure that those packages are installed in a user-writable
location (by default, your `$HOME` directory). Since your `$HOME` directory is
shared across nodes on Sherlock, you'll only need to install your Python
packages once, and they'll be ready to be used on every single node in the
cluster.

For example:

``` shell
$ pip install --user <package_name>
```

For Python 3, use `pip3`:

``` shell
$ pip3 install --user <package_name>
```

Python packages will be installed in <code> $HOME/.local/lib/python<<font
color=red>&lt;version&gt;</font>/site-packages</code>, meaning that packages
for Python 2.x and Python 3.x will be kept separate. This both means that they
won't interfere with each other, but also that if you need to use a package
with both Python 2.x and 3.x, you'll need to install it twice, once for each
Python version.

##### List installed packages

You can easily see the list of the Python packages installed in your
environment, and their location, with `pip list`:

``` shell
$ pip list -v
Package    Version Location                                                            Installer
---------- ------- ------------------------------------------------------------------- ---------
pip        18.1    /share/software/user/open/python/2.7.13/lib/python2.7/site-packages pip
setuptools 28.8.0  /share/software/user/open/python/2.7.13/lib/python2.7/site-packages pip
urllib3    1.24    /home/users/kilian/.local/lib/python2.7/site-packages               pip
virtualenv 15.1.0  /share/software/user/open/python/2.7.13/lib/python2.7/site-packages pip
```


##### Alternative installation path

!!! warning "Python paths"

    While theoretically possible, installing Python packages in alternate
    locations can be tricky, so we recommend trying to stick to the `pip
    install --user` way as often as possible. But in case you absolutely need
    it, we provide some guidelines below.


One common case of needing to install Python packages in alternate locations is
to share those packages with a group of users. Here's an example that will show
how to install the `urllib3` Python package in a group-shared location and let
users from the group use it without having to install it themselves.

First, you need to create a directory to store those packages. We'll put it in
`$GROUP_HOME`:

``` shell
$ mkdir -p $GROUP_HOME/python/
```

Then, we load the Python module we need, and we instruct `pip` to install its
packages in the directory we just created:

``` shell
$ ml python/2.7.13
$ PYTHONUSERBASE=$GROUP_HOME/python pip install --user urllib3
```

We still use the `--user` option, but with `PYTHONUSERBASE` pointing to a
different directory, `pip` will install packages there.

Now, to be able to use that Python module, since it's not been installed in a
default directory, you (and all the members of the group who will want to use
that module) need to set their `PYTHONPATH` to include our new shared
directory[^pythonpath]:

``` shell
$ export PYTHONPATH=$GROUP_HOME/python/lib/python2.7/site-packages:$PYTHONPATH
```

And now, the module should be visible:

``` shell
$ pip list -v
Package    Version Location                                                            Installer
---------- ------- ------------------------------------------------------------------- ---------
pip        18.1    /share/software/user/open/python/2.7.13/lib/python2.7/site-packages pip
setuptools 28.8.0  /share/software/user/open/python/2.7.13/lib/python2.7/site-packages pip
urllib3    1.24    /home/groups/ruthm/python/lib/python2.7/site-packages               pip
virtualenv 15.1.0  /share/software/user/open/python/2.7.13/lib/python2.7/site-packages pip
```

!!! tip "`$PYTHONPATH` depends on the Python version"

    The `$PYTHONPATH` environment variable is dependent on the Python version
    you're using, so for Python 3.6, it should include
    `$GROUP_HOME/python/lib/python3.6/site-packages`

!!! info "`$PATH` may also need to be updated"

    Some Python package sometimes also install executable scripts. To
    make them easily accessible in your environment, you may also want to
    modify your `$PATH` to include their installation directory.

    For instance, if you installed Python packages in `$GROUP_HOME/python`:
    ```
    $ export PATH=$GROUP_HOME/python/bin:$PATH
    ```


##### Installing from GitHub

`pip` also supports installing packages from a variety of sources, including
GitHub repositories.

For instance, to install [HTTPie][url_httpie], you can do:

``` shell
$ pip install --user git+git://github.com/jkbr/httpie.git
```


##### Installing from a requirements file

`pip` allows installing a list of packages listed in a file, which can be
pretty convenient to install several dependencies at once.

In order to do this, create a text file called `requirements.txt` and place
each package you would like to install on its own line:

=== "requirements.txt"

    ``` shell
    numpy
    scikit-learn
    keras
    tensorflow
    ```

You can now install your modules like so:

``` shell
$ ml python
$ pip install --user -r requirements.txt
```

#### Upgrading packages

`pip` can update already installed packages with the following command:

``` shell
$ pip install --user --upgrade <package_name>
```

Upgrading packages also works with `requirements.txt` files:

``` shell
$ pip install --user --upgrade -r requirements.txt
```


#### Uninstalling packages

To uninstall a Python package, you can use the `pip uninstall` command (note
that it doesn't take any `--user` option):

``` shell
$ pip uninstall <package_name>
$ pip uninstall -r requirements.txt
```



[comment]: #  (link URLs -----------------------------------------------------)

[url_python]:         //www.python.org/
[url_python_docs]:    //www.python.org/doc
[url_pip]:            //pip.pypa.io/en/stable/
[url_pip_docs]:       //pip.pypa.io/en/stable/user_guide/
[url_pypi]:           //pypi.python.org/pypi
[url_pep394]:         //www.python.org/dev/peps/pep-0394

[url_numpy]:          /www.numpy.org/
[url_scipy]:          //www.scipy.org/
[url_tensorflow]:     //www.tensorflow.org
[url_httpie]:         //httpie.org/

[url_modules]:        /docs/software/list
[url_module_numpy]:   /docs/software/list/#py-numpy
[url_module_scipy]:   /docs/software/list/#py-scipy
[url_module_tensorflow]:  /docs/software/list/#py-tensorflow

[comment]: #  (footnotes -----------------------------------------------------)

[^pythonpath]: This line can also be added to a user's `~/.profile` file, for a
  more permanent setting.


--8<--- "includes/_acronyms.md"


## R

## Introduction

[R][url_r] is a programming language and software environment for statistical
computing and graphics.  It is similar to the [S][url_s] language and
environment developed at Bell Laboratories (formerly AT&T, now Lucent
Technologies). R provides a wide variety of statistical and graphical
techniques and is highly extensible.


### More documentation

The following documentation is specifically intended for using R on Sherlock.
For more complete documentation about R in general, please see the [R
documentation][url_r_docs].


## R on Sherlock

R is available on Sherlock and the corresponding [module][url_modules] can be
loaded with:

``` shell
$ ml R
```

For a list of available versions, you can execute `ml spider R` at the Sherlock
prompt, or refer to the [Software list page][url_software_list].


### Using R

Once your environment is configured (_ie._ when the `R` module is loaded), R
can be started by simply typing R at the shell prompt:

``` shell
$ R

R version 3.5.1 (2018-07-02) -- "Feather Spray"
Copyright (C) 2018 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)
[...]
Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

>
```

For a listing of command line options:

``` shell
$ R --help
```

#### Running a R script

There are several ways to launch an R script on the command line, which will
have different ways of presenting the script's output:

| Method | Output |
| ------ | ------ |
| `Rscript script.R`| displayed on screen, on `stdout`|
| `R CMD BATCH script.R` | redirected to a `script.Rout` file |
| `R --no-save < script.R` | displayed on screen, on `stdout` |



#### Submitting a R job

Here's an example R batch script that can be submitted via `sbatch`. It runs a
simple matrix multiplication example, and demonstrate how to feed R code as a
[HEREDOC][url_heredoc] to R directly, so no intermediate R script is necessary:

=== "R-test.sbatch"

    ``` bash
    #!/usr/bin/bash
    #SBATCH --time=00:10:00
    #SBATCH --mem=10G
    #SBATCH --output=R-test.log

    # load the module
    ml R

    # run R code
    R --no-save << EOF
    set.seed (1)
    m <- 4000
    n <- 4000
    A <- matrix (runif (m*n),m,n)
    system.time (B <- crossprod(A))
    EOF
    ```

You can save this script as `R-test.sbatch` and submit it to the scheduler with:

``` shell
$ sbatch R-test.sbatch
```

Once the job is done, you should get a `R-test.out` file in the current
directory, with the following contents:

``` shell
R version 3.5.1 (2018-07-02) -- "Feather Spray"
[...]
> set.seed (1)
> m <- 4000
> n <- 4000
> A <- matrix (runif (m*n),m,n)
> system.time (B <- crossprod(A))
   user  system elapsed
  2.649   0.077   2.726
```



### R packages

R comes with a single package library in `$R_HOME/library`, which contains the
standard and most common packages. This is usually in a system location and is
not writable by end-users.

To accommodate individual user's requirements, R provides a way for each user
to install packages in the location of their choice. The default value for a
directory where users can install their own R packages is
`$HOME/R/x86_64-pc-linux-gnu-library/<R_version>` where `<R_version>` depends
on the R version that is used.  For instance, if you have the `R/3.5.1` module
loaded, the default R user library path will be
`$HOME/R/x86_64-pc-linux-gnu-library/3.5`.

This directory doesn't exist by default. The first time a user installs an R
package, R will ask if she wants to use the default location and create the
directory.


#### Installing packages

To install a R package in your personal environment, the first thing to do is
load the R module:

``` shell
$ ml R
```

Then start a R session, and use the `install.packages()` function at the R
prompt. For instance, the following example will install the `doParallel`
package, using the US mirror of the [CRAN repository][url_cran]:

``` shell
$ R

R version 3.5.1 (2018-07-02) -- "Feather Spray"
[...]

> install.packages('doParallel', repos='http://cran.us.r-project.org')
```

It should give the following warning:

``` shell
Warning in install.packages("doParallel", repos = "http://cran.us.r-project.org") :
  'lib = "/share/software/user/open/R/3.5.1/lib64/R/library"' is not writable
Would you like to use a personal library instead? (yes/No/cancel)
Would you like to create a personal library
‘~/R/x86_64-pc-linux-gnu-library/3.5’
to install packages into? (yes/No/cancel) y
```

Answering `y` twice will make R create a `~/R/x86_64-pc-linux-gnu-library/3.5`
directory and instruct it to install future R packages there.

The installation will then proceed:

``` shell
trying URL 'http://cran.us.r-project.org/src/contrib/doParallel_1.0.14.tar.gz'
Content type 'application/x-gzip' length 173607 bytes (169 KB)
==================================================
downloaded 169 KB

* installing *source* package ‘doParallel’ ...
** package ‘doParallel’ successfully unpacked and MD5 sums checked
** R
** demo
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
** building package indices
** installing vignettes
** testing if installed package can be loaded
* DONE (doParallel)

The downloaded source packages are in
        ‘/tmp/Rtmp0RHrMZ/downloaded_packages’
>
```

and when it's done, you should be able to load the package within R with:

``` R
> library(doParallel)
Loading required package: foreach
Loading required package: iterators
Loading required package: parallel
>
```

##### Package dependencies

Sometimes when installing R packages, other software is needed for the
installation and/or compilation.  For instance, when trying to install the `sf`
package, you may encounter the following error messages:

``` R
> install.packages("sf")
[...]
Configuration failed because libudunits2.so was not found. Try installing:...
[...]
configure: error: gdal-config not found or not executable.
```

This is because `sf` needs a few dependencies, like `udunits` and `gdal` in
order to compile and install successfully.  Fortunately those dependencies are
already available as modules on Sherlock.

Whenever you see "not found" errors, you may want to try searching the modules
inventory with `module spider`:

``` shell
$ module spider udunits

----------------------------------------------------------------------------
  udunits: udunits/2.2.26
----------------------------------------------------------------------------
    Description:
      The UDUNITS package from Unidata is a C-based package for the
      programatic handling of units of physical quantities.


    You will need to load all module(s) on any one of the lines below before
    the "udunits/2.2.26" module is available to load.

      physics
```

So for `sf`, in order to load the dependencies, exit `R`, load the `udunits`
and `gdal` modules, and try installing `sf` again:

``` shell
$ ml load physics udunits gdal
$ ml R
$ R
> install.packages("sf")
```

Sometimes, getting dependencies right is a matter of trial and error.  You may
have to load R, install packages, search modules, load modules, install
packages again and so forth.  Fortunately, R packages only need to be installed
once, and many R package dependencies are already available as modules on
Sherlock, you just need to search for them with `module spider` and load them.

And in case you're stuck, you can of course always [send us an
email][url_support] and we'll be happy to assist.

#### Installing large packages

Sometimes installation of large packages can be very time consuming.  To speed things up R
can utilize multiple CPUs at once.  Add "Ncpus=n"  where n is the number of CPUs you
can utilize.  You can use the `sdev` command to get a session with 4 CPUs:

``` shell
$ sdev -c 4
$ ml R
$ R
>install.packages("dplyr", repos = "http://cran.us.r-project.org", Ncpus=4)
```


##### Alternative installation path

To install R packages in a different location, you'll need to create that
directory, and instruct R to install the packages there:

``` shell
$ mkdir ~/R_libs/
$ R
[...]
> install.packages('doParallel', repos='http://cran.us.r-project.org', lib="~/R_libs")
```

The installation will proceed normally and the `doParallel` package will be
installed in `$HOME/R_libs/`.


Specifying the full destination path for each package installation could
quickly become tiresome, so to avoid this, you can create a `.Renviron`
file in your `$HOME` directory, and define your `R_libs` path there:

``` shell
$ cat << EOF > $HOME/.Renviron
R_LIBS=~/R_libs
EOF
```

With this, whenever R is started, the `$HOME/R_libs/` directory will be
added to the list of places R will look for packages, and you won't need to
specify this installation path when using `install.packages()` anymore.


!!! info "Where does R look for packages?"

    To see the directories where R searches for packages and libraries, you can
    use the following command in R:

    ``` R
    > .libPaths()
    ```

!!! tip "Sharing R packages"

    If you'd like to share R packages within your group, you can simply define
    `$R_LIBS` to point to a shared directory, such as `$GROUP_HOME/R_libs` and
    have each user in the group use the instructions below to define it in
    their own environment.


##### Setting the repository

When installing a package, R needs to know from which repository the package
should be downloaded. If it's not specified, it will prompt for it and display
a list of available CRAN mirrors.

To avoid setting the CRAN mirror each time you run install.packages you can
permanently set the mirror by creating a `.Rprofile` file in your `$HOME`
directory, which R will execute each time it starts.

For instance, adding the following contents to your `~/.Rprofile` will make
sure that every `install.packages()` invocation will use the closest CRAN
mirror:

``` R
## local creates a new, empty environment
## This avoids polluting the global environment with
## the object r
local({
  r = getOption("repos")
  r["CRAN"] = "https://cloud.r-project.org/"
  options(repos = r)
})
```

Once this is set, you only need to specify the name of the package to install,
and R will use the mirror you defined automatically:

``` R
> install.packages("doParallel")
[...]
trying URL 'https://cloud.r-project.org/src/contrib/doParallel_1.0.14.tar.gz'
Content type 'application/x-gzip' length 173607 bytes (169 KB)
==================================================
downloaded 169 KB
```

##### Installing packages from GitHub

R packages can be directly installed from GitHub using the `devtools` package.
`devtools` needs to be installed first, with:

``` R
> install.packages("devtools")
```

And then, you can then install a R package directly from its GitHub repository.
For instance, to install `dplyr` from [url_dplyr]:

``` R
> library(devtools)
> install_github("tidyverse/dplyr")
```


#### Updating Packages

To upgrade R packages, you can use the `update.packages()` function within a R
session.

For instance, to update the `doParallel` package:

``` R
> update.packages('doParallel')
```

When the package name is omitted, `update.pacakges()` will try to update all
the packages that are installed. Which is the most efficient way to ensure that
all the packages in your local R library are up to date.

!!! Warning "Centrally installed packages can not be updated"

    Note that attempting to update centrally installed packages will fail. You
    will have to use `install.packages()` to install your own version of the
    packages in your `$HOME` directory instead.


#### Removing packages

To remove a package from your local R library, you can use the
`remove.packages()` function. For instance:

``` R
> remove.packages('doParallel')
```

### Examples

#### Single node

R has a couple of powerful and easy to use tools for parallelizing your R jobs.
[`doParallel`][url_doparallel] is one of them. If the `doParallel` package is
not installed in your environment yet, you can [install it in a few easy
step](#installing).

Here is a quick `doParallel` example that uses one node and 16 cores on
Sherlock (more nodes or CPU cores can be requested, as needed).


Save the two scripts below in a directory on Sherlock:

=== "doParallel_test.R"

    ``` R
    # Example doParallel script

    if(!require(doParallel)) install.packages("doParallel")
    library(doParallel)

    # use the environment variable SLURM_NTASKS_PER_NODE to set
    # the number of cores to use
    registerDoParallel(cores=(Sys.getenv("SLURM_NTASKS_PER_NODE")))

    # bootstrap iteration example
    x <- iris[which(iris[,5] != "setosa"), c(1,5)]
    iterations <- 10000# Number of iterations to run

    # parallel loop
    # note the '%dopar%' instruction
    parallel_time <- system.time({
      r <- foreach(icount(iterations), .combine=cbind) %dopar% {
        ind <- sample(100, 100, replace=TRUE)
        result1 <- glm(x[ind,2]~x[ind,1], family=binomial(logit))
        coefficients(result1)
      }
    })[3]

    # show the number of parallel workers to be used
    getDoParWorkers()

    # execute the function
    parallel_time
    ```

=== "doParallel_test.sbatch"

    ``` shell
    #!/bin/bash

    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=16
    #SBATCH --output=doParallel_test.log

    # --ntasks-per-node will be used in doParallel_test.R to specify the number
    # of cores to use on the machine.

    # load modules
    ml R/3.5.1

    # execute script
    Rscript doParallel_test.R
    ```

And then submit the job with:

``` shell
$ sbatch doParallel_test.sbatch
```

Once the job has completed, the output file should contain something like this:

``` shell
$ cat doParallel_test.out
[1] "16"
elapsed
  3.551
```

**Bonus points**: observe the scalability of the `doParallel` loop by
submitting the same script using a varying number of CPU cores:

``` shell
$ for i in 2 4 8 16; do
    sbatch --out=doP_${i}.out --ntasks-per-node=$i doParallel_test.sbatch
done
```

When the jobs are done:

``` shell
$ for i in 2 4 8 16; do
    printf "%2i cores: %4.1fs\n" $i $(tail -n1 doP_$i.out)
done
 2 cores: 13.6s
 4 cores:  7.8s
 8 cores:  4.9s
16 cores:  3.6s
```


#### Multiple nodes

To distribute parallel R tasks on multiple nodes, you can use the
[`Rmpi`][url_rmpi] package, which provides MPI bindings for R.

To install the `Rmpi` package, a module providing MPI library must first be
loaded. For instance:

``` shell
$ ml openmpi R
$ R
> install.packages("Rmpi")
```

Once the package is installed, the following scripts demonstrate a very basic
`Rmpi` example.


=== "Rmpi-test.R"

    ``` R
    # Example Rmpi script

    if (!require("Rmpi")) install.packages("Rmpi")
    library(Rmpi)

    # initialize an Rmpi environment
    ns <- mpi.universe.size() - 1
    mpi.spawn.Rslaves(nslaves=ns, needlog=TRUE)

    # send these commands to the slaves
    mpi.bcast.cmd( id <- mpi.comm.rank() )
    mpi.bcast.cmd( ns <- mpi.comm.size() )
    mpi.bcast.cmd( host <- mpi.get.processor.name() )

    # all slaves execute this command
    mpi.remote.exec(paste("I am", id, "of", ns, "running on", host))

    # close down the Rmpi environment
    mpi.close.Rslaves(dellog = FALSE)
    mpi.exit()
    ```

=== "Rmpi-test.sbatch"

    ``` shell
    #!/bin/bash

    #SBATCH --nodes=2
    #SBATCH --ntasks=4
    #SBATCH --output=Rmpi-test.log

    ## load modules
    # openmpi is not loaded by default with R, so it must be loaded explicitely
    ml R openmpi

    ## run script
    # we use '-np 1' since Rmpi does its own task management
    mpirun -np 1 Rscript Rmpi-test.R
    ```

You can save those scripts as `Rmpi-test.R` and
`Rmpi-test.sbatch` and then submit your job with:

``` shell
$ sbatch Rmpi-test.sbatch
```

When the job is done, its output should look like this:

``` shell
$ cat Rmpi-test.log
        3 slaves are spawned successfully. 0 failed.
master (rank 0, comm 1) of size 4 is running on: sh-06-33
slave1 (rank 1, comm 1) of size 4 is running on: sh-06-33
slave2 (rank 2, comm 1) of size 4 is running on: sh-06-33
slave3 (rank 3, comm 1) of size 4 is running on: sh-06-34
$slave1
[1] "I am 1 of 4 running on sh-06-33"

$slave2
[1] "I am 2 of 4 running on sh-06-33"

$slave3
[1] "I am 3 of 4 running on sh-06-34"

[1] 1
[1] "Detaching Rmpi. Rmpi cannot be used unless relaunching R."
```

#### GPUs

Here's a quick example that compares running a matrix multiplication on a CPU
and on a GPU using R. It requires [submitting a job to a GPU node][url_gpu] and
the [`gpuR`][url_gpuR] R package.

=== "gpuR-test.R"

    ``` R
    # Example gpuR script

    if (!require("gpuR")) install.packages("gpuR")
    library(gpuR)

    print("CPU times")
    for(i in seq(1:7)) {
        ORDER = 64*(2^i)
        A = matrix(rnorm(ORDER^2), nrow=ORDER)
        B = matrix(rnorm(ORDER^2), nrow=ORDER)
        print(paste(i, sprintf("%5.2f", system.time({C = A %*% B})[3])))
    }

    print("GPU times")
    for(i in seq(1:7)) {
        ORDER = 64*(2^i)
        A = matrix(rnorm(ORDER^2), nrow=ORDER)
        B = matrix(rnorm(ORDER^2), nrow=ORDER)
        gpuA = gpuMatrix(A, type="double")
        gpuB = gpuMatrix(B, type="double")
        print(paste(i, sprintf("%5.2f", system.time({gpuC = gpuA %*% gpuB})[3])))
    }
    ```

=== "gpuR-test.sbatch"

    ``` shell
    #!/bin/bash

    #SBATCH --partition gpu
    #SBATCH --mem 8GB
    #SBATCH --gres gpu:1
    #SBATCH --output=gpuR-test.log

    ## load modules
    # cuda is not loaded by default with R, so it must be loaded explicitely
    ml R cuda

    Rscript gpuR-test.R
    ```

After submitting the job with `sbatch gpuR-test.sbatch`, the output file should
contain something like this:

``` shell
[1] "CPU times"
[1] "1  0.00"
[1] "2  0.00"
[1] "3  0.02"
[1] "4  0.13"
[1] "5  0.97"
[1] "6  7.56"
[1] "7 60.47"

[1] "GPU times"
[1] "1  0.10"
[1] "2  0.04"
[1] "3  0.02"
[1] "4  0.07"
[1] "5  0.39"
[1] "6  2.04"
[1] "7 11.59"
```

which shows a decent speedup for running on a GPU for the largest matrix sizes.



[comment]: #  (link URLs -----------------------------------------------------)

[url_r]:                //www.r-project.org/
[url_r_docs]:           //stat.ethz.ch/R-manual/
[url_s]:                /ect.bell-labs.com/sl/S/
[url_heredoc]:          //en.wikipedia.org/wiki/Here_document
[url_doparallel]:       //cran.r-project.org/web/packages/doParallel/index.html
[url_cran]:             //cran.r-project.org/
[url_dplyr]:            //github.com/tidyverse/dplyr
[url_rmpi]:             //cran.r-project.org/web/packages/Rmpi
[url_gpur]:             //cran.r-project.org/web/packages/gpuR
[url_support]:          mailto:{{ support_email }}

[url_modules]:          /docs/software/modules
[url_software_list]:    /docs/software/list
[url_storage]:          /docs/storage
[url_gpu]:              /docs/user-guide/gpu


--8<--- "includes/_acronyms.md"

