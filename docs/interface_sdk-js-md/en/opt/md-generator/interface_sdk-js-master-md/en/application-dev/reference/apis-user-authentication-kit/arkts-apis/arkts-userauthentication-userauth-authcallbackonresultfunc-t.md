# AuthCallbackOnResultFunc

```TypeScript
type AuthCallbackOnResultFunc = (result: UserAuthResult) => void
```

Called to return the authentication result. If the authentication is successful, UserAuthResult contains the token information.

**Since:** 23

**Deprecated since:** -1

<!--Device-userAuth-type AuthCallbackOnResultFunc = (result: UserAuthResult) => void--><!--Device-userAuth-type AuthCallbackOnResultFunc = (result: UserAuthResult) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | [UserAuthResult](arkts-userauthentication-userauth-userauthresult-i.md) | Yes |
