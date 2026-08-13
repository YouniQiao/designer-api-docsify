# removeProcessor

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## removeProcessor

```TypeScript
function removeProcessor(id: number): void
```

Removes the data processor of a reported event.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-hiAppEvent-function removeProcessor(id: long): void--><!--Device-hiAppEvent-function removeProcessor(id: long): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

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
