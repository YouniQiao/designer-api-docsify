# getUserId

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## getUserId

```TypeScript
function getUserId(name: string): string
```

Obtains the value set through **setUserId**.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function getUserId(name: string): string--><!--Device-hiAppEvent-function getUserId(name: string): string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';

hiAppEvent.setUserId('key', 'value');
try {
  let value: string = hiAppEvent.getUserId('key');
  hilog.info(0x0000, 'hiAppEvent', `getUserId event was successful, userId=${value}`);
} catch (error) {
  hilog.error(0x0000, 'hiAppEvent', `failed to getUserId event, code=${error.code}`);
}
```
