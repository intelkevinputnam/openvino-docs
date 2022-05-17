.. index:: pair: page; Plugin
.. _doxid-openvino_docs_ie_plugin_dg_plugin:


Plugin
======

:target:`doxid-openvino_docs_ie_plugin_dg_plugin_1md_openvino_docs_ie_plugin_dg_plugin` Inference Engine Plugin usually represents a wrapper around a backend. Backends can be:

* OpenCL-like backend (e.g. clDNN library) for GPU devices.

* oneDNN backend for Intel CPU devices.

* NVIDIA cuDNN for NVIDIA GPUs.

The responsibility of Inference Engine Plugin:

* Initializes a backend and throw exception in ``Engine`` constructor if backend cannot be initialized.

* Provides information about devices enabled by a particular backend, e.g. how many devices, their properties and so on.

* Loads or imports :ref:`executable network <doxid-openvino_docs_ie_plugin_dg_executable_network>` objects.

In addition to the Inference Engine Public API, the Inference Engine provides the Plugin API, which is a set of functions and helper classes that simplify new plugin development:

* header files in the ``inference_engine/src/plugin_api`` directory

* implementations in the ``inference_engine/src/inference_engine`` directory

* symbols in the Inference Engine Core shared library

To build an Inference Engine plugin with the Plugin API, see the :ref:`Inference Engine Plugin Building <doxid-openvino_docs_ie_plugin_dg_plugin_build>` guide.

Plugin Class
~~~~~~~~~~~~

Inference Engine Plugin API provides the helper :ref:`InferenceEngine::IInferencePlugin <doxid-class_inference_engine_1_1_i_inference_plugin>` class recommended to use as a base class for a plugin. Based on that, declaration of a plugin class can look as follows:

.. ref-code-block:: cpp

	namespace TemplatePlugin {
	
	class Plugin : public :ref:`InferenceEngine::IInferencePlugin <doxid-class_inference_engine_1_1_i_inference_plugin>` {
	public:
	    using Ptr = std::shared_ptr<Plugin>;
	
	    Plugin();
	    ~Plugin();
	
	    void SetConfig(const std::map<std::string, std::string>& config) override;
	    :ref:`InferenceEngine::QueryNetworkResult <doxid-struct_inference_engine_1_1_query_network_result>` QueryNetwork(const :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>`& network,
	                                                     const std::map<std::string, std::string>& config) const override;
	    :ref:`InferenceEngine::IExecutableNetworkInternal::Ptr <doxid-class_inference_engine_1_1_i_executable_network_internal_1a264e3e04130a2e44d0b257ae63c9feae>` LoadExeNetworkImpl(
	        const :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>`& network,
	        const std::map<std::string, std::string>& config) override;
	    void AddExtension(const std::shared_ptr<InferenceEngine::IExtension>& extension) override;
	    :ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` GetConfig(
	        const std::string& name,
	        const std::map<std::string, InferenceEngine::Parameter>& options) const override;
	    :ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` GetMetric(
	        const std::string& name,
	        const std::map<std::string, InferenceEngine::Parameter>& options) const override;
	    :ref:`InferenceEngine::IExecutableNetworkInternal::Ptr <doxid-class_inference_engine_1_1_i_executable_network_internal_1a264e3e04130a2e44d0b257ae63c9feae>` ImportNetwork(
	        std::istream& :ref:`model <doxid-group__ov__runtime__cpp__prop__api_1ga461856fdfb6d7533dc53355aec9e9fad>`,
	        const std::map<std::string, std::string>& config) override;
	
	private:
	    friend class ExecutableNetwork;
	    friend class TemplateInferRequest;
	
	    std::shared_ptr<ngraph::runtime::Backend> _backend;
	    Configuration _cfg;
	    :ref:`InferenceEngine::ITaskExecutor::Ptr <doxid-class_inference_engine_1_1_i_task_executor_1a8ba60f739a36331eb8ed3492ffc55eb5>` _waitExecutor;
	};
	
	}  // namespace TemplatePlugin



Class Fields
++++++++++++

The provided plugin class also has several fields:

* ``_backend`` - a backend engine that is used to perform actual computations for network inference. For ``Template`` plugin ``ngraph::runtime::Backend`` is used which performs computations using OpenVINO™ reference implementations.

