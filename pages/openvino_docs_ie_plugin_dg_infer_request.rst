.. index:: pair: page; Synchronous Inference Request
.. _doxid-openvino_docs_ie_plugin_dg_infer_request:


Synchronous Inference Request
=============================

:target:`doxid-openvino_docs_ie_plugin_dg_infer_request_1md_openvino_docs_ie_plugin_dg_inferrequest` ``InferRequest`` class functionality:

* Allocate input and output blobs needed for a backend-dependent network inference.

* Define functions for inference process stages (for example, ``preprocess``, ``upload``, ``infer``, ``download``, ``postprocess``). These functions can later be used to define an execution pipeline during :ref:`Asynchronous Inference Request <doxid-openvino_docs_ie_plugin_dg_async_infer_request>` implementation.

* Call inference stages one by one synchronously.

Class
~~~~~

Inference Engine Plugin API provides the helper :ref:`InferenceEngine::IInferRequestInternal <doxid-class_inference_engine_1_1_i_infer_request_internal>` class recommended to use as a base class for a synchronous inference request implementation. Based of that, a declaration of a synchronous request class can look as follows:

.. ref-code-block:: cpp

	class TemplateInferRequest : public :ref:`InferenceEngine::IInferRequestInternal <doxid-class_inference_engine_1_1_i_infer_request_internal>` {
	public:
	    typedef std::shared_ptr<TemplateInferRequest> :ref:`Ptr <doxid-class_inference_engine_1_1_i_infer_request_internal_1a50c614e7a30e1e8ee58e984f210a1558>`;
	
	    TemplateInferRequest(const :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>`& networkInputs,
	                         const :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>`& networkOutputs,
	                         const std::shared_ptr<ExecutableNetwork>& executableNetwork);
	    TemplateInferRequest(const std::vector<std::shared_ptr<const ov::Node>>& inputs,
	                         const std::vector<std::shared_ptr<const ov::Node>>& outputs,
	                         const std::shared_ptr<ExecutableNetwork>& executableNetwork);
	    ~TemplateInferRequest();
	
	    void :ref:`InferImpl <doxid-class_inference_engine_1_1_i_infer_request_internal_1a0ff052d969d599023769a8f5f3a75a56>`() override;
	    std::map<std::string, InferenceEngine::InferenceEngineProfileInfo> :ref:`GetPerformanceCounts <doxid-class_inference_engine_1_1_i_infer_request_internal_1a2eefb67a9766a29e032dc57bbf26d592>`() const override;
	
	    // pipeline methods-stages which are used in async infer request implementation and assigned to particular executor
	    void inferPreprocess();
	    void startPipeline();
	    void waitPipeline();
	    void inferPostprocess();
	
	    :ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` :ref:`GetBlob <doxid-class_inference_engine_1_1_i_infer_request_internal_1ad15f46c840f339ee2dd5e827ad003166>`(const std::string& name) override;
	    void :ref:`SetBlob <doxid-class_inference_engine_1_1_i_infer_request_internal_1aaf6f8482fd4e8220edb8cb08558a4d6c>`(const std::string& name, const :ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>`& userBlob) override;
	
	    void :ref:`SetBlobsImpl <doxid-class_inference_engine_1_1_i_infer_request_internal_1a55ffc43c997b9e2034048523724a1a9a>`(const std::string& name, const :ref:`InferenceEngine::BatchedBlob::Ptr <doxid-class_inference_engine_1_1_batched_blob_1ac66bc6bfae9ffc4be2de9c1d2f9e4208>`& batchedBlob) override;
	
	private:
	    void createInferRequest();
	    void allocateDeviceBuffers();
	    void allocateBlobs();
	
	    enum { Preprocess, Postprocess, StartPipeline, WaitPipeline, numOfStages };
	
	    std::shared_ptr<ExecutableNetwork> _executableNetwork;
	    std::array<openvino::itt::handle_t, numOfStages> _profilingTask;
	    // for performance counters
	    std::array<std::chrono::duration<float, std::micro>, numOfStages> _durations;
	
	    :ref:`InferenceEngine::BlobMap <doxid-namespace_inference_engine_1ad1c63c694d34358a748f591ffa74a9d0>` _networkOutputBlobs;
	
	    std::vector<std::shared_ptr<ngraph::runtime::Tensor>> _inputTensors;
	    std::vector<std::shared_ptr<ngraph::runtime::Tensor>> _outputTensors;
	    std::shared_ptr<ngraph::runtime::Executable> _executable;
	};



