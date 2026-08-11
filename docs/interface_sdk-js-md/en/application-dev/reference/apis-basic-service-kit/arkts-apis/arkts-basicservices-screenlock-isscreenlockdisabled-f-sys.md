# isScreenLockDisabled (System API)

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## isScreenLockDisabled

```TypeScript
function isScreenLockDisabled(userId: int): boolean
```

Check whether screen lock is disabled for os account local userId.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK

<!--Device-screenLock-function isScreenLockDisabled(userId: int): boolean--><!--Device-screenLock-function isScreenLockDisabled(userId: int): boolean-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Os account local userId. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | whether screen lock is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |
| [13200002](../../apis-basic-services-kit/errorcode-screenlock.md#13200002-screen-lock-management-service-is-abnormal) | the screenlock management service is abnormal. |

