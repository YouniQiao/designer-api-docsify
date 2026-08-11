# getAvailableStatus

## getAvailableStatus

```TypeScript
function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void
```

查询指定类型和等级的认证能力是否支持。该接口用于检查当前设备是否支持指定的认证类型和认证可信等级，帮助应用在发起认证前判断认证能力是否可用，从而避免不必要的认证不通过。若查询通过（无错误抛出），表示认证能力可用；若抛出错误，应用应根据错误码判断具体原因并采取相应处理。

**起始版本：** 9

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-userAuth-function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void--><!--Device-userAuth-function getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authType | [UserAuthType](arkts-userauthentication-userauth-userauthtype-e.md) | 是 |
| authTrustLevel | [AuthTrustLevel](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtrustlevel-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [12500013](../errorcode-useriam.md#12500013-密码过期) |
| [12500010](../errorcode-useriam.md#12500010-该类型的凭据没有录入) |
| [12500006](../errorcode-useriam.md#12500006-认证信任等级不支持) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12500005](../errorcode-useriam.md#12500005-认证类型不支持) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## 示例

```TypeScript
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
  console.info('current auth trust level is supported');
} catch (error) {
  console.error(`current auth trust level is not supported. Code: ${error?.code}, message: ${error?.message}`);
}
```
