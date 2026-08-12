# getGraphicsMemorySync

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getGraphicsMemorySync

```TypeScript
function getGraphicsMemorySync(): number
```

Obtains the total GPU memory size (GL + graph) of an application in synchronous mode.

> **NOTE：**
> 
> This API involves multiple cross-process communications, which may take seconds. To avoid performance problems,
> you are advised to use the asynchronous API **getGraphicsMemory** instead of this API in the main thread.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-hidebug-function getGraphicsMemorySync(): int--><!--Device-hidebug-function getGraphicsMemorySync(): int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [11400104](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info(`graphicsMemory: ${hidebug.getGraphicsMemorySync()}`)
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```