* ``_waitExecutor`` - a task executor that waits for a response from a device about device tasks completion.

* ``_cfg`` of type ``Configuration`` :

.. ref-code-block:: cpp

	using ConfigMap = std::map<std::string, std::string>;
	
	struct Configuration {
	    Configuration();
	    Configuration(const Configuration&) = default;
	    Configuration(Configuration&&) = default;
	    Configuration& operator=(const Configuration&) = default;
	    Configuration& operator=(Configuration&&) = default;
	
	    explicit Configuration(const ConfigMap& config,
	                           const Configuration& defaultCfg = {},
	                           const bool throwOnUnsupported = true);
	
	    :ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` Get(const std::string& name) const;
	
	    // Plugin configuration parameters
	
	    int deviceId = 0;
	    bool perfCount = true;
	    :ref:`InferenceEngine::IStreamsExecutor::Config <doxid-struct_inference_engine_1_1_i_streams_executor_1_1_config>` _streamsExecutorConfig;
	    :ref:`ov::hint::PerformanceMode <doxid-group__ov__runtime__cpp__prop__api_1ga032aa530efa40760b79af14913d48d73>` :ref:`performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>` = ov::hint::PerformanceMode::UNDEFINED;
	};

As an example, a plugin configuration has three value parameters:

* ``deviceId`` - particular device ID to work with. Applicable if a plugin supports more than one ``Template`` device. In this case, some plugin methods, like ``SetConfig``, ``QueryNetwork``, and ``LoadNetwork``, must support the :ref:`CONFIG_KEY(KEY_DEVICE_ID) <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>` parameter.

* ``perfCounts`` - boolean value to identify whether to collect performance counters during :ref:`Inference Request <doxid-openvino_docs_ie_plugin_dg_infer_request>` execution.

* ``_streamsExecutorConfig`` - configuration of ``:ref:`InferenceEngine::IStreamsExecutor <doxid-class_inference_engine_1_1_i_streams_executor>``` to handle settings of multi-threaded context.

Engine Constructor
------------------

A plugin constructor must contain code that checks the ability to work with a device of the ``Template`` type. For example, if some drivers are required, the code must check driver availability. If a driver is not available (for example, OpenCL runtime is not installed in case of a GPU device or there is an improper version of a driver is on a host machine), an exception must be thrown from a plugin constructor.

A plugin must define a device name enabled via the ``_pluginName`` field of a base class:

.. ref-code-block:: cpp

	Plugin::Plugin() {
	    // TODO: fill with actual device name, backend engine
	    _pluginName = "TEMPLATE";
	
	    // create ngraph backend which performs inference using ngraph reference implementations
	    _backend = ngraph::runtime::Backend::create();
	
	    // create default stream executor with a given name
	    _waitExecutor = :ref:`executorManager <doxid-namespace_inference_engine_1adf3c09213f17002e0abafbf7377aec5c>`()->getIdleCPUStreamsExecutor({"TemplateWaitExecutor"});
	}



.. rubric::

**Implementation details:** The base :ref:`InferenceEngine::IInferencePlugin <doxid-class_inference_engine_1_1_i_inference_plugin>` class provides a common implementation of the public :ref:`InferenceEngine::IInferencePlugin::LoadNetwork <doxid-class_inference_engine_1_1_i_inference_plugin_1a07baadb21491baef977c424e59ec466b>` method that calls plugin-specific ``LoadExeNetworkImpl``, which is defined in a derived class.

This is the most important function of the ``Plugin`` class and creates an instance of compiled ``ExecutableNetwork``, which holds a backend-dependent compiled graph in an internal representation:

.. ref-code-block:: cpp

	:ref:`InferenceEngine::IExecutableNetworkInternal::Ptr <doxid-class_inference_engine_1_1_i_executable_network_internal_1a264e3e04130a2e44d0b257ae63c9feae>` Plugin::LoadExeNetworkImpl(const :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>`& network,
	                                                                            const ConfigMap& config) {
	    :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, "Plugin::LoadExeNetworkImpl");
	
	    :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>` networkInputs = network.:ref:`getInputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1a76de2a6101fe8276f56b0dc0f99c7ff7>`();
	    :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>` networkOutputs = network.:ref:`getOutputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1af8a6200f549b15a895e2cfefd304a9c2>`();
	
	    auto fullConfig = Configuration{config, _cfg};
	    return std::make_shared<ExecutableNetwork>(network.:ref:`getFunction <doxid-class_inference_engine_1_1_c_n_n_network_1a7246c6936dfc1ebfa2c776e97972f539>`(),
	                                               networkInputs,
	                                               networkOutputs,
	                                               fullConfig,
	                                               std::static_pointer_cast<Plugin>(shared_from_this()));
	}

