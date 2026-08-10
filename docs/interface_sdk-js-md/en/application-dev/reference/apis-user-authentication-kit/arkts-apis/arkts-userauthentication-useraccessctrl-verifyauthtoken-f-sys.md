# verifyAuthToken (System API)

## Modules to Import

```TypeScript
import { userAccessCtrl } from 'kits/@kit.UserAuthenticationKit';
```

## verifyAuthToken

```TypeScript
function verifyAuthToken(authToken: Uint8Array, allowableDuration: int): Promise<AuthToken>
```

验证认证令牌。该接口用于校验AuthToken的有效性，包括完整性校验和时效性校验，校验通过后返回解析后的AuthToken详细信息。使用Promise异步回调。

完整性校验通过验证AuthToken的数字签名确保令牌未被篡改；时效性校验通过比对AuthToken的签发时间与当前时间，并结合allowableDuration参数判断令牌是否在有效期内。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.USE_USER_ACCESS_MANAGER

<!--Device-userAccessCtrl-function verifyAuthToken(authToken: Uint8Array, allowableDuration: int): Promise<AuthToken>--><!--Device-userAccessCtrl-function verifyAuthToken(authToken: Uint8Array, allowableDuration: int): Promise<AuthToken>-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authToken | Uint8Array | Yes | 待验证的认证令牌。最大长度为1024字节，由用户认证通过后返回。令牌中包含用户身份认证的凭证信息，用于后续的安全操作验证。 |
| allowableDuration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 允许的认证有效时长。从AuthToken签发起允许使用的最大时间间隔，单位为毫秒。值需大于0且小于等于86400000（24小时）。用于校验令牌的时效性，防止过 期令牌被使用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AuthToken&gt; | Promise对象，验证成功时返回解析后的AuthToken数据，包含挑战值、认证信任等级、认证类型、用户ID等详细信息；验证失败时抛出相应错误码。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| 12500015 | AuthToken integrity check failed. |
| 201 | Permission denied. |
| 202 | Permission denied. Called by non-system application. |
| 12500002 | General operation error. |
| 12500016 | AuthToken has expired. |

## Examples

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
    title: 'Enter password',
  };

  const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
  // The authentication result is returned by onResult() only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.on('result', {
    onResult: (result) => {
        if (!result.token) {
            console.error('userAuthInstance callback result.token is null');
            return;
        }
        try {
          // Initiate a request for verifying the AuthToken.
          userAccessCtrl.verifyAuthToken(result.token, allowableDuration)
              .then((retAuthToken: userAccessCtrl.AuthToken) => {
                  Object.keys(retAuthToken).forEach((key) => {
                      // Process the service logic.
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
  // Start authentication.
  userAuthInstance.start();
  console.info('auth start successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```

