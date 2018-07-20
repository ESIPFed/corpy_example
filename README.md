This is simple demo program that exercises the 
[corpy](https://github.com/ESIPFed/corpy) 
python client module.

*Note*: The python client module is itself preliminary.

You can run this as follows:

- Optionally, use [virtualenv](https://virtualenv.pypa.io) to isolate the python 
  environment for this demo, for example:

        $ virtualenv --python=/usr/local/bin/python3.7 virtenv
        $ source virtenv/bin/activate

- Install the [`corpy`](https://github.com/ESIPFed/corpy) module:

        $ pip install git+https://github.com/ESIPFed/corpy.git
        
      (Use the `--upgrade` flag if you are upgrading.)

Then, execute:

        $ python demo1.py

See source for more details.
