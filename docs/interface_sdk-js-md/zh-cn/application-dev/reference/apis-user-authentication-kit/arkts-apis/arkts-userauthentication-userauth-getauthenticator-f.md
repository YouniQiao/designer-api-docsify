# getAuthenticator

## 导入模块

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
```

## getAuthenticator

```TypeScript
function getAuthenticator(): Authenticator
```

获取Authenticator对象，用于执行用户身份认证。

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为6。

**废弃版本：** 8

**替代接口：** [getAuthInstance](arkts-userauthentication-userauth-getauthinstance-f.md)

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**返回值：**

| 类型 |
| --- |
| [Authenticator](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-appaccount-authenticator-c.md) |

**示例**

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

let authenticator = userAuth.getAuthenticator();
```
