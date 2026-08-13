# getAuthInstance

## getAuthInstance

```TypeScript
function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance
```

获取AuthInstance对象，用于执行用户身份认证。 > **说明：** > > 每个AuthInstance只能进行一次认证，若需要再次进行认证则需重新获取AuthInstance。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [getUserAuthInstance](arkts-userauthentication-userauth-getuserauthinstance-f.md#getUserAuthInstance)

<!--Device-userAuth-function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance--><!--Device-userAuth-function getAuthInstance(challenge: Uint8Array, authType: UserAuthType, authTrustLevel: AuthTrustLevel): AuthInstance-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| challenge | Uint8Array | 是 |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | 是 |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AuthInstance](arkts-userauthentication-userauth-authinstance-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500006](../errorcode-useriam.md#12500006-认证信任等级不支持) |
| [12500005](../errorcode-useriam.md#12500005-认证类型不支持) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## 示例

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
