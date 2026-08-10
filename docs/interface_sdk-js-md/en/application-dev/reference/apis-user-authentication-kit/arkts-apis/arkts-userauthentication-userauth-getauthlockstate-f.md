# getAuthLockState

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## getAuthLockState

```TypeScript
function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>
```

查询指定认证类型的冻结状态，使用Promise异步回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-userAuth-function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>--><!--Device-userAuth-function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes | 认证类型，用于指定查询的凭据类型。支持FACE（人脸）、FINGERPRINT（指纹）、PIN（密码）等。根据业务场景安全需求选择合适的认证类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AuthLockState&gt; | Promise对象，当查询成功时，返回值为指定认证类型的身份认证冻结状态。失败时报错。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12500010 | The type of credential has not been enrolled. |
| 12500008 | The parameter is out of range. |
| 201 | Permission denied. |
| 12500005 | The authentication type is not supported. |
| 12500002 | General operation error. |

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

