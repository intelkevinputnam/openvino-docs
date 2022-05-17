.. index:: pair: page; Executable Network
.. _doxid-openvino_docs_ie_plugin_dg_executable_network:


Executable Network
==================

:target:`doxid-openvino_docs_ie_plugin_dg_executable_network_1md_openvino_docs_ie_plugin_dg_executablenetwork` ``ExecutableNetwork`` class functionality:

* Compile an :ref:`InferenceEngine::ICNNNetwork <doxid-class_inference_engine_1_1_i_c_n_n_network>` instance to a backend specific graph representation

* Create an arbitrary number of ``InferRequest`` objects

* Hold some common resources shared between different instances of ``InferRequest``. For example:
  
  * InferenceEngine::IExecutableNetworkInternal::_taskExecutor task executor to implement asynchronous execution
  
  * InferenceEngine::IExecutableNetworkInternal::_callbackExecutor task executor to run an asynchronous inference request callback in a separate thread

Class
~~~~~

Inference Engine Plugin API provides the helper :ref:`InferenceEngine::ExecutableNetworkThreadSafeDefault <doxid-class_inference_engine_1_1_executable_network_thread_safe_default>` class recommended to use as a base class for an executable network. Based on that, a declaration of an executable network class can look as follows:

.. ref-code-block:: cpp

	class ExecutableNetwork : public :ref:`InferenceEngine::ExecutableNetworkThreadSafeDefault <doxid-class_inference_engine_1_1_executable_network_thread_safe_default>` {
	public:
	    ExecutableNetwork(const std::shared_ptr<const ngraph::Function>& function,
	                      const :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>`& inputInfoMap,
	                      const :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>`& outputsInfoMap,
	                      const Configuration& cfg,
	                      const std::shared_ptr<Plugin>& plugin);
	
	    ExecutableNetwork(std::istream& :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`, const Configuration& cfg, const std::shared_ptr<Plugin>& plugin);
	
	    // Methods from a base class ExecutableNetworkThreadSafeDefault
	
	    void :ref:`Export <doxid-class_inference_engine_1_1_i_executable_network_internal_1a057bca9b0f955c03190bdf77635e9516>`(std::ostream& :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`) override;
	    :ref:`InferenceEngine::IInferRequestInternal::Ptr <doxid-class_inference_engine_1_1_i_infer_request_internal_1a50c614e7a30e1e8ee58e984f210a1558>` :ref:`CreateInferRequestImpl <doxid-class_inference_engine_1_1_i_executable_network_internal_1a6763f64c0b14fd3ef3af645c9c21e9be>`(
	        :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>` networkInputs,
	        :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>` networkOutputs) override;
	    :ref:`InferenceEngine::IInferRequestInternal::Ptr <doxid-class_inference_engine_1_1_i_infer_request_internal_1a50c614e7a30e1e8ee58e984f210a1558>` :ref:`CreateInferRequestImpl <doxid-class_inference_engine_1_1_i_executable_network_internal_1a6763f64c0b14fd3ef3af645c9c21e9be>`(
	        const std::vector<std::shared_ptr<const ov::Node>>& inputs,
	        const std::vector<std::shared_ptr<const ov::Node>>& outputs) override;
	    :ref:`InferenceEngine::IInferRequestInternal::Ptr <doxid-class_inference_engine_1_1_i_infer_request_internal_1a50c614e7a30e1e8ee58e984f210a1558>` :ref:`CreateInferRequest <doxid-class_inference_engine_1_1_executable_network_thread_safe_default_1ab16d0cad93d2838b44acd261fd6ce367>`() override;
	    :ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` :ref:`GetMetric <doxid-class_inference_engine_1_1_i_executable_network_internal_1abff44a61825a0da77a4a329225431708>`(const std::string& name) const override;
	    :ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` :ref:`GetConfig <doxid-class_inference_engine_1_1_i_executable_network_internal_1aab6b3c29e3fec7400548b0af1808a772>`(const std::string& name) const override;
	
	private:
	    friend class TemplateInferRequest;
	    friend class Plugin;
	
	    void CompileNetwork(const std::shared_ptr<const ngraph::Function>& function,
	                        const :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>`& inputInfoMap,
	                        const :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>`& outputsInfoMap);
	    void InitExecutor();
	
	    std::atomic<std::size_t> _requestId = {0};
	    Configuration _cfg;
	    std::shared_ptr<Plugin> :ref:`_plugin <doxid-class_inference_engine_1_1_i_executable_network_internal_1ab5afe5b65a69d13f1200e1662aed632a>`;
	    std::shared_ptr<ngraph::Function> _function;
	    std::map<std::string, std::size_t> _inputIndex;
	    std::map<std::string, std::size_t> _outputIndex;
	};



