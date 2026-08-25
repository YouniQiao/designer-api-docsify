# loadTrainModelFromBuffer

## Modules to Import

```TypeScript
import { mindSporeLite } from 'kits/@kit.MindSporeLiteKit';
```

## loadTrainModelFromBuffer

```TypeScript
function loadTrainModelFromBuffer(
    model: ArrayBuffer,
    trainCfg?: TrainCfg,
    context?: Context): Promise<Model>
```

Load train model from buffer

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| model | ArrayBuffer | Yes |
| trainCfg | [TrainCfg](arkts-mindsporelite-mindsporelite-traincfg-i.md) | No |
| context | [Context](arkts-mindsporelite-mindsporelite-context-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Model](arkts-mindsporelite-mindsporelite-model-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 1000001 |
| 1000010 |
| 1000011 |