Class Fields
++++++++++++

The example class has several fields:

* ``_executableNetwork`` - reference to an executable network instance. From this reference, an inference request instance can take a task executor, use counter for a number of created inference requests, and so on.

* ``_profilingTask`` - array of the ``std::array<InferenceEngine::ProfilingTask, numOfStages>`` type. Defines names for pipeline stages. Used to profile an inference pipeline execution with the Intel® instrumentation and tracing technology (ITT).

* ``_durations`` - array of durations of each pipeline stage.

* ``_networkInputBlobs`` - input blob map.

* ``_networkOutputBlobs`` - output blob map.

* ``_parameters`` - ``:ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>``` parameter operations.

* ``_results`` - ``:ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>``` result operations.

* backend specific fields:
  
  * ``_inputTensors`` - inputs tensors which wrap ``_networkInputBlobs`` blobs. They are used as inputs to backend ``_executable`` computational graph.
  
  * ``_outputTensors`` - output tensors which wrap ``_networkOutputBlobs`` blobs. They are used as outputs from backend ``_executable`` computational graph.
  
  * ``_executable`` - an executable object / backend computational graph.

Constructor
-----------

The constructor initializes helper fields and calls methods which allocate blobs:

.. ref-code-block:: cpp

	TemplateInferRequest::TemplateInferRequest(const :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>`& networkInputs,
	                                           const :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>`& networkOutputs,
	                                           const std::shared_ptr<TemplatePlugin::ExecutableNetwork>& executableNetwork)
	    : IInferRequestInternal(networkInputs, networkOutputs),
	      _executableNetwork(executableNetwork) {
	    createInferRequest();
	}
	
	TemplateInferRequest::TemplateInferRequest(const std::vector<std::shared_ptr<const ov::Node>>& inputs,
	                                           const std::vector<std::shared_ptr<const ov::Node>>& outputs,
	                                           const std::shared_ptr<TemplatePlugin::ExecutableNetwork>& executableNetwork)
	    : IInferRequestInternal(inputs, outputs),
	      _executableNetwork(executableNetwork) {
	    createInferRequest();
	}
	
	void TemplateInferRequest::createInferRequest() {
	    // TODO: allocate infer request device and host buffers if needed, fill actual list of profiling tasks
	
	    auto requestID = std::to_string(_executableNetwork->_requestId.fetch_add(1));
	
	    std::string name = _executableNetwork->_function->get_friendly_name() + "_Req" + requestID;
	    _profilingTask = {
	        :ref:`openvino::itt::handle <doxid-group__ie__dev__profiling_1ga8579f29ef5313d519bcaee20dd543a1b>`("Template" + std::to_string(_executableNetwork->_cfg.deviceId) + "_" + name +
	                              "_Preprocess"),
	        :ref:`openvino::itt::handle <doxid-group__ie__dev__profiling_1ga8579f29ef5313d519bcaee20dd543a1b>`("Template" + std::to_string(_executableNetwork->_cfg.deviceId) + "_" + name +
	                              "_Postprocess"),
	        :ref:`openvino::itt::handle <doxid-group__ie__dev__profiling_1ga8579f29ef5313d519bcaee20dd543a1b>`("Template" + std::to_string(_executableNetwork->_cfg.deviceId) + "_" + name +
	                              "_StartPipline"),
	        :ref:`openvino::itt::handle <doxid-group__ie__dev__profiling_1ga8579f29ef5313d519bcaee20dd543a1b>`("Template" + std::to_string(_executableNetwork->_cfg.deviceId) + "_" + name +
	                              "_WaitPipline"),
	    };
	
	    _executable = _executableNetwork->_plugin->_backend->compile(_executableNetwork->_function);
	
	    allocateDeviceBuffers();
	    allocateBlobs();
	}



