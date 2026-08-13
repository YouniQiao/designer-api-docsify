# startJsCpuProfiling

## Modules to Import

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
```

## startJsCpuProfiling

```TypeScript
function startJsCpuProfiling(filename : string) : void
```

Starts the VM profiling method. **startJsCpuProfiling(filename: string)** and **stopJsCpuProfiling()** are called in pairs. **startJsCpuProfiling(filename: string)** always occurs before **stopJsCpuProfiling()**. You are advised not to call either of these methods repeatedly. Otherwise, an exception may occur.

**Since:** 23

**Deprecated since:** -1

<!--Device-hidebug-function startJsCpuProfiling(filename : string) : void--><!--Device-hidebug-function startJsCpuProfiling(filename : string) : void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.startJsCpuProfiling("cpu_profiling");
  // ...
  hidebug.stopJsCpuProfiling();
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```
