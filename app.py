{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask_pymongo import PyMongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scrape_mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "You must specify a URI or set the MONGO_URI Flask config variable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-8313e1a89a62>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mapp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mFlask\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mmongo\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPyMongo\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m@\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mroute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"/\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mindex\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\flask_pymongo\\__init__.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, app, uri, *args, **kwargs)\u001b[0m\n\u001b[0;32m    108\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    109\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mapp\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 110\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minit_app\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0muri\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    111\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    112\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0minit_app\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mapp\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0muri\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\flask_pymongo\\__init__.py\u001b[0m in \u001b[0;36minit_app\u001b[1;34m(self, app, uri, *args, **kwargs)\u001b[0m\n\u001b[0;32m    142\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    143\u001b[0m             raise ValueError(\n\u001b[1;32m--> 144\u001b[1;33m                 \u001b[1;34m\"You must specify a URI or set the MONGO_URI Flask config variable\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    145\u001b[0m             )\n\u001b[0;32m    146\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: You must specify a URI or set the MONGO_URI Flask config variable"
     ]
    }
   ],
   "source": [
    "app = Flask(__name__)\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    return render_template(\"index.html\", mars = mars)\n",
    "\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "    mars = mongo.db.mars\n",
    "    mars_data = scrape_mars.scrape()\n",
    "    mars.update({}, mars_data, upsert=True)\n",
    "    return redirect(\"http://localhost:27017/\", code=302)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
