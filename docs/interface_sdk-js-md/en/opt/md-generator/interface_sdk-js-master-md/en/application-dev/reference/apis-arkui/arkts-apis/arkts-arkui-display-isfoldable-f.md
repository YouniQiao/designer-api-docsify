# isFoldable

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## isFoldable

```TypeScript
function isFoldable(): boolean
```

Checks whether this device is foldable.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function isFoldable(): boolean--><!--Device-display-function isFoldable(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

## Examples

```TypeScript
let ret: boolean = false;
ret = display.isFoldable();
```
