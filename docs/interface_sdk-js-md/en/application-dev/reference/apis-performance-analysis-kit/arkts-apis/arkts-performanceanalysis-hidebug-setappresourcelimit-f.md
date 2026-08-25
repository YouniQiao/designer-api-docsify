# setAppResourceLimit

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## setAppResourceLimit

```TypeScript
function setAppResourceLimit(type: string, value: number, enableDebugLog: boolean): void
```

Sets the number of FDs, number of threads, JS memory, or native memory limit of the application.This API is used to construct a memory leak. For details, see Subscribing to Resource Leak Events (ArkTS) and Subscribing to Resource Leak Events (C/C++).

> **NOTE：**&gt;
> Enable **System resource leak log** in **Developer options** and restart the device for the API to take effect.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | Yes |
| value | number | Yes |
| enableDebugLog | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11400104](../errorcode-hiviewdfx-hidebug-cpuusage.md#11400104-abnormal-cpu-usage) |
