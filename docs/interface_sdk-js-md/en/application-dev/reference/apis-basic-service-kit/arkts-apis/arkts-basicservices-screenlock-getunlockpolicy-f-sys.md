# getUnlockPolicy (System API)

## Modules to Import

```TypeScript
import { screenLock } from '@kit.BasicServicesKit';
```

## getUnlockPolicy

```TypeScript
function getUnlockPolicy(userId: int): UnlockPolicy
```

Obtains the authentication policy used to unlock the screen.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK

**Model restriction:** This API can be used only in the stage model.

<!--Device-screenLock-function getUnlockPolicy(userId: int): UnlockPolicy--><!--Device-screenLock-function getUnlockPolicy(userId: int): UnlockPolicy-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Local user ID of the OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| [UnlockPolicy](arkts-basicservices-screenlock-unlockpolicy-e-sys.md) | The unlock policy. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed: applications that are not system applications cannot use system API. |
| [13200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) | The screen lock management service is abnormal. |
| 13200004 | The userId is not the same as the caller, and the caller is not authorized. |

