# UserAuth

Provides APIs for managing the **UserAuth** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md#authinstance)

<!--Device-userAuth-class UserAuth--><!--Device-userAuth-class UserAuth-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
```

## auth

```TypeScript
auth(
      challenge: Uint8Array,
      authType: UserAuthType,
      authTrustLevel: AuthTrustLevel,
      callback: IUserAuthCallback
    ): Uint8Array
```

Starts user authentication. This API uses a callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: UserAuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: UserAuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |
| callback | [IUserAuthCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // Add the logic to be executed when the authentication is successful.
      } else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(`auth onResult failed. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
});
```

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): number
```

Cancels the authentication based on the context ID.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [cancel](arkts-userauthentication-userauth-authinstance-i.md#cancel)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-cancelAuth(contextID: Uint8Array): number--><!--Device-UserAuth-cancelAuth(contextID: Uint8Array): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| contextID | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

// contextId can be obtained via auth(). In this example, it is defined here.
let contextId = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7]);
let auth = new userAuth.UserAuth();
let cancelCode = auth.cancelAuth(contextId);
if (cancelCode == userAuth.ResultCode.SUCCESS) {
  console.info('cancel auth successfully.');
} else {
  console.error('cancel auth failed.');
}
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **UserAuth** instance.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md#getauthinstance)

<!--Device-UserAuth-constructor()--><!--Device-UserAuth-constructor()-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
```

## getAvailableStatus

```TypeScript
getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number
```

Checks whether the specified authentication capability is supported.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAvailableStatus](arkts-userauthentication-userauth-getavailablestatus-f.md#getavailablestatus)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number--><!--Device-UserAuth-getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
if (checkCode == userAuth.ResultCode.SUCCESS) {
  console.info('check auth support successfully.');
} else {
  console.error(`check auth support failed, code = ${checkCode}`);
}
```

## getVersion

```TypeScript
getVersion(): number
```

Obtains the version of this authenticator.

**Since:** 8

**Deprecated since:** 9

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-getVersion(): number--><!--Device-UserAuth-getVersion(): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let version = auth.getVersion();
console.info(`auth version = ${version}`);
```
