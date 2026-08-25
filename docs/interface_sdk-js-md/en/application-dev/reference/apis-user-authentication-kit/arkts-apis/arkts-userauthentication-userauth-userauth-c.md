# UserAuth

Provides APIs for managing the **UserAuth** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
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

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| challenge | Uint8Array | Yes |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |
| callback | [IUserAuthCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Uint8Array |

## cancelAuth

```TypeScript
cancelAuth(contextID: Uint8Array): number
```

Cancels the authentication based on the context ID.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [cancel](arkts-userauthentication-userauth-authinstance-i.md#cancel)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| contextID | Uint8Array | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **UserAuth** instance.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## getAvailableStatus

```TypeScript
getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number
```

Checks whether the specified authentication capability is supported.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getAvailableStatus](arkts-userauthentication-userauth-getavailablestatus-f.md)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | Yes |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getVersion

```TypeScript
getVersion(): number
```

Obtains the version of this authenticator.

**Since:** 8

**Deprecated since:** 9

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
