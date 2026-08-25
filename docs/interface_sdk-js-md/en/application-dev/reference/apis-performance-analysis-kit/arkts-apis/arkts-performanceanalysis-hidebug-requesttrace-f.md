# requestTrace

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## requestTrace

```TypeScript
function requestTrace(config: RequestTraceConfig): Promise<string>
```

Obtains the trace information of the current process, including the application tag, image window tag, CPU scheduling, and binder kernel information. This API uses a promise to return the result.A maximum of three .sys files returned by trace collection can be stored in the directory. If the number of .sys files is greater than or equal to three, error code 11400120 is reported when the API is called again.This API cannot be used in the input method applications.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [RequestTraceConfig](arkts-performanceanalysis-hidebug-requesttraceconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) |
| [11400120](../errorcode-hiviewdfx-hidebug-trace.md#11400120-trace-file-storage-limit-reached) |
| [11400302](../errorcode-hiviewdfx-hidebug-trace.md#11400302-trace-collection-exceeds-the-resource-quota) |