.. note:: Call :ref:`InferenceEngine::CNNNetwork::getInputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1a76de2a6101fe8276f56b0dc0f99c7ff7>` and :ref:`InferenceEngine::CNNNetwork::getOutputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1af8a6200f549b15a895e2cfefd304a9c2>` to specify both layout and precision of blobs, which you can set with :ref:`InferenceEngine::InferRequest::SetBlob <doxid-class_inference_engine_1_1_infer_request_1a27fb179e3bae652d76076965fd2a5653>` and get with :ref:`InferenceEngine::InferRequest::GetBlob <doxid-class_inference_engine_1_1_infer_request_1a9601a4cda3f309181af34feedf1b914c>`. A plugin uses these hints to determine its internal layouts and precisions for input and output blobs if needed.

Destructor
----------

Decrements a number of created inference requests:

.. ref-code-block:: cpp

	TemplateInferRequest::~TemplateInferRequest() {
	    _executableNetwork->_requestId--;
	}



.. rubric::

**Implementation details:** Base IInferRequestInternal class implements the public :ref:`InferenceEngine::IInferRequestInternal::Infer <doxid-class_inference_engine_1_1_i_infer_request_internal_1afb61e1de4ffb9927431085a91a40f352>` method as following:

* Checks blobs set by users

* Calls the ``InferImpl`` method defined in a derived class to call actual pipeline stages synchronously

.. ref-code-block:: cpp

	void TemplateInferRequest::InferImpl() {
	    // TODO: fill with actual list of pipeline stages, which are executed synchronously for sync infer requests
	    inferPreprocess();
	    startPipeline();
	    waitPipeline();  // does nothing in current implementation
	    inferPostprocess();
	}



1.
++

Below is the code of the ``inferPreprocess`` method to demonstrate Inference Engine common preprocessing step handling:

