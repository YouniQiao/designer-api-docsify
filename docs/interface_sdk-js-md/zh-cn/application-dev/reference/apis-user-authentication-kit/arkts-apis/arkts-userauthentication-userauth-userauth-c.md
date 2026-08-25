# UserAuth

认证器对象。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md)

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
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

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [start](arkts-userauthentication-userauth-authinstance-i.md#start)

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| challenge | Uint8Array | 是 |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | 是 |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | 是 |
| callback | [IUserAuthCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**示例**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // 此处添加认证成功逻辑。
      } else {
        // 此处添加认证失败逻辑。
      }
    } catch (error) {
      console.error(`Failed to auth onResult. Code: ${error.code}, message: ${error.message}`);
    }
  }
});
```

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): number
```

表示通过contextID取消本次认证。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [cancel](arkts-userauthentication-userauth-authinstance-i.md#cancel)

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| contextID | Uint8Array | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

// contextId可通过auth接口获取，此处直接定义。
let contextId = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7]);
let auth = new userAuth.UserAuth();
let cancelCode = auth.cancelAuth(contextId);
if (cancelCode == userAuth.ResultCode.SUCCESS) {
  console.info('cancel auth successfully.');
} else {
  console.error(`Failed to cancel auth.`);
}
```

## constructor

```TypeScript
constructor()
```

创建认证器对象。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md)

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**示例**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
```

## getAvailableStatus

```TypeScript
getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number
```

查询指定类型和等级的认证能力是否支持。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [getAvailableStatus](arkts-userauthentication-userauth-getavailablestatus-f.md)

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | 是 |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
  console.info('current auth trust level is supported');
} catch (error) {
  console.error(`Failed to check auth trust level. Code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
if (checkCode == userAuth.ResultCode.SUCCESS) {
  console.info('check auth support successfully.');
} else {
  console.error(`Failed to check auth support. Code: ${checkCode}`);
}
```

## getVersion

```TypeScript
getVersion(): number
```

获取认证器的版本信息。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let version = auth.getVersion();
console.info(`auth version = ${version}`);
```
