.. index:: pair: page; Asynchronous Inference Request
.. _doxid-openvino_docs_ie_plugin_dg_async_infer_request:


Asynchronous Inference Request
==============================

:target:`doxid-openvino_docs_ie_plugin_dg_async_infer_request_1md_openvino_docs_ie_plugin_dg_asyncinferrequest` Asynchronous Inference Request runs an inference pipeline asynchronously in one or several task executors depending on a device pipeline structure. OpenVINO Runtime Plugin API provides the base :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default>` class:

* The class has the ``_pipeline`` field of ``std::vector<std::pair<ITaskExecutor::Ptr, Task> >``, which contains pairs of an executor and executed task.

* All executors are passed as arguments to a class constructor and they are in the running state and ready to run tasks.

* The class has the :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault::StopAndWait <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default_1ad09f77f1467a13083e5f1a0eba1948b6>` method, which waits for ``_pipeline`` to finish in a class destructor. The method does not stop task executors and they are still in the running stage, because they belong to the executable network instance and are not destroyed.

Class
~~~~~

OpenVINO Runtime Plugin API provides the base :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default>` class for a custom asynchronous inference request implementation:

.. ref-code-block:: cpp

	class TemplateAsyncInferRequest : public :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default>` {
	public:
	    TemplateAsyncInferRequest(const TemplateInferRequest::Ptr& inferRequest,
	                              const :ref:`InferenceEngine::ITaskExecutor::Ptr <doxid-class_inference_engine_1_1_i_task_executor_1a8ba60f739a36331eb8ed3492ffc55eb5>`& taskExecutor,
	                              const :ref:`InferenceEngine::ITaskExecutor::Ptr <doxid-class_inference_engine_1_1_i_task_executor_1a8ba60f739a36331eb8ed3492ffc55eb5>`& waitExecutor,
	                              const :ref:`InferenceEngine::ITaskExecutor::Ptr <doxid-class_inference_engine_1_1_i_task_executor_1a8ba60f739a36331eb8ed3492ffc55eb5>`& callbackExecutor);
	
	    ~TemplateAsyncInferRequest();
	
	private:
	    TemplateInferRequest::Ptr _inferRequest;
	    :ref:`InferenceEngine::ITaskExecutor::Ptr <doxid-class_inference_engine_1_1_i_task_executor_1a8ba60f739a36331eb8ed3492ffc55eb5>` _waitExecutor;
	};



Class Fields
++++++++++++

* ``_inferRequest`` - a reference to the :ref:`synchronous inference request <doxid-openvino_docs_ie_plugin_dg_infer_request>` implementation. Its methods are reused in the ``AsyncInferRequest`` constructor to define a device pipeline.

* ``_waitExecutor`` - a task executor that waits for a response from a device about device tasks completion

.. note:: If a plugin can work with several instances of a device, ``_waitExecutor`` must be device-specific. Otherwise, having a single task executor for several devices does not allow them to work in parallel.

.. rubric::

The main goal of the ``AsyncInferRequest`` constructor is to define a device pipeline ``_pipeline``. The example below demonstrates ``_pipeline`` creation with the following stages:

* ``inferPreprocess`` is a CPU compute task.

* ``startPipeline`` is a CPU ligthweight task to submit tasks to a remote device.

* ``waitPipeline`` is a CPU non-compute task that waits for a response from a remote device.

* ``inferPostprocess`` is a CPU compute task.

.. ref-code-block:: cpp

	TemplateAsyncInferRequest::TemplateAsyncInferRequest(const TemplateInferRequest::Ptr& inferRequest,
	                                                     const :ref:`InferenceEngine::ITaskExecutor::Ptr <doxid-class_inference_engine_1_1_i_task_executor_1a8ba60f739a36331eb8ed3492ffc55eb5>`& cpuTaskExecutor,
	                                                     const :ref:`InferenceEngine::ITaskExecutor::Ptr <doxid-class_inference_engine_1_1_i_task_executor_1a8ba60f739a36331eb8ed3492ffc55eb5>`& waitExecutor,
	                                                     const :ref:`InferenceEngine::ITaskExecutor::Ptr <doxid-class_inference_engine_1_1_i_task_executor_1a8ba60f739a36331eb8ed3492ffc55eb5>`& callbackExecutor)
	    : AsyncInferRequestThreadSafeDefault(inferRequest, cpuTaskExecutor, callbackExecutor),
	      _inferRequest(inferRequest),
	      _waitExecutor(waitExecutor) {
	    // In current implementation we have CPU only tasks and no needs in 2 executors
	    // So, by default single stage pipeline is created.
	    // This stage executes InferRequest::Infer() using cpuTaskExecutor.
	    // But if remote asynchronous device is used the pipeline can by splitted tasks that are executed by cpuTaskExecutor
	    // and waiting tasks. Waiting tasks can lock execution thread so they use separate threads from other executor.
	    constexpr const auto remoteDevice = false;
	
	    if (remoteDevice) {
	        _pipeline = {{cpuTaskExecutor,
	                      [this] {
	                          :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin,
	                                             "TemplateAsyncInferRequest::PreprocessingAndStartPipeline");
	                          _inferRequest->inferPreprocess();
	                          _inferRequest->startPipeline();
	                      }},
	                     {_waitExecutor,
	                      [this] {
	                          :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, "TemplateAsyncInferRequest::WaitPipeline");
	                          _inferRequest->waitPipeline();
	                      }},
	                     {cpuTaskExecutor, [this] {
	                          :ref:`OV_ITT_SCOPED_TASK <doxid-group__ie__dev__profiling_1gac1e4b5bdc6097e2afd26b75d05dfe1ef>`(itt::domains::TemplatePlugin, "TemplateAsyncInferRequest::Postprocessing");
	                          _inferRequest->inferPostprocess();
	                      }}};
	    }
	}

The stages are distributed among two task executors in the following way:

* ``inferPreprocess`` and ``startPipeline`` are combined into a single task and run on ``_requestExecutor``, which computes CPU tasks.

* You need at least two executors to overlap compute tasks of a CPU and a remote device the plugin works with. Otherwise, CPU and device tasks are executed serially one by one.

* ``waitPipeline`` is sent to ``_waitExecutor``, which works with the device.

.. note:: ``callbackExecutor`` is also passed to the constructor and it is used in the base :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default>` class, which adds a pair of ``callbackExecutor`` and a callback function set by the user to the end of the pipeline.

Inference request stages are also profiled using IE_PROFILING_AUTO_SCOPE, which shows how pipelines of multiple asynchronous inference requests are run in parallel via the `Intel® VTune™ Profiler <https://software.intel.com/en-us/vtune>`__ tool.

.. rubric::

In the asynchronous request destructor, it is necessary to wait for a pipeline to finish. It can be done using the :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault::StopAndWait <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default_1ad09f77f1467a13083e5f1a0eba1948b6>` method of the base class.

.. ref-code-block:: cpp

	TemplateAsyncInferRequest::~TemplateAsyncInferRequest() {
	    :ref:`InferenceEngine::AsyncInferRequestThreadSafeDefault::StopAndWait <doxid-class_inference_engine_1_1_async_infer_request_thread_safe_default_1ad09f77f1467a13083e5f1a0eba1948b6>`();
	}

