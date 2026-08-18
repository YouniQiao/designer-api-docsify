# IAuthCallback

返回认证结果的回调对象。该接口定义了认证结果的回调方法，用于在认证完成后获取认证结果。应用通过实现onResult方法，可以在认证通过时获取认证令牌，在认证不通过时获取错误码和相关信息。

**起始版本：** 23

<!--Device-userAuth-interface IAuthCallback--><!--Device-userAuth-interface IAuthCallback-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

```TypeScript
```

## onResult

```TypeScript
onResult(result: UserAuthResult): void
```

回调函数，返回认证结果。认证通过时，可以通过UserAuthResult获取到认证通过的令牌信息，用于后续的安全操作验证；认证不通过时，可以通过result字段获取错误码，根据错误码采取相应的处理措施（如提示用户重新认证、引导 用户注册凭据等）。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-IAuthCallback-onResult(result: UserAuthResult): void--><!--Device-IAuthCallback-onResult(result: UserAuthResult): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | [UserAuthResult](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-backgroundtaskmanager-userauthresult-e.md) | 是 |

## onResult

```TypeScript
onResult: AuthCallbackOnResultFunc
```

返回认证结果。认证成功时，可以通过UserAuthResult获取到认证成功的令牌信息。

**类型：** [AuthCallbackOnResultFunc](arkts-userauthentication-userauth-authcallbackonresultfunc-t.md)

**起始版本：** 23

<!--Device-IAuthCallback-onResult: AuthCallbackOnResultFunc--><!--Device-IAuthCallback-onResult: AuthCallbackOnResultFunc-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core
