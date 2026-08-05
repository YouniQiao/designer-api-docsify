# UserAuth

Provides APIs for managing the **UserAuth** object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthInstance](arkts-userauthentication-userauth-authinstance-i.md)

<!--Device-userAuth-class UserAuth--><!--Device-userAuth-class UserAuth-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

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

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthInstance.start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: UserAuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array--><!--Device-UserAuth-auth(      challenge: Uint8Array,      authType: UserAuthType,      authTrustLevel: AuthTrustLevel,      callback: IUserAuthCallback    ): Uint8Array-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| challenge | Uint8Array | Yes | Challenge value, which can be passed in Uint8Array([]) format. |
| authType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authentication type. Currently, **FACE** and **FINGERPRINT** are supported. |
| authTrustLevel | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authentication trust level. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return the result. |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | Context ID, which is used as the input parameter of |

**Example**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let challenge = new Uint8Array([]);
auth.auth(challenge, userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1, {
  onResult: (result, extraInfo) => {
    try {
      console.info(`auth onResult result = ${result}`);
      console.info(`auth onResult extraInfo = ${JSON.stringify(extraInfo)}`);
      if (result == userAuth.ResultCode.SUCCESS) {
        // Add the logic to be executed when the authentication is successful.
      } else {
        // Add the logic to be executed when the authentication fails.
      }
    } catch (error) {
      console.error(`auth onResult error = ${error}`);
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

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.AuthInstance.cancel](arkts-userauthentication-userauth-authinstance-i.md#cancel)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-cancelAuth(contextID: Uint8Array): number--><!--Device-UserAuth-cancelAuth(contextID: Uint8Array): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contextID | Uint8Array | Yes | Context ID, which is obtained by [auth]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns **SUCCESS** if the cancellation is successful. Returns a |

**Example**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

// contextId can be obtained via auth(). In this example, it is defined here.
let contextId = new Uint8Array([0, 1, 2, 3, 4, 5, 6, 7]);
let auth = new userAuth.UserAuth();
let cancelCode = auth.cancelAuth(contextId);
if (cancelCode == userAuth.ResultCode.SUCCESS) {
  console.info('cancel auth success');
} else {
  console.error('cancel auth fail');
}
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **UserAuth** instance.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md#getauthinstance)

<!--Device-UserAuth-constructor()--><!--Device-UserAuth-constructor()-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Example**

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

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [userAuth.getAvailableStatus](arkts-userauthentication-userauth-getavailablestatus-f.md#getavailablestatus)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number--><!--Device-UserAuth-getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authentication type. Currently, **FACE** and **FINGERPRINT** are supported. |
| authTrustLevel | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Authentication trust level. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Query result. If the authentication capability is supported, **SUCCESS** is returned. |

**Example**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let checkCode = auth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL1);
if (checkCode == userAuth.ResultCode.SUCCESS) {
  console.info('check auth support success');
} else {
  console.error(`check auth support fail, code = ${checkCode}`);
}
```

## getVersion

```TypeScript
getVersion(): number
```

Obtains the version of this authenticator.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-UserAuth-getVersion(): number--><!--Device-UserAuth-getVersion(): number-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Return value:**

| Type | Description |
| --- | --- |
| number | Authenticator version obtained. |

**Example**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let auth = new userAuth.UserAuth();
let version = auth.getVersion();
console.info(`auth version = ${version}`);
```

