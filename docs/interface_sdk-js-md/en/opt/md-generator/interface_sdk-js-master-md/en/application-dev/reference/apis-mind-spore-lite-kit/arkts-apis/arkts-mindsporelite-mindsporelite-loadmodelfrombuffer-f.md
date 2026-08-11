# loadModelFromBuffer

## Modules to Import

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

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | ArrayBuffer | Yes |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Model&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 1000005 |
| 1000004 |
| 1000003 |
| 1000001 |

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

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | ArrayBuffer | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Model&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000005 |
| 1000004 |
| 1000003 |
| 1000001 |

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

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context: Context, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromBuffer(    model: ArrayBuffer,    context: Context, callback: Callback<Model>): void-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | ArrayBuffer | Yes |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Model&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 1000005 |
| 1000004 |
| 1000003 |
| 1000001 |

## Examples

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
