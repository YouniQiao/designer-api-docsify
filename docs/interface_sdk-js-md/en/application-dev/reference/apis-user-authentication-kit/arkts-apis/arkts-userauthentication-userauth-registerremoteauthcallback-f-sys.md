# registerRemoteAuthCallback (System API)

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## registerRemoteAuthCallback

```TypeScript
function registerRemoteAuthCallback(callback: IRemoteAuthCallback): void
```

Registers a remote authentication callback. This API is used to register a callback in remote authentication scenarios. After the callback is registered, the system can obtain the page parameters required for remote authentication through the callback and receive the authentication result after the authentication is complete. Repeated registration is not allowed. If the callback is not used, call [unregisterRemoteAuthCallback](arkts-userauthentication-userauth-unregisterremoteauthcallback-f-sys.md) to unregister it to avoid callback release failures.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-userAuth-function registerRemoteAuthCallback(callback: IRemoteAuthCallback): void--><!--Device-userAuth-function registerRemoteAuthCallback(callback: IRemoteAuthCallback): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [IRemoteAuthCallback](arkts-userauthentication-userauth-iremoteauthcallback-i-sys.md) | Yes | Remote authentication callback API. It contains the callback function for obtaining authentication page parameters and returning the authentication result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Called by non-system application. |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

