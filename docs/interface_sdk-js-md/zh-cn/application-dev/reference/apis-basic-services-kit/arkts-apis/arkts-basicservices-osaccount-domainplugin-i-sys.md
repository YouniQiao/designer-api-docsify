# DomainPlugin（系统接口）

域插件，提供域账号认证功能。

**起始版本：** 23

<!--Device-osAccount-interface DomainPlugin--><!--Device-osAccount-interface DomainPlugin-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## auth

```TypeScript
auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void
```

认证指定的域账号。

**起始版本：** 9

<!--Device-DomainPlugin-auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-auth(domainAccountInfo: DomainAccountInfo, credential: Uint8Array, callback: IUserAuthCallback): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 | 指示域账号信息。 |
| credential | Uint8Array | 是 | 指示域账号的凭据。 |
| callback | IUserAuthCallback | 是 | 指示认证结果回调。 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  userAuth.auth(challenge, authType, authTrustLevel, {
    onResult: (result: number, extraInfo: osAccount.AuthResult) => {
        console.info('auth result = ' + result);
        console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import osAccount from '@ohos.account.osAccount';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
try {
  userAuth.auth(challenge, authType, authTrustLevel, {
    onResult: (result: int, extraInfo: osAccount.AuthResult) => {
      console.info('auth result = ' + result);
      console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
let options: osAccount.AuthOptions = {
  accountId: 100
};
try {
  userAuth.auth(challenge, authType, authTrustLevel, options, {
    onResult: (result: number, extraInfo: osAccount.AuthResult) => {
      console.info('auth result = ' + result);
      console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import osAccount from '@ohos.account.osAccount';
import { BusinessError } from '@kit.BasicServicesKit';

let userAuth = new osAccount.UserAuth();
let challenge: Uint8Array = new Uint8Array([0]);
let authType: osAccount.AuthType = osAccount.AuthType.PIN;
let authTrustLevel: osAccount.AuthTrustLevel = osAccount.AuthTrustLevel.ATL1;
let options: osAccount.AuthOptions = {
  accountId: 100
};
try {
  userAuth.auth(challenge, authType, authTrustLevel, options, {
    onResult: (result: int, extraInfo: osAccount.AuthResult) => {
      console.info('auth result = ' + result);
      console.info('auth extraInfo = ' + JSON.stringify(extraInfo));
    }
  });
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
        callback: osAccount.IUserAuthCallback) => {
    // 模拟认证
    // 通知认证结果
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

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let domainAccountInfo: osAccount.DomainAccountInfo = {
  domain: 'CHINA',
  accountName: 'zhangsan'
}
let credential = new Uint8Array([0])
try {
  osAccount.DomainAccountManager.auth(domainAccountInfo, credential, {
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

ArkTS-Sta示例：

```TypeScript
let domainAccountInfo: osAccount.DomainAccountInfo = {
  domain: 'CHINA',
  accountName: 'zhangsan'
}
let credential = new Uint8Array([0])
try {
  osAccount.DomainAccountManager.auth(domainAccountInfo, credential, {
    onResult: (resultCode: int, authResult: osAccount.AuthResult) => {
      console.info('auth resultCode = ' + resultCode);
      console.info('auth authResult = ' + JSON.stringify(authResult));
    }
  });
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let domainAccountInfo: osAccount.DomainAccountInfo = {
  domain: 'CHINA',
  accountName: 'zhangsan'
}
let credential = new Uint8Array([0])
try {
  let serverParams: Record<string, Object> = {
    "uri": "test.example.com",
    "port": 100
  }
  let authOptions: osAccount.DomainAccountAuthOptions = {
    serverParams: serverParams
  }
  osAccount.DomainAccountManager.auth(domainAccountInfo, credential, authOptions, {
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

ArkTS--Sta示例：

```TypeScript
let domainAccountInfo: osAccount.DomainAccountInfo = {
  domain: 'CHINA',
  accountName: 'zhangsan'
}
let credential = new Uint8Array([0])
try {
  let serverParams: Record<string, RecordData> = {
    "uri": "test.example.com",
    "port": 100
  }
  let authOptions: osAccount.DomainAccountAuthOptions = {
    serverParams: serverParams
  }
  osAccount.DomainAccountManager.auth(domainAccountInfo, credential, authOptions, {
    onResult: (resultCode: int, authResult: osAccount.AuthResult) => {
      console.info('auth resultCode = ' + resultCode);
      console.info('auth authResult = ' + JSON.stringify(authResult));
    }
  });
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

## authWithPopup

```TypeScript
authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void
```

弹窗认证指定的域账号。

**起始版本：** 10

<!--Device-DomainPlugin-authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-authWithPopup(domainAccountInfo: DomainAccountInfo, callback: IUserAuthCallback): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 | 指示域账号信息。 |
| callback | IUserAuthCallback | 是 | 指示认证结果回调。 |

**示例**

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
    callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
    callback: osAccount.IUserAuthCallback) => {
    // 模拟认证
    // 通知认证结果
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

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  osAccount.DomainAccountManager.authWithPopup({
    onResult: (resultCode: number, authResult: osAccount.AuthResult) => {
      console.info('auth resultCode = ' + resultCode);
      console.info('auth authResult = ' + JSON.stringify(authResult));
    }
  })
} catch (e) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
try {
  osAccount.DomainAccountManager.authWithPopup({
    onResult: (resultCode: int, authResult: osAccount.AuthResult) => {
      console.info('auth resultCode = ' + resultCode);
      console.info('auth authResult = ' + JSON.stringify(authResult));
    }
  })
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`auth exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  osAccount.DomainAccountManager.authWithPopup(100, {
    onResult: (resultCode: number, authResult: osAccount.AuthResult) => {
      console.info('authWithPopup resultCode = ' + resultCode);
      console.info('authWithPopup authResult = ' + JSON.stringify(authResult));
    }
  })
} catch (e) {
  const err = e as BusinessError;
  console.error(`authWithPopup exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
try {
  osAccount.DomainAccountManager.authWithPopup(100, {
    onResult: (resultCode: int, authResult: osAccount.AuthResult) => {
      console.info('authWithPopup resultCode = ' + resultCode);
      console.info('authWithPopup authResult = ' + JSON.stringify(authResult));
    }
  })
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`authWithPopup exception = code is ${err.code}, message is ${err.message}`);
}
```

## authWithToken

```TypeScript
authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void
```

使用授权令牌认证指定的域账号。

**起始版本：** 10

<!--Device-DomainPlugin-authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void--><!--Device-DomainPlugin-authWithToken(domainAccountInfo: DomainAccountInfo, token: Uint8Array, callback: IUserAuthCallback): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 | 指示域账号信息。 |
| token | Uint8Array | 是 | 指示PIN码或生物识别认证成功时生成的授权令牌。 |
| callback | IUserAuthCallback | 是 | 指示认证结果回调。 |

**示例**

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

let plugin: osAccount.DomainPlugin = {
  auth: (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array,
    callback: osAccount.IUserAuthCallback) => {},
  authWithPopup: (domainAccountInfo: osAccount.DomainAccountInfo,
    callback: osAccount.IUserAuthCallback) => {},
  authWithToken: (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array,
    callback: osAccount.IUserAuthCallback) => {
    // 模拟认证
    // 通知认证结果
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
osAccount.DomainAccountManager.registerPlugin(plugin);
```

## bindAccount

```TypeScript
bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void
```

绑定指定的域账号。

**起始版本：** 10

<!--Device-DomainPlugin-bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void--><!--Device-DomainPlugin-bindAccount(domainAccountInfo: DomainAccountInfo, localId: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 | 指示域账号信息。 |
| localId | number | 是 | 系统账号ID。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 指示绑定结果回调。 |

**示例**

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
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
    // 模拟绑定操作
    // 通知绑定结果
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

根据指定的选项获取域访问令牌。使用callback异步回调。

**起始版本：** 10

<!--Device-DomainPlugin-getAccessToken(options: GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>): void--><!--Device-DomainPlugin-getAccessToken(options: GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetDomainAccessTokenOptions](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | 是 | 指示获取域访问令牌的选项。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Uint8Array&gt; | 是 | 指示结果回调。 |

**示例**

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
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
    // 模拟获取令牌操作
    // 通知结果
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

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let businessParams: Record<string, Object> = {
  'clientId': 'xxx',
  'secretId': 'yyy'
};  // depends on the implementation of the domain plugin
try {
  osAccount.DomainAccountManager.getAccessToken(businessParams,
    (err: BusinessError, result: Uint8Array) => {
    if (err) {
      console.error(`getAccessToken failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAccessToken result: ' + result);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccessToken exception = code is ${err.code}, message is ${err.message}`);
}
```

```TypeScript
import osAccount from '@ohos.account.osAccount';
import { BusinessError } from '@kit.BasicServicesKit';
import { RecordData } from '@ohos.base';

let businessParams: Record<string, RecordData> = {
  'clientId': 'xxx',
  'secretId': 'yyy'
};  // depends on the implementation of the domain plugin
try {
  osAccount.DomainAccountManager.getAccessToken(businessParams,
    (err: BusinessError | null, result: Uint8Array | undefined) => {
      if (err) {
        console.error(`getAccessToken failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAccessToken result: ' + result);
      }
    });
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`getAccessToken exception = code is ${err.code}, message is ${err.message}`);
}
```

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let businessParams: Record<string, Object> = {
  'clientId': 'xxx',
  'secretId': 'yyy'
};  // depends on the implementation of the domain plugin
try {
  osAccount.DomainAccountManager.getAccessToken(businessParams)
    .then((result: Uint8Array) => {
    console.info('getAccessToken result: ' + result);
  }).catch((err: BusinessError) => {
    console.error(`getAccessToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccessToken exception = code is ${err.code}, message is ${err.message}`);
}
```

```TypeScript
import osAccount from '@ohos.account.osAccount';
import { BusinessError } from '@kit.BasicServicesKit';
import { RecordData } from '@ohos.base';

let businessParams: Record<string, RecordData> = {
  'clientId': 'xxx',
  'secretId': 'yyy'
};  // depends on the implementation of the domain plugin
try {
  osAccount.DomainAccountManager.getAccessToken(businessParams)
    .then((result: Uint8Array) => {
      console.info('getAccessToken result: ' + result);
    }).catch((e: Error) => {
    const err = e as BusinessError;
    console.error(`getAccessToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`getAccessToken exception = code is ${err.code}, message is ${err.message}`);
}
```

## getAccountInfo

```TypeScript
getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void
```

查询指定域账号的信息。使用callback异步回调。

**起始版本：** 10

<!--Device-DomainPlugin-getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void--><!--Device-DomainPlugin-getAccountInfo(options: GetDomainAccountInfoPluginOptions, callback: AsyncCallback<DomainAccountInfo>): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetDomainAccountInfoPluginOptions](arkts-basicservices-osaccount-getdomainaccountinfopluginoptions-i-sys.md) | 是 | 指示域账号信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; | 是 | 指示查询结果回调。 |

**示例**

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
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
    // 模拟获取账号信息
    // 通知结果
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

ArkTS-Dyn示例：

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let domainAccountInfo: osAccount.GetDomainAccountInfoOptions = {
  domain: 'CHINA',
  accountName: 'zhangsan'
}
try {
  osAccount.DomainAccountManager.getAccountInfo(domainAccountInfo,
    (err: BusinessError, result: osAccount.DomainAccountInfo) => {
    if (err) {
      console.error(`call getAccountInfo failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAccountInfo result: ' + result);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccountInfo exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import osAccount from '@ohos.account.osAccount';
import { BusinessError } from '@kit.BasicServicesKit';

let domainAccountInfo: osAccount.GetDomainAccountInfoOptions = {
  domain: 'CHINA',
  accountName: 'zhangsan'
}
try {
  osAccount.DomainAccountManager.getAccountInfo(domainAccountInfo,
    (err: BusinessError | null, result: osAccount.DomainAccountInfo | undefined) => {
      if (err) {
        console.error(`call getAccountInfo failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAccountInfo result: ' + result);
      }
    });
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`getAccountInfo exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let domainAccountInfo: osAccount.GetDomainAccountInfoOptions = {
  domain: 'CHINA',
  accountName: 'zhangsan'
}
try {
  osAccount.DomainAccountManager.getAccountInfo(domainAccountInfo)
    .then((result: osAccount.DomainAccountInfo) => {
    console.info('getAccountInfo result: ' + result);
  }).catch((err: BusinessError) => {
    console.error(`call getAccountInfo failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccountInfo exception = code is ${err.code}, message is ${err.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import osAccount from '@ohos.account.osAccount';
import { BusinessError } from '@kit.BasicServicesKit';

let domainAccountInfo: osAccount.GetDomainAccountInfoOptions = {
  domain: 'CHINA',
  accountName: 'zhangsan'
}
try {
  osAccount.DomainAccountManager.getAccountInfo(domainAccountInfo)
    .then((result: osAccount.DomainAccountInfo) => {
      console.info('getAccountInfo result: ' + result);
    }).catch((e: Error) => {
    const err = e as BusinessError;
    console.error(`call getAccountInfo failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e: Error) {
  const err = e as BusinessError;
  console.error(`getAccountInfo exception = code is ${err.code}, message is ${err.message}`);
}
```

## getAuthStatusInfo

```TypeScript
getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void
```

查询指定域账号的认证状态信息。

**起始版本：** 10

<!--Device-DomainPlugin-getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void--><!--Device-DomainPlugin-getAuthStatusInfo(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<AuthStatusInfo>): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 | 指示域账号信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;AuthStatusInfo&gt; | 是 | 指示查询结果回调。 |

**示例**

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
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

检查指定的域账号令牌是否有效。

**起始版本：** 10

<!--Device-DomainPlugin-isAccountTokenValid(      domainAccountInfo: DomainAccountInfo,      token: Uint8Array,      callback: AsyncCallback<boolean>    ): void--><!--Device-DomainPlugin-isAccountTokenValid(      domainAccountInfo: DomainAccountInfo,      token: Uint8Array,      callback: AsyncCallback<boolean>    ): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 | 指示域账号信息。 |
| token | Uint8Array | 是 | 指示域账号令牌。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | 指示检查结果回调。true表示指定的域账号令牌是有效的；false表示指定的域账号令牌是无效的。 |

**示例**

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
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
    // 模拟检查操作
    // 通知结果
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

解绑指定的域账号。

**起始版本：** 10

<!--Device-DomainPlugin-unbindAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<void>): void--><!--Device-DomainPlugin-unbindAccount(domainAccountInfo: DomainAccountInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 | 指示域账号信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 指示绑定结果回调。 |

**示例**

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
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
    // 模拟解绑操作
    // 通知解绑结果
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

认证指定的域账号。

**类型：** [DomainPluginAuthFunc](arkts-basicservices-osaccount-domainpluginauthfunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-auth: DomainPluginAuthFunc--><!--Device-DomainPlugin-auth: DomainPluginAuthFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## authWithPopup

```TypeScript
authWithPopup: DomainPluginAuthWithPopupFunc
```

弹窗认证指定的域账号。

**类型：** [DomainPluginAuthWithPopupFunc](arkts-basicservices-osaccount-domainpluginauthwithpopupfunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-authWithPopup: DomainPluginAuthWithPopupFunc--><!--Device-DomainPlugin-authWithPopup: DomainPluginAuthWithPopupFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## authWithToken

```TypeScript
authWithToken: DomainPluginAuthWithTokenFunc
```

使用授权令牌认证指定的域账号。

**类型：** [DomainPluginAuthWithTokenFunc](arkts-basicservices-osaccount-domainpluginauthwithtokenfunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-authWithToken: DomainPluginAuthWithTokenFunc--><!--Device-DomainPlugin-authWithToken: DomainPluginAuthWithTokenFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## bindAccount

```TypeScript
bindAccount: DomainPluginBindAccountFunc
```

绑定指定的域账号。

**类型：** [DomainPluginBindAccountFunc](arkts-basicservices-osaccount-domainpluginbindaccountfunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-bindAccount: DomainPluginBindAccountFunc--><!--Device-DomainPlugin-bindAccount: DomainPluginBindAccountFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## getAccessToken

```TypeScript
getAccessToken: DomainPluginGetAccessTokenFunc
```

根据指定的选项获取域访问令牌。

**类型：** [DomainPluginGetAccessTokenFunc](arkts-basicservices-osaccount-domainplugingetaccesstokenfunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-getAccessToken: DomainPluginGetAccessTokenFunc--><!--Device-DomainPlugin-getAccessToken: DomainPluginGetAccessTokenFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## getAccountInfo

```TypeScript
getAccountInfo: DomainPluginGetAccountInfoFunc
```

查询指定域账号的信息。

**类型：** [DomainPluginGetAccountInfoFunc](arkts-basicservices-osaccount-domainplugingetaccountinfofunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-getAccountInfo: DomainPluginGetAccountInfoFunc--><!--Device-DomainPlugin-getAccountInfo: DomainPluginGetAccountInfoFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## getAuthStatusInfo

```TypeScript
getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc
```

查询指定域账号的认证状态信息。

**类型：** [DomainPluginGetAuthStatusInfoFunc](arkts-basicservices-osaccount-domainplugingetauthstatusinfofunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc--><!--Device-DomainPlugin-getAuthStatusInfo: DomainPluginGetAuthStatusInfoFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## isAccountTokenValid

```TypeScript
isAccountTokenValid: DomainPluginIsAccountTokenValidFunc
```

检查指定的域账号令牌是否有效。

**类型：** [DomainPluginIsAccountTokenValidFunc](arkts-basicservices-osaccount-domainpluginisaccounttokenvalidfunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-isAccountTokenValid: DomainPluginIsAccountTokenValidFunc--><!--Device-DomainPlugin-isAccountTokenValid: DomainPluginIsAccountTokenValidFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

## unbindAccount

```TypeScript
unbindAccount: DomainPluginUnbindAccountFunc
```

解绑指定的域账号。

**类型：** [DomainPluginUnbindAccountFunc](arkts-basicservices-osaccount-domainpluginunbindaccountfunc-t-sys.md)

**起始版本：** 23

<!--Device-DomainPlugin-unbindAccount: DomainPluginUnbindAccountFunc--><!--Device-DomainPlugin-unbindAccount: DomainPluginUnbindAccountFunc-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

