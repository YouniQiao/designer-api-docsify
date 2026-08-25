# getEnrolledState

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## getEnrolledState

```TypeScript
function getEnrolledState(authType: UserAuthType): EnrolledState
```

Obtains the credential state. This API is used to obtain the credential enrollment information of a specified authentication type, including the credential digest and quantity. The application can compare the current query result with the previously saved result to determine whether the user has added or deleted credentials, and then perform corresponding service processing.

**Since:** 12

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EnrolledState](arkts-userauthentication-userauth-enrolledstate-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |
| [12500005](../errorcode-useriam.md#12500005-unsupported-authentication-type) |
| [12500010](../errorcode-useriam.md#12500010-credential-not-enrolled) |
