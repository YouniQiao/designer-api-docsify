# loadModelFromFd

## 导入模块

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## loadModelFromFd

```TypeScript
function loadModelFromFd(
    model: int,
    context?: Context): Promise<Model>
```

Creates a Model instance file description

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-mindSporeLite-function loadModelFromFd(    model: int,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadModelFromFd(    model: int,    context?: Context): Promise<Model>-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | model indicates model file description to be loaded |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | 否 | context indicates model context information |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Model&gt; | the promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1000007 | Failed to create native model from file descriptor (fd). Possible causes: 1. The file descriptor (fd) is incorrect; 2. The model file is damaged.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |

## 示例

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, File descriptor: ${file.fd}, Result: null`);
  } else if (modelInputs.length === 0) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, File descriptor: ${file.fd}, Input count: 0`);
  } else {
    console.info(`Succeeded in getting model inputs. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
  }
}).catch((error: Error) => {
  console.error(`Failed to load model from file descriptor. Model file: ${modelFile}, File descriptor: ${file.fd}, Error: ${error.message}`);
});
```


## loadModelFromFd

```TypeScript
function loadModelFromFd(
    model: int, callback: Callback<Model>): void
```

Create a Model instance from file description

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-mindSporeLite-function loadModelFromFd(    model: int, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFd(    model: int, callback: Callback<Model>): void-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | model indicates model file description to be loaded |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Model&gt; | 是 | the callback of model |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1000007 | Failed to create native model from file descriptor (fd). Possible causes: 1. The file descriptor (fd) is incorrect; 2. The model file is damaged.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |

## 示例

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, File descriptor: ${file.fd}, Result: null`);
  } else if (modelInputs.length === 0) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, File descriptor: ${file.fd}, Input count: 0`);
  } else {
    console.info(`Succeeded in getting model inputs. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
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

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-mindSporeLite-function loadModelFromFd(    model: int,    context: Context, callback: Callback<Model>): void--><!--Device-mindSporeLite-function loadModelFromFd(    model: int,    context: Context, callback: Callback<Model>): void-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | model indicates model file description to be loaded |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | 是 | context indicates model context information |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Model&gt; | 是 | the callback of model |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1000007 | Failed to create native model from file descriptor (fd). Possible causes: 1. The file descriptor (fd) is incorrect; 2. The model file is damaged.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |

## 示例

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let context: mindSporeLite.Context = {};
context.target = ['cpu'];
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadModelFromFd(file.fd, context, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, File descriptor: ${file.fd}, Context: ${JSON.stringify(context)}, Result: null`);
  } else if (modelInputs.length === 0) {
    console.error(`Failed to get model inputs. Model file: ${modelFile}, File descriptor: ${file.fd}, Context: ${JSON.stringify(context)}, Input count: 0`);
  } else {
    console.info(`Succeeded in getting model inputs. Model file: ${modelFile}, Input name: ${modelInputs[0].name}`);
  }
})
```

