# AuthCallbackOnResultFunc

```TypeScript
type AuthCallbackOnResultFunc = (result: UserAuthResult) => void
```

Called to return the authentication result. If the authentication is successful,UserAuthResult contains the token information.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-userAuth-type AuthCallbackOnResultFunc = (result: UserAuthResult) => void--><!--Device-userAuth-type AuthCallbackOnResultFunc = (result: UserAuthResult) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md) | Yes | Authentication result information. |

