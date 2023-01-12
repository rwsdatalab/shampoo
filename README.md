# shampoo

[![Python](https://img.shields.io/pypi/pyversions/shampoo)](https://img.shields.io/pypi/pyversions/shampoo)
[![Pypi](https://img.shields.io/pypi/v/shampoo)](https://pypi.org/project/shampoo/)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://rwsdatalab.github.io/shampoo/)
[![LOC](https://sloc.xyz/github/rwsdatalab/shampoo/?category=code)](https://github.com/rwsdatalab/shampoo/)
[![Downloads](https://static.pepy.tech/personalized-badge/shampoo?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/shampoo)
[![Downloads](https://static.pepy.tech/personalized-badge/shampoo?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/shampoo)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/rwsdatalab/shampoo/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/rwsdatalab/shampoo.svg)](https://github.com/rwsdatalab/shampoo/network)
[![Issues](https://img.shields.io/github/issues/rwsdatalab/shampoo.svg)](https://github.com/rwsdatalab/shampoo/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
![GitHub Repo stars](https://img.shields.io/github/stars/rwsdatalab/shampoo)
![GitHub repo size](https://img.shields.io/github/repo-size/rwsdatalab/shampoo)


* ``shampoo`` is Python package

# 
**Star this repo if you like it! ⭐️**
#


## Blog/Documentation

* [**shampoo documentation pages (Sphinx)**](https://rwsdatalab.github.io/shampoo/)
* [**Notebook with examples**](https://colab.research.google.com/github/rwsdatalab/shampoo/blob/master/notebooks/shampoo.ipynb)
* [**Read more details and usage about shampoo in this blog!**](https://towardsdatascience.com/shampoo)

* <a href="https://rwsdatalab.github.io/shampoo/"> <img src="https://img.shields.io/badge/Sphinx-Docs-Green" alt="Open documentation pages"/> </a> shampoo documentation pages 
* <a href="https://colab.research.google.com/github/rwsdatalab/shampoo/blob/master/notebooks/shampoo.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open example In Colab"/> </a> Notebook example 
* <a href="https://towardsdatascience.com/a-step-by-step-guide-for-clustering-images-4b45f9906128"> <img src="https://img.shields.io/badge/Medium-Blog-blue" alt="Open Blog"/> </a> Blog: A step-by-step guide for clustering images 


### Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install shampoo from PyPI (recommended). shampoo is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as following:

```bash
conda create -n env_shampoo python=3.8
conda activate env_shampoo
```

```bash
pip install shampoo            # normal install
pip install --upgrade shampoo # or update if needed
```

* Alternatively, you can install from the GitHub source:
```bash
# Directly install from github source
pip install -e git://github.com/rwsdatalab/shampoo.git@0.1.0#egg=master
pip install git+https://github.com/rwsdatalab/shampoo#egg=master
pip install git+https://github.com/rwsdatalab/shampoo

# By cloning
git clone https://github.com/rwsdatalab/shampoo.git
cd shampoo
pip install -U .
```  

#### Import shampoo package
```python
import shampoo as shampoo
```

#### Example:
```python
df = pd.read_csv('https://github.com/rwsdatalab/hnet/blob/master/shampoo/data/example_data.csv')
model = shampoo.fit(df)
G = shampoo.plot(model)
```
<p align="center">
  <img src="https://github.com/rwsdatalab/shampoo/blob/master/docs/figs/fig1.png" width="600" />
  
</p>


#### References
* https://github.com/rwsdatalab/shampoo

### Licence
See [LICENSE](LICENSE) for details.