Class Fields
++++++++++++

The example class has several fields:

* ``_requestId`` - Tracks a number of created inference requests, which is used to distinguish different inference requests during profiling via the Intel® Instrumentation and Tracing Technology (ITT) library.

* ``_cfg`` - Defines a configuration an executable network was compiled with.

* ``_plugin`` - Refers to a plugin instance.

* ``_function`` - Keeps a reference to transformed ``:ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>``` which is used in ngraph reference backend computations. Note, in case of other backends with backend specific graph representation ``_function`` has different type and represents backend specific graph or just a set of computational kernels to perform an inference.

* ``_inputIndex`` - maps a name of input with its index among all network inputs.

* ``_outputIndex`` - maps a name of output with its index among all network outputs.

Constructor with
----------------

This constructor accepts a generic representation of a neural network as an :ref:`InferenceEngine::ICNNNetwork <doxid-class_inference_engine_1_1_i_c_n_n_network>` reference and is compiled into a backend specific device graph:

.. ref-code-block:: cpp

	TemplatePlugin::ExecutableNetwork::ExecutableNetwork(const std::shared_ptr<const ngraph::Function>& function,
	                                                     const :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>`& inputInfoMap,
	                                                     const :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>`& outputsInfoMap,
	                                                     const Configuration& cfg,
	                                                     const Plugin::Ptr& plugin)
	    : :ref:`InferenceEngine <doxid-namespace_inference_engine>`::ExecutableNetworkThreadSafeDefault(nullptr, nullptr),  // Disable default threads creation
	      _cfg(cfg),
	      _plugin(plugin) {
	    // TODO: if your plugin supports device ID (more that single instance of device can be on host machine)
	    // you should select proper device based on KEY_DEVICE_ID or automatic behavior
	    // In this case, _waitExecutor should also be created per device.
	    try {
	        CompileNetwork(function, inputInfoMap, outputsInfoMap);
	        InitExecutor();  // creates thread-based executor using for async requests
	    } catch (const :ref:`InferenceEngine::Exception <doxid-struct_inference_engine_1_1_exception>`&) {
	        throw;
	    } catch (const std::exception& e) {
	        :ref:`IE_THROW <doxid-ie__common_8h_1a643ef2aa5e1c6b7523e55cc4396e3e02>`(Unexpected) << "Standard exception from compilation library: " << e.what();
	    } catch (...) {
	        :ref:`IE_THROW <doxid-ie__common_8h_1a643ef2aa5e1c6b7523e55cc4396e3e02>`(Unexpected) << "Generic exception is thrown";
	    }
	}

The implementation ``CompileNetwork`` is fully device-specific.

.. rubric::

The function accepts a const shared pointer to ``:ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>``` object and performs the following steps:

#. Applies nGraph passes using ``TransformNetwork`` function, which defines plugin-specific conversion pipeline. To support low precision inference, the pipeline can include Low Precision Transformations. These transformations are usually hardware specific. You can find how to use and configure Low Precisions Transformations in :ref:`Low Precision Transformations <doxid-openvino_docs__o_v__u_g_lpt>` guide.

#. Maps the transformed graph to a backend specific graph representation (for example, to CPU plugin internal graph representation).

#. Allocates and fills memory for graph weights, backend specific memory handles and so on.

