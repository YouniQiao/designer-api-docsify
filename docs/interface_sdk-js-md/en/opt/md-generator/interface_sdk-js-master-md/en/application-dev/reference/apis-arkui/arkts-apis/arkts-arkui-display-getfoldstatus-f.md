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

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function getFoldStatus(): FoldStatus--><!--Device-display-function getFoldStatus(): FoldStatus-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FoldStatus](../../apis-na/arkts-apis/arkts-na-enums-foldstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## Examples

```TypeScript
let data: display.FoldStatus = display.getFoldStatus();
console.info(`Succeeded in obtaining fold status. Data: ${data}`);
```
