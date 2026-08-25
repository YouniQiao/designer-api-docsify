# queryReusableAuthResult (System API)

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## queryReusableAuthResult

```TypeScript
function queryReusableAuthResult(authParam: AuthParam): Uint8Array
```

Queries whether there is any reusable identity authentication result. This API is used to query whether there is an authentication result that meets the reuse conditions before authentication is initiated. If such a result exists, the **AuthToken** that can be reused is returned directly, and the user does not need to perform authentication again.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_USER_AUTH_INTERNAL

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [authParam](arkts-userauthentication-useriam-userauthicon-userauthicon-s.md) | [AuthParam](arkts-userauthentication-userauth-authparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |
| [12500008](../errorcode-useriam.md#12500008-parameter-verification-failed) |
| [12500017](../errorcode-useriam.md#12500017-authentication-result-reuse-failed) |
