# requestStrongAuth (System API)

## Modules to Import

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## requestStrongAuth

```TypeScript
function requestStrongAuth(reasonFlag: StrongAuthReasonFlags, userId: int): Promise<void>
```

Request strong authentication for os account local userId.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_SCREEN_LOCK

<!--Device-screenLock-function requestStrongAuth(reasonFlag: StrongAuthReasonFlags, userId: int): Promise<void>--><!--Device-screenLock-function requestStrongAuth(reasonFlag: StrongAuthReasonFlags, userId: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.ScreenLock

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| reasonFlag | [StrongAuthReasonFlags](arkts-basicservices-screenlock-strongauthreasonflags-e-sys.md) | Yes | The strong authentication reason flag. |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Os account local userId. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 201 | permission denied. |
| 202 | permission verification failed. A non-system application calls a system API. |
| 13200002 | the screenlock management service is abnormal. |

