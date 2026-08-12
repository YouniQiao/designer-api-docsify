# AuthInstance

Implements user authentication.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md#UserAuthInstance)

<!--Device-userAuth-interface AuthInstance--><!--Device-userAuth-interface AuthInstance-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## cancel

```TypeScript
cancel: () => void
```

Cancels this authentication.

> **NOTE：**
> 
> Use the obtained [AuthInstance](#AuthInstance) object to call this API to cancel authentication.
> This [AuthInstance](#AuthInstance) must be the object that is currently performing
> authentication.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [cancel](arkts-userauthentication-userauth-userauthinstance-i.md#cancel)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-AuthInstance-cancel: () => void--><!--Device-AuthInstance-cancel: () => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12500002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.cancel();
  console.info('cancel auth successfully.');
} catch (error) {
  console.error(`cancel auth failed. Code: ${error?.code}, message: ${error?.message}`);
}
```

## off

```TypeScript
off: (name: AuthEventKey) => void
```

Unsubscribes from the user authentication events of the specified type.

- **name**: indicates the authentication event type. The value **result** means to unsubscribe from the  
authentication result, and the value **tip** means to unsubscribe from the authentication tip information. For details, see [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md#AuthEventKey).

> **NOTE：**
> 
> The [AuthInstance](#AuthInstance) instance used to invoke this API must be the one used to
> subscribe to the event.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [off](#off)

<!--Device-AuthInstance-off: (name: AuthEventKey) => void--><!--Device-AuthInstance-off: (name: AuthEventKey) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12500002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // Subscribe to the authentication result.
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`result: ${result.result}`);
    }
  });
  // Unsubscribe from the authentication result.
  auth.off('result');
  console.info('cancel subscribe authentication event successfully.');
} catch (error) {
  console.error(`cancel subscribe authentication event failed. Code: ${error?.code}, message: ${error?.message}`);
  // do error.
}
```

## on

```TypeScript
on: (name: AuthEventKey, callback: AuthEvent) => void
```

Subscribes to the user authentication events of the specified type.

- **name**: indicates the authentication event type. The value **result** means that the callback returns the  
authentication result, and the value **tip** means that the callback returns the authentication tip information.For details, see [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md#AuthEventKey).  
- **callback**: callback used to return the authentication result or tip information. For details, see  
[AuthEvent](arkts-userauthentication-userauth-authevent-i.md#AuthEvent).

> **NOTE：**
> 
> Use the [AuthInstance](#AuthInstance) instance obtained to call this API.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [on](userAuth.UserAuthInstance.on)

<!--Device-AuthInstance-on: (name: AuthEventKey, callback: AuthEvent) => void--><!--Device-AuthInstance-on: (name: AuthEventKey, callback: AuthEvent) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | [AuthEventKey](arkts-userauthentication-userauth-autheventkey-t.md) | Yes |
| callback | [AuthEvent](arkts-userauthentication-userauth-authevent-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12500002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;
try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  // Subscribe to the authentication result.
  auth.on('result', {
    callback: (result: userAuth.AuthResultInfo) => {
      console.info(`result: ${result.result}`);
    }
  });
  // Subscribe to authentication tip information.
  auth.on('tip', {
    callback : (result : userAuth.TipInfo) => {
      switch (result.tip) {
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_BRIGHT:
          // Do something.
          break;
        case userAuth.FaceTips.FACE_AUTH_TIP_TOO_DARK:
          // Do something.
          break;
        default:
          // do others.
      }
    }
  } as userAuth.AuthEvent);
  auth.start();
  console.info('auth start successfully.');
} catch (error) {
  console.error(`auth failed. Code: ${error?.code}, message: ${error?.message}`);
  // do error.
}
```

## start

```TypeScript
start: () => void
```

Starts authentication.

> **NOTE：**
> 
> Use the obtained [AuthInstance](#AuthInstance) object to call this API for authentication.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [start](arkts-userauthentication-userauth-userauthinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-AuthInstance-start: () => void--><!--Device-AuthInstance-start: () => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12500010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500010-credential-not-enrolled) |
| [12500009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500009-authentication-locked) |
| [12500006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500006-unsupported-authentication-trust-level) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12500007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500007-authentication-service-is-busy) |
| [12500004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500004-authentication-timed-out) |
| [12500005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500005-unsupported-authentication-type) |
| [12500002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |
| [12500003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500003-authentication-canceled) |
| [12500001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500001-authentication-failed) |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let challenge = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8]);
let authType = userAuth.UserAuthType.FACE;
let authTrustLevel = userAuth.AuthTrustLevel.ATL1;

try {
  let auth = userAuth.getAuthInstance(challenge, authType, authTrustLevel);
  auth.start();
  console.info('auth start successfully.');
} catch (error) {
  console.error(`auth failed. Code: ${error?.code}, message: ${error?.message}`);
}
```
