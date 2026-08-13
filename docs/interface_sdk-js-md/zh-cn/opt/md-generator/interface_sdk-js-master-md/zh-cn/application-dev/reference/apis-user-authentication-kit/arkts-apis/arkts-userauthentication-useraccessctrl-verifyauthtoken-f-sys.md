# verifyAuthToken（系统接口）

## verifyAuthToken

```TypeScript
function verifyAuthToken(authToken: Uint8Array, allowableDuration: number): Promise<AuthToken>
```

验证认证令牌。该接口用于校验AuthToken的有效性，包括完整性校验和时效性校验，校验通过后返回解析后的AuthToken详细信息。使用Promise异步回调。 完整性校验通过验证AuthToken的数字签名确保令牌未被篡改；时效性校验通过比对AuthToken的签发时间与当前时间，并结合allowableDuration参数判断令牌是否在有效期内。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.USE_USER_ACCESS_MANAGER

<!--Device-userAccessCtrl-function verifyAuthToken(authToken: Uint8Array, allowableDuration: int): Promise<AuthToken>--><!--Device-userAccessCtrl-function verifyAuthToken(authToken: Uint8Array, allowableDuration: int): Promise<AuthToken>-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| authToken | Uint8Array | 是 |
| allowableDuration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthToken](arkts-userauthentication-useraccessctrl-authtoken-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12500015](../errorcode-useriam.md#12500015-authtoken完整性校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12500002](../errorcode-useriam.md#12500002-身份认证系统通用错误码) |
| [12500016](../errorcode-useriam.md#12500016-authtoken过期) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAccessCtrl } from '@kit.UserAuthenticationKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const allowableDuration: number = 5000;
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

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // 需要调用UserAuthInstance的start()接口，启动认证后，才能通过onResult获取到认证结果。
  userAuthInstance.on('result', {
    onResult: (result) => {
        if (!result.token) {
            console.error('userAuthInstance callback result.token is null');
            return;
        }
        try {
          // 发起AuthToken验证请求。
          userAccessCtrl.verifyAuthToken(result.token, allowableDuration)
              .then((retAuthToken: userAccessCtrl.AuthToken) => {
                  Object.keys(retAuthToken).forEach((key) => {
                      // 处理业务逻辑。
                      console.info(`retAuthToken key:${key}`);
                  })
              }).catch ((error: BusinessError) => {
                  console.error(`verify authToken failed. Code is ${error?.code}, message is ${error?.message}`);
              })
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          console.error(`verify authToken failed. Code is ${err?.code}, message is ${err?.message}`);
        }
    }
  });
  console.info('auth on successfully.');
  // 启动认证。
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```
