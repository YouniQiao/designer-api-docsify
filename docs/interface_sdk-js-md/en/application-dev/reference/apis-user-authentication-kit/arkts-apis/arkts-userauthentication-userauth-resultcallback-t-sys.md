# ResultCallback (System API)

```TypeScript
type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void
```

Defines the callback for returning remote authentication results. This type is used in remote authentication scenarios. After the remote authentication is complete, the system invokes this callback to return the authentication result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-userAuth-type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void--><!--Device-userAuth-type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| challenge | Uint8Array | Yes | Challenge value. It is a one-time random number used to prevent replay attacks, which is consistent with the challenge value passed during authentication initiation. |
| result | UserAuthResult | Yes | User authentication result, including the authentication result code and authentication token. |

