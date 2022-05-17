.. index:: pair: page; Layout API overview
.. _doxid-openvino_docs__o_v__u_g__layout__overview:


Layout API overview
===================

:target:`doxid-openvino_docs__o_v__u_g__layout__overview_1md_openvino_docs_ov_runtime_ug_layout_overview`

Introduction
~~~~~~~~~~~~

In few words, with layout ``NCHW`` it is easier to understand what model's shape ``{8, 3, 224, 224}`` means. Without layout it is just a 4-dimensional tensor.

Concept of layout helps you (and your application) to understand what does each particular dimension of input/output tensor mean. For example, if your input has shape ``{1, 3, 720, 1280}`` and layout "NCHW" - it is clear that ``N(batch) = 1``, ``C(channels) = 3``, ``H(height) = 720`` and ``W(width) = 1280``. Without layout information ``{1, 3, 720, 1280}`` doesn't give any idea to your application what these number mean and how to resize input image to fit model's expectations.

Reasons when you may want to care about input/output layout:

* Perform model modification:
  
  * Apply :ref:`preprocessing <doxid-openvino_docs__o_v__u_g__preprocessing__overview>` steps, like subtract means, divide by scales, resize image, convert RGB<->BGR
  
  * Set/get batch for a model

* Same operations, used during model conversion phase, see :ref:`Model Optimizer Embedding Preprocessing Computation <doxid-openvino_docs__m_o__d_g__additional__optimization__use__cases>`

* Improve readability of a model's input and output

Layout syntax
~~~~~~~~~~~~~

Short
-----

The easiest way is to fully specify each dimension with one alphabetical letter

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("NHWC");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.runtime import Layout
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW')





.. raw:: html

   </div>







.. raw:: html

   </div>



This assigns 'N' to first dimension, 'C' to second, 'H' to 3rd and 'W' to 4th

Advanced
--------

Advanced syntax allows assigning a word to a dimension. To do this, wrap layout with square brackets ``[]`` and specify each name separated by comma ``,``

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// Each dimension has name separated by comma, layout is wrapped with square brackets
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("[time,temperature,humidity]");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# Each dimension has name separated by comma
	# Layout is wrapped with square brackets
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('[time,temperature,humidity]')





.. raw:: html

   </div>







.. raw:: html

   </div>

Partially defined layout
------------------------

If some dimension is not important, it's name can be set to ``?``

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// First dimension is batch, 4th is 'channels'. Others are not important for us
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("N??C");
	// Or the same using advanced syntax
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("[n,?,?,c]");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# First dimension is batch, 4th is 'channels'.
	# Others are not important for us
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('N??C')
	
	# Or the same using advanced syntax
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('[n,?,?,c]')





.. raw:: html

   </div>







.. raw:: html

   </div>

Dynamic layout
--------------

If number of dimensions is not important, ellipsis ``...`` can be used to specify variadic number of dimensions.

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// First dimension is 'batch' others are whatever
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("N...");
	
	// Second dimension is 'channels' others are whatever
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("?C...");
	
	// Last dimension is 'channels' others are whatever
	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("...C");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	# First dimension is 'batch' others are whatever
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('N...')
	
	# Second dimension is 'channels' others are whatever
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('?C...')
	
	# Last dimension is 'channels' others are whatever
	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('...C')





.. raw:: html

   </div>







.. raw:: html

   </div>





Predefined names
----------------

Layout has pre-defined some widely used in computer vision dimension names:

* N/Batch - batch size

* C/Channels - channels dimension

* D/Depth - depth

* H/Height - height

* W/Width - width

These names are used in :ref:`PreProcessing API <doxid-openvino_docs__o_v__u_g__preprocessing__overview>` and there is a set of helper functions to get appropriate dimension index from layout

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	// returns 0 for batch
	:ref:`ov::layout::batch_idx <doxid-group__ov__layout__cpp__api_1gae57e9fcaa7d8eaa7ddbcdfece346bccb>`("NCDHW");
	
	// returns 1 for channels
	:ref:`ov::layout::channels_idx <doxid-group__ov__layout__cpp__api_1ga4c4a2d4a226d5b264a0f74c6c7839f4f>`("NCDHW");
	
	// returns 2 for depth
	:ref:`ov::layout::depth_idx <doxid-group__ov__layout__cpp__api_1ga69af957b8f6a69956f38dfa1afc7039a>`("NCDHW");
	
	// returns -2 for height
	:ref:`ov::layout::height_idx <doxid-group__ov__layout__cpp__api_1ga83da0183fe7f811912436ddb4aa4bb28>`("...HW");
	
	// returns -1 for width
	:ref:`ov::layout::width_idx <doxid-group__ov__layout__cpp__api_1ga8730a2b5c3fd24f752c550ee3d07b870>`("...HW");





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	from openvino.runtime import layout_helpers
	# returns 0 for batch
	layout_helpers.batch_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCDHW'))
	
	# returns 1 for channels
	layout_helpers.channels_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCDHW'))
	
	# returns 2 for depth
	layout_helpers.depth_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCDHW'))
	
	# returns -2 for height
	layout_helpers.height_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('...HW'))
	
	# returns -1 for width
	layout_helpers.width_idx(:ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('...HW'))





.. raw:: html

   </div>







.. raw:: html

   </div>





Equality
--------

Layout names are case-insensitive, which means that ``Layout("NCHW") == Layout("nChW") == Layout("[N,c,H,w]")``

Dump layout
-----------

Layout can be converted to string in advanced syntax format. Can be useful for debugging and serialization purposes

.. raw:: html

   <div class='sphinxtabset'>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="C++">





.. ref-code-block:: cpp

	layout = :ref:`ov::Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`("NCHW");
	std::cout << layout.to_string(); // prints [N,C,H,W]





.. raw:: html

   </div>







.. raw:: html

   <div class="sphinxtab" data-sphinxtab-value="Python">





.. ref-code-block:: cpp

	layout = :ref:`Layout <doxid-namespace_inference_engine_1a246d143abc5ca07da8d2cadeeb88fdb8>`('NCHW')
	print(layout)    # prints [N,C,H,W]





.. raw:: html

   </div>







.. raw:: html

   </div>





See also
~~~~~~~~

* ``:ref:`ov::Layout <doxid-classov_1_1_layout>``` C++ class documentation

