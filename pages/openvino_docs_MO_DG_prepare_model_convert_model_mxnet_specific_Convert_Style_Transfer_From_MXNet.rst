.. index:: pair: page; Convert MXNet Style Transfer Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_mxnet_specific__convert__style__transfer__from__m_x_net:


Convert MXNet Style Transfer Model
==================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_mxnet_specific__convert__style__transfer__from__m_x_net_1md_openvino_docs_mo_dg_prepare_model_convert_model_mxnet_specific_convert_style_transfer_from_mxnet` The tutorial explains how to generate a model for style transfer using the public MXNet\* neural style transfer sample. To use the style transfer sample from OpenVINO, follow the steps below as no public pre-trained style transfer model is provided with the OpenVINO toolkit.

1. Download or clone the repository with an MXNet neural style transfer sample: .
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

2. Prepare the environment required to work with the cloned repository:
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Install packages dependency:
   
   
   
   .. ref-code-block:: cpp
   
   	sudo apt-get install python-tk

Installing python-tk step is needed only for Linux, as it is included by default in Python\* for Windows\*.

#. Install Python\* requirements:
   
   .. ref-code-block:: cpp
   
   	pip3 install --user mxnet
   	pip3 install --user matplotlib
   	pip3 install --user scikit-image

3. Download the pre-trained  and save it to the root directory of the cloned repository because the sample expects the model  file to be in that directory.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

4. Modify source code files of style transfer sample from cloned repository.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Go to the ``fast_mrf_cnn`` subdirectory.
   
   .. ref-code-block:: cpp
   
   	cd ./fast_mrf_cnn

#. Open the ``symbol.py`` file and modify the ``decoder_symbol()`` function. Replace.
   
   .. ref-code-block:: cpp
   
   	def decoder_symbol():
   	    data = mx.sym.Variable('data')
   	    data = mx.sym.Convolution(data=data, num_filter=256, kernel=(3,3), pad=(1,1), stride=(1, 1), name='deco_conv1')

with the following code:



.. ref-code-block:: cpp

	def decoder_symbol_with_vgg(vgg_symbol):
	    data = mx.sym.Convolution(data=vgg_symbol, num_filter=256, kernel=(3,3), pad=(1,1), stride=(1, 1), name='deco_conv1')

#. Save and close the ``symbol.py`` file.

#. Open and edit the ``make_image.py`` file: Modify the ``__init__()`` function in the ``Maker`` class. Replace:
   
   
   
   .. ref-code-block:: cpp
   
   	decoder = symbol.decoder_symbol()

with the following code:



.. ref-code-block:: cpp

	decoder = symbol.decoder_symbol_with_vgg(vgg_symbol)

#. To join the pre-trained weights with the decoder weights, make the following changes: After the code lines for loading the decoder weights:
   
   
   
   .. ref-code-block:: cpp
   
   	args = mx.nd.load('%s_decoder_args.nd'%model_prefix)
   	auxs = mx.nd.load('%s_decoder_auxs.nd'%model_prefix)

add the following line:



.. ref-code-block:: cpp

	arg_dict.update(args)

#. Use ``arg_dict`` instead of ``args`` as a parameter of the ``decoder.bind()`` function. Replace the line:
   
   
   
   .. ref-code-block:: cpp
   
   	self.deco_executor = decoder.bind(ctx=mx.gpu(), args=args, aux_states=auxs)

with the following:



.. ref-code-block:: cpp

	self.deco_executor = decoder.bind(ctx=mx.cpu(), args=arg_dict, aux_states=auxs)

#. To save the result model as a ``.json`` file, add the following code to the end of the ``generate()`` function in the ``Maker`` class:
   
   
   
   .. ref-code-block:: cpp
   
   	self.vgg_executor._symbol.save('{}-symbol.json'.format('vgg19'))
   	self.deco_executor._symbol.save('{}-symbol.json'.format('nst_vgg19'))

#. Save and close the ``make_image.py`` file.

5. Run the sample with a decoder model according to the instructions from the  file in the  directory of the cloned repository.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

For example, to run the sample with the pre-trained decoder weights from the ``models`` folder and output shape, use the following code:



.. ref-code-block:: cpp

	import make_image
	maker = make_image.Maker('models/13', (1024, 768))
	maker.generate('output.jpg', '../images/tubingen.jpg')

Where the ``models/13`` string is composed of the following substrings:

* ``models/`` : path to the folder that contains .nd files with pre-trained styles weights

* ``13`` : prefix pointing to 13_decoder, which is the default decoder for the repository.

.. note:: If you get an error saying "No module named 'cPickle'", try running the script from this step in Python 2. Then return to Python 3 for the remaining steps.

You can choose any style from `collection of pre-trained weights <https://pan.baidu.com/s/1skMHqYp>`__. (On the Chinese-language page, click the down arrow next to a size in megabytes. Then wait for an overlay box to appear, and click the blue button in it to download.) The ``generate()`` function generates ``nst_vgg19-symbol.json`` and ``vgg19-symbol.json`` files for the specified shape. In the code, it is [1024 x 768] for a 4:3 ratio, and you can specify another, for example, [224,224] for a square ratio.

6. Run the Model Optimizer to generate an Intermediate Representation (IR):
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Create a new directory. For example:
   
   
   
   .. ref-code-block:: cpp
   
   	mkdir nst_model

#. Copy the initial and generated model files to the created directory. For example, to copy the pre-trained decoder weights from the ``models`` folder to the ``nst_model`` directory, run the following commands:
   
   
   
   .. ref-code-block:: cpp
   
   	cp nst_vgg19-symbol.json nst_model
   	cp vgg19-symbol.json nst_model
   	cp ../vgg19.params nst_model/vgg19-0000.params
   	cp models/13_decoder_args.nd nst_model
   	cp models/13_decoder_auxs.nd nst_model

.. note:: Make sure that all the ``.params`` and ``.json`` files are in the same directory as the ``.nd`` files. Otherwise, the conversion process fails.

#. Run the Model Optimizer for MXNet. Use the ``--nd_prefix_name`` option to specify the decoder prefix and ``--input_shape`` to specify input shapes in [N,C,W,H] order. For example:
   
   
   
   .. ref-code-block:: cpp
   
   	mo --input_symbol <path/to/nst_model>/nst_vgg19-symbol.json --framework mxnet --output_dir <path/to/output_dir> --input_shape [1,3,224,224] --nd_prefix_name 13_decoder --pretrained_model <path/to/nst_model>/vgg19-0000.params

#. The IR is generated (``.bin``, ``.xml`` and ``.mapping`` files) in the specified output directory and ready to be consumed by the OpenVINO Runtime.

