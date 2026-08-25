# getUnlockPolicy (System API)

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## getUnlockPolicy

```TypeScript
function getUnlockPolicy(userId: number): UnlockPolicy
```

Obtains the authentication policy used to unlock the screen.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UnlockPolicy](arkts-basicservices-screenlock-unlockpolicy-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13200002](../errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) |
| 13200004 |