Before a creation of an ``ExecutableNetwork`` instance via a constructor, a plugin may check if a provided :ref:`InferenceEngine::ICNNNetwork <doxid-class_inference_engine_1_1_i_c_n_n_network>` object is supported by a device. In the example above, the plugin checks precision information.

The very important part before creation of ``ExecutableNetwork`` instance is to call ``TransformNetwork`` method which applies OpenVINO™ transformation passes.

Actual graph compilation is done in the ``ExecutableNetwork`` constructor. Refer to the :ref:`ExecutableNetwork Implementation Guide <doxid-openvino_docs_ie_plugin_dg_executable_network>` for details.

.. note:: Actual configuration map used in ``ExecutableNetwork`` is constructed as a base plugin configuration set via ``Plugin::SetConfig``, where some values are overwritten with ``config`` passed to ``Plugin::LoadExeNetworkImpl``. Therefore, the config of ``Plugin::LoadExeNetworkImpl`` has a higher priority.

.. rubric::

The function accepts a const shared pointer to ``:ref:`ov::Model <doxid-classov_1_1_model>``` object and performs the following steps:

#. Deep copies a const object to a local object, which can later be modified.

#. Applies common and plugin-specific transformations on a copied graph to make the graph more friendly to hardware operations. For details how to write custom plugin-specific transformation, please, refer to :ref:`Writing OpenVINO™ transformations <doxid-openvino_docs_transformations>` guide. See detailed topics about network representation:
   
   * `Intermediate Representation and Operation Sets <../_docs_MO_DG_IR_and_opsets.html>`__
   
   * :ref:`Quantized networks <doxid-openvino_docs_ie_plugin_dg_quantized_networks>`.

.. ref-code-block:: cpp

	
	std::shared_ptr<ngraph::Function> TransformNetwork(const std::shared_ptr<const ngraph::Function>& function,
	                                                   const :ref:`InferenceEngine::InputsDataMap <doxid-namespace_inference_engine_1a08270747275eb79985154365aa782a2a>`& inputInfoMap,
	                                                   const :ref:`InferenceEngine::OutputsDataMap <doxid-namespace_inference_engine_1a76ce999f68455cf962a473718deb500c>`& outputsInfoMap) {
	    // 1. Copy ngraph::Function first to apply some transformations which modify original ngraph::Function
	    auto transformedNetwork = :ref:`ngraph::clone_function <doxid-namespacengraph_1a5f75e639342db986514594f167340d69>`(\*function);
	
	    // 2. Perform common optimizations and device-specific transformations
	    :ref:`ngraph::pass::Manager <doxid-classov_1_1pass_1_1_manager>` passManager;
	    // Example: register transformation to convert preprocessing information to graph nodes
	    passManager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<ngraph::pass::AddPreprocessing>(inputInfoMap);
	    // TODO: add post-processing based on outputsInfoMap
	    // Example: register CommonOptimizations transformation from transformations library
	    passManager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<:ref:`ngraph::pass::CommonOptimizations <doxid-classngraph_1_1pass_1_1_common_optimizations>`>();
	    // G-API supports only FP32 networks for pre-processing
	    bool needF16toF32 = false;
	    for (const auto& param : :ref:`function <doxid-namespacengraph_1_1runtime_1_1reference_1a4bbb4f04db61c605971a3eb4c1553b6e>`->get_parameters()) {
	        if (param->get_element_type() == :ref:`ngraph::element::f16 <doxid-group__ov__element__cpp__api_1ga2a30b8bad0c8cb5c76a4947c9d5074d1>` &&
	            inputInfoMap.at(param->get_friendly_name())->getTensorDesc().getPrecision() !=
	                :ref:`InferenceEngine::Precision::FP16 <doxid-class_inference_engine_1_1_precision_1ade75bd7073b4aa966c0dda4025bcd0f5a084e737560206865337ee681e1ab3f5a>`) {
	            needF16toF32 = true;
	            break;
	        }
	    }
	    if (needF16toF32) {
	        passManager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<:ref:`ngraph::pass::ConvertPrecision <doxid-classngraph_1_1pass_1_1_convert_precision>`>(
	            :ref:`precisions_array <doxid-convert__precision_8hpp_1a4a87a7ac5af13aa6efaf3f00dadea5e1>`{{:ref:`ngraph::element::f16 <doxid-group__ov__element__cpp__api_1ga2a30b8bad0c8cb5c76a4947c9d5074d1>`, :ref:`ngraph::element::f32 <doxid-group__ov__element__cpp__api_1gadc8a5dda3244028a5c0b024897215d43>`}});
	    }
	    // Example: register plugin specific transformation
	    passManager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<ov::pass::DecomposeDivideMatcher>();
	    passManager.:ref:`register_pass <doxid-classov_1_1pass_1_1_manager_1affc722b2463a786b66398472141d45f2>`<ov::pass::ReluReluFusionMatcher>();
	    // Register any other transformations
	    // ..
	
	    // After `run_passes`, we have the transformed function, where operations match device operations,
	    // and we can create device backend-dependent graph
	    passManager.:ref:`run_passes <doxid-classov_1_1pass_1_1_manager_1a8b155191130f2c15e294cfd259d4ca0d>`(transformedNetwork);
	
	    return transformedNetwork;
	}



