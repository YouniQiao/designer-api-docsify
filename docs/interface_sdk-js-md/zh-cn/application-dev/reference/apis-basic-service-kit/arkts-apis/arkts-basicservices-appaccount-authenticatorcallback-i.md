# AuthenticatorCallback

OAuth认证器回调接口。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃。建议使用[AuthCallback](arkts-basicservices-appaccount-authcallback-i.md#AuthCallback)替代。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md#AuthCallback)

<!--Device-appAccount-interface AuthenticatorCallback--><!--Device-appAccount-interface AuthenticatorCallback-End-->

**系统能力：** SystemCapability.Account.AppAccount

## onRequestRedirected

```TypeScript
onRequestRedirected: (request: Want) => void
```

通知请求被跳转。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃。建议使用[onRequestRedirected](#onrequestredirected9)替代。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [onRequestRedirected](AppAccount.AuthCallback.onRequestRedirected)

<!--Device-AuthenticatorCallback-onRequestRedirected: (request: Want) => void--><!--Device-AuthenticatorCallback-onRequestRedirected: (request: Want) => void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |  |

## 示例

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
      token: 'xxxxxx'}
    );
  }
}
```

## onResult

```TypeScript
onResult: (code: number, result: { [key: string]: any }) => void
```

通知请求结果。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃。建议使用[onResult](#onresult9)替代。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [onResult](AppAccount.AuthCallback.onResult)

<!--Device-AuthenticatorCallback-onResult: (code: number, result: { [key: string]: any }) => void--><!--Device-AuthenticatorCallback-onResult: (code: number, result: { [key: string]: any }) => void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 |  |
| result | { [key: string]: any } | 是 |  |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();
let sessionId = '1234';
appAccountManager.getAuthenticatorCallback(sessionId).then((callback: appAccount.AuthenticatorCallback) => {
  callback.onResult(appAccount.ResultCode.SUCCESS, {
    name: 'LiSi',
    owner: 'com.example.accountjsdemo',
    authType: 'getSocialData',
    token: 'xxxxxx'}
  );
}).catch((err: BusinessError) => {
  console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
});
```