.. ref-code-block:: cpp

	void TemplateInferRequest::inferPreprocess() {
	    :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, _profilingTask[Preprocess]);
	    auto start = Time::now();
	    convertBatchedInputBlobs();
	    // NOTE: After IInferRequestInternal::execDataPreprocessing call
	    //       input can points to other memory region than it was allocated in constructor.
	    IInferRequestInternal::execDataPreprocessing(_deviceInputs);
	    for (auto&& networkInput : _deviceInputs) {
	        auto index = _executableNetwork->_inputIndex[networkInput.first];
	        const auto& parameter = _executableNetwork->_function->get_parameters()[index];
	        auto parameterShape = networkInput.second->getTensorDesc().getDims();
	        auto srcShape = networkInput.second->getTensorDesc().getBlockingDesc().getBlockDims();
	        const auto& parameterType = parameter->get_element_type();
	        auto mem_blob = InferenceEngine::as<InferenceEngine::MemoryBlob>(networkInput.second);
	        auto isNonRoiDesc = [](const BlockingDesc& desc) {
	            size_t exp_stride = 1;
	            for (size_t i = 0; i < desc.getBlockDims().size(); i++) {
	                size_t rev_idx = desc.getBlockDims().size() - i - 1;
	                :ref:`OPENVINO_ASSERT <doxid-openvino_2core_2except_8hpp_1a7ff78e5accf3159b30b4b32bbb72d272>`(desc.getOrder()[rev_idx] == rev_idx,
	                                "Template plugin: unsupported tensors with mixed axes order: ",
	                                :ref:`ngraph::vector_to_string <doxid-namespacengraph_1a7539123fc4727343234fd272ffbe2d0c>`(desc.getOrder()));
	                if (desc.getStrides()[rev_idx] != exp_stride || desc.getOffsetPaddingToData()[rev_idx] != 0) {
	                    return false;
	                }
	                exp_stride \*= desc.getBlockDims()[rev_idx];
	            }
	            return true;
	        };
	        if (isNonRoiDesc(networkInput.second->getTensorDesc().getBlockingDesc())) {
	            // No ROI extraction is needed
	            _inputTensors[index] = _executableNetwork->_plugin->_backend->create_tensor(parameterType,
	                                                                                        parameterShape,
	                                                                                        mem_blob->rmap().as<void\*>());
	        } else {
	            :ref:`OPENVINO_ASSERT <doxid-openvino_2core_2except_8hpp_1a7ff78e5accf3159b30b4b32bbb72d272>`(parameterType.bitwidth() % 8 == 0,
	                            "Template plugin: Unsupported ROI tensor with element type having ",
	                            std::to_string(parameterType.bitwidth()),
	                            " bits size");
	            // Perform manual extraction of ROI tensor
	            // Basic implementation doesn't take axis order into account `desc.getBlockingDesc().getOrder()`
	            // Performance of manual extraction is not optimal, but it is ok for template implementation
	            _inputTensors[index] = _executableNetwork->_plugin->_backend->create_tensor(parameterType, parameterShape);
	            auto desc = mem_blob->getTensorDesc();
	            auto\* src_data = mem_blob->rmap().as<uint8_t\*>();
	            auto dst_tensor = std::dynamic_pointer_cast<ngraph::runtime::HostTensor>(_inputTensors[index]);
	            :ref:`OPENVINO_ASSERT <doxid-openvino_2core_2except_8hpp_1a7ff78e5accf3159b30b4b32bbb72d272>`(dst_tensor, "Template plugin error: Can't cast created tensor to HostTensor");
	            auto\* dst_data = dst_tensor->get_data_ptr<uint8_t>();
	            std::vector<size_t> indexes(parameterShape.size());
	            for (size_t dst_idx = 0; dst_idx < :ref:`ov::shape_size <doxid-group__ov__model__cpp__api_1gafe8cdd6477ae9810c2bf368602d35883>`(parameterShape); dst_idx++) {
	                size_t val = dst_idx;
	                size_t src_idx = 0;
	                for (size_t j1 = 0; j1 < indexes.size(); j1++) {
	                    size_t j = indexes.size() - j1 - 1;
	                    indexes[j] = val % parameterShape[j] + desc.getBlockingDesc().getOffsetPaddingToData()[j];
	                    val /= parameterShape[j];
	                    src_idx += indexes[j] \* desc.getBlockingDesc().getStrides()[j];
	                }
	                memcpy(dst_data + dst_idx \* parameterType.size(),
	                       src_data + src_idx \* parameterType.size(),
	                       parameterType.size());
	            }
	        }
	    }
	    for (auto&& output : _outputs) {
	        auto outputBlob = output.second;
	        auto networkOutput = _networkOutputBlobs[output.first];
	        auto index = _executableNetwork->_outputIndex[output.first];
	        if (outputBlob->getTensorDesc().getPrecision() == networkOutput->getTensorDesc().getPrecision()) {
	            networkOutput = outputBlob;
	        }
	        const auto& :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>` = _executableNetwork->_function->get_results()[index];
	        if (:ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`->get_output_partial_shape(0).is_dynamic()) {
	            _outputTensors[index] = _executableNetwork->_plugin->_backend->create_tensor();
	            continue;
	        }
	        const auto& resultShape = :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`->get_shape();
	        const auto& resultType = :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`->get_element_type();
	        _outputTensors[index] = _executableNetwork->_plugin->_backend->create_tensor(
	            resultType,
	            resultShape,
	            InferenceEngine::as<InferenceEngine::MemoryBlob>(networkOutput)->wmap().as<void\*>());
	    }
	    _durations[Preprocess] = Time::now() - start;
	}

