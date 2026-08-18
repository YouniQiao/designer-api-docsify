# ResultCallback (System API)

```TypeScript
type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void
```

Defines the callback for returning remote authentication results. This type is used in remote authentication scenarios. After the remote authentication is complete, the system invokes this callback to return the authentication result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-userAuth-type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void--><!--Device-userAuth-type ResultCallback = (challenge: Uint8Array, result: UserAuthResult) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |
| result | [UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md) | Yes |
