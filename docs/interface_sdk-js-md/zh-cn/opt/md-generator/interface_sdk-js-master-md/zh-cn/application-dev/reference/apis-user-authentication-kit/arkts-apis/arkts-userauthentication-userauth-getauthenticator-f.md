# getAuthenticator

## getAuthenticator

```TypeScript
function getAuthenticator(): Authenticator
```

获取Authenticator对象，用于执行用户身份认证。

**起始版本：** 6

**废弃版本：** 8

**替代接口：** [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md#getAuthInstance)

<!--Device-userAuth-function getAuthenticator(): Authenticator--><!--Device-userAuth-function getAuthenticator(): Authenticator-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 |
| --- |
| [Authenticator](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-appaccount-authenticator-c.md) |

## 示例

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
```
