# Authenticator

认证器对象。

**起始版本：** 6

**废弃版本：** 8

**替代接口：** [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md)

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## execute

```TypeScript
execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void
```

执行用户认证，使用callback方式作为异步方法。

**起始版本：** 6

**废弃版本：** 8

**替代接口：** [start](arkts-userauthentication-userauth-authinstance-i.md#start)

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AuthType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |
| level | [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

## execute

```TypeScript
execute(type: AuthType, level: SecureLevel): Promise<number>
```

执行用户认证，使用promise方式作为异步方法。

**起始版本：** 6

**废弃版本：** 8

**替代接口：** [start](arkts-userauthentication-userauth-authinstance-i.md#start)

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AuthType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |
| level | [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
