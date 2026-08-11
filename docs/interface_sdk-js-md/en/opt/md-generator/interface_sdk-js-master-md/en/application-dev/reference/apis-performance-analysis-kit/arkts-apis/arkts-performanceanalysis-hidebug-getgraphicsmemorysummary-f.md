# getGraphicsMemorySummary

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getGraphicsMemorySummary

```TypeScript
function getGraphicsMemorySummary(interval?: number): Promise<GraphicsMemorySummary>
```

Obtains the size of the GPU memory summary. This API uses a promise to return the result.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-hidebug-function getGraphicsMemorySummary(interval?: int): Promise<GraphicsMemorySummary>--><!--Device-hidebug-function getGraphicsMemorySummary(interval?: int): Promise<GraphicsMemorySummary>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| interval | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;GraphicsMemorySummary&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemorySummary().then((ret: hidebug.GraphicsMemorySummary) => {
  console.info(`get graphicsMemory gl: ${ret.gl} graph: ${ret.graph}.`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}.`);
})
```
