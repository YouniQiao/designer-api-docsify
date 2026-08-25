# verifyAuthToken (System API)

## Modules to Import

```TypeScript
import { userAccessCtrl } from 'kits/@kit.UserAuthenticationKit';
```

## verifyAuthToken

```TypeScript
function verifyAuthToken(authToken: Uint8Array, allowableDuration: number): Promise<AuthToken>
```

Verifies an authentication token. This API is used to verify the validity of an **AuthToken**, including the integrity and validity check. After the verification is successful, the detailed information about the parsed **AuthToken** is returned. This API uses a promise to return the result.The integrity check verifies the digital signature of the **AuthToken** to ensure that the token has not been tampered with. The validity check compares the issuance time of the **AuthToken** with the current time and determines whether the token is within the validity period based on the **allowableDuration** parameter.

**Since:** 18

**Required permissions:** ohos.permission.USE_USER_ACCESS_MANAGER

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authToken | Uint8Array | Yes |
| allowableDuration | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AuthToken](arkts-userauthentication-useraccessctrl-authtoken-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |
| [12500015](../errorcode-useriam.md#12500015-authtoken-integrity-check-failed) |
| [12500016](../errorcode-useriam.md#12500016-authtoken-has-expired) |
