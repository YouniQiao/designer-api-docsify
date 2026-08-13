# loadModelFromBuffer

## Modules to Import

```TypeScript
import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

## loadModelFromBuffer

```TypeScript
function loadModelFromBuffer(
    model: ArrayBuffer,
    context?: Context): Promise<Model>
```

Create a Model instance from buffer

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | ArrayBuffer | Yes | model indicates model buffer to be loaded |
| context | Context | No | context indicates model context information |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000005 | Failed to create native model from buffer. Possible causes: 1. The buffer size is incorrect; 2. The buffer file is damaged.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000004 | Model buffer error. Possible causes: 1. The buffer size is 0; 2. The buffer is a null pointer.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((buffer: Uint8Array) => {
    let modelBuffer = buffer.buffer;
    mindSporeLite.loadModelFromBuffer(modelBuffer).then((mindSporeLiteModel: mindSporeLite.Model) => {
      let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
      console.info('MS_LITE_LOG: ' + modelInputs[0].name);
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```


## loadModelFromBuffer

```TypeScript
function loadModelFromBuffer(
    model: ArrayBuffer, callback: Callback<Model>): void
```

Create a Model instance from buffer

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | ArrayBuffer | Yes | model indicates model buffer to be loaded |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes | the callback of model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000005 | Failed to create native model from buffer. Possible causes: 1. The buffer size is incorrect; 2. The buffer file is damaged.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000004 | Model buffer error. Possible causes: 1. The buffer size is 0; 2. The buffer is a null pointer.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((buffer: Uint8Array) => {
    let modelBuffer = buffer.buffer;
    mindSporeLite.loadModelFromBuffer(modelBuffer, (mindSporeLiteModel: mindSporeLite.Model) => {
      let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
      console.info('MS_LITE_LOG: ' + modelInputs[0].name);
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```


## loadModelFromBuffer

```TypeScript
function loadModelFromBuffer(
    model: ArrayBuffer,
    context: Context, callback: Callback<Model>): void
```

Create a Model instance from buffer

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context: Context, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context: Context, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | ArrayBuffer | Yes | model indicates model buffer to be loaded |
| context | Context | Yes | context indicates model context information |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes | the callback of model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000005 | Failed to create native model from buffer. Possible causes: 1. The buffer size is incorrect; 2. The buffer file is damaged.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000004 | Model buffer error. Possible causes: 1. The buffer size is 0; 2. The buffer is a null pointer.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((buffer: Uint8Array) => {
    let modelBuffer = buffer.buffer;
    let context: mindSporeLite.Context = {};
    context.target = ['cpu'];
    mindSporeLite.loadModelFromBuffer(modelBuffer, context, (mindSporeLiteModel: mindSporeLite.Model) => {
      let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
      console.info('MS_LITE_LOG: ' + modelInputs[0].name);
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });
```

