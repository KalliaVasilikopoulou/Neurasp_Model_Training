training_configurations = {
	"mnist_dataset_portion": 1.0,

	"epochs": 15,
	"batch_size": 12,
	"validation_split": 0.1,
	"dropout_rate": 0.5,
	"learning_rate": 1e-3,
	"decay": 1e-5,
	
	"neurasp_conf": {
		"list_of_possible_output_classes": range(19),
		"output_type" : "sum_value",
		"classifiers_conf": {
			"1": {
				"objects": [0,1],
				"list_of_object_classes": range(10),
				"object_type": "image",
				"classes_type" : "digit"
			}
		}
	}
}
