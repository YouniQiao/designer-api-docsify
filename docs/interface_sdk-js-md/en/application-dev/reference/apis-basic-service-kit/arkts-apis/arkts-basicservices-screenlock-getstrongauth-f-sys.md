# getStrongAuth (System API)

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## getStrongAuth

```TypeScript
function getStrongAuth(userId: int): int
```

Obtain strong authentication reason flags for os account local userId.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK

<!--Device-screenLock-function getStrongAuth(userId: int): int--><!--Device-screenLock-function getStrongAuth(userId: int): int-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Os account local userId. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | the strong authentication reason flags. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 201 | permission denied. |
| 202 | permission verification failed. A non-system application calls a system API. |
| 13200002 | the screenlock management service is abnormal. |

