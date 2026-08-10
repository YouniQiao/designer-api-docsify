# setScreenLockAuthState (System API)

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## setScreenLockAuthState

```TypeScript
function setScreenLockAuthState(state: AuthState, userId: int, authToken: Uint8Array): Promise<boolean>
```

Set the screen lock authentication state for os account local userId.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK_INNER

<!--Device-screenLock-function setScreenLockAuthState(state: AuthState, userId: int, authToken: Uint8Array): Promise<boolean>--><!--Device-screenLock-function setScreenLockAuthState(state: AuthState, userId: int, authToken: Uint8Array): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [AuthState](arkts-basicservices-screenlock-authstate-e-sys.md) | Yes | the screen lock authentication state. |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Os account local userId. |
| authToken | Uint8Array | Yes | the authentication token for this state |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 201 | permission denied. |
| 202 | permission verification failed, application which is not a system application uses system API. |
| 13200002 | the screenlock management service is abnormal. |

