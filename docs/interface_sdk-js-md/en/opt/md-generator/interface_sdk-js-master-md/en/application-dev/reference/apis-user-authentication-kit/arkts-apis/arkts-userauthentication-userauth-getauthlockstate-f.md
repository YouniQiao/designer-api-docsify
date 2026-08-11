# getAuthLockState

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## getAuthLockState

```TypeScript
function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>
```

Queries the lockout state of the specified authentication type. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-userAuth-function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>--><!--Device-userAuth-function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;AuthLockState&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12500010](../errorcode-useriam.md#12500010-credential-not-enrolled) |
| [12500008](../errorcode-useriam.md#12500008-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12500005](../errorcode-useriam.md#12500005-unsupported-authentication-type) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

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
  .then((result: userAuth.AuthLockState) => {
    authLockState = result;
    console.info('get auth lock state successfully.');
  })
  .catch((err: BusinessError) => {
    console.error(`get auth lock state failed, err code is : ${err?.code}, err message is : ${err?.message}`);
  })
```
