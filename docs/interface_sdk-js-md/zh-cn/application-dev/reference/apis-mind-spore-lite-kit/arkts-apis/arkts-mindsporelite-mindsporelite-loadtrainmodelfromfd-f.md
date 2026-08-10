# loadTrainModelFromFd

## 导入模块

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## loadTrainModelFromFd

```TypeScript
function loadTrainModelFromFd(
    model: int,
    trainCfg?: TrainCfg,
    context?: Context): Promise<Model>
```

Load train model from file description

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-mindSporeLite-function loadTrainModelFromFd(    model: int,    trainCfg?: TrainCfg,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadTrainModelFromFd(    model: int,    trainCfg?: TrainCfg,    context?: Context): Promise<Model>-End-->

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | model file description |
| trainCfg | [TrainCfg](arkts-mindsporelite-mindsporelite-traincfg-i.md) | 否 | model train configuration |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | 否 | model build context |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Model&gt; | the promise of the built model |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1000012 | Failed to create native training model from file descriptor (fd). Possible causes: 1. The model file or file descriptor (fd) is incorrect; 2. The training configuration is incorrect.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS模式：** 该错误码仅适用于ArkTS-Sta。 |

## 示例

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadTrainModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
  console.info(`Succeeded in loading train model. Train mode: ${mindSporeLiteModel.trainMode}`);
}).catch((error: Error) => {
  console.error(`Failed to load train model from file descriptor. Model file: ${modelFile}, File descriptor: ${file.fd}, Error: ${error.message}`);
});
```

