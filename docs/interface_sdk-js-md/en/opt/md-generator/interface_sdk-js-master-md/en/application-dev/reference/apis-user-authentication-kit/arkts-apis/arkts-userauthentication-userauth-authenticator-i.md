# Authenticator

Provides APIs for managing the **Authenticator** object.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md#authinstance)

<!--Device-userAuth-interface Authenticator--><!--Device-userAuth-interface Authenticator-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
```

## execute

```TypeScript
execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void
```

Starts user authentication. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-Authenticator-execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void--><!--Device-Authenticator-execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AuthType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| level | [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
authenticator.execute('FACE_ONLY', 'S2', (error, code) => {
  if (code === userAuth.ResultCode.SUCCESS) {
    console.info('auth successfully.');
    return;
  }
  console.error(`auth failed, code = ${code}`);
});
```

## execute

```TypeScript
execute(type: AuthType, level: SecureLevel): Promise<number>
```

Starts user authentication. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 8

**Substitutes:** [start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-Authenticator-execute(type: AuthType, level: SecureLevel): Promise<number>--><!--Device-Authenticator-execute(type: AuthType, level: SecureLevel): Promise<number>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [AuthType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtype-e-sys.md) | Yes |
| level | [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Examples**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  let authenticator = userAuth.getAuthenticator();
  authenticator.execute('FACE_ONLY', 'S2').then((code) => {
    console.info('auth successfully.');
  })
} catch (error) {
  console.error(`auth failed, Code: ${error?.code}, message: ${error?.message}`);
}
```
