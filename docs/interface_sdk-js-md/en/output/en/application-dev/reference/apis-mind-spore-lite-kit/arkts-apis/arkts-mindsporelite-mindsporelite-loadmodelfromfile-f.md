# loadModelFromFile

## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string,
    context?: Context): Promise<Model>
```

Create a Model instance from file path

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | string | Yes | model indicates model path to be loaded |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | context indicates model context information |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Model&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000000 | Model path error. Possible causes: 1. The model path is null; 2. The model path does not exist.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000002 | Failed to create native model. Possible causes: 1. Insufficient permission to access the model path; 2. The model file is corrupted.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

**Example**

```TypeScript
let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```


## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string, callback: Callback<Model>): void
```

Create a Model instance from file path.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFile(    model: string, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | string | Yes | model indicates model path to be loaded |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Model&gt; | Yes | the callback of model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000000 | Model path error. Possible causes: 1. The model path is null; 2. The model path does not exist.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000002 | Failed to create native model. Possible causes: 1. Insufficient permission to access the model path; 2. The model file is corrupted.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

**Example**

```TypeScript
let modelFile: string = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```


## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string,
    context: Context, callback: Callback<Model>): void
```

Create a Model instance from file path.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context: Context, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context: Context, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | string | Yes | model indicates model path to be loaded |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | context indicates model context information |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Model&gt; | Yes | the callback of model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000000 | Model path error. Possible causes: 1. The model path is null; 2. The model path does not exist.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000002 | Failed to create native model. Possible causes: 1. Insufficient permission to access the model path; 2. The model file is corrupted.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

**Example**

```TypeScript
let context: mindSporeLite.Context = {};
context.target = ['cpu'];
let modelFile: string = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile, context, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

