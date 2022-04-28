import sys

for input_model in sys.argv[1:]:
    output_model = input_model + "-TRT"

    # Optimize to TensorRT
    from tensorflow.python.compiler.tensorrt import trt_convert as trt
    converter = trt.TrtGraphConverterV2(input_saved_model_dir=input_model)
    converter.convert()
    converter.save(output_saved_model_dir=output_model)