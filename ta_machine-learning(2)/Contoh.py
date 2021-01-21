#!/usr/bin/env python
# coding: utf-8

# ## Kebutuhan library

# In[97]:


import os
import graphviz
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

from sklearn import tree
from statistics import mean
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import RandomOverSampler
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.tree import DecisionTreeClassifier
os.environ['PATH'] = os.environ['PATH']+';'+os.environ['CONDA_PREFIX']+r"\Library\bin\graphviz"
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO


# ##### msc

# In[2]:


warnings.filterwarnings('ignore')


# ## Inisialisasi data

# In[102]:


working_dir = os.getcwd()

ecoli_file_direktori = os.path.join(working_dir, "ecoli.data")

colnames = ['SEQUENCE_NAME', 'MCG', 'GVH', 'LIP', 'CHG', 'AAC', 'ALM1', 'ALM2', 'CLASS']

ecoli_df = pd.read_csv(ecoli_file_direktori, delim_whitespace=True, names=colnames)

fitur =  ['SEQUENCE_NAME', 'MCG', 'GVH', 'LIP', 'CHG', 'AAC', 'ALM1', 'ALM2']


# ## Deskripsi data

# ### Jumlah sample data 

# In[5]:


ecoli_df.shape


# ### Lihat sebagian samle data

# In[6]:


ecoli_df.head()


# ### Lihat kolom, jumlah sample data, dan tipe data 

# In[7]:


ecoli_df.info()


# Terdapat 336 sample data dengan tipe data numerik.

# ### Lihat kelas

# In[8]:


print((ecoli_df['CLASS'].unique()))


# Pada dataset ini terdapat 8 kelas.

# ### Deskripsi statistik 

# #### Kolom 1 sampai 3

# In[9]:


ecoli_df.describe().loc[['count','mean','min','max']]


# Berdasarkan deskripsi statisiknya, dapat dilihat dari nilai meannya bahwa rentang di antara sample data tidak terlalu jauh. Hal ini menandakan bahwa tidak perlunya dilakukan normalisasi pada data.

# ### Periksa missing value

# In[10]:


ecoli_df.isnull().sum()


# Pada dataset ini tidak terdapat missing value, sehingga tidak perlu dilakukan imputasi atau penanganan terhadap missing value.

# ### Visualisasi sebaran data pada tiap kelas

# In[11]:


x_plot_before = ecoli_df['CLASS'].unique()
y_plot_before = ecoli_df['CLASS'].value_counts()

fig, ax = plt.subplots(figsize=(20, 10))
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
width = 0.75
ind = np.arange(len(y_plot_before))
ax.barh(ind, y_plot_before, width, color="blue")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x_plot_before)
plt.title('Jumlah sebaran sample data tiap kelas', fontsize=18)
plt.xlabel('jumlah', fontsize=18)
plt.ylabel('kelas', fontsize=18)

for i, v in enumerate(y_plot_before):
    ax.text(v, i, str(v), va='center', fontsize=18)
plt.show()


# Seperti yang dapat dilihat pada plot di atas bahwa sebaran data sangat tidak seimbang atau dataset ini adalah dataset yang imbalanced. Dapat dilihat bahwa jumlah sample data pada kelas __pp__ hanya sejumlah 2, sedangkan jumlah sample data pada kelas __cp__ berjumlah 143.

# ## Preprocessing data

# ### Penghapusan kolom SEQUENCE_NAME
# 
# Kolom __SEQUENCE_NAME__ akan dihapus karena kolom tersebut merupakan ID dari tiap sample data.

# In[12]:


ecoli_df_2 = ecoli_df.drop('SEQUENCE_NAME', axis=1)
ecoli_df_2.head()


# ### Resampling data
# 
# Seperti yang sudah dijelaskan sebelumnya bahwa dataset ini adalah dataset yang tidak seimbang. Maka dari itu, kami akan melakukan resampling data yang bertujuan untuk membuat sample data baru untuk menyeimbangkan dataset.
# 
# Untuk referensi resampling data diambil dari sini: [Resampling strategies for imbalanced datasets](https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets), [How to do cross-validation when upsampling data](https://kiwidamien.github.io/how-to-do-cross-validation-when-upsampling-data.html), [An opinionated guide to imbalanced classes](https://soph.info/2019/05/07/imbalance/).
# 
# Metode yang kami ambil untuk melakukan resampling data adalah metode ROS (Random Over Sampling). Metode ini akan melakukan penambahan jumlah sample data berdasarkan contoh dari sample data asli. Sayangnya metode ini tidak menambahkan variasi sample data. Berikut adalah ilustrasi dari metode ROS:
# 
# <img src="ros_sampling.png">
# 
# Yang akan dilakukan di bawah ini hanyalah sebagai contoh untuk mempraktekkan resampling data. Proses resampling data yang sesungguhnya akan dilakukan di dalam proses cross validation bersamaan dengan proses modeling.

# #### Pisahkan dataset menjadi dataframe X dan y
# 
# X adalah dataframe yang menampung atribut atau fitur, y adalah dataframe yang menampung kelas.

# In[13]:


fitur = ['MCG','GVH','LIP','CHG','AAC','ALM1','ALM2']
kelas = ['CLASS']

X = np.array(ecoli_df_2[fitur])
y = np.array(ecoli_df_2[kelas])


# #### Lakukan pembagian dataset menjadi training set dan testing set
# 
# Pembagian akan dilakukan dengan presentase 70% training set dan 30% testing set. Pembagian dataset dilakukan dengan menggunakan fungsi train_test_split().

