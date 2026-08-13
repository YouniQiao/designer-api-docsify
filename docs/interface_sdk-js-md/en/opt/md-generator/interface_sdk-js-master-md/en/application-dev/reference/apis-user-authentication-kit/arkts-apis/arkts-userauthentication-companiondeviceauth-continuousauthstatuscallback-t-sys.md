# ContinuousAuthStatusCallback (System API)

```TypeScript
type ContinuousAuthStatusCallback = (isAuthPassed: boolean, authTrustLevel?: UserAuth.AuthTrustLevel) => void
```

Defines the callback triggered for receiving notifications of continuous authentication status changes. When the authentication status of a companion device changes, the system applies the current authentication result and authentication reliability level through this callback notification.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-type ContinuousAuthStatusCallback = (isAuthPassed: boolean, authTrustLevel?: UserAuth.AuthTrustLevel) => void--><!--Device-companionDeviceAuth-type ContinuousAuthStatusCallback = (isAuthPassed: boolean, authTrustLevel?: UserAuth.AuthTrustLevel) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isAuthPassed | boolean | Yes |
| authTrustLevel | UserAuth.AuthTrustLevel | No |
