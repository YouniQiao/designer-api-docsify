# setUserProperty

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## setUserProperty

```TypeScript
function setUserProperty(name: string, value: string): void
```

Sets a user property, which is used for association when a [Processor](arkts-performanceanalysis-hiappevent-processor-i.md#Processor) is configured.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function setUserProperty(name: string, value: string): void--><!--Device-hiAppEvent-function setUserProperty(name: string, value: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  hiAppEvent.setUserProperty('key', 'value');
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to setUserProperty event, code=${error.code}`);
}
```