.. ref-code-block:: cpp

	// forward declaration
	std::shared_ptr<ngraph::Function> TransformNetwork(const std::shared_ptr<const ngraph::Function>& function,
	                                                   const :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>`& inputInfoMap,
	                                                   const :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>`& outputsInfoMap);
	
	void TemplatePlugin::ExecutableNetwork::CompileNetwork(const std::shared_ptr<const ngraph::Function>& function,
	                                                       const :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>`& inputInfoMap,
	                                                       const :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>`& outputsInfoMap) {
	    // TODO: perform actual graph compilation / mapping to backend graph representation / kernels
	
	    // apply plugins transformations
	    _function = TransformNetwork(function, inputInfoMap, outputsInfoMap);
	
	    // Generate backend specific blob mappings. For example Inference Engine uses not ngraph::Result nodes friendly name
	    // as inference request output names but the name of the layer before.
	    size_t idx = 0;
	    for (auto&& :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>` : _function->get_results()) {
	        const auto& input = :ref:`result <doxid-namespacengraph_1_1runtime_1_1reference_1a9f63c4359f72e8f64b3d6ff4883447f0>`->input_value(0);
	        auto name = :ref:`ngraph::op::util::get_ie_output_name <doxid-namespacengraph_1_1op_1_1util_1af293e8c9af929d11cc5f9e05fdc218da>`(input);
	        if (_outputIndex.emplace(name, idx).second)
	            idx++;
	    }
	    for (auto&& parameter : _function->get_parameters()) {
	        _inputIndex.emplace(parameter->get_friendly_name(), _function->get_parameter_index(parameter));
	    }
	
	    // Perform any other steps like allocation and filling backend specific memory handles and so on
	}



.. note:: After all these steps, the backend specific graph is ready to create inference requests and perform inference.

Constructor Importing from Stream
---------------------------------

This constructor creates a backend specific graph by importing from a stream object:

.. note:: The export of backend specific graph is done in the ``Export`` method, and data formats must be the same for both import and export.

.. ref-code-block:: cpp

	TemplatePlugin::ExecutableNetwork::ExecutableNetwork(std::istream& :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`,
	                                                     const Configuration& cfg,
	                                                     const Plugin::Ptr& plugin)
	    : _cfg(cfg),
	      _plugin(plugin) {
	    // read XML content
	    std::string xmlString;
	    std::uint64_t dataSize = 0;
	    :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`.read(reinterpret_cast<char\*>(&dataSize), sizeof(dataSize));
	    xmlString.resize(dataSize);
	    :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`.read(const_cast<char\*>(xmlString.c_str()), dataSize);
	
	    // read blob content
	    :ref:`InferenceEngine::Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` dataBlob;
	    :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`.read(reinterpret_cast<char\*>(&dataSize), sizeof(dataSize));
	    if (0 != dataSize) {
	        dataBlob = InferenceEngine::make_shared_blob<std::uint8_t>(
	            :ref:`InferenceEngine::TensorDesc <doxid-class_inference_engine_1_1_tensor_desc>`(:ref:`InferenceEngine::Precision::U8 <doxid-class_inference_engine_1_1_precision_1ade75bd7073b4aa966c0dda4025bcd0f5a046eaf31a4345f526ed54271c9fcd39c>`,
	                                        {static_cast<std::size_t>(dataSize)},
	                                        :ref:`InferenceEngine::Layout::C <doxid-ie__preprocess__gapi_8cpp_1a5464533d23b59ba11030432e73528730>`));
	        dataBlob->allocate();
	        :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`.read(dataBlob->buffer(), dataSize);
	    }
	
	    auto cnnnetwork = _plugin->GetCore()->ReadNetwork(xmlString, std::move(dataBlob));
	
	    // TODO: implement Import / Export of configuration options and merge with `cfg`
	    // TODO: implement Import / Export of network precisions, layouts, preprocessing info
	    :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>` inputInfoMap = cnnnetwork.getInputsInfo();
	    :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>` outputInfoMap = cnnnetwork.getOutputsInfo();
	
	    setNetworkInputs(inputInfoMap);
	    setNetworkOutputs(outputInfoMap);
	    SetPointerToPlugin(_plugin->shared_from_this());
	
	    try {
	        // TODO: remove compilation, network is already compiled and serialized in compiled form
	        CompileNetwork(cnnnetwork.getFunction(), inputInfoMap, outputInfoMap);
	        InitExecutor();  // creates thread-based executor using for async requests
	    } catch (const :ref:`InferenceEngine::Exception <doxid-struct_inference_engine_1_1_exception>`&) {
	        throw;
	    } catch (const std::exception& e) {
	        :ref:`IE_THROW <doxid-ie__common_8h_1a643ef2aa5e1c6b7523e55cc4396e3e02>`(Unexpected) << "Standard exception from compilation library: " << e.what();
	    } catch (...) {
	        :ref:`IE_THROW <doxid-ie__common_8h_1a643ef2aa5e1c6b7523e55cc4396e3e02>`(Unexpected) << "Generic exception is thrown";
	    }
	}



.. rubric::

The implementation of the method should write all data to the ``model`` stream, which is required to import a backend specific graph later in the ``Plugin::Import`` method:

