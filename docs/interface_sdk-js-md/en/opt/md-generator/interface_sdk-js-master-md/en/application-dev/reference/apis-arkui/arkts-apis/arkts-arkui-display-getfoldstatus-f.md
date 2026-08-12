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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function getFoldStatus(): FoldStatus--><!--Device-display-function getFoldStatus(): FoldStatus-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FoldStatus](arkts-arkui-enums-foldstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |

## Examples

```TypeScript
let data: display.FoldStatus = display.getFoldStatus();
console.info(`Succeeded in obtaining fold status. Data: ${data}`);
```
