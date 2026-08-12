# AuthenticatorCallback

Provides OAuth authenticator callbacks.

> **NOTE：**
> 
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md#AuthCallback) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md#AuthCallback)

<!--Device-appAccount-interface AuthenticatorCallback--><!--Device-appAccount-interface AuthenticatorCallback-End-->

**System capability:** SystemCapability.Account.AppAccount

## Modules to Import

```TypeScript
import { appAccount } from '@kit.BasicServicesKit';
```

## onRequestRedirected

```TypeScript
onRequestRedirected: (request: Want) => void
```

Called to redirect a request.

> **NOTE：**
> 
> This API is supported since API version 8 and deprecated since API version 9. Use [onRequestRedirected](#onrequestredirected9) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onRequestRedirected](AppAccount.AuthCallback.onRequestRedirected)

<!--Device-AuthenticatorCallback-onRequestRedirected: (request: Want) => void--><!--Device-AuthenticatorCallback-onRequestRedirected: (request: Want) => void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';

class MyAuthenticator extends appAccount.Authenticator {
  addAccountImplicitly(authType: string, callerBundleName: string,
    options: Record<string, Object>, callback: appAccount.AuthenticatorCallback) {
    let want: Want = {
      bundleName: 'com.example.accountjsdemo',
      abilityName: 'com.example.accountjsdemo.LoginAbility',
    };
    callback.onRequestRedirected(want);
  }

  authenticate(name: string, authType: string, callerBundleName: string,
    options: Record<string, Object>, callback: appAccount.AuthenticatorCallback) {
    callback.onResult(appAccount.ResultCode.SUCCESS, {
      name: name,
      authType: authType,
      token: 'xxxxxx'
    });
  }
}
```

## onResult

```TypeScript
onResult: (code: number, result: { [key: string]: any }) => void
```

Called to return the result of an authentication request.

> **NOTE：**
> 
> This API is supported since API version 8 and deprecated since API version 9. Use [onResult](#onresult9) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onResult](AppAccount.AuthCallback.onResult)

<!--Device-AuthenticatorCallback-onResult: (code: number, result: { [key: string]: any }) => void--><!--Device-AuthenticatorCallback-onResult: (code: number, result: { [key: string]: any }) => void-End-->

**System capability:** SystemCapability.Account.AppAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |
| result | { [key: string]: any } | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
let sessionId = '1234';
appAccountManager.getAuthenticatorCallback(sessionId).then((callback: appAccount.AuthenticatorCallback) => {
  callback.onResult(appAccount.ResultCode.SUCCESS, {
    name: 'LiSi',
    owner: 'com.example.accountjsdemo',
    authType: 'getSocialData',
    token: 'xxxxxx'
  });
}).catch((err: BusinessError) => {
  console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
});
```
