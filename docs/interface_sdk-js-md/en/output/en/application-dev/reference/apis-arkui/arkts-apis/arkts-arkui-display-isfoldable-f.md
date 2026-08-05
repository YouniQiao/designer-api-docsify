# isFoldable

## isFoldable

```TypeScript
function isFoldable(): boolean
```

Checks whether this device is foldable.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-display-function isFoldable(): boolean--><!--Device-display-function isFoldable(): boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the device is foldable. **true** if foldable, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

**Example**

```TypeScript
import { display } from '@kit.ArkUI';

let ret: boolean = false;
ret = display.isFoldable();
```

