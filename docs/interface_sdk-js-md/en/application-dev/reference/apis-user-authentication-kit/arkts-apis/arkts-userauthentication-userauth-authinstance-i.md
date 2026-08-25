# AuthInstance

Implements user authentication.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## cancel

```TypeScript
cancel: () => void
```

Cancels this authentication.

> **NOTE：**&gt;
> Use the obtained [AuthInstance](#authinstance) object to call this API to cancel authentication.
> This [AuthInstance](#authinstance) must be the object that is currently performing
> authentication.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [cancel](arkts-userauthentication-userauth-userauthinstance-i.md#cancel)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## off

```TypeScript
off: (name: AuthEventKey) => void
```

Unsubscribes from the user authentication events of the specified type.  
- **name**: indicates the authentication event type. The value **result** means to unsubscribe from the  
authentication result, and the value **tip** means to unsubscribe from the authentication tip information. For details, see [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md).

> **NOTE：**&gt;
> The [AuthInstance](#authinstance) instance used to invoke this API must be the one used to
> subscribe to the event.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [off](arkts-userauthentication-userauth-userauthinstance-i.md#offresult)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## on

```TypeScript
on: (name: AuthEventKey, callback: AuthEvent) => void
```

Subscribes to the user authentication events of the specified type.  
- **name**: indicates the authentication event type. The value **result** means that the callback returns the  
authentication result, and the value **tip** means that the callback returns the authentication tip information. For details, see [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md).  
- **callback**: callback used to return the authentication result or tip information. For details, see  
[AuthEvent](arkts-userauthentication-userauth-authevent-i.md).

> **NOTE：**&gt;
> Use the [AuthInstance](#authinstance) instance obtained to call this API.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [on](arkts-userauthentication-userauth-userauthinstance-i.md#onresult)

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md) | Yes |
| callback | [AuthEvent](arkts-userauthentication-userauth-authevent-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## start

```TypeScript
start: () => void
```

Starts authentication.

> **NOTE：**&gt;
> Use the obtained [AuthInstance](#authinstance) object to call this API for authentication.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [start](arkts-userauthentication-userauth-userauthinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500001](../errorcode-useriam.md#12500001-authentication-failed) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |
| [12500003](../errorcode-useriam.md#12500003-authentication-canceled) |
| [12500004](../errorcode-useriam.md#12500004-authentication-timed-out) |
| [12500005](../errorcode-useriam.md#12500005-unsupported-authentication-type) |
| [12500006](../errorcode-useriam.md#12500006-unsupported-authentication-trust-level) |
| [12500007](../errorcode-useriam.md#12500007-authentication-service-is-busy) |
| [12500009](../errorcode-useriam.md#12500009-authentication-locked) |
| [12500010](../errorcode-useriam.md#12500010-credential-not-enrolled) |