.. ref-code-block:: cpp

	void TemplatePlugin::ExecutableNetwork::Export(std::ostream& modelStream) {
	    :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, "ExecutableNetwork::Export");
	
	    // Note: custom ngraph extensions are not supported
	    std::map<std::string, ngraph::OpSet> custom_opsets;
	    std::stringstream xmlFile, binFile;
	    :ref:`OPENVINO_SUPPRESS_DEPRECATED_START <doxid-openvino_2core_2deprecated_8hpp_1a80720d314461cf6f3098efd1719f54c5>`
	    :ref:`ov::pass::Serialize <doxid-classov_1_1pass_1_1_serialize>` serializer(xmlFile, binFile, custom_opsets);
	    :ref:`OPENVINO_SUPPRESS_DEPRECATED_END <doxid-openvino_2core_2deprecated_8hpp_1ac8c3082fae0849f6d58b442d540b5767>`
	    serializer.run_on_model(_function);
	
	    auto m_constants = binFile.str();
	    auto m_model = xmlFile.str();
	
	    auto dataSize = static_cast<std::uint64_t>(m_model.size());
	    modelStream.write(reinterpret_cast<char\*>(&dataSize), sizeof(dataSize));
	    modelStream.write(m_model.c_str(), dataSize);
	
	    dataSize = static_cast<std::uint64_t>(m_constants.size());
	    modelStream.write(reinterpret_cast<char\*>(&dataSize), sizeof(dataSize));
	    modelStream.write(reinterpret_cast<char\*>(&m_constants[0]), dataSize);
	
	    // TODO: implement network precision, layout, preprocessing info serialization
	}



.. rubric::

The method creates an asynchronous inference request and returns it. While the public Inference Engine API has a single interface for inference request, which can be executed in synchronous and asynchronous modes, a plugin library implementation has two separate classes:

* :ref:`Synchronous inference request <doxid-openvino_docs_ie_plugin_dg_infer_request>`, which defines pipeline stages and runs them synchronously in the ``Infer`` method.

* :ref:`Asynchronous inference request <doxid-openvino_docs_ie_plugin_dg_async_infer_request>`, which is a wrapper for a synchronous inference request and can run a pipeline asynchronously. Depending on a device pipeline structure, it can has one or several stages:
  
  * For single-stage pipelines, there is no need to define this method and create a class derived from :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default>`. For single stage pipelines, a default implementation of this method creates :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default>` wrapping a synchronous inference request and runs it asynchronously in the ``_taskExecutor`` executor.
  
  * For pipelines with multiple stages, such as performing some preprocessing on host, uploading input data to a device, running inference on a device, or downloading and postprocessing output data, schedule stages on several task executors to achieve better device use and performance. You can do it by creating a sufficient number of inference requests running in parallel. In this case, device stages of different inference requests are overlapped with preprocessing and postprocessing stage giving better performance.
    
    .. warning:: It is up to you to decide how many task executors you need to optimally execute a device pipeline.

.. ref-code-block:: cpp

	:ref:`InferenceEngine::IInferRequestInternal::Ptr <doxid-class_inference_engine_1_1_i_infer_request_internal_1a50c614e7a30e1e8ee58e984f210a1558>` TemplatePlugin::ExecutableNetwork::CreateInferRequest() {
	    :ref:`InferenceEngine::IInferRequestInternal::Ptr <doxid-class_inference_engine_1_1_i_infer_request_internal_1a50c614e7a30e1e8ee58e984f210a1558>` internalRequest;
	    if (this->_plugin) {
	        const auto& core = _plugin->GetCore();
	        if (core && core->isNewAPI())
	            internalRequest = CreateInferRequestImpl(_parameters, _results);
	    }
	    if (!internalRequest)
	        internalRequest = CreateInferRequestImpl(_networkInputs, _networkOutputs);
	    return std::make_shared<TemplateAsyncInferRequest>(std::static_pointer_cast<TemplateInferRequest>(internalRequest),
	                                                       _taskExecutor,
	                                                       _plugin->_waitExecutor,
	                                                       _callbackExecutor);
	}



.. rubric::

This is a helper method used by ``CreateInferRequest`` to create a :ref:`synchronous inference request <doxid-openvino_docs_ie_plugin_dg_infer_request>`, which is later wrapped with the asynchronous inference request class:

.. ref-code-block:: cpp

	:ref:`InferenceEngine::IInferRequestInternal::Ptr <doxid-class_inference_engine_1_1_i_infer_request_internal_1a50c614e7a30e1e8ee58e984f210a1558>` TemplatePlugin::ExecutableNetwork::CreateInferRequestImpl(
	    :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>` networkInputs,
	    :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>` networkOutputs) {
	    return std::make_shared<TemplateInferRequest>(networkInputs,
	                                                  networkOutputs,
	                                                  std::static_pointer_cast<ExecutableNetwork>(shared_from_this()));
	}
	
	:ref:`InferenceEngine::IInferRequestInternal::Ptr <doxid-class_inference_engine_1_1_i_infer_request_internal_1a50c614e7a30e1e8ee58e984f210a1558>` TemplatePlugin::ExecutableNetwork::CreateInferRequestImpl(
	    const std::vector<std::shared_ptr<const ov::Node>>& inputs,
	    const std::vector<std::shared_ptr<const ov::Node>>& outputs) {
	    return std::make_shared<TemplateInferRequest>(inputs,
	                                                  outputs,
	                                                  std::static_pointer_cast<ExecutableNetwork>(shared_from_this()));
	}



