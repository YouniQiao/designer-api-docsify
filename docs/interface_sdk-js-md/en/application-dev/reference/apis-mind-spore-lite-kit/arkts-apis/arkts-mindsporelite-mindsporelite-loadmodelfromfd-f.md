# loadModelFromFd

## Modules to Import

```TypeScript
import { mindSporeLite } from 'mindSporeLite';
```

## loadModelFromFd

```TypeScript
function loadModelFromFd(
    model: int,
    context?: Context): Promise<Model>
```

Creates a Model instance file description

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFd(    model: int,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadModelFromFd(    model: int,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | int | Yes | model indicates model file description to be loaded |
| context | Context | No | context indicates model context information |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000007 | Failed to create native model from file descriptor (fd). Possible causes: 1. The file descriptor (fd) is incorrect; 2. The model file is damaged.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```


## loadModelFromFd

```TypeScript
function loadModelFromFd(
    model: int, callback: Callback<Model>): void
```

Create a Model instance from file description

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFd(    model: int, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFd(    model: int, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | int | Yes | model indicates model file description to be loaded |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes | the callback of model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000007 | Failed to create native model from file descriptor (fd). Possible causes: 1. The file descriptor (fd) is incorrect; 2. The model file is damaged.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```


## loadModelFromFd

```TypeScript
function loadModelFromFd(
    model: int,
    context: Context, callback: Callback<Model>): void
```

Create a Model instance from file description

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromFd(    model: int,    context: Context, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFd(    model: int,    context: Context, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | int | Yes | model indicates model file description to be loaded |
| context | Context | Yes | context indicates model context information |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; | Yes | the callback of model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000007 | Failed to create native model from file descriptor (fd). Possible causes: 1. The file descriptor (fd) is incorrect; 2. The model file is damaged.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

## Examples

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let context: mindSporeLite.Context = {};
context.target = ['cpu'];
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd, context, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS_LITE_ERR: getInputs failed.')
  } else {
    console.info(modelInputs[0].name);
  }
})
```