.. note:: After all these transformations, a ``:ref:`ov::Model <doxid-classov_1_1_model>``` object contains operations which can be perfectly mapped to backend kernels. E.g. if backend has kernel computing ``A + B`` operations at once, the ``TransformNetwork`` function should contain a pass which fuses operations ``A`` and ``B`` into a single custom operation ``A + B`` which fits backend kernels set.

.. rubric::

Use the method with the ``HETERO`` mode, which allows to distribute network execution between different devices based on the ``:ref:`ov::Node::get_rt_info() <doxid-classov_1_1_node_1a5c73794fbc47e510198261d61682fe79>``` map, which can contain the ``"affinity"`` key. The ``QueryNetwork`` method analyzes operations of provided ``network`` and returns a list of supported operations via the :ref:`InferenceEngine::QueryNetworkResult <doxid-struct_inference_engine_1_1_query_network_result>` structure. The ``QueryNetwork`` firstly applies ``TransformNetwork`` passes to input ``:ref:`ov::Model <doxid-classov_1_1_model>``` argument. After this, the transformed network in ideal case contains only operations are 1:1 mapped to kernels in computational backend. In this case, it's very easy to analyze which operations is supposed (``_backend`` has a kernel for such operation or extensions for the operation is provided) and not supported (kernel is missed in ``_backend``):

#. Store original names of all operations in input ``:ref:`ov::Model <doxid-classov_1_1_model>```

#. Apply ``TransformNetwork`` passes. Note, the names of operations in a transformed network can be different and we need to restore the mapping in the steps below.

#. Construct ``supported`` and ``unsupported`` maps which contains names of original operations. Note, that since the inference is performed using OpenVINO™ reference backend, the decision whether the operation is supported or not depends on whether the latest OpenVINO opset contains such operation.

#. ``QueryNetworkResult.supportedLayersMap`` contains only operations which are fully supported by ``_backend``.

