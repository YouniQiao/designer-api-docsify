# setUserId

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## setUserId

```TypeScript
function setUserId(name: string, value: string): void
```

Sets a user ID, which is used for association when a [Processor](arkts-performanceanalysis-hiappevent-processor-i.md) is configured.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function setUserId(name: string, value: string): void--><!--Device-hiAppEvent-function setUserId(name: string, value: string): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  hiAppEvent.setUserId('key', 'value');
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to setUserId event, code=${error.code}`);
}
```
