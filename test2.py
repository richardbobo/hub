{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'mlxtend'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-5aec4d2102df>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mmlxtend\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpreprocessing\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mTransactionEncoder\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mmlxtend\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfrequent_patterns\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mapriori\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m#设置数据集\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'mlxtend'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from mlxtend.preprocessing import TransactionEncoder\n",
    "from mlxtend.frequent_patterns import apriori\n",
    "\n",
    "#设置数据集\n",
    "dataset = [['牛奶','洋葱','肉豆蔻','芸豆','鸡蛋','酸奶'],\n",
    "        ['莳萝','洋葱','肉豆蔻','芸豆','鸡蛋','酸奶'],\n",
    "        ['牛奶','苹果','芸豆','鸡蛋'],\n",
    "        ['牛奶','独角兽','玉米','芸豆','酸奶'],\n",
    "        ['玉米','洋葱','洋葱','芸豆','冰淇淋','鸡蛋']]\n",
    "te = TransactionEncoder()\n",
    "#进行 one-hot 编码\n",
    "te_ary = te.fit(dataset).transform(dataset)\n",
    "df = pd.DataFrame(te_ary, columns=te.columns_)\n",
    "#利用 Apriori 找出频繁项集\n",
    "freq = apriori(df, min_support=0.05, use_colnames=True)\n",
    "\n",
    "print(freq)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
