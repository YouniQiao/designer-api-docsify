# dumpJsHeapData

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## dumpJsHeapData

```TypeScript
function dumpJsHeapData(filename : string) : void
```

Dumps VM heap data.

> **NOTE：**
> 
> Exporting the VM heap is time-consuming, and this API is a synchronous API. Therefore, you are advised not to
> call this API in the release version. Otherwise, the application screen may freeze, affecting user experience.

**Since:** 9

<!--Device-hidebug-function dumpJsHeapData(filename : string) : void--><!--Device-hidebug-function dumpJsHeapData(filename : string) : void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.dumpJsHeapData("heapData");
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```


## dumpJsHeapData

```TypeScript
function dumpJsHeapData(filename: string, needClean: boolean): void
```

Exports the heap data.The input parameter is a user-defined file name, excluding the file suffix.The generated file is in the files folder under the application directory.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-hidebug-function dumpJsHeapData(filename: string, needClean: boolean): void--><!--Device-hidebug-function dumpJsHeapData(filename: string, needClean: boolean): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |
| needClean | boolean | Yes |

## Examples

```TypeScript
import { hidebug } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  hidebug.dumpJsHeapData("heapData", true);
} catch (error) {
  console.error(`error code: ${(error as BusinessError).code}, error msg: ${(error as BusinessError).message}`);
}
```
