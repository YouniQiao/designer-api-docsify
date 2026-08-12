# getDisplayByIdSync

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## getDisplayByIdSync

```TypeScript
function getDisplayByIdSync(displayId: number): Display
```

Obtains a Display object based on the display ID.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function getDisplayByIdSync(displayId: long): Display--><!--Device-display-function getDisplayByIdSync(displayId: long): Display-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Display](arkts-arkui-display-display-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |

## Examples

```TypeScript
let displayClass: display.Display | null = null;

try {
  // Use the value of the displayId property in WindowProperties as the input parameter.
  let displayId = 0; 
  displayClass = display.getDisplayByIdSync(displayId);
} catch (exception) {
  console.error(`Failed to get display. Code: ${exception.code}, message: ${exception.message}`);
}
```
