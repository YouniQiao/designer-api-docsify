# @ohos.userIAM.userAccessCtrl

The **userAccessCtrl** module is a core component of the OpenHarmony user identity and access management (UserIAM) system. It is dedicated to the verification and management of authentication tokens. This module provides APIs for verifying authentication tokens (**AuthToken**). It can parse and verify user authentication results and return detailed authentication information. This module applies to the following scenarios: - System-level applications need to verify the validity of user authentication tokens to ensure access security. - Detailed information about the authentication token needs to be obtained, such as the authentication type, trust level, and user ID, for precise user identity identification. - Access control decisions need to be made based on the authentication result to implement fine-grained permission management.

**Since:** 23

<!--Device-unnamed-declare namespace userAccessCtrl--><!--Device-unnamed-declare namespace userAccessCtrl-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [verifyAuthToken](arkts-userauthentication-useraccessctrl-verifyauthtoken-f-sys.md#verifyauthtoken-system-api) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthToken](arkts-userauthentication-useraccessctrl-authtoken-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthTokenType](arkts-userauthentication-useraccessctrl-authtokentype-e-sys.md) |
<!--DelEnd-->
