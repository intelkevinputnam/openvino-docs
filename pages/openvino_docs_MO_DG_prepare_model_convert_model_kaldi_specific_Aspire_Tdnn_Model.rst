.. index:: pair: page; Convert Kaldi\* ASpIRE Chain Time Delay Neural Network (TDNN) Model
.. _doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_kaldi_specific__aspire__tdnn__model:


Convert Kaldi\* ASpIRE Chain Time Delay Neural Network (TDNN) Model
===================================================================

:target:`doxid-openvino_docs__m_o__d_g_prepare_model_convert_model_kaldi_specific__aspire__tdnn__model_1md_openvino_docs_mo_dg_prepare_model_convert_model_kaldi_specific_aspire_tdnn_model` You can `download a pre-trained model <https://kaldi-asr.org/models/1/0001_aspire_chain_model.tar.gz>`__ for the ASpIRE Chain Time Delay Neural Network (TDNN) from the Kaldi\* project official website.

Convert ASpIRE Chain TDNN Model to IR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To generate the Intermediate Representation (IR) of the model, run the Model Optimizer with the following parameters:

.. ref-code-block:: cpp

	mo --input_model exp/chain/tdnn_7b/final.mdl --output output

The IR will have two inputs: ``input`` for data and ``ivector`` for ivectors.

Example: Run ASpIRE Chain TDNN Model with the Speech Recognition Sample
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These instructions show how to run the converted model with the :ref:`Speech Recognition sample <doxid-openvino_inference_engine_samples_speech_sample__r_e_a_d_m_e>`. In this example, the input data contains one utterance from one speaker.

To follow the steps described below, you must first do the following:

#. Download a `Kaldi repository <https://github.com/kaldi-asr/kaldi>`__.

#. Build it using instructions in ``README.md`` in the repository.

#. Download the `model archive <https://kaldi-asr.org/models/1/0001_aspire_chain_model.tar.gz>`__ from Kaldi website.

#. Extract the downloaded model archive to the ``egs/aspire/s5`` folder of the Kaldi repository.

To run the ASpIRE Chain TDNN Model with Speech Recognition sample:

#. Prepare the model for decoding. Refer to the ``README.txt`` file from the downloaded model archive for instructions.

#. Convert data and ivectors to ``.ark`` format. Refer to the corresponding sections below for instructions.

Prepare Data
------------

If you have a ``.wav`` data file, you can convert it to ``.ark`` format using the following command:

.. ref-code-block:: cpp

	<path_to_kaldi_repo>/src/featbin/compute-mfcc-feats --config=<path_to_kaldi_repo>/egs/aspire/s5/conf/mfcc_hires.conf scp:./wav.scp ark,scp:feats.ark,feats.scp

Add the ``feats.ark`` absolute path to ``feats.scp`` to avoid errors in later commands.

Prepare Ivectors
----------------

To prepare ivectors for the Speech Recognition sample, do the following:

#. Copy the ``feats.scp`` file to the ``egs/aspire/s5/`` directory of the built Kaldi repository and navigate there:
   
   .. ref-code-block:: cpp
   
   	cp feats.scp <path_to_kaldi_repo>/egs/aspire/s5/
   	cd <path_to_kaldi_repo>/egs/aspire/s5/

#. Extract ivectors from the data:
   
   .. ref-code-block:: cpp
   
   	./steps/online/nnet2/extract_ivectors_online.sh --nj 1 --ivector_period <max_frame_count_in_utterance> <data folder> exp/tdnn_7b_chain_online/ivector_extractor <ivector folder>

To simplify the preparation of ivectors for the Speech Recognition sample, specify the maximum number of frames in utterances as a parameter for ``--ivector_period`` to get only one ivector per utterance.

To get the maximum number of frames in utterances, you can use the following command line:

.. ref-code-block:: cpp

	../../../src/featbin/feat-to-len scp:feats.scp ark,t: | cut -d' ' -f 2 - | sort -rn | head -1

As a result, in ``<ivector folder>``, you will find the ``ivector_online.1.ark`` file.

#. Go to the ``<ivector folder>`` :
   
   .. ref-code-block:: cpp
   
   	cd <ivector folder>

#. Convert the ``ivector_online.1.ark`` file to text format using the ``copy-feats`` tool. Run the following command:
   
   .. ref-code-block:: cpp
   
   	<path_to_kaldi_repo>/src/featbin/copy-feats --binary=False ark:ivector_online.1.ark ark,t:ivector_online.1.ark.txt

#. For the Speech Recognition sample, the ``.ark`` file must contain an ivector for each frame. You must copy the ivector ``frame_count`` times. To do this, you can run the following script in the Python\* command prompt:
   
   .. ref-code-block:: cpp
   
   	import subprocess
   	
   	subprocess.run(["<path_to_kaldi_repo>/src/featbin/feat-to-len", "scp:<path_to_kaldi_repo>/egs/aspire/s5/feats.scp", "ark,t:feats_length.txt"])
   	
   	f = open("ivector_online.1.ark.txt", "r")
   	g = open("ivector_online_ie.ark.txt", "w")
   	length_file = open("feats_length.txt", "r")
   	for line in f:
   	    if "[" not in line:
   	        for i in range(frame_count):
   	            line = line.replace("]", " ")
   	            g.write(line)
   	    else:
   	        g.write(line)
   	        frame_count = int(length_file.read().split(" ")[1])
   	g.write("]")
   	f.close()
   	g.close()
   	length_file.close()

#. Create an ``.ark`` file from ``.txt`` :
   
   .. ref-code-block:: cpp
   
   	<path_to_kaldi_repo>/src/featbin/copy-feats --binary=True ark,t:ivector_online_ie.ark.txt ark:ivector_online_ie.ark

Run the Speech Recognition Sample
---------------------------------

Run the Speech Recognition sample with the created ivector ``.ark`` file as follows:

.. ref-code-block:: cpp

	speech_sample -i feats.ark,ivector_online_ie.ark -m final.xml -d CPU -o prediction.ark -cw_l 17 -cw_r 12

Results can be decoded as described in "Use of Sample in Kaldi\* Speech Recognition Pipeline" chapter in :ref:`the Speech Recognition Sample description <doxid-openvino_inference_engine_samples_speech_sample__r_e_a_d_m_e>`.