.. ref-code-block:: cpp

	:ref:`InferenceEngine::QueryNetworkResult <doxid-struct_inference_engine_1_1_query_network_result>` Plugin::QueryNetwork(const :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>`& network,
	                                                         const ConfigMap& config) const {
	    :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, "Plugin::QueryNetwork");
	
	    Configuration fullConfig{config, _cfg, false};
	    auto function = network.:ref:`getFunction <doxid-class_inference_engine_1_1_c_n_n_network_1a7246c6936dfc1ebfa2c776e97972f539>`();
	
	    // 1. First of all we should store initial input operation set
	    std::unordered_set<std::string> originalOps;
	    std::map<std::string, ngraph::NodeTypeInfo> friendlyNameToType;
	    for (auto&& node : :ref:`function <doxid-namespacengraph_1_1runtime_1_1reference_1a4bbb4f04db61c605971a3eb4c1553b6e>`->get_ops()) {
	        originalOps.emplace(node->get_friendly_name());
	        friendlyNameToType[node->get_friendly_name()] = node->get_type_info();
	    }
	
	    // 2. It is needed to apply all transformations as it is done in LoadExeNetworkImpl
	    auto transformedFunction = TransformNetwork(function, network.:ref:`getInputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1a76de2a6101fe8276f56b0dc0f99c7ff7>`(), network.:ref:`getOutputsInfo <doxid-class_inference_engine_1_1_c_n_n_network_1af8a6200f549b15a895e2cfefd304a9c2>`());
	
	    // 3. The same input node can be transformed into supported and unsupported backend node
	    // So we need store as supported either unsupported node sets
	    std::unordered_set<std::string> supported;
	    std::unordered_set<std::string> unsupported;
	    :ref:`ngraph::OpSet <doxid-classngraph_1_1_op_set>` op_super_set;
	#define _OPENVINO_OP_REG(NAME, NAMESPACE) op_super_set.insert<NAMESPACE::NAME>();
	#include "openvino/opsets/opset1_tbl.hpp"
	#include "openvino/opsets/opset2_tbl.hpp"
	#include "openvino/opsets/opset3_tbl.hpp"
	#include "openvino/opsets/opset4_tbl.hpp"
	#include "openvino/opsets/opset5_tbl.hpp"
	#include "openvino/opsets/opset6_tbl.hpp"
	#include "openvino/opsets/opset7_tbl.hpp"
	#include "openvino/opsets/opset8_tbl.hpp"
	#undef _OPENVINO_OP_REG
	    for (auto&& node : transformedFunction->get_ops()) {
	        // Extract transformation history from transformed node as list of nodes
	        for (auto&& fusedLayerName : :ref:`ngraph::getFusedNamesVector <doxid-group__ie__runtime__attr__api_1ga927345dceac1f145e05e7b7af4600946>`(node)) {
	            // Filter just nodes from original operation set
	            // TODO: fill with actual decision rules based on whether kernel is supported by backend
	            if (:ref:`InferenceEngine::details::contains <doxid-namespaceov_1_1util_1aa63ec0c8f3eb1d9ca97ca24f11d6cd9a>`(originalOps, fusedLayerName)) {
	                if (op_super_set.:ref:`contains_type <doxid-classov_1_1_op_set_1a4d266ed2b9ec6f8857cd762189571f89>`(friendlyNameToType[fusedLayerName])) {
	                    supported.emplace(fusedLayerName);
	                } else {
	                    unsupported.emplace(fusedLayerName);
	                }
	            }
	        }
	    }
	
	    // 4. The result set should contain just nodes from supported set
	    for (auto&& unsupportedNode : unsupported) {
	        supported.erase(unsupportedNode);
	    }
	
	    for (auto&& node : :ref:`function <doxid-namespacengraph_1_1runtime_1_1reference_1a4bbb4f04db61c605971a3eb4c1553b6e>`->get_ops()) {
	        // 5. If some housekeeping nodes were not added - add them.
	        if (:ref:`InferenceEngine::details::contains <doxid-namespaceov_1_1util_1aa63ec0c8f3eb1d9ca97ca24f11d6cd9a>`(supported, node->get_friendly_name())) {
	            for (auto&& inputNodeOutput : node->input_values()) {
	                if (:ref:`ngraph::op::is_constant <doxid-namespaceov_1_1op_1_1util_1ab4c248ad8ea86edd3aa31919265fe261>`(inputNodeOutput.get_node()) ||
	                    :ref:`ngraph::op::is_parameter <doxid-namespaceov_1_1op_1_1util_1a3661dace12ff612e64d1c6e9a1221213>`(inputNodeOutput.get_node())) {
	                    supported.emplace(inputNodeOutput.get_node()->get_friendly_name());
	                }
	            }
	            for (auto&& outputs : node->outputs()) {
	                for (auto&& outputNodeInput : outputs.get_target_inputs()) {
	                    if (:ref:`ngraph::op::is_output <doxid-namespaceov_1_1op_1_1util_1acbc7b08408d076757bfa4d8c70e1f7bd>`(outputNodeInput.get_node())) {
	                        supported.emplace(outputNodeInput.get_node()->get_friendly_name());
	                    }
	                }
	            }
	        }
	
	        // 6. Eliminate subgraphs that consist of housekeeping nodes only
	        if (:ref:`ngraph::op::is_constant <doxid-namespaceov_1_1op_1_1util_1ab4c248ad8ea86edd3aa31919265fe261>`(node) || :ref:`ngraph::op::is_parameter <doxid-namespaceov_1_1op_1_1util_1a3661dace12ff612e64d1c6e9a1221213>`(node)) {
	            if (!:ref:`InferenceEngine::details::contains <doxid-namespaceov_1_1util_1aa63ec0c8f3eb1d9ca97ca24f11d6cd9a>`(
	                    supported,
	                    node->output(0).get_target_inputs().begin()->get_node()->get_friendly_name())) {
	                supported.erase(node->get_friendly_name());
	            }
	        } else if (:ref:`ngraph::op::is_output <doxid-namespaceov_1_1op_1_1util_1acbc7b08408d076757bfa4d8c70e1f7bd>`(node)) {
	            if (!:ref:`InferenceEngine::details::contains <doxid-namespaceov_1_1util_1aa63ec0c8f3eb1d9ca97ca24f11d6cd9a>`(supported,
	                                                    node->input_values().begin()->get_node()->get_friendly_name())) {
	                supported.erase(node->get_friendly_name());
	            }
	        }
	    }
	
	    // 7. Produce the result
	    :ref:`InferenceEngine::QueryNetworkResult <doxid-struct_inference_engine_1_1_query_network_result>` res;
	    for (auto&& layerName : supported) {
	        res.:ref:`supportedLayersMap <doxid-struct_inference_engine_1_1_query_network_result_1aff431e5d7451f364dee1c1c54ca78333>`.emplace(layerName, GetName());
	    }
	
	    return res;
	}



.. rubric::

Adds an extension of the :ref:`InferenceEngine::IExtensionPtr <doxid-namespace_inference_engine_1a7a4456ae150afbff5140be2d92680fa4>` type to a plugin. If a plugin does not support extensions, the method must throw an exception:

.. ref-code-block:: cpp

	void Plugin::AddExtension(const :ref:`InferenceEngine::IExtensionPtr <doxid-namespace_inference_engine_1a7a4456ae150afbff5140be2d92680fa4>`& /\*extension\*/) {
	    // TODO: add extensions if plugin supports extensions
	    :ref:`IE_THROW <doxid-ie__common_8h_1a643ef2aa5e1c6b7523e55cc4396e3e02>`(NotImplemented);
	}



.. rubric::

Sets new values for plugin configuration keys:

.. ref-code-block:: cpp

	void Plugin::SetConfig(const ConfigMap& config) {
	    _cfg = Configuration{config, _cfg};
	}

In the snippet above, the ``Configuration`` class overrides previous configuration values with the new ones. All these values are used during backend specific graph compilation and execution of inference requests.

.. note:: The function must throw an exception if it receives an unsupported configuration key.

.. rubric::

Returns a current value for a specified configuration key:

.. ref-code-block:: cpp

	:ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` Plugin::GetConfig(
	    const std::string& name,
	    const std::map<std::string, InferenceEngine::Parameter>& /\*options\*/) const {
	    return _cfg.Get(name);
	}

The function is implemented with the ``Configuration::Get`` method, which wraps an actual configuration key value to the :ref:`InferenceEngine::Parameter <doxid-namespace_inference_engine_1aff2231f886c9f8fc9c226fd343026789>` and returns it.

.. note:: The function must throw an exception if it receives an unsupported configuration key.

.. rubric::

Returns a metric value for a metric with the name ``name``. A device metric is a static type of information from a plugin about its devices or device capabilities.

Examples of metrics:

* :ref:`METRIC_KEY(AVAILABLE_DEVICES) <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>` - list of available devices that are required to implement. In this case, you can use all devices of the same ``Template`` type with automatic logic of the ``MULTI`` device plugin.

* :ref:`METRIC_KEY(FULL_DEVICE_NAME) <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>` - full device name. In this case, a particular device ID is specified in the ``option`` parameter as ``{ :ref:`CONFIG_KEY(KEY_DEVICE_ID) <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`, "deviceID" }``.

* :ref:`METRIC_KEY(SUPPORTED_METRICS) <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>` - list of metrics supported by a plugin

* :ref:`METRIC_KEY(SUPPORTED_CONFIG_KEYS) <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>` - list of configuration keys supported by a plugin that affects their behavior during a backend specific graph compilation or an inference requests execution

* :ref:`METRIC_KEY(OPTIMIZATION_CAPABILITIES) <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>` - list of optimization capabilities of a device. For example, supported data types and special optimizations for them.

* Any other device-specific metrics. In this case, place metrics declaration and possible values to a plugin-specific public header file, for example, ``template/template_config.hpp``. The example below demonstrates the definition of a new optimization capability value specific for a device:

.. ref-code-block:: cpp

	/\*\*
	 \* @brief Defines whether current Template device instance supports hardware blocks for fast convolution computations.
	 \*/
	DECLARE_TEMPLATE_METRIC_VALUE(HARDWARE_CONVOLUTION);

The snippet below provides an example of the implementation for ``GetMetric`` :

.. ref-code-block:: cpp

	:ref:`InferenceEngine::Parameter <doxid-classov_1_1_any>` Plugin::GetMetric(const std::string& name,
	                                             const std::map<std::string, InferenceEngine::Parameter>& options) const {
	    if (:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(SUPPORTED_METRICS) == name) {
	        std::vector<std::string> supportedMetrics = {:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(AVAILABLE_DEVICES),
	                                                     :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(SUPPORTED_METRICS),
	                                                     :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(SUPPORTED_CONFIG_KEYS),
	                                                     :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(FULL_DEVICE_NAME),
	                                                     :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(IMPORT_EXPORT_SUPPORT),
	                                                     :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(DEVICE_ARCHITECTURE),
	                                                     :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(OPTIMIZATION_CAPABILITIES),
	                                                     :ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(RANGE_FOR_ASYNC_INFER_REQUESTS)};
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(SUPPORTED_METRICS, supportedMetrics);
	    } else if (:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(SUPPORTED_CONFIG_KEYS) == name) {
	        std::vector<std::string> configKeys = {:ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(DEVICE_ID),
	                                               :ref:`CONFIG_KEY <doxid-ie__plugin__config_8hpp_1aad09cfba062e8ec9fb7ab9383f656ec7>`(PERF_COUNT),
	                                               :ref:`ov::hint::performance_mode <doxid-group__ov__runtime__cpp__prop__api_1ga2691fe27acc8aa1d1700ad40b6da3ba2>`.name(),
	                                               TEMPLATE_CONFIG_KEY(THROUGHPUT_STREAMS)};
	        auto streamExecutorConfigKeys = :ref:`InferenceEngine::IStreamsExecutor::Config <doxid-struct_inference_engine_1_1_i_streams_executor_1_1_config>`{}.:ref:`SupportedKeys <doxid-struct_inference_engine_1_1_i_streams_executor_1_1_config_1af5194c42f86951299ba6a9ef334627ef>`();
	        for (auto&& configKey : streamExecutorConfigKeys) {
	            if (configKey != :ref:`InferenceEngine::PluginConfigParams::KEY_CPU_THROUGHPUT_STREAMS <doxid-namespace_inference_engine_1_1_plugin_config_params_1ae04df28b5ac394e398297e432f3c7b6e>`) {
	                configKeys.emplace_back(configKey);
	            }
	        }
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(SUPPORTED_CONFIG_KEYS, configKeys);
	    } else if (:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(AVAILABLE_DEVICES) == name) {
	        // TODO: fill list of available devices
	        std::vector<std::string> availableDevices = {""};
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(AVAILABLE_DEVICES, availableDevices);
	    } else if (:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(FULL_DEVICE_NAME) == name) {
	        std::string name = "Template Device Full Name";
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(FULL_DEVICE_NAME, name);
	    } else if (:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(IMPORT_EXPORT_SUPPORT) == name) {
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(IMPORT_EXPORT_SUPPORT, true);
	    } else if (:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(DEVICE_ARCHITECTURE) == name) {
	        // TODO: return device architecture for device specified by DEVICE_ID config
	        std::string arch = "TEMPLATE";
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(DEVICE_ARCHITECTURE, arch);
	    } else if (:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(OPTIMIZATION_CAPABILITIES) == name) {
	        // TODO: fill actual list of supported capabilities: e.g. Template device supports only FP32
	        std::vector<std::string> :ref:`capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>` = {:ref:`METRIC_VALUE <doxid-ie__plugin__config_8hpp_1ad6dd157c1a4d27888bfdcdf1b64cfdb2>`(:ref:`FP32 <doxid-namespace_inference_engine_1_1_metrics_1a33f8ec1373b4a3550b87abf3a7773aa2>`) /\*, TEMPLATE_METRIC_VALUE(HARDWARE_CONVOLUTION)\*/};
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(OPTIMIZATION_CAPABILITIES, :ref:`capabilities <doxid-group__ov__runtime__cpp__prop__api_1gadb13d62787fc4485733329f044987294>`);
	    } else if (:ref:`METRIC_KEY <doxid-ie__plugin__config_8hpp_1a69d0efa20c5b2bec020a706279f0c7be>`(RANGE_FOR_ASYNC_INFER_REQUESTS) == name) {
	        // TODO: fill with actual values
	        using uint = unsigned int;
	        :ref:`IE_SET_METRIC_RETURN <doxid-group__ie__dev__api_1gad59db954d9dfcbd6f490d5cbadd3a91d>`(RANGE_FOR_ASYNC_INFER_REQUESTS, std::make_tuple(uint{1}, uint{1}, uint{1}));
	    } else {
	        :ref:`IE_THROW <doxid-ie__common_8h_1a643ef2aa5e1c6b7523e55cc4396e3e02>`(NotFound) << "Unsupported device metric: " << name;
	    }
	}



.. note:: If an unsupported metric key is passed to the function, it must throw an exception.

.. rubric::

The importing network mechanism allows to import a previously exported backend specific graph and wrap it using an :ref:`ExecutableNetwork <doxid-openvino_docs_ie_plugin_dg_executable_network>` object. This functionality is useful if backend specific graph compilation takes significant time and/or cannot be done on a target host device due to other reasons.

During export of backend specific graph using ``ExecutableNetwork::Export``, a plugin may export any type of information it needs to import a compiled graph properly and check its correctness. For example, the export information may include:

* Compilation options (state of ``Plugin::_cfg`` structure)

* Information about a plugin and a device type to check this information later during the import and throw an exception if the ``model`` stream contains wrong data. For example, if devices have different capabilities and a graph compiled for a particular device cannot be used for another, such type of information must be stored and checked during the import.

* Compiled backend specific graph itself

* Information about precisions and shapes set by the user

.. ref-code-block:: cpp

	:ref:`InferenceEngine::IExecutableNetworkInternal::Ptr <doxid-class_inference_engine_1_1_i_executable_network_internal_1a264e3e04130a2e44d0b257ae63c9feae>` Plugin::ImportNetwork(
	    std::istream& modelStream,
	    const std::map<std::string, std::string>& config) {
	    :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, "Plugin::ImportNetwork");
	
	    auto fullConfig = Configuration{config, _cfg};
	    auto exec = std::make_shared<ExecutableNetwork>(modelStream,
	                                                    fullConfig,
	                                                    std::static_pointer_cast<Plugin>(shared_from_this()));
	    :ref:`SetExeNetworkInfo <doxid-namespace_inference_engine_1a31ef38523e4aec9bc04b8fe8c2fa0a70>`(exec, exec->_function);
	    return exec;
	}



Create Instance of Plugin Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inference Engine plugin library must export only one function creating a plugin instance using IE_DEFINE_PLUGIN_CREATE_FUNCTION macro:

.. ref-code-block:: cpp

	static const :ref:`InferenceEngine::Version <doxid-struct_inference_engine_1_1_version>` version = {{2, 1}, CI_BUILD_NUMBER, "openvino_template_plugin"};
	:ref:`IE_DEFINE_PLUGIN_CREATE_FUNCTION <doxid-group__ie__dev__api__plugin__api_1ga06b197cbe37f59f94b15a7d861e17d4e>`(Plugin, version)

Next step in a plugin library implementation is the :ref:`ExecutableNetwork <doxid-openvino_docs_ie_plugin_dg_executable_network>` class.

