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

> **NOTE：**&gt;
> Exporting the VM heap is time-consuming, and this API is a synchronous API. Therefore, you are advised not to
> call this API in the release version. Otherwise, the application screen may freeze, affecting user experience.

**Since:** 9

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## dumpJsHeapData

```TypeScript
function dumpJsHeapData(filename : string, needClean : boolean) : void
```

Dumps VM heap data and clears the nodeId cache.

> **NOTE：**&gt;
> Exporting the VM heap is time-consuming, and this API is a synchronous API. Therefore, you are advised not to
> call this API in the release version. Otherwise, the application screen may freeze, affecting user experience.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filename | string | Yes |
| needClean | boolean | Yes |
