# getAuthLockState

## getAuthLockState

```TypeScript
function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>
```

查询指定认证类型的冻结状态，使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-userAuth-function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>--><!--Device-userAuth-function getAuthLockState(authType: UserAuthType): Promise<AuthLockState>-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthLockState](arkts-userauthentication-userauth-authlockstate-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12500010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500010-该类型的凭据没有录入) |
| [12500008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500008-参数校验失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [12500005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500005-认证类型不支持) |
| [12500002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-user-authentication-kit/errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## 示例

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let queryType = userAuth.UserAuthType.PIN;
let authLockState : userAuth.AuthLockState = {
  isLocked : false,
  remainingAuthAttempts : 0,
  lockoutDuration : 0
}

userAuth.getAuthLockState(queryType)
  .then((result: userAuth.AuthLockState) => {
    authLockState = result;
    console.info('get auth lock state successfully.');
  })
  .catch((err: BusinessError) => {
    console.error(`get auth lock state failed, err code is : ${err?.code}, err message is : ${err?.message}`);
  })
```
