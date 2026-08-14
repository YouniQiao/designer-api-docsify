# getAuthenticator

## Modules to Import

```TypeScript
import { userAuth } from 'userAuth';
```

## getAuthenticator

```TypeScript
function getAuthenticator(): Authenticator
```

Obtains an **Authenticator** instance for user authentication.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md#getAuthInstance)

<!--Device-userAuth-function getAuthenticator(): Authenticator--><!--Device-userAuth-function getAuthenticator(): Authenticator-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Return value:**

| Type | Description |
| --- | --- |
| Authenticator | Authenticator** instance obtained. |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
```

