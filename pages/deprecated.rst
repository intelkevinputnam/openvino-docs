.. index:: pair: page; Deprecated List
.. _doxid-deprecated:


Deprecated List
===============

.. list-table::
	:widths: 20 80

	*
		- Global :ref:`InferenceEngine::Blob::element_size <doxid-class_inference_engine_1_1_blob_1a25690a7dd30e0c07abbf32f09c5f8735>` () const =0

		- :target:`doxid-deprecated_1_deprecated000095` Cast to :ref:`MemoryBlob <doxid-class_inference_engine_1_1_memory_blob>` and use its API instead. :ref:`Blob <doxid-class_inference_engine_1_1_blob>` class can represent compound blob, which do not refer to the only solid memory.

	*
		- Global :ref:`InferenceEngine::ExecutableNetwork::CreateInferRequestPtr <doxid-class_inference_engine_1_1_executable_network_1a6579210c5507855ddf3306df28682e9c>` ()

		- :target:`doxid-deprecated_1_deprecated000078` Use :ref:`ExecutableNetwork::CreateInferRequest <doxid-class_inference_engine_1_1_executable_network_1a5516b9b68b8fa0bcc72f19bc812ccf47>`

	*
		- Global :ref:`InferenceEngine::ExecutableNetwork::operator std::shared_ptr\< IExecutableNetwork > <doxid-class_inference_engine_1_1_executable_network_1ab9899dca8b19f723bff911a581a3cce0>` ()

		- :target:`doxid-deprecated_1_deprecated000077` Will be removed. Use operator bool

	*
		- Global :ref:`InferenceEngine::ExecutableNetwork::reset <doxid-class_inference_engine_1_1_executable_network_1a047641f157ef8745ba3a7d0017386af3>` (std::shared_ptr< IExecutableNetwork > newActual)

		- :target:`doxid-deprecated_1_deprecated000076` The method Will be removed

	*
		- Global :ref:`InferenceEngine::CNNNetwork::operator const ICNNNetwork & <doxid-class_inference_engine_1_1_c_n_n_network_1aeb37a0d25c851bf29caa6dcb76f5aaf6>` () const

		- :target:`doxid-deprecated_1_deprecated000075` :ref:`InferenceEngine::ICNNNetwork <doxid-class_inference_engine_1_1_i_c_n_n_network>` interface is deprecated

	*
		- Global :ref:`InferenceEngine::CNNNetwork::operator ICNNNetwork & <doxid-class_inference_engine_1_1_c_n_n_network_1ab037f4b0efb1f76e9821d808327ae77e>` ()

		- :target:`doxid-deprecated_1_deprecated000074` :ref:`InferenceEngine::ICNNNetwork <doxid-class_inference_engine_1_1_i_c_n_n_network>` interface is deprecated

	*
		- Global :ref:`InferenceEngine::CNNNetwork::operator ICNNNetwork::Ptr <doxid-class_inference_engine_1_1_c_n_n_network_1a1c3489090ce7f3a0e2be88325d835776>` ()

		- :target:`doxid-deprecated_1_deprecated000073` :ref:`InferenceEngine::ICNNNetwork <doxid-class_inference_engine_1_1_i_c_n_n_network>` interface is deprecated

	*
		- Global :ref:`InferenceEngine::CNNNetwork::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network_1a65d11914bffbce3db04dc42ac0b373dd>` (std::shared_ptr< ICNNNetwork > network)

		- :target:`doxid-deprecated_1_deprecated000072` Don't use this constructor. It will be removed soon

	*
		- Global :ref:`InferenceEngine::IInferencePlugin::ImportNetwork <doxid-class_inference_engine_1_1_i_inference_plugin_1ab17c290b8d9d53d65425caa299b955c6>` (const std::string &modelFileName, const std::map< std::string, std::string > &config)

		- :target:`doxid-deprecated_1_deprecated000071` Use :ref:`ImportNetwork(std::istream& networkModel, const std::map\<std::string, std::string>& config) <doxid-class_inference_engine_1_1_i_inference_plugin_1a749679b57c27073d5492518ff5d94d09>`

	*
		- Global :ref:`InferenceEngine::IExecutableNetworkInternal::Export <doxid-class_inference_engine_1_1_i_executable_network_internal_1a057bca9b0f955c03190bdf77635e9516>` (const std::string &modelFileName)

		- :target:`doxid-deprecated_1_deprecated000070` Use :ref:`IExecutableNetworkInternal::Export(std::ostream& networkModel) <doxid-class_inference_engine_1_1_i_executable_network_internal_1a2b5e212158cd5bf3a2f903cd405fdd3d>`

	*
		- Global :ref:`ngraph::CoordinateTransformBasic::index <doxid-classngraph_1_1_coordinate_transform_basic_1a93ac5a4ead81a70fca6b93bf1cd28240>` (const Coordinate &c) const

		- :target:`doxid-deprecated_1_deprecated000069`

	*
		- Class :ref:`ngraph::CoordinateIterator <doxid-classngraph_1_1_coordinate_iterator>`

		- :target:`doxid-deprecated_1_deprecated000067`

	*
		- Global :ref:`ov::Node::evaluate <doxid-classov_1_1_node_1afe8b36f599d5f2f1f8b4ef0f1a56a65c>` (const :ref:`ov::HostTensorVector <doxid-namespaceov_1a2e5bf6dcca008b0147e825595f57c03b>` &output_values, const :ref:`ov::HostTensorVector <doxid-namespaceov_1a2e5bf6dcca008b0147e825595f57c03b>` &input_values, const EvaluationContext &evaluationContext) const

		- :target:`doxid-deprecated_1_deprecated000066` Use evaluate with :ref:`ov::Tensor <doxid-classov_1_1_tensor>` instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::addOutput <doxid-class_inference_engine_1_1_i_c_n_n_network_1a07f2f7ada6d7208710ae3dc144347df8>` (const std::string &layerName, size_t outputIndex=0, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*resp=nullptr) noexcept=0

		- :target:`doxid-deprecated_1_deprecated000113` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`ov::Core::add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>` (const std::shared_ptr< InferenceEngine::IExtension > &extension)

		- :target:`doxid-deprecated_1_deprecated000128` This method is deprecated. Please use other :ref:`Core::add_extension <doxid-classov_1_1_core_1a68d0dea1cbcd42a67bea32780e32acea>` methods.

	*
		- Class :ref:`InferenceEngine::Version::ApiVersion <doxid-struct_inference_engine_1_1_version_1_1_api_version>`

		- :target:`doxid-deprecated_1_deprecated000127` Use IE_VERSION_[MAJOR|MINOR|PATCH] definitions, buildNumber property

	*
		- Global :ref:`InferenceEngine::LowLatency <doxid-namespace_inference_engine_1a94efd17b1649a1e7dbc6e89d45ed81be>` (:ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` &network)

		- :target:`doxid-deprecated_1_deprecated000126` Use :ref:`InferenceEngine::lowLatency2 <doxid-namespace_inference_engine_1a472a46b52ae2ae5d4fe42de27031c0b5>` instead. This transformation will be removed in 2023.1.

	*
		- Global :ref:`InferenceEngine::PluginConfigParams::KEY_DUMP_EXEC_GRAPH_AS_DOT <doxid-namespace_inference_engine_1_1_plugin_config_params_1a02ac10820f3dc0b48358a343d54f3a52>`

		- :target:`doxid-deprecated_1_deprecated000125` Use InferenceEngine::ExecutableNetwork::GetExecGraphInfo::serialize method

	*
		- Class :ref:`InferenceEngine::IInferRequest <doxid-class_inference_engine_1_1_i_infer_request>`

		- :target:`doxid-deprecated_1_deprecated000124` Use :ref:`InferenceEngine::InferRequest <doxid-class_inference_engine_1_1_infer_request>` C++ wrapper

	*
		- Global :ref:`InferenceEngine::IExecutableNetwork::GetExecGraphInfo <doxid-class_inference_engine_1_1_i_executable_network_1a761c2a454d46b66ed6538ed9ab42d85a>` (:ref:`ICNNNetwork::Ptr <doxid-class_inference_engine_1_1_i_c_n_n_network_1a05b6f650d23e571e03da46a3a89db633>` &graphPtr, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*resp) noexcept=0

		- :target:`doxid-deprecated_1_deprecated000123` Use :ref:`InferenceEngine::ExecutableNetwork::GetExecGraphInfo <doxid-class_inference_engine_1_1_executable_network_1a00db8bf2706042fb616e0f6683c6a847>` instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::getOVNameForTensor <doxid-class_inference_engine_1_1_i_c_n_n_network_1a9909922d0ba2139f1e6315d8d19f33e0>` (std::string &ov_name, const std::string &orig_name, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*resp) const noexcept

		- :target:`doxid-deprecated_1_deprecated000122` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::serialize <doxid-class_inference_engine_1_1_i_c_n_n_network_1a1e678ce338cdfd9b0a056a55acb402ba>` (std::ostream &xmlStream, :ref:`Blob::Ptr <doxid-class_inference_engine_1_1_blob_1abb6c4f89181e2dd6d8a29ada2dfb4060>` &binData, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*resp) const noexcept=0

		- :target:`doxid-deprecated_1_deprecated000121` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::serialize <doxid-class_inference_engine_1_1_i_c_n_n_network_1a07dfb4ea0bcd5a3008fdc82535969d97>` (std::ostream &xmlStream, std::ostream &binStream, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*resp) const noexcept=0

		- :target:`doxid-deprecated_1_deprecated000120` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::serialize <doxid-class_inference_engine_1_1_i_c_n_n_network_1acd12b5e9b9c6881ce33230a77b3031cf>` (const std::string &xmlPath, const std::string &binPath, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*resp) const noexcept=0

		- :target:`doxid-deprecated_1_deprecated000119` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::reshape <doxid-class_inference_engine_1_1_i_c_n_n_network_1a91791651378668551ea48040b30b7459>` (const std::map< std::string, ngraph::PartialShape > &partialShapes, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*resp) noexcept

		- :target:`doxid-deprecated_1_deprecated000118` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::reshape <doxid-class_inference_engine_1_1_i_c_n_n_network_1abcfd19bd3e69cbf69ed77285f748b1cf>` (const InputShapes &inputShapes, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*resp) noexcept

		- :target:`doxid-deprecated_1_deprecated000117` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::InputShapes <doxid-class_inference_engine_1_1_i_c_n_n_network_1a8bcef7f638f6588a672a32080047ff1d>`

		- :target:`doxid-deprecated_1_deprecated000116` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::getBatchSize <doxid-class_inference_engine_1_1_i_c_n_n_network_1a42a783cf372dca11b615c6f28d5456cb>` () const =0

		- :target:`doxid-deprecated_1_deprecated000115` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::setBatchSize <doxid-class_inference_engine_1_1_i_c_n_n_network_1ac29fc798d8a318f380624bd350b28501>` (size_t size, :ref:`ResponseDesc <doxid-struct_inference_engine_1_1_response_desc>` \*responseDesc) noexcept=0

		- :target:`doxid-deprecated_1_deprecated000114` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`ov::Node::evaluate <doxid-classov_1_1_node_1acfb82acc8349d7138aeaa05217c7014e>` (const :ref:`ov::HostTensorVector <doxid-namespaceov_1a2e5bf6dcca008b0147e825595f57c03b>` &output_values, const :ref:`ov::HostTensorVector <doxid-namespaceov_1a2e5bf6dcca008b0147e825595f57c03b>` &input_values) const

		- :target:`doxid-deprecated_1_deprecated000065` Use evaluate with :ref:`ov::Tensor <doxid-classov_1_1_tensor>` instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::layerCount <doxid-class_inference_engine_1_1_i_c_n_n_network_1ae6205636e448fe10f860012910f50ffd>` () const =0

		- :target:`doxid-deprecated_1_deprecated000112` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::getName <doxid-class_inference_engine_1_1_i_c_n_n_network_1a5cb3d873dd395d2537cbafce612f5a44>` () const noexcept=0

		- :target:`doxid-deprecated_1_deprecated000111` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::getInput <doxid-class_inference_engine_1_1_i_c_n_n_network_1ae952db225b323f5c809ded22c30da4ed>` (const std::string &inputName) const noexcept=0

		- :target:`doxid-deprecated_1_deprecated000110` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::getInputsInfo <doxid-class_inference_engine_1_1_i_c_n_n_network_1ac0d904dcfd039972e04923f1e0befbdd>` (InputsDataMap &inputs) const noexcept=0

		- :target:`doxid-deprecated_1_deprecated000109` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::getOutputsInfo <doxid-class_inference_engine_1_1_i_c_n_n_network_1a67b659f1a8fd1574bb1939ea3f672fad>` (OutputsDataMap &out) const noexcept=0

		- :target:`doxid-deprecated_1_deprecated000108` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::getFunction <doxid-class_inference_engine_1_1_i_c_n_n_network_1a1abddf86b53ec3faffd4ee27175ddbc0>` () const noexcept=0

		- :target:`doxid-deprecated_1_deprecated000107` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::getFunction <doxid-class_inference_engine_1_1_i_c_n_n_network_1ace8fe66eb55229bd517576e01d1a5f90>` () noexcept=0

		- :target:`doxid-deprecated_1_deprecated000106` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::ICNNNetwork::Ptr <doxid-class_inference_engine_1_1_i_c_n_n_network_1a05b6f650d23e571e03da46a3a89db633>`

		- :target:`doxid-deprecated_1_deprecated000105` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Class :ref:`InferenceEngine::ICNNNetwork <doxid-class_inference_engine_1_1_i_c_n_n_network>`

		- :target:`doxid-deprecated_1_deprecated000104` Use :ref:`InferenceEngine::CNNNetwork <doxid-class_inference_engine_1_1_c_n_n_network>` wrapper instead

	*
		- Global :ref:`InferenceEngine::Data::reshape <doxid-class_inference_engine_1_1_data_1abaf4dede294e598b7e8c5f1822ce860f>` (const std::initializer_list< size_t > &dims, Layout layout)

		- :target:`doxid-deprecated_1_deprecated000103` Use :ref:`InferenceEngine::Data::reshape(const SizeVector&, Layout) <doxid-class_inference_engine_1_1_data_1a2292c0006218a73fd5c5f47f62e2d746>`

	*
		- Global :ref:`InferenceEngine::Core::ImportNetwork <doxid-class_inference_engine_1_1_core_1a91273c76ba8495be1b73b03deeb9093f>` (std::istream &networkModel)

		- :target:`doxid-deprecated_1_deprecated000102` Use :ref:`Core::ImportNetwork <doxid-class_inference_engine_1_1_core_1af5dd52e92164a99ce9ed90f78b14d013>` with explicit device name

	*
		- Global :ref:`InferenceEngine::Blob::properProduct <doxid-class_inference_engine_1_1_blob_1ae3a50b95fb064ff296ed92eb160cb46d>` (const SizeVector &dims) noexcept

		- :target:`doxid-deprecated_1_deprecated000099` Cast to :ref:`MemoryBlob <doxid-class_inference_engine_1_1_memory_blob>` and use its API instead.

	*
		- Global :ref:`InferenceEngine::Blob::product <doxid-class_inference_engine_1_1_blob_1a0bb6babfa0c8a4ab07ecdfc5abf91d28>` (const SizeVector &dims) noexcept

		- :target:`doxid-deprecated_1_deprecated000098` Cast to :ref:`MemoryBlob <doxid-class_inference_engine_1_1_memory_blob>` and use its API instead.

	*
		- Class :ref:`InferenceEngine::ReLULayer <doxid-class_inference_engine_1_1_re_l_u_layer>`

		- :target:`doxid-deprecated_1_deprecated000017` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::PowerLayer <doxid-class_inference_engine_1_1_power_layer>`

		- :target:`doxid-deprecated_1_deprecated000032` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::PReLULayer <doxid-class_inference_engine_1_1_p_re_l_u_layer>`

		- :target:`doxid-deprecated_1_deprecated000031` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::RNNSequenceLayer <doxid-class_inference_engine_1_1_r_n_n_sequence_layer>`

		- :target:`doxid-deprecated_1_deprecated000030` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::RNNCell <doxid-class_inference_engine_1_1_r_n_n_cell>`

		- :target:`doxid-deprecated_1_deprecated000029` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::GRUCell <doxid-class_inference_engine_1_1_g_r_u_cell>`

		- :target:`doxid-deprecated_1_deprecated000028` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::LSTMCell <doxid-class_inference_engine_1_1_l_s_t_m_cell>`

		- :target:`doxid-deprecated_1_deprecated000027` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::RNNCellBase <doxid-class_inference_engine_1_1_r_n_n_cell_base>`

		- :target:`doxid-deprecated_1_deprecated000026` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::TensorIterator <doxid-class_inference_engine_1_1_tensor_iterator>`

		- :target:`doxid-deprecated_1_deprecated000025` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ScaleShiftLayer <doxid-class_inference_engine_1_1_scale_shift_layer>`

		- :target:`doxid-deprecated_1_deprecated000024` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::TileLayer <doxid-class_inference_engine_1_1_tile_layer>`

		- :target:`doxid-deprecated_1_deprecated000023` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ReshapeLayer <doxid-class_inference_engine_1_1_reshape_layer>`

		- :target:`doxid-deprecated_1_deprecated000022` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::CropLayer <doxid-class_inference_engine_1_1_crop_layer>`

		- :target:`doxid-deprecated_1_deprecated000021` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::EltwiseLayer <doxid-class_inference_engine_1_1_eltwise_layer>`

		- :target:`doxid-deprecated_1_deprecated000020` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ReLU6Layer <doxid-class_inference_engine_1_1_re_l_u6_layer>`

		- :target:`doxid-deprecated_1_deprecated000019` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ClampLayer <doxid-class_inference_engine_1_1_clamp_layer>`

		- :target:`doxid-deprecated_1_deprecated000018` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::BatchNormalizationLayer <doxid-class_inference_engine_1_1_batch_normalization_layer>`

		- :target:`doxid-deprecated_1_deprecated000033` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::MVNLayer <doxid-class_inference_engine_1_1_m_v_n_layer>`

		- :target:`doxid-deprecated_1_deprecated000016` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::GRNLayer <doxid-class_inference_engine_1_1_g_r_n_layer>`

		- :target:`doxid-deprecated_1_deprecated000015` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::SoftMaxLayer <doxid-class_inference_engine_1_1_soft_max_layer>`

		- :target:`doxid-deprecated_1_deprecated000014` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::NormLayer <doxid-class_inference_engine_1_1_norm_layer>`

		- :target:`doxid-deprecated_1_deprecated000013` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::SplitLayer <doxid-class_inference_engine_1_1_split_layer>`

		- :target:`doxid-deprecated_1_deprecated000012` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ConcatLayer <doxid-class_inference_engine_1_1_concat_layer>`

		- :target:`doxid-deprecated_1_deprecated000011` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::FullyConnectedLayer <doxid-class_inference_engine_1_1_fully_connected_layer>`

		- :target:`doxid-deprecated_1_deprecated000010` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::BinaryConvolutionLayer <doxid-class_inference_engine_1_1_binary_convolution_layer>`

		- :target:`doxid-deprecated_1_deprecated000009` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::PoolingLayer <doxid-class_inference_engine_1_1_pooling_layer>`

		- :target:`doxid-deprecated_1_deprecated000008` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::DeformableConvolutionLayer <doxid-class_inference_engine_1_1_deformable_convolution_layer>`

		- :target:`doxid-deprecated_1_deprecated000007` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::DeconvolutionLayer <doxid-class_inference_engine_1_1_deconvolution_layer>`

		- :target:`doxid-deprecated_1_deprecated000006` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ConvolutionLayer <doxid-class_inference_engine_1_1_convolution_layer>`

		- :target:`doxid-deprecated_1_deprecated000005` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::WeightableLayer <doxid-class_inference_engine_1_1_weightable_layer>`

		- :target:`doxid-deprecated_1_deprecated000004` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::CNNLayer <doxid-class_inference_engine_1_1_c_n_n_layer>`

		- :target:`doxid-deprecated_1_deprecated000003` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::LayerParams <doxid-struct_inference_engine_1_1_layer_params>`

		- :target:`doxid-deprecated_1_deprecated000002` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::OneHotLayer <doxid-class_inference_engine_1_1_one_hot_layer>`

		- :target:`doxid-deprecated_1_deprecated000049` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Global :ref:`ov::Model::evaluate <doxid-classov_1_1_model_1ac1e725aeeb2d68dd7f7fd696534e11fa>` (const :ref:`ov::HostTensorVector <doxid-namespaceov_1a2e5bf6dcca008b0147e825595f57c03b>` &output_tensors, const :ref:`ov::HostTensorVector <doxid-namespaceov_1a2e5bf6dcca008b0147e825595f57c03b>` &input_tensors, :ref:`ov::EvaluationContext <doxid-namespaceov_1a46b08f86068f674a4e0748651b85a4b6>` evaluation_context= :ref:`ov::EvaluationContext() <doxid-namespaceov_1a46b08f86068f674a4e0748651b85a4b6>`) const

		- :target:`doxid-deprecated_1_deprecated000064` Use evaluate with :ref:`ov::Tensor <doxid-classov_1_1_tensor>` instead

	*
		- Global :ref:`ngraph::maximum_value <doxid-namespacengraph_1a32557cb4210f12fcbc013f9f0295fca7>` (const Output< Node > &value)

		- :target:`doxid-deprecated_1_deprecated000063` Use evaluate_upper_bound instead

	*
		- Class :ref:`InferenceEngine::ExperimentalDetectronPriorGridGeneratorLayer <doxid-class_inference_engine_1_1_experimental_detectron_prior_grid_generator_layer>`

		- :target:`doxid-deprecated_1_deprecated000062` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ScatterElementsUpdateLayer <doxid-class_inference_engine_1_1_scatter_elements_update_layer>`

		- :target:`doxid-deprecated_1_deprecated000061` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ScatterUpdateLayer <doxid-class_inference_engine_1_1_scatter_update_layer>`

		- :target:`doxid-deprecated_1_deprecated000060` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::NonMaxSuppressionLayer <doxid-class_inference_engine_1_1_non_max_suppression_layer>`

		- :target:`doxid-deprecated_1_deprecated000059` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::UniqueLayer <doxid-class_inference_engine_1_1_unique_layer>`

		- :target:`doxid-deprecated_1_deprecated000058` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::TopKLayer <doxid-class_inference_engine_1_1_top_k_layer>`

		- :target:`doxid-deprecated_1_deprecated000057` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ReduceLayer <doxid-class_inference_engine_1_1_reduce_layer>`

		- :target:`doxid-deprecated_1_deprecated000056` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::MathLayer <doxid-class_inference_engine_1_1_math_layer>`

		- :target:`doxid-deprecated_1_deprecated000055` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::QuantizeLayer <doxid-class_inference_engine_1_1_quantize_layer>`

		- :target:`doxid-deprecated_1_deprecated000054` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::BroadcastLayer <doxid-class_inference_engine_1_1_broadcast_layer>`

		- :target:`doxid-deprecated_1_deprecated000053` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::SelectLayer <doxid-class_inference_engine_1_1_select_layer>`

		- :target:`doxid-deprecated_1_deprecated000052` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::FillLayer <doxid-class_inference_engine_1_1_fill_layer>`

		- :target:`doxid-deprecated_1_deprecated000051` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::RangeLayer <doxid-class_inference_engine_1_1_range_layer>`

		- :target:`doxid-deprecated_1_deprecated000050` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ReverseSequenceLayer <doxid-class_inference_engine_1_1_reverse_sequence_layer>`

		- :target:`doxid-deprecated_1_deprecated000048` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::BucketizeLayer <doxid-class_inference_engine_1_1_bucketize_layer>`

		- :target:`doxid-deprecated_1_deprecated000047` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::SparseToDenseLayer <doxid-class_inference_engine_1_1_sparse_to_dense_layer>`

		- :target:`doxid-deprecated_1_deprecated000046` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ExperimentalSparseWeightedReduceLayer <doxid-class_inference_engine_1_1_experimental_sparse_weighted_reduce_layer>`

		- :target:`doxid-deprecated_1_deprecated000045` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::SparseSegmentReduceLayer <doxid-class_inference_engine_1_1_sparse_segment_reduce_layer>`

		- :target:`doxid-deprecated_1_deprecated000044` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::SparseFillEmptyRowsLayer <doxid-class_inference_engine_1_1_sparse_fill_empty_rows_layer>`

		- :target:`doxid-deprecated_1_deprecated000043` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::BatchToSpaceLayer <doxid-class_inference_engine_1_1_batch_to_space_layer>`

		- :target:`doxid-deprecated_1_deprecated000042` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::SpaceToBatchLayer <doxid-class_inference_engine_1_1_space_to_batch_layer>`

		- :target:`doxid-deprecated_1_deprecated000041` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::SpaceToDepthLayer <doxid-class_inference_engine_1_1_space_to_depth_layer>`

		- :target:`doxid-deprecated_1_deprecated000040` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::DepthToSpaceLayer <doxid-class_inference_engine_1_1_depth_to_space_layer>`

		- :target:`doxid-deprecated_1_deprecated000039` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::ShuffleChannelsLayer <doxid-class_inference_engine_1_1_shuffle_channels_layer>`

		- :target:`doxid-deprecated_1_deprecated000038` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::StridedSliceLayer <doxid-class_inference_engine_1_1_strided_slice_layer>`

		- :target:`doxid-deprecated_1_deprecated000037` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::GatherLayer <doxid-class_inference_engine_1_1_gather_layer>`

		- :target:`doxid-deprecated_1_deprecated000036` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::PadLayer <doxid-class_inference_engine_1_1_pad_layer>`

		- :target:`doxid-deprecated_1_deprecated000035` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

	*
		- Class :ref:`InferenceEngine::GemmLayer <doxid-class_inference_engine_1_1_gemm_layer>`

		- :target:`doxid-deprecated_1_deprecated000034` Migrate to IR v10 and work with :ref:`ngraph::Function <doxid-classngraph_1a14d7fe7c605267b52c145579e12d2a5f>` directly. The method will be removed in 2021.1

