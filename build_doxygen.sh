cd openvino
mkdir build
cd build
cmake -DENABLE_DOCS=ON -DENABLE_PYTHON=ON -DNGRAPH_PYTHON_BUILD_ENABLE=ON -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --target sphinx_docs