# UserAuth

认证器对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md)

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

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

**起始版本：** 8

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

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): number
```

表示通过contextID取消本次认证。

**起始版本：** 8

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

## constructor

```TypeScript
constructor()
```

创建认证器对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md)

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## getAvailableStatus

```TypeScript
getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number
```

查询指定类型和等级的认证能力是否支持。

**起始版本：** 8

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

## getVersion

```TypeScript
getVersion(): number
```

获取认证器的版本信息。

**起始版本：** 8

**废弃版本：** 9

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 |
| --- |
| number |
