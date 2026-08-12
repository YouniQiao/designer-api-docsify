# getAuthLockState

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## getAuthLockState

```TypeScript
function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>
```

Queries the lockout state of the specified authentication type. This API uses a promise to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-userAuth-function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>--><!--Device-userAuth-function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes | Authentication type, which is used to specify the credential type to query. Supported values: **FACE**, **FINGERPRINT**, and **PIN**. Select an appropriate authentication type based on the security requirements of the service scenario. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AuthLockState](arkts-userauthentication-userauth-authlockstate-i.md)&gt; | Promise used to return the result. An error is reported when the operation fails. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12500010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500010-credential-not-enrolled) | The type of credential has not been enrolled. |
| [12500008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500008-parameter-verification-failed) | The parameter is out of range. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12500005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500005-unsupported-authentication-type) | The authentication type is not supported. |
| [12500002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) | General operation error. |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let queryType = userAuth.UserAuthType.PIN;
let authLockState : userAuth.AuthLockState = {
  isLocked : false,
  remainingAuthAttempts : 0,
  lockoutDuration : 0
}

userAuth.getAuthLockState(queryType)
  .then((result : userAuth.AuthLockState) => {
    authLockState = result;
    console.info(`get auth lock state success, authLockState is: ${JSON.stringify(authLockState)}`);
  })
  .catch((err : BusinessError) => {
    console.info(`get auth lock state failed, err code is : ${err?.code}, err message is : ${err?.message}`);
  })
```