.. rubric::

Returns a metric value for a metric with the name ``name``. A metric is a static type of information about an executable network. Examples of metrics:

* :ref:`EXEC_NETWORK_METRIC_KEY(NETWORK_NAME) <doxid-ie__plugin__config_8hpp_1adb48efa632ae9bacfa86b8a3a0d9541e>` - name of an executable network

* :ref:`EXEC_NETWORK_METRIC_KEY(OPTIMAL_NUMBER_OF_INFER_REQUESTS) <doxid-ie__plugin__config_8hpp_1adb48efa632ae9bacfa86b8a3a0d9541e>` - heuristic to denote an optimal (or at least sub-optimal) number of inference requests needed to run asynchronously to use the current device fully

* Any other executable network metric specific for a particular device. Such metrics and possible values must be declared in a plugin configuration public header, for example, ``template/template_config.hpp``

.. ref-code-block:: cpp

	:ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` TemplatePlugin::ExecutableNetwork::GetMetric(const std::string& name) const {
	    // TODO: return more supported values for metrics
	    if (:ref:`EXEC_NETWORK_METRIC_KEY <doxid-ie__plugin__config_8hpp_1adb48efa632ae9bacfa86b8a3a0d9541e>`(SUPPORTED_METRICS) == name) {
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(SUPPORTED_METRICS,
	                             std::vector<std::string>{:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(NETWORK_NAME),
	                                                      :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(SUPPORTED_METRICS),
	                                                      :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(SUPPORTED_CONFIG_KEYS),
	                                                      :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(OPTIMAL_NUMBER_OF_INFER_REQUESTS)});
	    } else if (:ref:`EXEC_NETWORK_METRIC_KEY <doxid-ie__plugin__config_8hpp_1adb48efa632ae9bacfa86b8a3a0d9541e>`(SUPPORTED_CONFIG_KEYS) == name) {
	        std::vector<std::string> configKeys = {:ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(DEVICE_ID),
	                                               :ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(PERF_COUNT),
	                                               TEMPLATE_CONFIG_KEY(THROUGHPUT_STREAMS)};
	        auto streamExecutorConfigKeys = :ref:`InferenceEngine::IStreamsExecutor::Config <doxid-struct_inference_engine_1_1_i_streams_executor_1_1_config>`{}.:ref:`SupportedKeys <doxid-struct_inference_engine_1_1_i_streams_executor_1_1_config_1af5194c42f86951299ba6a9ef334627ef>`();
	        for (auto&& configKey : streamExecutorConfigKeys) {
	            configKeys.emplace_back(configKey);
	        }
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(SUPPORTED_CONFIG_KEYS, configKeys);
	    } else if (:ref:`EXEC_NETWORK_METRIC_KEY <doxid-ie__plugin__config_8hpp_1adb48efa632ae9bacfa86b8a3a0d9541e>`(NETWORK_NAME) == name) {
	        auto networkName = _function->get_friendly_name();
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(NETWORK_NAME, networkName);
	    } else if (:ref:`EXEC_NETWORK_METRIC_KEY <doxid-ie__plugin__config_8hpp_1adb48efa632ae9bacfa86b8a3a0d9541e>`(OPTIMAL_NUMBER_OF_INFER_REQUESTS) == name) {
	        unsigned int value = _cfg._streamsExecutorConfig._streams;
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(OPTIMAL_NUMBER_OF_INFER_REQUESTS, value);
	    } else {
	        :ref:`IE_THROW <doxid-ie__common_8h_1a643ef2aa5e1c6b7523e55cc4396e3e02>`() << "Unsupported ExecutableNetwork metric: " << name;
	    }
	}

The IE_SET_METRIC_RETURN helper macro sets metric value and checks that the actual metric type matches a type of the specified value.

.. rubric::

Returns a current value for a configuration key with the name ``name``. The method extracts configuration values an executable network is compiled with.

.. ref-code-block:: cpp

	:ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` TemplatePlugin::ExecutableNetwork::GetConfig(const std::string& name) const {
	    return _cfg.Get(name);
	}

This function is the only way to get configuration values when a network is imported and compiled by other developers and tools (for example, the `Compile tool <../_inference_engine_tools_compile_tool_README.html>`__).

The next step in plugin library implementation is the :ref:`Synchronous Inference Request <doxid-openvino_docs_ie_plugin_dg_infer_request>` class.

