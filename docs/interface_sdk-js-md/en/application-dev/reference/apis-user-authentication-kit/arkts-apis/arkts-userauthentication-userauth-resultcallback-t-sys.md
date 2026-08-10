# ResultCallback (System API)

```TypeScript
type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void
```

返回远程认证结果的回调函数类型。该类型用于远程认证场景，在远程认证完成后，系统会调用此回调函数返回认证结果。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-userAuth-type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void--><!--Device-userAuth-type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| challenge | Uint8Array | Yes | 挑战值。用于防止重放攻击的一次性随机数，与发起认证时传入的challenge值一致。 |
| result | [UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md) | Yes | 用户认证结果。包含认证结果码、认证令牌等信息。 |

