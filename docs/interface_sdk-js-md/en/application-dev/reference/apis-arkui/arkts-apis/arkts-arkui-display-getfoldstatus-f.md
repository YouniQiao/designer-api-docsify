# getFoldStatus

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## getFoldStatus

```TypeScript
function getFoldStatus(): FoldStatus
```

Obtains the fold status of this foldable device.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function getFoldStatus(): FoldStatus--><!--Device-display-function getFoldStatus(): FoldStatus-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| FoldStatus | Fold status of the device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

## Examples

```TypeScript
import { display } from '@kit.ArkUI';

let data: display.FoldStatus = display.getFoldStatus();
console.info(`Succeeded in obtaining fold status. Data: ${data}`);
```

