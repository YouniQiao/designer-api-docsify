# AuthTipCallback

```TypeScript
type AuthTipCallback = (authTipInfo: AuthTipInfo) => void
```

Defines the callback to return the intermediate authentication status. This callback is used to obtain various intermediate status information during authentication, including authentication failure, lockout, and loading and release of the authentication screen. By subscribing to these intermediate statuses, the application can provide more refined user interaction and status management during the authentication process.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-userAuth-type AuthTipCallback = (authTipInfo: AuthTipInfo) => void--><!--Device-userAuth-type AuthTipCallback = (authTipInfo: AuthTipInfo) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authTipInfo | [AuthTipInfo](arkts-userauthentication-userauth-authtipinfo-i.md) | Yes |
