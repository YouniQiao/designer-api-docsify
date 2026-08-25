# getAuthLockState

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## getAuthLockState

```TypeScript
function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>
```

查询指定认证类型的冻结状态，使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthLockState](arkts-userauthentication-userauth-authlockstate-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
| [12500005](../errorcode-useriam.md#12500005-认证类型不支持) |
| [12500008](../errorcode-useriam.md#12500008-参数校验失败) |
| [12500010](../errorcode-useriam.md#12500010-该类型的凭据没有录入) |
