# getGraphicsMemorySync

## Modules to Import

```TypeScript
import { hidebug } from 'hidebug';
```

## getGraphicsMemorySync

```TypeScript
function getGraphicsMemorySync(): int
```

Obtains the total GPU memory size (GL + graph) of an application in synchronous mode. > **NOTE：**> > This API involves multiple cross-process communications, which may take seconds. To avoid performance problems, > you are advised to use the asynchronous API **getGraphicsMemory** instead of this API in the main thread.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hidebug-function getGraphicsMemorySync(): int--><!--Device-hidebug-function getGraphicsMemorySync(): int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| int | Total size of the application's GPU memory, in KB. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) | Failed to get the application memory due to a remote exception. |

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

