# getSystemCpuUsage

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## getSystemCpuUsage

```TypeScript
function getSystemCpuUsage(): number
```

Obtains the CPU usage of the system.

> **NOTE：**
> 
> This API involves cross-process communication and takes a long time. To avoid performance problems, you are
> advised not to call this API in the main thread.

**Since:** 12

<!--Device-hidebug-function getSystemCpuUsage(): double--><!--Device-hidebug-function getSystemCpuUsage(): double-End-->

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
  console.info(`getSystemCpuUsage: ${hidebug.getSystemCpuUsage()}`)
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```
