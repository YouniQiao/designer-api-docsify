# isFoldable

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## isFoldable

```TypeScript
function isFoldable(): boolean
```

Checks whether this device is foldable.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

**Examples**

```TypeScript
import { display } from '@kit.ArkUI';

let ret: boolean = false;
ret = display.isFoldable();
```
