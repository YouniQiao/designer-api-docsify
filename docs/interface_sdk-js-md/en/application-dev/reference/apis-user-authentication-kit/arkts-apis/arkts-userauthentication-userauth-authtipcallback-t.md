# AuthTipCallback

```TypeScript
type AuthTipCallback = (authTipInfo: AuthTipInfo) => void
```

Defines the callback to return the intermediate authentication status. This callback is used to obtain various intermediate status information during authentication, including authentication failure, lockout, and loading and release of the authentication screen. By subscribing to these intermediate statuses, the application can provide more refined user interaction and status management during the authentication process.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-userAuth-type AuthTipCallback = (authTipInfo: AuthTipInfo) => void--><!--Device-userAuth-type AuthTipCallback = (authTipInfo: AuthTipInfo) => void-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| authTipInfo | [AuthTipInfo](arkts-userauthentication-userauth-authtipinfo-i.md) | Yes | Intermediate authentication status. It contains the authentication type ( **tipType**) and status code (**tipCode**). The application should perform the corresponding processing based on the value of **tipCode**: <br>- **COMPARE_FAILURE(1)**: Prompt the user to try again. <br>- **TIMEOUT(2)**: Prompt the user that the operation has timed out. <br>- **TEMPORARILY_LOCKED(3)**: Prompt the user to wait for unlocking. <br>- **PERMANENTLY_LOCKED(4)**: Prompt the user to use PIN authentication. <br>- **WIDGET_LOADED(5)**: The authentication screen has been loaded and initialization can be performed. <br>- **WIDGET_RELEASED(6)**: The authentication screen has been released, and the subsequent operations can be performed. <br>- **COMPARE_FAILURE_WITH_FROZEN(7)**: Prompt the user that the authentication fails and the authenticator is locked. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { userAuth } from '@kit.UserAuthenticationKit';

try {
  const rand = cryptoFramework.createRandom();
  const len: number = 16;
  let randData: Uint8Array | null = null;
  let retryCount = 0;
  while(retryCount < 3){
    randData = rand?.generateRandomSync(len)?.data;
    if(randData){
      break;
    }
    retryCount++;
  }
  if(!randData){
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
  console.info('get userAuth instance success');
  // The intermediate authentication status is returned by onAuthTip only after the authentication is started by start() of UserAuthInstance.
  userAuthInstance.on('authTip', (authTipInfo: userAuth.AuthTipInfo) => {
    console.info(`userAuthInstance callback authTipInfo = ${JSON.stringify(authTipInfo)}`);
  });
  console.info('auth on success');
  userAuthInstance.start();
  console.info('auth start success');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth catch error. Code is ${err?.code}, message is ${err?.message}`);
}
```

