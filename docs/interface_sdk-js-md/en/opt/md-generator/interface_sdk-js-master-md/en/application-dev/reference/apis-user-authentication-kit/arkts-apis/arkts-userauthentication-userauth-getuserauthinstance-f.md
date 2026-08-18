# getUserAuthInstance

## Modules to Import

```TypeScript
```

## getUserAuthInstance

```TypeScript
function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance
```

Obtains a [UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md#userauthinstance) instance for user authentication. The user authentication widget is also supported. This API is used to create a user authentication instance. After authentication parameters and UI parameters are configured, you can use the returned instance object to start authentication and subscribe to the authentication result. > **NOTE：**> Each **UserAuthInstance** can be used for authentication only once. To perform authentication again, you must > obtain a new **UserAuthInstance**. After the authentication is complete (regardless of whether it is successful > or fails), the instance cannot be used again.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-userAuth-function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance--><!--Device-userAuth-function getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [authParam](../../apis-na/arkts-apis/arkts-na-useriam-userauthicon-userauthicon-s.md) | [AuthParam](arkts-userauthentication-userauth-authparam-i.md) | Yes |
| [widgetParam](../../apis-na/arkts-apis/arkts-na-useriam-userauthicon-userauthicon-s.md) | [WidgetParam](arkts-userauthentication-userauth-widgetparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UserAuthInstance](arkts-userauthentication-userauth-userauthinstance-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12500006](../errorcode-useriam.md#12500006-unsupported-authentication-trust-level) |
| [12500005](../errorcode-useriam.md#12500005-unsupported-authentication-type) |
| [12500002](../errorcode-useriam.md#12500002-common-error-code-of-the-identity-authentication-system) |

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
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  console.info('get userAuth instance successfully.');
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`auth failed. Code is ${err?.code}, message is ${err?.message}`);
}
```
