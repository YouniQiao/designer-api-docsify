# loadModelFromBuffer

## 导入模块

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## loadModelFromBuffer

```TypeScript
function loadModelFromBuffer(
    model: ArrayBuffer,
    context?: Context): Promise<Model>
```

Create a Model instance from buffer

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context?: Context): Promise<Model>-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArrayBuffer | 是 | model indicates model buffer to be loaded |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | 否 | context indicates model context information |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Model&gt; | the promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1000005 | Failed to create native model from buffer. Possible causes: 1. The buffer size is incorrect; 2. The buffer file is damaged.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000004 | Model buffer error. Possible causes: 1. The buffer size is 0; 2. The buffer is a null pointer.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |

## 示例

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
      if (modelInputs == null || modelInputs.length === 0) {
        console.error(`Failed to get model inputs from buffer. Model file: ${modelFile}, Buffer size: ${modelBuffer.byteLength}`);
      } else {
        console.info(`Succeeded in getting model inputs from buffer. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
      }
    }).catch((error: Error) => {
      console.error(`Failed to load model from buffer. Model file: ${modelFile}, Buffer size: ${modelBuffer.byteLength}, Error: ${error.message}`);
    });
  })
  .catch((error: BusinessError) => {
    console.error(`Failed to read model file from resources. File name: ${modelFile}, Error code: ${error.code}, Error message: ${error.message}`);
  });
```


## loadModelFromBuffer

```TypeScript
function loadModelFromBuffer(
    model: ArrayBuffer, callback: Callback<Model>): void
```

Create a Model instance from buffer

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer, callback: Callback<Model>): void-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArrayBuffer | 是 | model indicates model buffer to be loaded |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Model&gt; | 是 | the callback of model |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1000005 | Failed to create native model from buffer. Possible causes: 1. The buffer size is incorrect; 2. The buffer file is damaged.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000004 | Model buffer error. Possible causes: 1. The buffer size is 0; 2. The buffer is a null pointer.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |

## 示例

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
      if (modelInputs == null || modelInputs.length === 0) {
        console.error(`Failed to get model inputs from buffer. Model file: ${modelFile}, Buffer size: ${modelBuffer.byteLength}`);
      } else {
        console.info(`Succeeded in getting model inputs from buffer. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
      }
    })
  })
  .catch((error: BusinessError) => {
    console.error(`Failed to read model file from resources. File name: ${modelFile}, Error code: ${error.code}, Error message: ${error.message}`);
  });
```


## loadModelFromBuffer

```TypeScript
function loadModelFromBuffer(
    model: ArrayBuffer,
    context: Context, callback: Callback<Model>): void
```

Create a Model instance from buffer

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context: Context, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context: Context, callback: Callback<Model>): void-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArrayBuffer | 是 | model indicates model buffer to be loaded |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | 是 | context indicates model context information |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Model&gt; | 是 | the callback of model |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1000005 | Failed to create native model from buffer. Possible causes: 1. The buffer size is incorrect; 2. The buffer file is damaged.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000004 | Model buffer error. Possible causes: 1. The buffer size is 0; 2. The buffer is a null pointer.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000003 | Error in model loading method. Possible causes: 1. The loading method must be path, buffer, or fd.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |

## 示例

```TypeScript
import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
let context: mindSporeLite.Context = {};
context.target = ['cpu'];

globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((buffer: Uint8Array) => {
    let modelBuffer = buffer.buffer;
    mindSporeLite.loadModelFromBuffer(modelBuffer, context, (mindSporeLiteModel: mindSporeLite.Model) => {
      let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
      if (modelInputs == null || modelInputs.length === 0) {
        console.error(`Failed to get model inputs from buffer. Model file: ${modelFile}, Context: ${JSON.stringify(context)}, Buffer size: ${modelBuffer.byteLength}`);
      } else {
        console.info(`Succeeded in getting model inputs from buffer. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
      }
    })
  })
  .catch((error: BusinessError) => {
    console.error(`Failed to read model file from resources. File name: ${modelFile}, Error code: ${error.code}, Error message: ${error.message}`);
  });
```

