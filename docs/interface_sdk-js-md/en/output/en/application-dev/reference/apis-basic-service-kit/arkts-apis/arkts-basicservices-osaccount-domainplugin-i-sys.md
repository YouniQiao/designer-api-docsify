# DomainPlugin (System API)

Provides APIs for domain account authentication.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-osAccount-interface DomainPlugin--><!--Device-osAccount-interface DomainPlugin-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## auth

```TypeScript
auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void
```

Authenticates a domain account.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-DomainPlugin-auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Domain account information. |
| credential | Uint8Array | Yes | Credentials of the domain account. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return the authentication result. |

**Example**

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

## authWithPopup

```TypeScript
authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void
```

Authenticates a domain account in a pop-up window.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Domain account information. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return the authentication result. |

**Example**

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

## authWithToken

```TypeScript
authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void
```

Authenticates a domain account by the authorization token.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Domain account information. |
| token | Uint8Array | Yes | Authorization token generated when the PIN or biometric authentication is successful. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Callback used to return the authentication result. |

**Example**

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

## bindAccount

```TypeScript
bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void
```

Binds a domain account.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void--><!--Device-DomainPlugin-bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Domain account information. |
| localId | number | Yes | ID of the target OS account. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Example**

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

## getAccessToken

```TypeScript
getAccessToken(options: GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>): void
```

Obtains the domain access token based on the specified conditions. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-getAccessToken(options: GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>): void--><!--Device-DomainPlugin-getAccessToken(options: GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options specified for obtaining the domain access token. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Uint8Array&gt; | Yes | Callback used to return the result. |

**Example**

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

## getAccountInfo

```TypeScript
getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void
```

Obtains information about a domain account. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void--><!--Device-DomainPlugin-getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Domain account information. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;DomainAccountInfo&gt; | Yes | Callback used to return the result. |

**Example**

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

## getAuthStatusInfo

```TypeScript
getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void
```

Obtains the authentication status of a domain account.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void--><!--Device-DomainPlugin-getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Domain account information. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AuthStatusInfo&gt; | Yes | Callback used to return the result. |

**Example**

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

## isAccountTokenValid

```TypeScript
isAccountTokenValid(
      domainAccountInfo: DomainAccountInfo,
      token: Uint8Array,
      callback: AsyncCallback<boolean>
    ): void
```

Checks whether the specified domain account token is valid.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-isAccountTokenValid(      domainAccountInfo: DomainAccountInfo,      token: Uint8Array,      callback: AsyncCallback<boolean>    ): void--><!--Device-DomainPlugin-isAccountTokenValid(      domainAccountInfo: DomainAccountInfo,      token: Uint8Array,      callback: AsyncCallback<boolean>    ): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Domain account information. |
| token | Uint8Array | Yes | Domain account token to check. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;boolean&gt; | Yes | Callback used to return the result.The value **true** means that the specified domain account token is valid;the value **false** means the opposite. |

**Example**

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

## unbindAccount

```TypeScript
unbindAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<void>): void
```

Unbinds a domain account.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DomainPlugin-unbindAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<void>): void--><!--Device-DomainPlugin-unbindAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainAccountInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Domain account information. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |

**Example**

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

## auth

```TypeScript
auth: DomainPluginAuthFunc
```

Authenticates the specified domain account.

**Type:** DomainPluginAuthFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-auth: DomainPluginAuthFunc--><!--Device-DomainPlugin-auth: DomainPluginAuthFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authWithPopup

```TypeScript
authWithPopup: DomainPluginAuthWithPopupFunc
```

Authenticates the specified domain account with a popup.

**Type:** DomainPluginAuthWithPopupFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-authWithPopup: DomainPluginAuthWithPopupFunc--><!--Device-DomainPlugin-authWithPopup: DomainPluginAuthWithPopupFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## authWithToken

```TypeScript
authWithToken: DomainPluginAuthWithTokenFunc
```

Authenticates the specified domain account with an authorization token.

**Type:** DomainPluginAuthWithTokenFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-authWithToken: DomainPluginAuthWithTokenFunc--><!--Device-DomainPlugin-authWithToken: DomainPluginAuthWithTokenFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## bindAccount

```TypeScript
bindAccount: DomainPluginBindAccountFunc
```

Binds the specified domain account with an OS account.

**Type:** DomainPluginBindAccountFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-bindAccount: DomainPluginBindAccountFunc--><!--Device-DomainPlugin-bindAccount: DomainPluginBindAccountFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## getAccessToken

```TypeScript
getAccessToken: DomainPluginGetAccessTokenFunc
```

Gets the access token based on the specified options.

**Type:** DomainPluginGetAccessTokenFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-getAccessToken: DomainPluginGetAccessTokenFunc--><!--Device-DomainPlugin-getAccessToken: DomainPluginGetAccessTokenFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## getAccountInfo

```TypeScript
getAccountInfo: DomainPluginGetAccountInfoFunc
```

Gets the domain account information with the specified options.

**Type:** DomainPluginGetAccountInfoFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-getAccountInfo: DomainPluginGetAccountInfoFunc--><!--Device-DomainPlugin-getAccountInfo: DomainPluginGetAccountInfoFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## getAuthStatusInfo

```TypeScript
getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc
```

Gets the domain authentication property for the specified domain account.

**Type:** DomainPluginGetAuthStatusInfoFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc--><!--Device-DomainPlugin-getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## isAccountTokenValid

```TypeScript
isAccountTokenValid: DomainPluginIsAccountTokenValidFunc
```

Checks whether the token of specified domain account is valid.

**Type:** DomainPluginIsAccountTokenValidFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-isAccountTokenValid: DomainPluginIsAccountTokenValidFunc--><!--Device-DomainPlugin-isAccountTokenValid: DomainPluginIsAccountTokenValidFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## unbindAccount

```TypeScript
unbindAccount: DomainPluginUnbindAccountFunc
```

Unbind the specified domain account.

**Type:** DomainPluginUnbindAccountFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DomainPlugin-unbindAccount: DomainPluginUnbindAccountFunc--><!--Device-DomainPlugin-unbindAccount: DomainPluginUnbindAccountFunc-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

