# getGraphicsMemory

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getGraphicsMemory

```TypeScript
function getGraphicsMemory(): Promise<number>
```

Obtains the total GPU memory size (**gl** + **graph**) of the application. This API uses a promise to return the result.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-hidebug-function getGraphicsMemory(): Promise<int>--><!--Device-hidebug-function getGraphicsMemory(): Promise<int>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemory().then((ret: number) => {
  console.info(`graphicsMemory: ${ret}`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```
