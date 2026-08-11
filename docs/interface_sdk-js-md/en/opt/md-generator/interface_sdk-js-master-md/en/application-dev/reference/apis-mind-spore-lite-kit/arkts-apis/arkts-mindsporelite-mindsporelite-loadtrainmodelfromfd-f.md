# loadTrainModelFromFd

## Modules to Import

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## loadTrainModelFromFd

```TypeScript
function loadTrainModelFromFd(
    model: number,
    trainCfg?: TrainCfg,
    context?: Context): Promise<Model>
```

Load train model from file description

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadTrainModelFromFd(    model: int,    trainCfg?: TrainCfg,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadTrainModelFromFd(    model: int,    trainCfg?: TrainCfg,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | number | Yes |
| trainCfg | [TrainCfg](arkts-mindsporelite-mindsporelite-traincfg-i.md) | No |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Model&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 1000012 |
| 1000001 |

## Examples

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