**Details:**

* ``InferImpl`` must call the :ref:`InferenceEngine::IInferRequestInternal::execDataPreprocessing <doxid-class_inference_engine_1_1_i_infer_request_internal_1a1ca532a389eb95c12ff9c8d463e93268>` function, which executes common Inference Engine preprocessing step (for example, applies resize or color conversion operations) if it is set by the user. The output dimensions, layout and precision matches the input information set via :ref:`InferenceEngine::CNNNetwork::getInputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1a76de2a6101fe8276f56b0dc0f99c7ff7>`.

* If ``inputBlob`` passed by user differs in terms of precisions from precision expected by plugin, ``blobCopy`` is performed which does actual precision conversion.

2.
++

Executes a pipeline synchronously using ``_executable`` object:

.. ref-code-block:: cpp

	void TemplateInferRequest::startPipeline() {
	    :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, _profilingTask[StartPipeline])
	    auto start = Time::now();
	    _executable->call(_outputTensors, _inputTensors);
	    _durations[StartPipeline] = Time::now() - start;
	}



3.
++

Converts output blobs if precisions of backend output blobs and blobs passed by user are different:

.. ref-code-block:: cpp

	void TemplateInferRequest::inferPostprocess() {
	    :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, _profilingTask[Postprocess]);
	    auto start = Time::now();
	    for (auto&& output : _networkOutputs) {
	        auto index = _executableNetwork->_outputIndex[output.first];
	        const auto& :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>` = _executableNetwork->_function->get_results()[index];
	        if (:ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`->get_output_partial_shape(0).is_dynamic()) {
	            // Touch blob to allocate it
	            GetBlob(output.first);
	        }
	        auto outputBlob = _outputs.at(output.first);
	        auto networkOutput = _networkOutputBlobs[output.first];
	        if (outputBlob->getTensorDesc().getPrecision() != networkOutput->getTensorDesc().getPrecision()) {
	            blobCopy(networkOutput, outputBlob);
	        } else if (:ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`->get_output_partial_shape(0).is_dynamic()) {
	            auto tensor = _outputTensors[_executableNetwork->_outputIndex.at(output.first)];
	            tensor->read(InferenceEngine::as<InferenceEngine::MemoryBlob>(outputBlob)->wmap().as<char\*>(),
	                         tensor->get_size_in_bytes());
	        }
	    }
	    _durations[Postprocess] = Time::now() - start;
	}



.. rubric::

The method sets performance counters which were measured during pipeline stages execution:

.. ref-code-block:: cpp

	std::map<std::string, InferenceEngineProfileInfo> TemplateInferRequest::GetPerformanceCounts() const {
	    std::map<std::string, InferenceEngineProfileInfo> perfMap;
	    InferenceEngineProfileInfo info;
	    info.execution_index = 0;
	    info.status = InferenceEngineProfileInfo::EXECUTED;
	
	    info.cpu_uSec = info.realTime_uSec = _durations[Preprocess].count();
	    perfMap["1. input preprocessing"] = info;
	    info.cpu_uSec = info.realTime_uSec = 0;
	    perfMap["2. input transfer to a device"] = info;
	    info.cpu_uSec = info.realTime_uSec = _durations[StartPipeline].count();
	    perfMap["3. execution time"] = info;
	    info.cpu_uSec = info.realTime_uSec = 0;
	    perfMap["4. output transfer from a device"] = info;
	    info.cpu_uSec = info.realTime_uSec = _durations[Postprocess].count();
	    perfMap["5. output postprocessing"] = info;
	    return perfMap;
	}

The next step in the plugin library implementation is the :ref:`Asynchronous Inference Request <doxid-openvino_docs_ie_plugin_dg_async_infer_request>` class.

