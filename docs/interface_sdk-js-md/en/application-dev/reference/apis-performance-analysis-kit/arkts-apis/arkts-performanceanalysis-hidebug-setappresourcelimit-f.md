# setAppResourceLimit

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## setAppResourceLimit

```TypeScript
function setAppResourceLimit(type: string, value: int, enableDebugLog: boolean): void
```

Sets the number of FDs, number of threads, JS memory, or native memory limit of the application.

> **NOTE：**
> 
> Enable **System resource leak log** in **Developer options** and restart the device for the API to take effect.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-hidebug-function setAppResourceLimit(type: string, value: int, enableDebugLog: boolean): void--><!--Device-hidebug-function setAppResourceLimit(type: string, value: int, enableDebugLog: boolean): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Types of leak resources:&lt;br&gt;- pss_memory (native memory)&lt;br&gt;- js_heap (JavaScript heap memory)&lt;br&gt;- fd (file descriptor)&lt;br&gt;- thread (thread) |
| value | int | Yes | Value range of the maximum values of the leak resource types:&lt;br&gt;- pss_memory: **[1024, 4 × 1024 × 1024]** (Unit: KB)&lt;br&gt;- js_heap: **[85, 95]** (85% to 95% of the upper size limit of the JS heap memory)&lt;br&gt;- fd: **[10, 10000]**&lt;br&gt;- thread: **[1, 1000]**. If the value is out of range, the feature becomes invalid. |
| enableDebugLog | boolean | Yes | Whether to enable external debugging logs. Enable external debugging logs only in the grayscale version (test version released to a small number of users before the official version is released). Collecting debugging logs occupies a large number of CPU and memory resources, which may cause application smoothness problems.&lt;br&gt;The value **true** means to enable external debugging logs, and false means the opposite.&lt;br&gt; |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid argument, Possible causes: 1.The limit parameter is too small. 2.The parameter is not in the specified type. 3.The parameter type error or parameter order error. |
| [11400104](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) | Set limit failed due to remote exception. |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let type: string = 'js_heap';
let value: number = 85;
let enableDebugLog: boolean = false;
try {
  hidebug.setAppResourceLimit(type, value, enableDebugLog);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```

