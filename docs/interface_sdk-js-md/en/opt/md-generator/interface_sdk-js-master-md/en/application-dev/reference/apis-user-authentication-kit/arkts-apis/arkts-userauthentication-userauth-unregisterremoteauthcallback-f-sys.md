# unregisterRemoteAuthCallback (System API)

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## unregisterRemoteAuthCallback

```TypeScript
function unregisterRemoteAuthCallback(): void
```

Unregisters the remote authentication callback. This API is used to unregister a previously registered remote authentication callback. After unregistration, the system no longer receives remote authentication page parameter requests or authentication result notification.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**Model restriction:** This API can be used only in the stage model.

<!--Device-userAuth-function unregisterRemoteAuthCallback(): void--><!--Device-userAuth-function unregisterRemoteAuthCallback(): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12500002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  userAuth.unregisterRemoteAuthCallback();
  console.info('Remote auth callback unregistered successfully');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`failed to unregister remote auth callback. Code is ${err?.code}, message is ${err?.message}`);
}
```
