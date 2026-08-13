# preloadCallUI (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## preloadCallUI

```TypeScript
function preloadCallUI(): Promise<boolean>
```

Preload callUI.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function preloadCallUI(): Promise<boolean>--><!--Device-call-function preloadCallUI(): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
