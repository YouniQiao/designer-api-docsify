# loadModelFromFile

## Modules to Import

```TypeScript
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

## loadModelFromFile

```TypeScript
function loadModelFromFile(
    model: string,
    context?: Context): Promise<Model>
```

Create a Model instance from file path

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | string | Yes | model indicates model path to be loaded |
| context | Context | No | context indicates model context information |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd. |
| 1000002 | Failed to create native model. Possible causes: 1. Insufficient permission to access the model path; 2. The model file is corrupted. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect. |
| 1000000 | Model path error. Possible causes: 1. The model path is null; 2. The model path does not exist. |

**Examples**

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

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFile(    model: string, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | string | Yes | model indicates model path to be loaded |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes | the callback of model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd. |
| 1000002 | Failed to create native model. Possible causes: 1. Insufficient permission to access the model path; 2. The model file is corrupted. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect. |
| 1000000 | Model path error. Possible causes: 1. The model path is null; 2. The model path does not exist. |

**Examples**

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

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context: Context, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFile(    model: string,    context: Context, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | string | Yes | model indicates model path to be loaded |
| context | Context | Yes | context indicates model context information |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes | the callback of model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd. |
| 1000002 | Failed to create native model. Possible causes: 1. Insufficient permission to access the model path; 2. The model file is corrupted. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect. |
| 1000000 | Model path error. Possible causes: 1. The model path is null; 2. The model path does not exist. |

**Examples**

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

