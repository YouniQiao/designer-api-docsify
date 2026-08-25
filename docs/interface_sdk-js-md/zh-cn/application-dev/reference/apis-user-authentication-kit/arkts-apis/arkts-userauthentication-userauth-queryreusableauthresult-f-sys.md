# queryReusableAuthResult（系统接口）

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## queryReusableAuthResult

```TypeScript
function queryReusableAuthResult(authParam: AuthParam): Uint8Array
```

查询是否有可复用的身份认证结果。该接口用于在发起认证前查询是否存在满足复用条件的认证结果，若存在则直接返回可复用的AuthToken，无需用户再次进行认证交互。

**起始版本：** 20

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [authParam](arkts-userauthentication-useriam-userauthicon-userauthicon-s.md) | [AuthParam](arkts-userauthentication-userauth-authparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
| [12500008](../errorcode-useriam.md#12500008-参数校验失败) |
| [12500017](../errorcode-useriam.md#12500017-复用身份认证结果失败) |
