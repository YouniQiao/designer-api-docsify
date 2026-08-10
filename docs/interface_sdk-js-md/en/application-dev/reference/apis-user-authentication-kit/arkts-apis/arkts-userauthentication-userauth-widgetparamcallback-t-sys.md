# WidgetParamCallback (System API)

```TypeScript
type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam
```

获取远程认证页面参数的回调函数类型。该类型用于远程认证场景，在需要获取远程认证界面的配置参数时，系统会调用此回调函数。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-userAuth-type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam--><!--Device-userAuth-type WidgetParamCallback = (challenge: Uint8Array) => WidgetParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| challenge | Uint8Array | Yes | 随机挑战值，可用于防重放攻击。最大长度为32字节，可传Uint8Array([])。建议使用 [加解密算法库框架](../../apis-crypto-architecture-kit/arkts-apis/arkts-security-cryptoframework.md/arkts-security-cryptoframework.md)生成的随机数作为挑战值，以增强安全性。 |

**Return value:**

| Type | Description |
| --- | --- |
| [WidgetParam](arkts-userauthentication-userauth-widgetparam-i-sys.md) | 用户认证界面配置参数。包含认证界面的标题、导航按钮文本等配置信息。 |