# In[14]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


# #### Resampling dengan metode ROS
# 
# Resampling data hanya dilakukan pada training setnya saja.

# In[15]:


ros_resampler = RandomOverSampler(random_state=42)
X_res, y_res = ros_resampler.fit_sample(X_train, y_train)

print('Jumlah sample data pada training set sebelum resampling data {}' . format(X_train.shape))
print('Jumlah sample data pada training set setelah resampling data {}' . format(X_res.shape))


# #### Visualisasi sebaran data setelah resampling data

# In[16]:


x_plot_after, y_plot_after = np.unique(y_res, return_counts=True)

fig, ax = plt.subplots(figsize=(20, 10))
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
width = 0.75
ind = np.arange(len(y_plot_after))
ax.barh(ind, y_plot_after, width, color="blue")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x_plot_after)
plt.title('Jumlah sebaran sample data tiap kelas', fontsize=18)
plt.xlabel('jumlah', fontsize=18)
plt.ylabel('kelas', fontsize=18)

for i, v in enumerate(y_plot_after):
    ax.text(v, i, str(v), va='center', fontsize=18)
plt.show()


# ## Modeling

# ### Inisiasi kfold
# 
# Pada praktek ini akan digunakan StratifiedKFold dengan jumlah k=10 atau dataset akan dibagi menjadi 10 partisi. Sedangkan StratifiedKFold akan membagi data dengan proporsi yang seseimbang mungkin, yaitu presentase pembagian data di tiap partisinya akan sama.

# In[17]:


kf = StratifiedKFold(n_splits=10, random_state=42, shuffle=True)


# ### Inisiasi model GaussianNB

# #### Model

# In[18]:


gaussiannb_clf = GaussianNB


# #### Parameter model GaussianNB
# 
# Model gaussian tidak menerima parameter apapun sehingga dapat dikosongkan.

# In[19]:


gaussiannb_parameter = {}


# ### Inisiasi model RandomForestClassifier

# #### Model

# In[20]:


randomforest_clf = RandomForestClassifier


# #### Parameter model RandomForestClassifier
# 
# Ini bisa diubah-ubah. Mungkin ada parameter lain yang menghasilkan akurasi lebih baik. Referensi liat di sini: [How to do cross-validation when upsampling data](https://kiwidamien.github.io/how-to-do-cross-validation-when-upsampling-data.html). Setiap kali ubah parameter, compile lagi, dan jalanin lagi fungsi get_score(). Kalo udah dapet akurasi setelah ganti parameter, catet akurasinya di excel buat perbandingan.

# In[78]:


randomforest_parameter = {'n_estimators': 200, 'max_depth': 7, 'random_state': 13}


# ### Inisiasi model DecisionTreeClassifier

# #### Model

# In[91]:


DesicionTree_clf = DecisionTreeClassifier
clf = DecisionTree_clf.fit


# #### Parameter model DecisionTreeClassifier
# 
# Ini bisa dubah-ubah juga. Mungkin ada parameter lain yang menghasilkan akurasi lebih baik. Referensi liat di sini: [How to tune a Decision Tree?](https://towardsdatascience.com/how-to-tune-a-decision-tree-f03721801680). Setiap kali ubah parameter, compile lagi, dan jalanin lagi fungsi get_score(). Kalo udah dapet akurasi setelah ganti parameter, catet akurasinya di excel buat perbandingan.

# In[93]:


decisiontree_parameter = {}


# ### Fungsi untuk resampling dan modeling di dalam cross validation

# In[23]:


def get_score(model, params, cv=None):
    if cv is None:
        cv = StratifiedKFold(n_splits=10, random_state=42, shuffle=True)
    
    ros = RandomOverSampler(random_state=42)
    
    scores = []
    
    for train_fold_index, test_fold_index in cv.split(X_train, y_train):
        # generate training set
        X_train_fold, y_train_fold = X_train[train_fold_index], y_train[train_fold_index]
        # generate testing set
        X_test_fold, y_test_fold = X_train[test_fold_index], y_train[test_fold_index]
        # resampling data hanya pada training set saja
        X_train_fold_resample, y_train_fold_resample = ros.fit_sample(X_train_fold, y_train_fold)
        # fit model pada training set yang telah diresample
        model_obj = model(**params).fit(X_train_fold_resample, y_train_fold_resample)
        # nilai model pada testing set
        score = accuracy_score(y_test_fold, model_obj.predict(X_test_fold))
        # masukkan score ke dalam array scores
        scores.append(score)
    
    return np.array(scores)


# ### Score untuk model GaussianNB

# #### Array score

# In[24]:


print(get_score(GaussianNB, gaussiannb_parameter, cv=kf))


# #### Rata-rata akurasi

# In[25]:


print(mean(get_score(gaussiannb_clf, gaussiannb_parameter, cv=kf)))


# ### Score untuk model RandomForestClassifier

# #### Array score

# In[79]:


print(get_score(randomforest_clf, randomforest_parameter, cv=kf))


# #### Rata-rata akurasi

# In[80]:


print(mean(get_score(randomforest_clf, randomforest_parameter, cv=kf)))


# ### Score untuk model DecisionTreeClassifier

# #### Array score

# In[94]:


print(get_score(DesicionTree_clf, decisiontree_parameter))


# #### Rata-rata akurasi

# In[105]:


print(mean(get_score(DesicionTree_clf, decisiontree_parameter)))


# In[ ]:





# In[ ]:





# In[ ]:




