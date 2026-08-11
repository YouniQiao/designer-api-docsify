# isLocked (System API)

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## isLocked

```TypeScript
function isLocked(): boolean
```

Checks whether the screen is currently locked.

**Since:** 9

<!--Device-screenLock-function isLocked(): boolean--><!--Device-screenLock-function isLocked(): boolean-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let isLocked = screenLock.isLocked();
```
