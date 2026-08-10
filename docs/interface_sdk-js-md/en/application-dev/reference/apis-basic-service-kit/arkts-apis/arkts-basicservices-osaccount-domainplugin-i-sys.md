# DomainPlugin (System API)

域插件，提供域账号认证功能。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-osAccount-interface DomainPlugin--><!--Device-osAccount-interface DomainPlugin-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## auth

```TypeScript
auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void
```

认证指定的域账号。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-DomainPlugin-auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 指示域账号信息。 |
| credential | Uint8Array | Yes | 指示域账号的凭据。 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 指示认证结果回调。 |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {
    // mock authentication
    // notify authentication result
    let result: osAccount.AuthResult = {
      token: new Uint8Array([0]),
      remainTimes: 5,
      freezingTime: 0
    };
    callback.onResult(0, result);
  },
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {},
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {},
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                    callback: AsyncCallback<osAccount.AuthStatusInfo>) => {},
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {},
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {},
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {},
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {}
}
osAccount.DomainAccountManager.registerPlugin(plugin);
let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.DOMAIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  userAuth.auth(challenge, authType, authTrustLevel, {
    onResult: (resultCode: number, authResult: osAccount.AuthResult) => {
        console.info('auth resultCode = ' + resultCode);
        console.info('auth authResult = ' + JSON.stringify(authResult));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

## auth

```TypeScript
auth: DomainPluginAuthFunc
```

认证指定的域账号。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-auth: DomainPluginAuthFunc--><!--Device-DomainPlugin-auth: DomainPluginAuthFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authWithPopup

```TypeScript
authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void
```

弹窗认证指定的域账号。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 指示域账号信息。 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 指示认证结果回调。 |

## Examples

```TypeScript
import { AsyncCallback } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {
    // mock authentication
    // notify authentication result
    let result: osAccount.AuthResult = {
      token: new Uint8Array([0]),
      remainTimes: 5,
      freezingTime: 0
    };
    callback.onResult(0, result);
  },
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {},
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {},
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                      callback: AsyncCallback<osAccount.AuthStatusInfo>) => {},
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {},
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {},
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {},
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {}
}
osAccount.DomainAccountManager.registerPlugin(plugin)
```

## authWithPopup

```TypeScript
authWithPopup: DomainPluginAuthWithPopupFunc
```

弹窗认证指定的域账号。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-authWithPopup: DomainPluginAuthWithPopupFunc--><!--Device-DomainPlugin-authWithPopup: DomainPluginAuthWithPopupFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authWithToken

```TypeScript
authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void
```

使用授权令牌认证指定的域账号。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 指示域账号信息。 |
| token | Uint8Array | Yes | 指示PIN码或生物识别认证成功时生成的授权令牌。 |
| callback | [IUserAuthCallback](arkts-basicservices-osaccount-iuserauthcallback-i-sys.md) | Yes | 指示认证结果回调。 |

## Examples

```TypeScript
import { AsyncCallback } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {
    // mock authentication
    // notify authentication result
    let result: osAccount.AuthResult = {
      token: new Uint8Array([0]),
      remainTimes: 5,
      freezingTime: 0
    };
    callback.onResult(0, result);
  },
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {},
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                      callback: AsyncCallback<osAccount.AuthStatusInfo>) => {},
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {},
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {},
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {},
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {}
}
osAccount.DomainAccountManager.registerPlugin(plugin)
```

## authWithToken

```TypeScript
authWithToken: DomainPluginAuthWithTokenFunc
```

使用授权令牌认证指定的域账号。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-authWithToken: DomainPluginAuthWithTokenFunc--><!--Device-DomainPlugin-authWithToken: DomainPluginAuthWithTokenFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## bindAccount

```TypeScript
bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void
```

绑定指定的域账号。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void--><!--Device-DomainPlugin-bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 指示域账号信息。 |
| localId | number | Yes | 系统账号ID。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 指示绑定结果回调。 |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {},
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {},
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                      callback: AsyncCallback<osAccount.AuthStatusInfo>) => {},
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {
    // mock unbinding operation
    // notify binding result
    let code: BusinessError = {
      code: 0,
      name: "",
      message: ""
    };
    callback(code);
  },
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {},
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {},
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {}
}
osAccount.DomainAccountManager.registerPlugin(plugin)
```

## bindAccount

```TypeScript
bindAccount: DomainPluginBindAccountFunc
```

绑定指定的域账号。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-bindAccount: DomainPluginBindAccountFunc--><!--Device-DomainPlugin-bindAccount: DomainPluginBindAccountFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## getAccessToken

```TypeScript
getAccessToken(options: GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>): void
```

根据指定的选项获取域访问令牌。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-getAccessToken(options: GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>): void--><!--Device-DomainPlugin-getAccessToken(options: GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetDomainAccessTokenOptions](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | Yes | 指示获取域访问令牌的选项。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Uint8Array&gt; | Yes | 指示结果回调。 |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {},
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {},
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                      callback: AsyncCallback<osAccount.AuthStatusInfo>) => {},
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {},
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {},
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {},
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {
    // mock getting operation
    // notify result
    let code: BusinessError = {
      code: 0,
      name: "",
      message: ""
    };
    let token: Uint8Array = new Uint8Array([0]);
    callback(code, token);
  }
}
osAccount.DomainAccountManager.registerPlugin(plugin)
```

## getAccessToken

```TypeScript
getAccessToken: DomainPluginGetAccessTokenFunc
```

根据指定的选项获取域访问令牌。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-getAccessToken: DomainPluginGetAccessTokenFunc--><!--Device-DomainPlugin-getAccessToken: DomainPluginGetAccessTokenFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## getAccountInfo

```TypeScript
getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void
```

查询指定域账号的信息。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void--><!--Device-DomainPlugin-getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetDomainAccountInfoPluginOptions](arkts-basicservices-osaccount-getdomainaccountinfopluginoptions-i-sys.md) | Yes | 指示域账号信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DomainAccountInfo&gt; | Yes | 指示查询结果回调。 |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {},
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {
    // mock getting account information
    // notify result
    let code: BusinessError = {
      code: 0,
      name: "",
      message: ""
    };
    let accountInfo: osAccount.DomainAccountInfo = {
      domain: options.domain ? options.domain : "",
      accountName: options.accountName,
      accountId: 'xxxx'
    };
    callback(code, accountInfo);
  },
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                      callback: AsyncCallback<osAccount.AuthStatusInfo>) => {},
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {},
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {},
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {},
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {}
}
osAccount.DomainAccountManager.registerPlugin(plugin)
```

## getAccountInfo

```TypeScript
getAccountInfo: DomainPluginGetAccountInfoFunc
```

查询指定域账号的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-getAccountInfo: DomainPluginGetAccountInfoFunc--><!--Device-DomainPlugin-getAccountInfo: DomainPluginGetAccountInfoFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## getAuthStatusInfo

```TypeScript
getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void
```

查询指定域账号的认证状态信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void--><!--Device-DomainPlugin-getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 指示域账号信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;AuthStatusInfo&gt; | Yes | 指示查询结果回调。 |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {},
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {},
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                      callback: AsyncCallback<osAccount.AuthStatusInfo>) => {
    let code: BusinessError = {
      code: 0,
      name: "",
      message: ""
    };
    let statusInfo: osAccount.AuthStatusInfo = {
      remainTimes: 5,
      freezingTime: 0
    };
    callback(code, statusInfo);
  },
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {},
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {},
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {},
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {}
}
osAccount.DomainAccountManager.registerPlugin(plugin)
```

