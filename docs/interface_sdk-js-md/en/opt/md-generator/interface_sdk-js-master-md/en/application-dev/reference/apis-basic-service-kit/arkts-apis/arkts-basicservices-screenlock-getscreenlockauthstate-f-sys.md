# getScreenLockAuthState (System API)

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## getScreenLockAuthState

```TypeScript
function getScreenLockAuthState(userId: number): AuthState
```

Obtain the screen lock authentication state for os account local userId.

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK

<!--Device-screenLock-function getScreenLockAuthState(userId: int): AuthState--><!--Device-screenLock-function getScreenLockAuthState(userId: int): AuthState-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AuthState](arkts-basicservices-screenlock-authstate-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |
