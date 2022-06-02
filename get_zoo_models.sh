git clone https://github.com/openvinotoolkit/open_model_zoo.git
cp -rf open_model_zoo/models models
cp -rf open_model_zoo/demos demos
rm -rf open_model_zoo
cat models/intel/index.md intel_models_toc.txt >> temp.txt
mv temp.txt models/intel/index.md
cat models/public/index.md public_models_toc.txt >> temp.txt
mv temp.txt models/public/index.md
cat demos/README.md demos_toc.txt >> temp.txt
mv temp.txt demos/README.md