## getAuthStatusInfo

```TypeScript
getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc
```

查询指定域账号的认证状态信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc--><!--Device-DomainPlugin-getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## isAccountTokenValid

```TypeScript
isAccountTokenValid(
      domainAccountInfo: DomainAccountInfo,
      token: Uint8Array,
      callback: AsyncCallback<boolean>
    ): void
```

检查指定的域账号令牌是否有效。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-isAccountTokenValid(      domainAccountInfo: DomainAccountInfo,      token: Uint8Array,      callback: AsyncCallback<boolean>    ): void--><!--Device-DomainPlugin-isAccountTokenValid(      domainAccountInfo: DomainAccountInfo,      token: Uint8Array,      callback: AsyncCallback<boolean>    ): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 指示域账号信息。 |
| token | Uint8Array | Yes | 指示域账号令牌。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 指示检查结果回调。true表示指定的域账号令牌是有效的；false表示指定的域账号令牌是无效的。 |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {},
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {},
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                      callback: AsyncCallback<osAccount.AuthStatusInfo>) => {},
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {},
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {},
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {
    // mock checking operation
    // notify checking result
    let code: BusinessError = {
      code: 0,
      name: "",
      message: ""
    };
    callback(code, true);
  },
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {}
}
osAccount.DomainAccountManager.registerPlugin(plugin)
```

## isAccountTokenValid

```TypeScript
isAccountTokenValid: DomainPluginIsAccountTokenValidFunc
```

检查指定的域账号令牌是否有效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-isAccountTokenValid: DomainPluginIsAccountTokenValidFunc--><!--Device-DomainPlugin-isAccountTokenValid: DomainPluginIsAccountTokenValidFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## unbindAccount

```TypeScript
unbindAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<void>): void
```

解绑指定的域账号。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-unbindAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<void>): void--><!--Device-DomainPlugin-unbindAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i-sys.md) | Yes | 指示域账号信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 指示绑定结果回调。 |

## Examples

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
                  callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                  callback: osAccount.IUserAuthCallback) => {},
  getAccountInfo: (options: osAccount.GetDomainAccountInfoPluginOptions,
                  callback: AsyncCallback<osAccount.DomainAccountInfo>) => {},
  getAuthStatusInfo: (domainAccountInfo: osAccount.DomainAccountInfo,
                      callback: AsyncCallback<osAccount.AuthStatusInfo>) => {},
  bindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, localId: number,
                callback: AsyncCallback<void>) => {},
  unbindAccount: (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {
    // mock unbinding operation
    // notify unbinding result
    let code: BusinessError = {
      code: 0,
      name: "",
      message: ""
    };
    callback(code);
  },
  isAccountTokenValid: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
                        callback: AsyncCallback<boolean>) => {},
  getAccessToken: (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {}
}
osAccount.DomainAccountManager.registerPlugin(plugin)
```

## unbindAccount

```TypeScript
unbindAccount: DomainPluginUnbindAccountFunc
```

解绑指定的域账号。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-unbindAccount: DomainPluginUnbindAccountFunc--><!--Device-DomainPlugin-unbindAccount: DomainPluginUnbindAccountFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

