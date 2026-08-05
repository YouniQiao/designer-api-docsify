# loadTrainModelFromFd

## loadTrainModelFromFd

```TypeScript
function loadTrainModelFromFd(
    model: int,
    trainCfg?: TrainCfg,
    context?: Context): Promise<Model>
```

Load train model from file description

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-mindSporeLite-function loadTrainModelFromFd(    model: int,    trainCfg?: TrainCfg,    context?: Context): Promise<Model>--><!--Device-mindSporeLite-function loadTrainModelFromFd(    model: int,    trainCfg?: TrainCfg,    context?: Context): Promise<Model>-End-->

**System capability:** SystemCapability.AI.MindSporeLite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| model | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | model file description |
| trainCfg | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | model train configuration |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | model build context |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Model&gt; | the promise of the built model |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1000001 | Invalid context. Possible causes: 1. The context target is incorrect; 2. The device information is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |
| 1000012 | Failed to create native training model from file descriptor (fd). Possible causes: 1. The model file or file descriptor (fd) is incorrect; 2. The training configuration is incorrect.  **ArkTS mode:** This error code applies only to ArkTS-Sta. |

**Example**

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
mindSporeLite.loadTrainModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
  console.info("MSLITE trainMode: ", mindSporeLiteModel.trainMode);
});
```

