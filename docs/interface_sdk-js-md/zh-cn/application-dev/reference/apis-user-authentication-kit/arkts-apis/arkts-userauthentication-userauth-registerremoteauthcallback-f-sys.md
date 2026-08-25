# registerRemoteAuthCallback（系统接口）

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## registerRemoteAuthCallback

```TypeScript
function registerRemoteAuthCallback(callback: IRemoteAuthCallback): void
```

注册远程认证回调。该接口用于在远程认证场景下注册回调接口，注册后系统可通过回调获取远程认证所需的页面参数，并在认证完成后接收认证结果。不允许重复注册，在不使用时应调用 [unregisterRemoteAuthCallback](arkts-userauthentication-userauth-unregisterremoteauthcallback-f-sys.md)取消注册，避免回调无法释放。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [IRemoteAuthCallback](arkts-userauthentication-userauth-iremoteauthcallback-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
