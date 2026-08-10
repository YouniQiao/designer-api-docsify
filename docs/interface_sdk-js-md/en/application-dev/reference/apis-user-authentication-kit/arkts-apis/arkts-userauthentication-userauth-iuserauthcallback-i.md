# IUserAuthCallback

返回认证结果的回调对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthEvent](arkts-userauthentication-userauth-authevent-i.md)

<!--Device-userAuth-interface IUserAuthCallback--><!--Device-userAuth-interface IUserAuthCallback-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## onAcquireInfo

```TypeScript
onAcquireInfo?: (module: number, acquire: number, extraInfo: any) => void
```

回调函数，返回认证过程中的提示信息，非必须实现。

- **module**: 发送提示信息的模块标识。  
- **acquire**: 认证执过程中的提示信息。  
- **extraInfo**: 预留字段。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthEvent.callback](arkts-userauthentication-userauth-authevent-i.md#callback)

<!--Device-IUserAuthCallback-onAcquireInfo?: (module: number, acquire: number, extraInfo: any) => void--><!--Device-IUserAuthCallback-onAcquireInfo?: (module: number, acquire: number, extraInfo: any) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| module | number | Yes |  |
| acquire | number | Yes |  |
| extraInfo | any | Yes |  |

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
      }  else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(`auth onResult failed. Code: ${error?.code}, message: ${error?.message}`);
    }
  },
  onAcquireInfo: (module, acquire, extraInfo : userAuth.AuthResult) => {
    try {
      console.info('auth onAcquireInfo successfully.');
    } catch (error) {
      console.error(`auth onAcquireInfo failed. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
});
```

## onResult

```TypeScript
onResult: (result: number, extraInfo: AuthResult) => void
```

回调函数，返回认证结果。

- **result**: 认证结果，参见[ResultCode](arkts-userauthentication-userauth-resultcode-e.md)。  
- **extraInfo**: 扩展信息，不同情况下的具体信息。如果身份验证通过，则在extraInfo中返回用户认证令牌；如果身份验证失败，则在extraInfo中返回剩余的用户认证次数；如果身份验证执行器被锁定，则在  
extraInfo中返回冻结时间，类型为[AuthResult](arkts-userauthentication-userauth-authresult-i.md)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthEvent.callback](arkts-userauthentication-userauth-authevent-i.md#callback)

<!--Device-IUserAuthCallback-onResult: (result: number, extraInfo: AuthResult) => void--><!--Device-IUserAuthCallback-onResult: (result: number, extraInfo: AuthResult) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | number | Yes |  |
| extraInfo | [AuthResult](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-appaccount-authresult-i.md) | Yes |  |

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
      }  else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(`auth onResult failed. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
});
```

