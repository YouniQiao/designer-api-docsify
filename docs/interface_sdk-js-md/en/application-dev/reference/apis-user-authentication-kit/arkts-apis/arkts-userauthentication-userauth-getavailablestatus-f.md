# getAvailableStatus

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## getAvailableStatus

```TypeScript
function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void
```

Checks whether the specified authentication capability is supported. This API is used to check whether the current device supports the specified authentication type and authentication trust level. It helps an application determine whether the authentication capability is available before initiating authentication, thereby avoiding unnecessary authentication failures. If the query is successful (no error is thrown), the authentication capability is available. If an error is thrown, the application should determine the cause based on the error code and take appropriate measures.

**Since:** 9

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |
| [12500005](../errorcode-useriam.md#12500005-unsupported-authentication-type) |
| [12500006](../errorcode-useriam.md#12500006-unsupported-authentication-trust-level) |
| [12500010](../errorcode-useriam.md#12500010-credential-not-enrolled) |
| [12500013](../errorcode-useriam.md#12500013-password-expired) |
