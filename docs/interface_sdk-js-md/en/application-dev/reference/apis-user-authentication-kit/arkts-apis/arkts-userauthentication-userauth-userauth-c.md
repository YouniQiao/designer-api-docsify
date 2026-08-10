# UserAuth

认证器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthInstance](arkts-userauthentication-userauth-authinstance-i.md)

<!--Device-userAuth-class UserAuth--><!--Device-userAuth-class UserAuth-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## auth

```TypeScript
auth(
      challenge: Uint8Array,
      authType: UserAuthType,
      authTrustLevel: AuthTrustLevel,
      callback: IUserAuthCallback
    ): Uint8Array
```

执行用户认证，使用回调函数返回结果。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthInstance.start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: UserAuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: UserAuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| challenge | Uint8Array | Yes | 挑战值，可以传Uint8Array([])。 |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes | 认证信任等级。 |
| callback | [IUserAuthCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | ContextId，作为取消认证[cancelAuth]{ |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // Add the logic to be executed when the authentication is successful.
      } else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(`auth onResult failed. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
});
```

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): number
```

表示通过contextID取消本次认证。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthInstance.cancel](arkts-userauthentication-userauth-authinstance-i.md#cancel)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-cancelAuth(contextID: Uint8Array): number--><!--Device-UserAuth-cancelAuth(contextID: Uint8Array): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contextID | Uint8Array | Yes | 上下文的标识，通过[auth](arkts-userauthentication-userauth-userauth-c.md#auth)接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 取消认证的结果，结果为SUCCESS时表示取消成功，其他返回值参见[ResultCode]{ |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

// contextId can be obtained via auth(). In this example, it is defined here.
let contextId = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7]);
let auth = new userAuth.UserAuth();
let cancelCode = auth.cancelAuth(contextId);
if (cancelCode == userAuth.ResultCode.SUCCESS) {
  console.info('cancel auth successfully.');
} else {
  console.error('cancel auth failed.');
}
```

## constructor

```TypeScript
constructor()
```

创建认证器对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md#getauthinstance)

<!--Device-UserAuth-constructor()--><!--Device-UserAuth-constructor()-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
```

## getAvailableStatus

```TypeScript
getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number
```

查询指定类型和等级的认证能力是否支持。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.getAvailableStatus](arkts-userauthentication-userauth-getavailablestatus-f.md#getavailablestatus)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number--><!--Device-UserAuth-getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes | 认证类型，当前支持FACE和FINGERPRINT。 |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes | 认证信任等级。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 查询结果，结果为SUCCESS时表示支持，其他返回值参见[ResultCode]{ |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
if (checkCode == userAuth.ResultCode.SUCCESS) {
  console.info('check auth support successfully.');
} else {
  console.error(`check auth support failed, code = ${checkCode}`);
}
```

## getVersion

```TypeScript
getVersion(): number
```

获取认证器的版本信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-getVersion(): number--><!--Device-UserAuth-getVersion(): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | 认证器版本信息。 |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let version = auth.getVersion();
console.info(`auth version = ${version}`);
```

