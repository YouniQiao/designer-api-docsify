# Authenticator

认证器对象。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [userAuth.AuthInstance](arkts-userauthentication-userauth-authinstance-i.md)

<!--Device-userAuth-interface Authenticator--><!--Device-userAuth-interface Authenticator-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

## Modules to Import

```TypeScript
import { userAuth } from 'kits/@kit.UserAuthenticationKit';
```

## execute

```TypeScript
execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void
```

执行用户认证，使用callback方式作为异步方法。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [userAuth.AuthInstance.start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-Authenticator-execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void--><!--Device-Authenticator-execute(type: AuthType, level: SecureLevel, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [AuthType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtype-e-sys.md) | Yes | 认证类型，当前只支持"FACE_ONLY"。&lt;br/&gt;ALL为预留参数。当前版本暂不支持ALL类型的认证。 |
| level | [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) | Yes | 安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。&lt;br/&gt;具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。 &lt;br/&gt;具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 回调函数。number表示认证结果，参见 [AuthenticationResult](arkts-userauthentication-userauth-authenticationresult-e.md)。 |

## Examples

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

执行用户认证，使用promise方式作为异步方法。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** [userAuth.AuthInstance.start](arkts-userauthentication-userauth-authinstance-i.md#start)

**Required permissions:** ohos.permission.ACCESS_BIOMETRIC

<!--Device-Authenticator-execute(type: AuthType, level: SecureLevel): Promise<number>--><!--Device-Authenticator-execute(type: AuthType, level: SecureLevel): Promise<number>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [AuthType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtype-e-sys.md) | Yes | 认证类型，当前只支持"FACE_ONLY"。&lt;br/&gt;ALL为预留参数。当前版本暂不支持ALL类型的认证。 |
| level | [SecureLevel](arkts-userauthentication-userauth-securelevel-t.md) | Yes | 安全级别，对应认证的安全级别，有效值为"S1"（最低）、"S2"、"S3"、"S4"（最高）。&lt;br/&gt;具备3D人脸识别能力的设备支持"S3"及以下安全级别的认证。 &lt;br/&gt;具备2D人脸识别能力的设备支持"S2"及以下安全级别的认证。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | 返回携带一个number的Promise。number 为认证结果，参见 [AuthenticationResult]{ |

## Examples

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

