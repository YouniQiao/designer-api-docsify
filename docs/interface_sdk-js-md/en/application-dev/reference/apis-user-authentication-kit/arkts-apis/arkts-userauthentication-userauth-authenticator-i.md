# Authenticator

Provides APIs for managing the **Authenticator** object.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md#AuthInstance)

<!--Device-userAuth-interface Authenticator--><!--Device-userAuth-interface Authenticator-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## execute

```TypeScript
execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void
```

Starts user authentication. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-Authenticator-execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void--><!--Device-Authenticator-execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | AuthType | Yes | Authentication type. Currently, only **FACE_ONLY** is supported. &lt;br&gt;**ALL** is reserved and not supported by the current version. |
| level | [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) | Yes | Security level of the authentication. It can be **S1** (lowest), **S2**, **S3**, or **S4** (highest). &lt;br&gt;Devices capable of 3D facial recognition support S3 and lower-level authentication. &lt;br&gt;Devices capable of 2D facial recognition support S2 and lower-level authentication. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;number&gt; | Yes | Callback used to return the result. **number** indicates the [AuthenticationResult](arkts-userauthentication-userauth-authenticationresult-e.md#AuthenticationResult). |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
authenticator.execute('FACE_ONLY', 'S2', (error, code)=>{
  if (code === userAuth.ResultCode.SUCCESS) {
    console.info('auth success');
    return;
  }
  console.error(`auth fail, code = ${code}`);
});
```

## execute

```TypeScript
execute(type: AuthType, level: SecureLevel): Promise<number>
```

Starts user authentication. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-Authenticator-execute(type: AuthType, level: SecureLevel): Promise<number>--><!--Device-Authenticator-execute(type: AuthType, level: SecureLevel): Promise<number>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | AuthType | Yes | Authentication type. Currently, only **FACE_ONLY** is supported. &lt;br&gt;**ALL** is reserved and not supported by the current version. |
| level | [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) | Yes | Security level of the authentication. It can be **S1** (lowest), **S2**, **S3**, or **S4** (highest). &lt;br&gt;Devices capable of 3D facial recognition support S3 and lower-level authentication. &lt;br&gt;Devices capable of 2D facial recognition support S2 and lower-level authentication. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the authentication result, which is a number. For details, see [AuthenticationResult]{ |

## Examples

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  let authenticator = userAuth.getAuthenticator();
  authenticator.execute('FACE_ONLY', 'S2').then((code)=>{
    console.info('auth success');
  })
} catch (error) {
  console.error(`auth fail, code = ${error}`);
}
```

