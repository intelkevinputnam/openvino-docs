.. index:: pair: page; Result
.. _doxid-openvino_docs_ops_infrastructure__result_1:


Result
======

:target:`doxid-openvino_docs_ops_infrastructure__result_1_1md_openvino_docs_ops_infrastructure_result_1` **Versioned name** : *Result-1*

**Category** : *Infrastructure*

**Short description** : *Result* layer specifies output of the model.

**Attributes** :

.. code-block:: cpp

	No attributes available.

**Inputs**

* **1** : A tensor of type *T*. **Required.**

**Types**

* *T* : arbitrary supported type.

**Example**

.. ref-code-block:: cpp

	<layer ... type="Result" ...>
	    <input>
	        <port id="0">
	            <dim>1</dim>
	            <dim>3</dim>
	            <dim>224</dim>
	            <dim>224</dim>
	        </port>
	    </input>
	</layer>

