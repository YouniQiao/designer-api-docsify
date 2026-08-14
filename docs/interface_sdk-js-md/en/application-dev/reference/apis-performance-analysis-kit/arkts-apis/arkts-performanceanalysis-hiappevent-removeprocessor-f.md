# removeProcessor

## Modules to Import

```TypeScript
import { hiAppEvent } from 'hiAppEvent';
```

## removeProcessor

```TypeScript
function removeProcessor(id: long): void
```

Removes the data processor of a reported event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hiAppEvent-function removeProcessor(id: long): void--><!--Device-hiAppEvent-function removeProcessor(id: long): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | long | Yes | ID of a data processor. The value must be greater than **0**. The value is obtained by calling [addProcessor](arkts-performanceanalysis-hiappevent-addprocessor-f.md#addProcessor) or [addProcessorFromConfig](arkts-performanceanalysis-hiappevent-addprocessorfromconfig-f.md#addProcessorFromConfig). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
    let processor: hiAppEvent.Processor = {
      name: 'analytics_demo'
    };
    let id: number = hiAppEvent.addProcessor(processor);
    // Remove a specified data processor based on the ID returned after the data processor is added.
    hiAppEvent.removeProcessor(id);
} catch (error) {
    hilog.error(0x0000, 'hiAppEvent', `failed to removeProcessor event, code=${error.code}`);
}
```

