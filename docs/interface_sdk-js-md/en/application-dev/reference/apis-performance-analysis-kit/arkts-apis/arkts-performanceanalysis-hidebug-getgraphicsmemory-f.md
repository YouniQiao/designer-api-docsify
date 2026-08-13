# getGraphicsMemory

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getGraphicsMemory

```TypeScript
function getGraphicsMemory(): Promise<int>
```

Obtains the total GPU memory size (**gl** + **graph**) of the application. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hidebug-function getGraphicsMemory(): Promise<int>--><!--Device-hidebug-function getGraphicsMemory(): Promise<int>-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the total GPU memory size of the application, in KB. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) | Failed to get the application memory due to a remote exception. |

## Examples

```TypeScript
import { hidebug, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

hidebug.getGraphicsMemory().then((ret: number) => {
  console.info(`graphicsMemory: ${ret}`)
}).catch((error: BusinessError) => {
  console.error(`error code: ${error.code}, error msg: ${error.message}`);
})
```

