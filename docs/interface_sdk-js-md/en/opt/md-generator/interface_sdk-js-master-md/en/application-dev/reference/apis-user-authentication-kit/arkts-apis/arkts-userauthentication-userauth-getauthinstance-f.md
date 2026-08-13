# getAuthInstance

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## getAuthInstance

```TypeScript
function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance
```

Obtains an **AuthInstance** instance for user authentication. > **NOTE：**> > Each **AuthInstance** can perform authentication only once. To perform authentication again, obtain a new > **AuthInstance**.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [getUserAuthInstance](arkts-userauthentication-userauth-getuserauthinstance-f.md#getUserAuthInstance)

<!--Device-userAuth-function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance--><!--Device-userAuth-function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500006](../errorcode-useriam.md#12500006-unsupported-authentication-trust-level) |
| [12500005](../errorcode-useriam.md#12500005-unsupported-authentication-type) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  console.info('get auth instance successfully.');
} catch (error) {
  console.error(`get auth instance failed. Code: ${error?.code}, message: ${error?.message}`);
}
```
