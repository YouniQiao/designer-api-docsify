# getUserAuthInstance

## getUserAuthInstance

```TypeScript
function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance
```

获取[UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md)对象，执行用户身份认证，并支持使用统一用户身份认证控件。该接口用于创建一个用户认证实例，配置认证参数和界面参数后，可通过返回的实例对象启动认证、订阅认证结果等。

> **说明：**
> 
> 每个UserAuthInstance只能进行一次认证，需要再次认证时，必须重新获取UserAuthInstance。认证完成后（无论成功或失败），该实例将无法再次使用。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-userAuth-function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance--><!--Device-userAuth-function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authParam | [AuthParam](arkts-userauthentication-userauth-authparam-i.md) | 是 |
| widgetParam | [WidgetParam](arkts-userauthentication-userauth-widgetparam-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [12500006](../errorcode-useriam.md#12500006-认证信任等级不支持) |
| [12500005](../errorcode-useriam.md#12500005-认证类型不支持) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while (retryCount < 3) {
    randData = rand?.generateRandomSync(len)?.data;
    if (randData) {
      break;
    }
    retryCount++;
  }
  if (!randData) {
    return;
  }
  const authParam: userAuth.AuthParam = {
    challenge: randData,
    authType: [userAuth.UserAuthType.PIN],
    authTrustLevel: userAuth.AuthTrustLevel.ATL3,
  };
  const widgetParam: userAuth.WidgetParam = {
    title: '请输入密码',
  };
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```
