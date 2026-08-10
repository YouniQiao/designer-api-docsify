# IAuthCallback

返回认证结果的回调对象。该接口定义了认证结果的回调方法，用于在认证完成后获取认证结果。应用通过实现onResult方法，可以在认证通过时获取认证令牌，在认证不通过时获取错误码和相关信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-userAuth-interface IAuthCallback--><!--Device-userAuth-interface IAuthCallback-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

## 导入模块

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## onResult

```TypeScript
onResult(result: UserAuthResult): void
```

回调函数，返回认证结果。认证通过时，可以通过UserAuthResult获取到认证通过的令牌信息，用于后续的安全操作验证；认证不通过时，可以通过result字段获取错误码，根据错误码采取相应的处理措施（如提示用户重新认证、引导用户注册凭据等）。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-IAuthCallback-onResult(result: UserAuthResult): void--><!--Device-IAuthCallback-onResult(result: UserAuthResult): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md) | 是 | 认证结果。包含认证结果码、认证令牌（成功时）、认证类型和凭据状态等信息。应用应检查result.result字段判断认证是否成功： &lt;br&gt;- 若result.result为SUCCESS(12500000)，表示认证通过，可使用result.token进行后续操作。 &lt;br&gt;- 若result.result为其他值，表示认证不通过，应根据具体错误码进行处理。 |

## onResult

```TypeScript
onResult: AuthCallbackOnResultFunc
```

返回认证结果。认证成功时，可以通过UserAuthResult获取到认证成功的令牌信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-IAuthCallback-onResult: AuthCallbackOnResultFunc--><!--Device-IAuthCallback-onResult: AuthCallbackOnResultFunc-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

