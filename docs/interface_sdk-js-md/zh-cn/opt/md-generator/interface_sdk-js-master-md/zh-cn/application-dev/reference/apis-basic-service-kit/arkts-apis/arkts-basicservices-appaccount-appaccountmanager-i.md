# AppAccountManager

应用账号管理器，可用于管理应用自身的账号信息。

**起始版本：** 23

<!--Device-appAccount-interface AppAccountManager--><!--Device-appAccount-interface AppAccountManager-End-->

**系统能力：** SystemCapability.Account.AppAccount

## 导入模块

```TypeScript
```

## addAccount

```TypeScript
addAccount(name: string, callback: AsyncCallback<void>): void
```

根据账号名添加应用账号。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [createAccount](#createaccount)替 > 代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createAccount](#createaccount)(name: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-addAccount(name: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-addAccount(name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('WangWu', (err: BusinessError) => { 
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

## addAccount

```TypeScript
addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void
```

根据账号名和额外信息添加应用账号。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [createAccount](#createaccount) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createAccount](#createaccount)(name: string, options: CreateAccountOptions, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-addAccount(name: string, extraInfo: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| extraInfo | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('LiSi', 'token101', (err: BusinessError) => { 
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

## addAccount

```TypeScript
addAccount(name: string, extraInfo?: string): Promise<void>
```

根据账号名和额外信息添加应用账号。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [createAccount](#createaccount) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [createAccount](#createaccount)(name: string, options?: CreateAccountOptions)

<!--Device-AppAccountManager-addAccount(name: string, extraInfo?: string): Promise<void>--><!--Device-AppAccountManager-addAccount(name: string, extraInfo?: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| extraInfo | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.addAccount('LiSi', 'token101').then(()=> { 
  console.info('addAccount Success');
}).catch((err: BusinessError) => {
  console.error(`addAccount err: code is ${err.code}, message is ${err.message}`);
});
```

## addAccountImplicitly

```TypeScript
addAccountImplicitly(
      owner: string,
      authType: string,
      options: { [key: string]: any },
      callback: AuthenticatorCallback
    ): void
```

根据指定的账号所有者隐式地添加应用账号。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [createAccountImplicitly](#createaccountimplicitly) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [createAccountImplicitly](#createaccountimplicitly)(owner: string, callback: AuthCallback)

<!--Device-AppAccountManager-addAccountImplicitly(      owner: string,      authType: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void--><!--Device-AppAccountManager-addAccountImplicitly(      owner: string,      authType: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| authType | string | 是 |
| options | { [key: string]: any } | 是 |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result: Record<string, Object>): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    appAccountManager.addAccountImplicitly('com.example.accountjsdemo', 'getSocialData', {}, {
      onResult: this.onResultCallback,
      onRequestRedirected: this.onRequestRedirectedCallback
    });
  }

  build() {}
}
```

## auth

```TypeScript
auth(name: string, owner: string, authType: string, callback: AuthCallback): void
```

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-auth(name: string, owner: string, authType: string, callback: AuthCallback): void--><!--Device-AppAccountManager-auth(name: string, owner: string, authType: string, callback: AuthCallback): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, authResult?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('authResult: ' + JSON.stringify(authResult));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    try {
      appAccountManager.auth('LiSi', 'com.example.accountjsdemo', 'getSocialData', {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`auth exception: code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {}
}
```

## auth

```TypeScript
auth(
      name: string,
      owner: string,
      authType: string,
      options: Record<string, Object>,
      callback: AuthCallback
    ): void
```

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**起始版本：** 9

<!--Device-AppAccountManager-auth(      name: string,      owner: string,      authType: string,      options: Record<string, Object>,      callback: AuthCallback    ): void--><!--Device-AppAccountManager-auth(      name: string,      owner: string,      authType: string,      options: Record<string, Object>,      callback: AuthCallback    ): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| options | Record & lt;string, Object & gt; | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, authResult?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('authResult: ' + JSON.stringify(authResult));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    let options: Record<string, Object> = {
      'password': 'xxxx',
    };
    try {
      appAccountManager.auth('LiSi', 'com.example.accountjsdemo', 'getSocialData', options, {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`auth exception: code is ${err.code}, message is ${err.message}`);
    }
  }

  build() {}
}
```

## auth

```TypeScript
auth(
      name: string,
      owner: string,
      authType: string,
      options: Record<string, RecordData>,
      callback: AuthCallback
    ): void
```

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-auth(      name: string,      owner: string,      authType: string,      options: Record<string, RecordData>,      callback: AuthCallback    ): void--><!--Device-AppAccountManager-auth(      name: string,      owner: string,      authType: string,      options: Record<string, RecordData>,      callback: AuthCallback    ): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| options | Record&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt; | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

## authenticate

```TypeScript
authenticate(
      name: string,
      owner: string,
      authType: string,
      options: { [key: string]: any },
      callback: AuthenticatorCallback
    ): void
```

对应用账号进行鉴权以获取授权令牌。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [auth](#auth) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [auth](#auth)(name: string, owner: string, authType: string, callback: AuthCallback)

<!--Device-AppAccountManager-authenticate(      name: string,      owner: string,      authType: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void--><!--Device-AppAccountManager-authenticate(      name: string,      owner: string,      authType: string,      options: { [key: string]: any },      callback: AuthenticatorCallback    ): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| options | { [key: string]: any } | 是 |
| callback | [AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md) | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result: Record<string, Object>): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    appAccountManager.authenticate('LiSi', 'com.example.accountjsdemo', 'getSocialData', {}, {
      onResult: this.onResultCallback,
      onRequestRedirected: this.onRequestRedirectedCallback
    });
  }

  build() {}
}
```

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void
```

检查指定应用账号是否满足特定的标签集合。使用callback异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**起始版本：** 23

<!--Device-AppAccountManager-checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void--><!--Device-AppAccountManager-checkAccountLabels(name: string, owner: string, labels: Array<string>, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| labels | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let labels = ['student'];
try {
  appAccountManager.checkAccountLabels('zhangsan', 'com.example.accountjsdemo', labels,
    (err: BusinessError, hasAllLabels: boolean) => {
      if (err) {
        console.error(`checkAccountLabels failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAccountLabels successfully, hasAllLabels: ' + hasAllLabels);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAccountLabels exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkAccountLabels

```TypeScript
checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>
```

检查指定应用账号是否满足特定的标签集合。使用Promise异步回调。该方法依赖目标应用的认证器提供标签检查的能力。

**起始版本：** 23

<!--Device-AppAccountManager-checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>--><!--Device-AppAccountManager-checkAccountLabels(name: string, owner: string, labels: Array<string>): Promise<boolean>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| labels | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let labels = ['student'];
try {
  appAccountManager.checkAccountLabels('zhangsan', 'com.example.accountjsdemo', labels).then((
    hasAllLabels: boolean) => {
    console.info('checkAccountLabels successfully: ' + hasAllLabels);
  }).catch((err: BusinessError) => {
    console.error(`checkAccountLabels failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAccountLabels exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkAppAccess

```TypeScript
checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void
```

检查指定应用对特定账号的数据是否可访问。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void--><!--Device-AppAccountManager-checkAppAccess(name: string, bundleName: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAppAccess('ZhangSan', 'com.example.accountjsdemo',
    (err: BusinessError, isAccessible: boolean) => {
      if (err) {
        console.error(`checkAppAccess failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAppAccess successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkAppAccess

```TypeScript
checkAppAccess(name: string, bundleName: string): Promise<boolean>
```

检查指定应用对特定账号的数据是否可访问。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-checkAppAccess(name: string, bundleName: string): Promise<boolean>--><!--Device-AppAccountManager-checkAppAccess(name: string, bundleName: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAppAccess('ZhangSan', 'com.example.accountjsdemo').then((isAccessible: boolean) => {
    console.info('checkAppAccess successfully, isAccessible: ' + isAccessible);
  }).catch((err: BusinessError) => {
    console.error(`checkAppAccess failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkAppAccountSyncEnable

```TypeScript
checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void
```

检查指定应用账号是否开启数据同步功能。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [checkDataSyncEnabled](#checkdatasyncenabled) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkDataSyncEnabled](#checkdatasyncenabled)(name: string, callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-AppAccountManager-checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void--><!--Device-AppAccountManager-checkAppAccountSyncEnable(name: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkAppAccountSyncEnable('ZhangSan', (err: BusinessError, result: boolean) => { 
  if (err) {
    console.error(`checkAppAccountSyncEnable code: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('checkAppAccountSyncEnable result: ' + result);
  }
});
```

## checkAppAccountSyncEnable

```TypeScript
checkAppAccountSyncEnable(name: string): Promise<boolean>
```

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [checkDataSyncEnabled](#checkdatasyncenabled)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [checkDataSyncEnabled](#checkdatasyncenabled)(name: string)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-AppAccountManager-checkAppAccountSyncEnable(name: string): Promise<boolean>--><!--Device-AppAccountManager-checkAppAccountSyncEnable(name: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkAppAccountSyncEnable('ZhangSan').then((data: boolean) => { 
  console.info('checkAppAccountSyncEnable, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`checkAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
});
```

## checkAuthTokenVisibility

```TypeScript
checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void
```

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void--><!--Device-AppAccountManager-checkAuthTokenVisibility(name: string, authType: string, bundleName: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo',
    (err: BusinessError, isVisible: boolean) => {
      if (err) {
        console.error(`checkAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('checkAuthTokenVisibility successfully, isVisible: ' + isVisible);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkAuthTokenVisibility

```TypeScript
checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>
```

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>--><!--Device-AppAccountManager-checkAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo').then((
    isVisible: boolean) => {
    console.info('checkAuthTokenVisibility successfully, isVisible: ' + isVisible);
  }).catch((err: BusinessError) => {
    console.error(`checkAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkDataSyncEnabled

```TypeScript
checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void
```

检查指定应用账号是否开启数据同步功能。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-AppAccountManager-checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void--><!--Device-AppAccountManager-checkDataSyncEnabled(name: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkDataSyncEnabled('ZhangSan', (err: BusinessError, isEnabled: boolean) => {
    if (err) {
      console.error(`checkDataSyncEnabled failed, err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkDataSyncEnabled successfully, isEnabled: ' + isEnabled);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

## checkDataSyncEnabled

```TypeScript
checkDataSyncEnabled(name: string): Promise<boolean>
```

检查指定应用账号是否开启数据同步功能。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-AppAccountManager-checkDataSyncEnabled(name: string): Promise<boolean>--><!--Device-AppAccountManager-checkDataSyncEnabled(name: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.checkDataSyncEnabled('ZhangSan').then((isEnabled: boolean) => {
      console.info('checkDataSyncEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(`checkDataSyncEnabled failed, err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

## checkOAuthTokenVisibility

```TypeScript
checkOAuthTokenVisibility(
      name: string,
      authType: string,
      bundleName: string,
      callback: AsyncCallback<boolean>
    ): void
```

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [checkAuthTokenVisibility](#checkauthtokenvisibility) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [checkAuthTokenVisibility](#checkauthtokenvisibility)(name: string, authType: string, bundleName: string, callback: AsyncCallback&lt;boolean&gt;)

<!--Device-AppAccountManager-checkOAuthTokenVisibility(      name: string,      authType: string,      bundleName: string,      callback: AsyncCallback<boolean>    ): void--><!--Device-AppAccountManager-checkOAuthTokenVisibility(      name: string,      authType: string,      bundleName: string,      callback: AsyncCallback<boolean>    ): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo',
  (err: BusinessError, data: boolean) => {
    if (err) {
      console.error(`checkOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOAuthTokenVisibility isVisible: ' + data);
    }
  });
```

## checkOAuthTokenVisibility

```TypeScript
checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>
```

检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [checkAuthTokenVisibility](#checkauthtokenvisibility) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [checkAuthTokenVisibility](#checkauthtokenvisibility)(name: string, authType: string, bundleName: string)

<!--Device-AppAccountManager-checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>--><!--Device-AppAccountManager-checkOAuthTokenVisibility(name: string, authType: string, bundleName: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.checkOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo').then((
  data: boolean) => {
  console.info('checkOAuthTokenVisibility isVisible: ' + data);
}).catch((err: BusinessError) => {
  console.error(`checkOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
});
```

## createAccount

```TypeScript
createAccount(name: string, callback: AsyncCallback<void>): void
```

根据账号名创建应用账号。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-createAccount(name: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-createAccount(name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300007](../../apis-basic-services-kit/errorcode-account.md#12300007-账号数量已达上限) |
| [12300004](../../apis-basic-services-kit/errorcode-account.md#12300004-账号已存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.createAccount('WangWu', (err: BusinessError) => { 
    if (err) {
      console.error(`createAccount code: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('createAccount successful.');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount err: code is ${err.code}, message is ${err.message}`);
}
```

## createAccount

```TypeScript
createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void
```

根据账号名和可选项创建应用账号。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-createAccount(name: string, options: CreateAccountOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| options | [CreateAccountOptions](arkts-basicservices-appaccount-createaccountoptions-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300007](../../apis-basic-services-kit/errorcode-account.md#12300007-账号数量已达上限) |
| [12300004](../../apis-basic-services-kit/errorcode-account.md#12300004-账号已存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.CreateAccountOptions = {
  customData: {
    age: '10'
  }
}
try {
  appAccountManager.createAccount('LiSi', options, (err: BusinessError) => {
    if (err) {
      console.error(`createAccount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('createAccount successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## createAccount

```TypeScript
createAccount(name: string, options?: CreateAccountOptions): Promise<void>
```

根据账号名和可选项创建应用账号。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-createAccount(name: string, options?: CreateAccountOptions): Promise<void>--><!--Device-AppAccountManager-createAccount(name: string, options?: CreateAccountOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| options | [CreateAccountOptions](arkts-basicservices-appaccount-createaccountoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300007](../../apis-basic-services-kit/errorcode-account.md#12300007-账号数量已达上限) |
| [12300004](../../apis-basic-services-kit/errorcode-account.md#12300004-账号已存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.CreateAccountOptions = {
  customData: {
    age: '10'
  }
}
try {
  appAccountManager.createAccount('LiSi', options).then(() => {
    console.info('createAccount successfully');
  }).catch((err: BusinessError) => {
    console.error(`createAccount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## createAccountImplicitly

```TypeScript
createAccountImplicitly(owner: string, callback: AuthCallback): void
```

根据指定的账号所有者隐式地创建应用账号。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-createAccountImplicitly(owner: string, callback: AuthCallback): void--><!--Device-AppAccountManager-createAccountImplicitly(owner: string, callback: AuthCallback): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |
| [12300007](../../apis-basic-services-kit/errorcode-account.md#12300007-账号数量已达上限) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    try {
      appAccountManager.createAccountImplicitly('com.example.accountjsdemo', {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`createAccountImplicitly exception: code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {}
}
```

## createAccountImplicitly

```TypeScript
createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void
```

根据指定的账号所有者和可选项隐式地创建应用账号。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void--><!--Device-AppAccountManager-createAccountImplicitly(owner: string, options: CreateAccountImplicitlyOptions, callback: AuthCallback): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| options | [CreateAccountImplicitlyOptions](arkts-basicservices-appaccount-createaccountimplicitlyoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |
| [12300007](../../apis-basic-services-kit/errorcode-account.md#12300007-账号数量已达上限) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext

  onResultCallback(code: number, result?: appAccount.AuthResult): void {
    console.info('resultCode: ' + code);
    console.info('result: ' + JSON.stringify(result));
  }

  onRequestRedirectedCallback(request: Want): void {
    let wantInfo: Want = {
      deviceId: '',
      bundleName: 'com.example.accountjsdemo',
      action: 'ohos.want.action.viewData',
      entities: ['entity.system.default'],
    }
    this.context.startAbility(wantInfo).then(() => {
      console.info('startAbility successfully');
    }).catch((err: BusinessError) => {
      console.error(`startAbility err: code is ${err.code}, message is ${err.message}`);
    })
  }

  aboutToAppear(): void {
    let options: appAccount.CreateAccountImplicitlyOptions = {
      authType: 'getSocialData',
      requiredLabels: ['student']
    };
    try {
      appAccountManager.createAccountImplicitly('com.example.accountjsdemo', options, {
        onResult: this.onResultCallback,
        onRequestRedirected: this.onRequestRedirectedCallback
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`createAccountImplicitly exception: code is ${err.code}, message is ${err.message}`);
    }
  }
  build() {}
}
```

## deleteAccount

```TypeScript
deleteAccount(name: string, callback: AsyncCallback<void>): void
```

删除应用账号。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [removeAccount](#removeaccount)替 > 代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [removeAccount](#removeaccount)(name: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-deleteAccount(name: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-deleteAccount(name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteAccount('ZhaoLiu', (err: BusinessError) => { 
  console.error(`deleteAccount err: code is ${err.code}, message is ${err.message}`);
});
```

## deleteAccount

```TypeScript
deleteAccount(name: string): Promise<void>
```

删除应用账号。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [removeAccount](#removeaccount)替 > 代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [removeAccount](#removeaccount)(name: string)

<!--Device-AppAccountManager-deleteAccount(name: string): Promise<void>--><!--Device-AppAccountManager-deleteAccount(name: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteAccount('ZhaoLiu').then(() => { 
  console.info('deleteAccount Success');
}).catch((err: BusinessError) => {
  console.error(`deleteAccount err: code is ${err.code}, message is ${err.message}`);
});
```

## deleteAuthToken

```TypeScript
deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-deleteAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx',
    (err: BusinessError) => {
      if (err) {
        console.error(`deleteAuthToken failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('deleteAuthToken successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

## deleteAuthToken

```TypeScript
deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>
```

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>--><!--Device-AppAccountManager-deleteAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx').then(() => {
    console.info('deleteAuthToken successfully');
  }).catch((err: BusinessError) => {
    console.error(`deleteAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

## deleteCredential

```TypeScript
deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void
```

删除指定应用账号的特定类型的凭据信息。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-deleteCredential(name: string, credentialType: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-凭据不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteCredential('zhangsan', 'PIN_SIX', (err: BusinessError) => {
    if (err) {
      console.error(`deleteCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('deleteCredential successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

## deleteCredential

```TypeScript
deleteCredential(name: string, credentialType: string): Promise<void>
```

删除指定应用账号的特定类型的凭据信息。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-deleteCredential(name: string, credentialType: string): Promise<void>--><!--Device-AppAccountManager-deleteCredential(name: string, credentialType: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-凭据不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.deleteCredential('zhangsan', 'PIN_SIX').then(() => {
    console.info('deleteCredential successfully');
  }).catch((err: BusinessError) => {
    console.error(`deleteCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

## deleteOAuthToken

```TypeScript
deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

删除指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [deleteAuthToken](#deleteauthtoken) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [deleteAuthToken](#deleteauthtoken)(name: string, owner: string, authType: string, token: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-deleteOAuthToken(name: string, owner: string, authType: string, token: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx',
  (err: BusinessError) => {
    if (err) {
      console.error(`deleteOAuthToken err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('deleteOAuthToken successful.');
    }
  });
```

## deleteOAuthToken

```TypeScript
deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>
```

删除指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [deleteAuthToken](#deleteauthtoken) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [deleteAuthToken](#deleteauthtoken)(name: string, owner: string, authType: string, token: string)

<!--Device-AppAccountManager-deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>--><!--Device-AppAccountManager-deleteOAuthToken(name: string, owner: string, authType: string, token: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.deleteOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData', 'xxxxx').then(() => {
  console.info('deleteOAuthToken successfully');
}).catch((err: BusinessError) => {
  console.error(`deleteOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

## disableAppAccess

```TypeScript
disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void
```

禁止指定第三方应用账号名称对指定的第三方应用进行访问。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setAppAccess](#setappaccess) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-disableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.disableAppAccess('ZhangSan', 'com.example.accountjsdemo', (err: BusinessError) => { 
  console.error(`disableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

## disableAppAccess

```TypeScript
disableAppAccess(name: string, bundleName: string): Promise<void>
```

禁止指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setAppAccess](#setappaccess) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean)

<!--Device-AppAccountManager-disableAppAccess(name: string, bundleName: string): Promise<void>--><!--Device-AppAccountManager-disableAppAccess(name: string, bundleName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.disableAppAccess('ZhangSan', 'com.example.accountjsdemo').then(() => { 
  console.info('disableAppAccess Success');
}).catch((err: BusinessError) => {
  console.error(`disableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

## enableAppAccess

```TypeScript
enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void
```

允许指定第三方应用账号名称对指定包名称的第三方应用进行访问。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setAppAccess](#setappaccess) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-enableAppAccess(name: string, bundleName: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.enableAppAccess('ZhangSan', 'com.example.accountjsdemo', (err: BusinessError) => {
  if (err) {
    console.error(`enableAppAccess err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('enableAppAccess successful.');
  }
});
```

## enableAppAccess

```TypeScript
enableAppAccess(name: string, bundleName: string): Promise<void>
```

允许指定第三方应用账号的名称对指定包名称的第三方应用进行访问。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setAppAccess](#setappaccess) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setAppAccess](#setappaccess)(name: string, bundleName: string, isAccessible: boolean)

<!--Device-AppAccountManager-enableAppAccess(name: string, bundleName: string): Promise<void>--><!--Device-AppAccountManager-enableAppAccess(name: string, bundleName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.enableAppAccess('ZhangSan', 'com.example.accountjsdemo').then(() => { 
  console.info('enableAppAccess Success');
}).catch((err: BusinessError) => {
  console.error(`enableAppAccess err: code is ${err.code}, message is ${err.message}`);
});
```

## getAccountCredential

```TypeScript
getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的凭据。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getCredential](#getcredential) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCredential](#getcredential)(name: string, credentialType: string, callback: AsyncCallback&lt;string&gt;)

<!--Device-AppAccountManager-getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void--><!--Device-AppAccountManager-getAccountCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountCredential('ZhangSan', 'credentialType001', (err: BusinessError, result: string) => { 
  if (err) {
    console.error(`getAccountCredential err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAccountCredential result: ' + result);
  }
});
```

## getAccountCredential

```TypeScript
getAccountCredential(name: string, credentialType: string): Promise<string>
```

获取指定应用账号的凭据。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getCredential](#getcredential)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCredential](#getcredential)(name: string, credentialType: string)

<!--Device-AppAccountManager-getAccountCredential(name: string, credentialType: string): Promise<string>--><!--Device-AppAccountManager-getAccountCredential(name: string, credentialType: string): Promise<string>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountCredential('ZhangSan', 'credentialType001').then((data: string) => { 
  console.info('getAccountCredential, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAccountCredential err: code is ${err.code}, message is ${err.message}`);
});
```

## getAccountExtraInfo

```TypeScript
getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getCustomData](#getcustomdata) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCustomData](#getcustomdata)(name: string, key: string, callback: AsyncCallback&lt;string&gt;)

<!--Device-AppAccountManager-getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void--><!--Device-AppAccountManager-getAccountExtraInfo(name: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountExtraInfo('ZhangSan', (err: BusinessError, result: string) => { 
  if (err) {
    console.error(`getAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAccountExtraInfo result: ' + result);
  }
});
```

## getAccountExtraInfo

```TypeScript
getAccountExtraInfo(name: string): Promise<string>
```

获取指定应用账号的额外信息（能转换成string类型的其它信息）。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getCustomData](#getcustomdata)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCustomData](#getcustomdata)(name: string, key: string)

<!--Device-AppAccountManager-getAccountExtraInfo(name: string): Promise<string>--><!--Device-AppAccountManager-getAccountExtraInfo(name: string): Promise<string>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAccountExtraInfo('ZhangSan').then((data: string) => { 
  console.info('getAccountExtraInfo, result: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
});
```

## getAccountsByOwner

```TypeScript
getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。 此方法适用于以下账户： <br> 本应用的账户。 <br> 第三方应用的账户。要获取此类信息， <br> 您的应用必须已获得第三方应用的授权，或 <br> 已获得ohos.permission.GET_ALL_APP_ACCOUNTS权限。

**起始版本：** 23

<!--Device-AppAccountManager-getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-getAccountsByOwner(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400001](../../apis-basic-services-kit/errorcode-account.md#12400001-应用不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAccountsByOwner('com.example.accountjsdemo2',
    (err: BusinessError, data: appAccount.AppAccountInfo[]) => {
      if (err) {
        console.error(`getAccountsByOwner failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAccountsByOwner successfully, data:' + JSON.stringify(data));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccountsByOwner exception:code is ${err.code}, message is ${err.message}`);
}
```

## getAccountsByOwner

```TypeScript
getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>
```

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。 此方法适用于以下账户： <br> 本应用的账户。 <br> 第三方应用的账户。要获取此类信息， <br> 您的应用必须已获得第三方应用的授权，或 <br> 已获得ohos.permission.GET_ALL_APP_ACCOUNTS权限。

**起始版本：** 23

<!--Device-AppAccountManager-getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>--><!--Device-AppAccountManager-getAccountsByOwner(owner: string): Promise<Array<AppAccountInfo>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400001](../../apis-basic-services-kit/errorcode-account.md#12400001-应用不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAccountsByOwner('com.example.accountjsdemo2').then((
    data: appAccount.AppAccountInfo[]) => {
    console.info('getAccountsByOwner successfully, data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`getAccountsByOwner failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAccountsByOwner exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAllAccessibleAccounts

```TypeScript
getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void
```

获取所有可访问的应用账号信息。使用callback异步回调。 此方法适用于以下账户： <br> 本应用的账户。 <br> 第三方应用的账户。要获取此类信息， <br> 您的应用必须已获得第三方应用的授权。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getAllAccounts](#getallaccounts) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAllAccounts](#getallaccounts)(callback: AsyncCallback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS

<!--Device-AppAccountManager-getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-getAllAccessibleAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllAccessibleAccounts((err: BusinessError, data: appAccount.AppAccountInfo[])=>{
  if (err) {
    console.error(`getAllAccessibleAccounts err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAllAccessibleAccounts data: ' + JSON.stringify(data));
  }
});
```

## getAllAccessibleAccounts

```TypeScript
getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>
```

获取所有可访问的应用账号信息。使用Promise异步回调。 此方法适用于以下账户： <br> 本应用的账户。 <br> 第三方应用的账户。要获取此类信息， <br> 您的应用必须已获得第三方应用的授权。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用[getAllAccounts](#getallaccounts) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAllAccounts](#getallaccounts)()

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS

<!--Device-AppAccountManager-getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>--><!--Device-AppAccountManager-getAllAccessibleAccounts(): Promise<Array<AppAccountInfo>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllAccessibleAccounts().then((data: appAccount.AppAccountInfo[]) => { 
  console.info('getAllAccessibleAccounts: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAllAccessibleAccounts err: code is ${err.code}, message is ${err.message}`);
});
```

## getAllAccounts

```TypeScript
getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void
```

获取所有可访问的应用账号信息。使用callback异步回调。 此方法适用于以下账户： <br> 本应用的账户。 <br> 第三方应用的账户。要获取此类信息， <br> 您的应用必须已获得第三方应用的授权，或 <br> 已获得ohos.permission.GET_ALL_APP_ACCOUNTS权限。

**起始版本：** 23

<!--Device-AppAccountManager-getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-getAllAccounts(callback: AsyncCallback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAccounts((err: BusinessError, data: appAccount.AppAccountInfo[]) => {
    if (err) {
      console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAllAccounts successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAccounts exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAllAccounts

```TypeScript
getAllAccounts(): Promise<Array<AppAccountInfo>>
```

获取所有可访问的应用账号信息。使用Promise异步回调。 此方法适用于以下账户： <br> 本应用的账户。 <br> 第三方应用的账户。要获取此类信息， <br> 您的应用必须已获得第三方应用的授权，或 <br> 已获得ohos.permission.GET_ALL_APP_ACCOUNTS权限。

**起始版本：** 23

<!--Device-AppAccountManager-getAllAccounts(): Promise<Array<AppAccountInfo>>--><!--Device-AppAccountManager-getAllAccounts(): Promise<Array<AppAccountInfo>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAccounts().then((data: appAccount.AppAccountInfo[]) => {
    console.info('getAllAccounts successfully');
  }).catch((err: BusinessError) => {
    console.error(`getAllAccounts failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAccounts exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAllAccounts

```TypeScript
getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

根据应用账号所有者获取调用方可访问的应用账号列表。使用callback异步回调。 此方法适用于以下账户： <br> 本应用的账户。 <br> 第三方应用的账户。要获取此类信息， <br> 您的应用必须已获得第三方应用的授权。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getAccountsByOwner](#getaccountsbyowner) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAccountsByOwner](#getaccountsbyowner)(owner: string, callback: AsyncCallback&lt;Array&lt;AppAccountInfo&gt;&gt;)

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS

<!--Device-AppAccountManager-getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-getAllAccounts(owner: string, callback: AsyncCallback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const selfBundle = 'com.example.actsgetallaaccounts';
appAccountManager.getAllAccounts(selfBundle, (err: BusinessError, data: appAccount.AppAccountInfo[])=>{
  if (err) {
    console.error(`getAllAccounts err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAllAccounts data:' + JSON.stringify(data));
  }
});
```

## getAllAccounts

```TypeScript
getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>
```

根据应用账号所有者获取调用方可访问的应用账号列表。使用Promise异步回调。 此方法适用于以下账户： <br> 本应用的账户。 <br> 第三方应用的账户。要获取此类信息， <br> 您的应用必须已获得第三方应用的授权。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getAccountsByOwner](#getaccountsbyowner)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getAccountsByOwner](#getaccountsbyowner)(owner: string)

**需要权限：** ohos.permission.GET_ALL_APP_ACCOUNTS

<!--Device-AppAccountManager-getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>--><!--Device-AppAccountManager-getAllAccounts(owner: string): Promise<Array<AppAccountInfo>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const selfBundle = 'com.example.actsgetallaaccounts';
appAccountManager.getAllAccounts(selfBundle).then((data: appAccount.AppAccountInfo[]) => { 
  console.info('getAllAccounts: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAllAccounts err: code is ${err.code}, message is ${err.message}`);
});
```

## getAllAuthTokens

```TypeScript
getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void
```

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void--><!--Device-AppAccountManager-getAllAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<AuthTokenInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAuthTokens('LiSi', 'com.example.accountjsdemo',
    (err: BusinessError, tokenArr: appAccount.AuthTokenInfo[]) => {
      if (err) {
        console.error(`getAllAuthTokens failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAllAuthTokens successfully, tokenArr: ' + tokenArr);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAuthTokens exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAllAuthTokens

```TypeScript
getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>
```

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>--><!--Device-AppAccountManager-getAllAuthTokens(name: string, owner: string): Promise<Array<AuthTokenInfo>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AuthTokenInfo](arkts-basicservices-appaccount-authtokeninfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAllAuthTokens('LiSi', 'com.example.accountjsdemo').then((
    tokenArr: appAccount.AuthTokenInfo[]) => {
    console.info('getAllAuthTokens successfully, tokenArr: ' + JSON.stringify(tokenArr));
  }).catch((err: BusinessError) => {
    console.error(`getAllAuthTokens failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAllAuthTokens exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAllOAuthTokens

```TypeScript
getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void
```

获取指定账号对调用方可见的所有授权令牌。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [getAllAuthTokens](#getallauthtokens) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAllAuthTokens](#getallauthtokens)(name: string, owner: string, callback: AsyncCallback&lt;Array&lt;AuthTokenInfo&gt;&gt;)

<!--Device-AppAccountManager-getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void--><!--Device-AppAccountManager-getAllOAuthTokens(name: string, owner: string, callback: AsyncCallback<Array<OAuthTokenInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OAuthTokenInfo](arkts-basicservices-appaccount-oauthtokeninfo-i.md)&gt;&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllOAuthTokens('LiSi', 'com.example.accountjsdemo',
  (err: BusinessError, data: appAccount.OAuthTokenInfo[]) => {
    if (err) {
      console.error(`getAllOAuthTokens err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAllOAuthTokens data: ' + JSON.stringify(data));
    }
  });
```

## getAllOAuthTokens

```TypeScript
getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>
```

获取指定账号对调用方可见的所有授权令牌。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [getAllAuthTokens](#getallauthtokens)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAllAuthTokens](#getallauthtokens)(name: string, owner: string)

<!--Device-AppAccountManager-getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>--><!--Device-AppAccountManager-getAllOAuthTokens(name: string, owner: string): Promise<Array<OAuthTokenInfo>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[OAuthTokenInfo](arkts-basicservices-appaccount-oauthtokeninfo-i.md)&gt;&gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAllOAuthTokens('LiSi', 'com.example.accountjsdemo').then((
  data: appAccount.OAuthTokenInfo[]) => {
  console.info('getAllOAuthTokens data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getAllOAuthTokens err: code is ${err.code}, message is ${err.message}`);
});
```

## getAssociatedData

```TypeScript
getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void
```

根据指定键名获取特定应用账号的关联数据。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getCustomData](#getcustomdata) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCustomData](#getcustomdata)(name: string, key: string, callback: AsyncCallback&lt;string&gt;)

<!--Device-AppAccountManager-getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void--><!--Device-AppAccountManager-getAssociatedData(name: string, key: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAssociatedData('ZhangSan', 'k001', (err: BusinessError, result: string) => { 
  if (err) {
    console.error(`getAssociatedData err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getAssociatedData result: ' + result);
  }
});
```

## getAssociatedData

```TypeScript
getAssociatedData(name: string, key: string): Promise<string>
```

获取与此应用程序账号关联的数据。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [getCustomData](#getcustomdata)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getCustomData](#getcustomdata)(name: string, key: string)

<!--Device-AppAccountManager-getAssociatedData(name: string, key: string): Promise<string>--><!--Device-AppAccountManager-getAssociatedData(name: string, key: string): Promise<string>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAssociatedData('ZhangSan', 'k001').then((data: string) => { 
  console.info('getAssociatedData: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getAssociatedData err: code is ${err.code}, message is ${err.message}`);
});
```

## getAuthCallback

```TypeScript
getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void
```

获取鉴权会话的认证器回调对象。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void--><!--Device-AppAccountManager-getAuthCallback(sessionId: string, callback: AsyncCallback<AuthCallback>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300108](../../apis-basic-services-kit/errorcode-account.md#12300108-认证会话不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    try {
      appAccountManager.getAuthCallback(sessionId, (err: BusinessError, callback: appAccount.AuthCallback) => {
        if (err != null) {
          console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
          return;
        }
        let result: appAccount.AuthResult = {
          account: {
            name: 'Lisi',
            owner: 'com.example.accountjsdemo',
          },
          tokenInfo: {
            token: 'xxxxxx',
            authType: 'getSocialData'
          }
        }; 
        callback.onResult(0, result);
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`getAuthCallback exception: code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

## getAuthCallback

```TypeScript
getAuthCallback(sessionId: string): Promise<AuthCallback>
```

获取鉴权会话的认证器回调对象。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getAuthCallback(sessionId: string): Promise<AuthCallback>--><!--Device-AppAccountManager-getAuthCallback(sessionId: string): Promise<AuthCallback>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthCallback](arkts-basicservices-appaccount-authcallback-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300108](../../apis-basic-services-kit/errorcode-account.md#12300108-认证会话不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    try {
      appAccountManager.getAuthCallback(sessionId).then((callback: appAccount.AuthCallback) => {
      let result: appAccount.AuthResult = {
        account: {
          name: 'Lisi',
          owner: 'com.example.accountjsdemo',
        },
        tokenInfo: {
          token: 'xxxxxx',
          authType: 'getSocialData'
        }
      };
      callback.onResult(0, result);
      }).catch((err: BusinessError) => {
        console.error(`getAuthCallback err: code is ${err.code}, message is ${err.message}`);
      });
    } catch (e) {
      const err = e as BusinessError;
      console.error(`getAuthCallback exception: code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

## getAuthList

```TypeScript
getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void
```

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过 [setAuthTokenVisibility](#setauthtokenvisibility) 来设置）。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void--><!--Device-AppAccountManager-getAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthList('LiSi', 'getSocialData', (err: BusinessError, authList: string[]) => {
    if (err) {
      console.error(`getAuthList failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAuthList successfully, authList: ' + authList);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthList exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAuthList

```TypeScript
getAuthList(name: string, authType: string): Promise<Array<string>>
```

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过 [setAuthTokenVisibility](#setauthtokenvisibility) 来设置）。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getAuthList(name: string, authType: string): Promise<Array<string>>--><!--Device-AppAccountManager-getAuthList(name: string, authType: string): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthList('LiSi', 'getSocialData').then((authList: string[]) => {
    console.info('getAuthList successfully, authList: ' + authList);
  }).catch((err: BusinessError) => {
    console.error(`getAuthList failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthList exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAuthToken

```TypeScript
getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void--><!--Device-AppAccountManager-getAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData',
    (err: BusinessError, token: string) => {
      if (err) {
        console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('getAuthToken successfully, token: ' + token);
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAuthToken

```TypeScript
getAuthToken(name: string, owner: string, authType: string): Promise<string>
```

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getAuthToken(name: string, owner: string, authType: string): Promise<string>--><!--Device-AppAccountManager-getAuthToken(name: string, owner: string, authType: string): Promise<string>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData').then((token: string) => {
    console.info('getAuthToken successfully, token: ' + token);
  }).catch((err: BusinessError) => {
    console.error(`getAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

## getAuthenticatorCallback

```TypeScript
getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void
```

获取鉴权会话的认证器回调。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [getAuthCallback](#getauthcallback) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthCallback](#getauthcallback)(sessionId: string, callback: AsyncCallback&lt;AuthCallback&gt;)

<!--Device-AppAccountManager-getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void--><!--Device-AppAccountManager-getAuthenticatorCallback(sessionId: string, callback: AsyncCallback<AuthenticatorCallback>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md)&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    appAccountManager.getAuthenticatorCallback(sessionId,
        (err: BusinessError, callback: appAccount.AuthenticatorCallback) => {
        if (err.code != appAccount.ResultCode.SUCCESS) {
            console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
            return;
        }
        callback.onResult(appAccount.ResultCode.SUCCESS, {
          name: 'LiSi',
          owner: 'com.example.accountjsdemo',
          authType: 'getSocialData',
          token: 'xxxxxx'
        });
      });
  }
}
```

## getAuthenticatorCallback

```TypeScript
getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>
```

获取鉴权会话的认证器回调。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [getAuthCallback](#getauthcallback)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthCallback](#getauthcallback)(sessionId: string)

<!--Device-AppAccountManager-getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>--><!--Device-AppAccountManager-getAuthenticatorCallback(sessionId: string): Promise<AuthenticatorCallback>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthenticatorCallback](arkts-basicservices-appaccount-authenticatorcallback-i.md)&gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) { // ability 生命周期函数
    let sessionId: string = want.parameters![appAccount.Constants.KEY_SESSION_ID] as string;
    appAccountManager.getAuthenticatorCallback(sessionId).then((
      callback: appAccount.AuthenticatorCallback) => {
      callback.onResult(appAccount.ResultCode.SUCCESS, {
        name: 'LiSi',
        owner: 'com.example.accountjsdemo',
        authType: 'getSocialData',
        token: 'xxxxxx'
      });
    }).catch((err: BusinessError) => {
      console.error(`getAuthenticatorCallback err: code is ${err.code}, message is ${err.message}`);
    });
  }
}
```

## getAuthenticatorInfo

```TypeScript
getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void
```

获取指定应用的认证器信息。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [queryAuthenticatorInfo](#queryauthenticatorinfo) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [queryAuthenticatorInfo](#queryauthenticatorinfo)(owner: string, callback: AsyncCallback&lt;AuthenticatorInfo&gt;)

<!--Device-AppAccountManager-getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void--><!--Device-AppAccountManager-getAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAuthenticatorInfo('com.example.accountjsdemo',
  (err: BusinessError, data: appAccount.AuthenticatorInfo) => {
    if (err) {
      console.error(`getAuthenticatorInfo err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getAuthenticatorInfo data: ' + JSON.stringify(data));
    }
  });
```

## getAuthenticatorInfo

```TypeScript
getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>
```

获取指定应用的认证器信息。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [queryAuthenticatorInfo](#queryauthenticatorinfo)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [queryAuthenticatorInfo](#queryauthenticatorinfo)(owner: string)

<!--Device-AppAccountManager-getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>--><!--Device-AppAccountManager-getAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getAuthenticatorInfo('com.example.accountjsdemo').then((
  data: appAccount.AuthenticatorInfo) => { 
  console.info('getAuthenticatorInfo: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getAuthenticatorInfo err: code is ${err.code}, message is ${err.message}`);
});
```

## getCredential

```TypeScript
getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的凭据。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void--><!--Device-AppAccountManager-getCredential(name: string, credentialType: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-凭据不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCredential('ZhangSan', 'PIN_SIX', (err: BusinessError, result: string) => {
    if (err) {
      console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getCredential successfully, result: ' + result);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCredential err: code is ${err.code}, message is ${err.message}`);
}
```

## getCredential

```TypeScript
getCredential(name: string, credentialType: string): Promise<string>
```

获取指定应用账号的凭据。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getCredential(name: string, credentialType: string): Promise<string>--><!--Device-AppAccountManager-getCredential(name: string, credentialType: string): Promise<string>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300102](../../apis-basic-services-kit/errorcode-account.md#12300102-凭据不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCredential('ZhangSan', 'PIN_SIX').then((credential: string) => {
    console.info('getCredential successfully, credential: ' + credential);
  }).catch((err: BusinessError) => {
    console.error(`getCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

## getCustomData

```TypeScript
getCustomData(name: string, key: string, callback: AsyncCallback<string>): void
```

根据指定键名获取特定应用账号的自定义数据。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getCustomData(name: string, key: string, callback: AsyncCallback<string>): void--><!--Device-AppAccountManager-getCustomData(name: string, key: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400002](../../apis-basic-services-kit/errorcode-account.md#12400002-自定义数据不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCustomData('ZhangSan', 'age', (err: BusinessError, data: string) => {
    if (err) {
      console.error('getCustomData failed, error: ' + err);
    } else {
      console.info('getCustomData successfully, data: ' + data);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

## getCustomData

```TypeScript
getCustomData(name: string, key: string): Promise<string>
```

根据指定键名获取特定应用账号的自定义数据。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-getCustomData(name: string, key: string): Promise<string>--><!--Device-AppAccountManager-getCustomData(name: string, key: string): Promise<string>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400002](../../apis-basic-services-kit/errorcode-account.md#12400002-自定义数据不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.getCustomData('ZhangSan', 'age').then((data: string) => {
    console.info('getCustomData successfully, data: ' + data);
  }).catch((err: BusinessError) => {
    console.error(`getCustomData failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

## getCustomDataSync

```TypeScript
getCustomDataSync(name: string, key: string): string
```

根据指定键名获取特定应用账号的自定义数据。使用同步方式返回结果。

**起始版本：** 23

<!--Device-AppAccountManager-getCustomDataSync(name: string, key: string): string--><!--Device-AppAccountManager-getCustomDataSync(name: string, key: string): string-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400002](../../apis-basic-services-kit/errorcode-account.md#12400002-自定义数据不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value = appAccountManager.getCustomDataSync('ZhangSan', 'age');
  console.info('getCustomDataSync successfully, value: ' + value);
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCustomDataSync failed, code is ${err.code}, message is ${err.message}`);
}
```

## getOAuthList

```TypeScript
getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void
```

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过 [setOAuthTokenVisibility](#setoauthtokenvisibility) 来设置）。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [getAuthList](#getauthlist) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthList](#getauthlist)(name: string, authType: string, callback: AsyncCallback&lt;Array&lt;string&gt;&gt;)

<!--Device-AppAccountManager-getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void--><!--Device-AppAccountManager-getOAuthList(name: string, authType: string, callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthList('LiSi', 'getSocialData', (err: BusinessError, data: string[]) => {
  if (err) {
    console.error(`getOAuthList err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOAuthList data: ' + JSON.stringify(data));
  }
});
```

## getOAuthList

```TypeScript
getOAuthList(name: string, authType: string): Promise<Array<string>>
```

获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过 [setOAuthTokenVisibility](#setoauthtokenvisibility) 来设置）。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [getAuthList](#getauthlist)替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthList](#getauthlist)(name: string, authType: string)

<!--Device-AppAccountManager-getOAuthList(name: string, authType: string): Promise<Array<string>>--><!--Device-AppAccountManager-getOAuthList(name: string, authType: string): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthList('LiSi', 'getSocialData').then((data: string[]) => {
  console.info('getOAuthList data: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`getOAuthList err: code is ${err.code}, message is ${err.message}`);
});
```

## getOAuthToken

```TypeScript
getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void
```

获取指定应用账号的特定鉴权类型的授权令牌。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [getAuthToken](#getauthtoken) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthToken](#getauthtoken)(name: string, owner: string, authType: string, callback: AsyncCallback&lt;string&gt;)

<!--Device-AppAccountManager-getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void--><!--Device-AppAccountManager-getOAuthToken(name: string, owner: string, authType: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData',
  (err: BusinessError, data: string) => {
    if (err) {
      console.error(`getOAuthToken err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOAuthToken token: ' + data);
    }
  });
```

## getOAuthToken

```TypeScript
getOAuthToken(name: string, owner: string, authType: string): Promise<string>
```

获取指定应用账号的特定鉴权类型的授权令牌。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [getAuthToken](#getauthtoken)替 > 代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getAuthToken](#getauthtoken)(name: string, owner: string, authType: string)

<!--Device-AppAccountManager-getOAuthToken(name: string, owner: string, authType: string): Promise<string>--><!--Device-AppAccountManager-getOAuthToken(name: string, owner: string, authType: string): Promise<string>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| authType | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.getOAuthToken('LiSi', 'com.example.accountjsdemo', 'getSocialData').then((data: string) => {
  console.info('getOAuthToken token: ' + data);
}).catch((err: BusinessError) => {
  console.error(`getOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

## offAccountChange

```TypeScript
offAccountChange(callback?: Callback<Array<AppAccountInfo>>): void
```

取消订阅账号信息变更事件。

**起始版本：** 23

<!--Device-AppAccountManager-offAccountChange(callback?: Callback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-offAccountChange(callback?: Callback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

## off_accountChange

```TypeScript
off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void
```

取消订阅账号信息变更事件。

**起始版本：** 9

<!--Device-AppAccountManager-off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-off(type: 'accountChange', callback?: Callback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'accountChange' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('accountChange', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountChange failed, code is ${err.code}, message is ${err.message}`);
}
try {
  appAccountManager.off('accountChange', changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`off accountChange failed, code is ${err.code}, message is ${err.message}`);
}
```

## off_change

```TypeScript
off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void
```

取消订阅账号信息变更事件。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [off('accountChange')](#offchange) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [off](#offchange)(type: 'accountChange', callback?: Callback&lt;Array&lt;AppAccountInfo&gt;&gt;)

<!--Device-AppAccountManager-off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-off(type: 'change', callback?: Callback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 否 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data: ' + JSON.stringify(data));
  appAccountManager.off('change', () => {
    console.info('off finish');
  })
}

try {
  appAccountManager.on('change', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountOnOffDemo err: code is ${err.code}, message is ${err.message}`);
}
```

## onAccountChange

```TypeScript
onAccountChange(owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void
```

订阅指定应用的账号信息变更事件。

**起始版本：** 23

<!--Device-AppAccountManager-onAccountChange(owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-onAccountChange(owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owners | Array & lt;string & gt; | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

## on_accountChange

```TypeScript
on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void
```

订阅指定应用的账号信息变更事件。

**起始版本：** 9

<!--Device-AppAccountManager-on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-on(type: 'accountChange', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'accountChange' | 是 |
| owners | Array & lt;string & gt; | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400001](../../apis-basic-services-kit/errorcode-account.md#12400001-应用不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('accountChange', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountChange failed, code is ${err.code}, message is ${err.message}`);
}
```

## on_change

```TypeScript
on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void
```

订阅指定应用的账号信息变更事件。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [on('accountChange')](#onchange) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [on](#onchange)(type: 'accountChange', owners: Array&lt;string&gt;, callback: Callback&lt;Array&lt;AppAccountInfo&gt;&gt;)

<!--Device-AppAccountManager-on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-on(type: 'change', owners: Array<string>, callback: Callback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| owners | Array & lt;string & gt; | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function changeOnCallback(data: appAccount.AppAccountInfo[]): void {
  console.info('receive change data:' + JSON.stringify(data));
}

try {
  appAccountManager.on('change', ['com.example.actsaccounttest'], changeOnCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`on accountOnOffDemo code is ${err.code}, message is ${err.message}`);
}
```

## queryAuthenticatorInfo

```TypeScript
queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void
```

获取指定应用的认证器信息。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void--><!--Device-AppAccountManager-queryAuthenticatorInfo(owner: string, callback: AsyncCallback<AuthenticatorInfo>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.queryAuthenticatorInfo('com.example.accountjsdemo',
    (err: BusinessError, info: appAccount.AuthenticatorInfo) => {
      if (err) {
        console.error(`queryAuthenticatorInfo failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('queryAuthenticatorInfo successfully, info: ' + JSON.stringify(info));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryAuthenticatorInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryAuthenticatorInfo

```TypeScript
queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>
```

获取指定应用的认证器信息。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>--><!--Device-AppAccountManager-queryAuthenticatorInfo(owner: string): Promise<AuthenticatorInfo>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AuthenticatorInfo](arkts-basicservices-appaccount-authenticatorinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.queryAuthenticatorInfo('com.example.accountjsdemo').then((
    info: appAccount.AuthenticatorInfo) => { 
    console.info('queryAuthenticatorInfo successfully, info: ' + JSON.stringify(info));
  }).catch((err: BusinessError) => {
    console.error(`queryAuthenticatorInfo failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryAuthenticatorInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

## removeAccount

```TypeScript
removeAccount(name: string, callback: AsyncCallback<void>): void
```

删除应用账号。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-removeAccount(name: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-removeAccount(name: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.removeAccount('ZhaoLiu', (err: BusinessError) => {
    if (err) {
      console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('removeAccount successfully');
    }
 });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## removeAccount

```TypeScript
removeAccount(name: string): Promise<void>
```

删除应用账号。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-removeAccount(name: string): Promise<void>--><!--Device-AppAccountManager-removeAccount(name: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.removeAccount('Lisi').then(() => {
    console.info('removeAccount successfully');
  }).catch((err: BusinessError) => {
    console.error(`removeAccount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## selectAccountsByOptions

```TypeScript
selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void
```

根据选项选择调用方可访问的账号列表。使用callback异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**起始版本：** 23

<!--Device-AppAccountManager-selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void--><!--Device-AppAccountManager-selectAccountsByOptions(options: SelectAccountsOptions, callback: AsyncCallback<Array<AppAccountInfo>>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SelectAccountsOptions](arkts-basicservices-appaccount-selectaccountsoptions-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SelectAccountsOptions = {
  allowedOwners: ['com.example.accountjsdemo'],
  requiredLabels: ['student']
};
try {
  appAccountManager.selectAccountsByOptions(options,
    (err: BusinessError, accountArr: appAccount.AppAccountInfo[]) => {
      if (err) {
        console.error(`selectAccountsByOptions failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('selectAccountsByOptions successfully, accountArr: ' + JSON.stringify(accountArr));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`selectAccountsByOptions exception: code is ${err.code}, message is ${err.message}`);
}
```

## selectAccountsByOptions

```TypeScript
selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>
```

根据选项选择调用方可访问的账号列表。使用Promise异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**起始版本：** 23

<!--Device-AppAccountManager-selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>--><!--Device-AppAccountManager-selectAccountsByOptions(options: SelectAccountsOptions): Promise<Array<AppAccountInfo>>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [SelectAccountsOptions](arkts-basicservices-appaccount-selectaccountsoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[AppAccountInfo](arkts-basicservices-appaccount-appaccountinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SelectAccountsOptions = {
  allowedOwners: ['com.example.accountjsdemo']
};
try {
  appAccountManager.selectAccountsByOptions(options).then((accountArr: appAccount.AppAccountInfo[]) => {
    console.info('selectAccountsByOptions successfully, accountArr: ' + JSON.stringify(accountArr));
  }).catch((err: BusinessError) => {
    console.error(`selectAccountsByOptions failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`selectAccountsByOptions exception: code is ${err.code}, message is ${err.message}`);
}
```

## setAccountCredential

```TypeScript
setAccountCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>): void
```

设置指定应用账号的凭据。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setCredential](#setcredential) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCredential](#setcredential)(name: string, credentialType: string, credential: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-setAccountCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setAccountCredential(name: string, credentialType: string, credential: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| credential | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountCredential('ZhangSan', 'credentialType001', 'credential001', (err: BusinessError) => { 
  if (err) {
    console.error(`setAccountCredential err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAccountCredential successful.');
  }
});
```

## setAccountCredential

```TypeScript
setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>
```

设置指定应用账号的凭据。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃，建议使用 > [setCredential](#setcredential) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCredential](#setcredential)(name: string, credentialType: string, credential: string)

<!--Device-AppAccountManager-setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>--><!--Device-AppAccountManager-setAccountCredential(name: string, credentialType: string, credential: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| credential | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountCredential('ZhangSan', 'credentialType001', 'credential001').then(() => { 
  console.info('setAccountCredential Success');
}).catch((err: BusinessError) => {
  console.error(`setAccountCredential err: code is ${err.code}, message is ${err.message}`);
});
```

## setAccountExtraInfo

```TypeScript
setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void
```

设置指定应用账号的额外信息。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setCustomData](#setcustomdata) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCustomData](#setcustomdata)(name: string, key: string, value: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setAccountExtraInfo(name: string, extraInfo: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| extraInfo | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountExtraInfo('ZhangSan', 'Tk002', (err: BusinessError) => { 
  if (err) {
    console.error(`setAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAccountExtraInfo successful.');
  }
});
```

## setAccountExtraInfo

```TypeScript
setAccountExtraInfo(name: string, extraInfo: string): Promise<void>
```

设置此应用程序账号的额外信息。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setCustomData](#setcustomdata)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCustomData](#setcustomdata)(name: string, key: string, value: string)

<!--Device-AppAccountManager-setAccountExtraInfo(name: string, extraInfo: string): Promise<void>--><!--Device-AppAccountManager-setAccountExtraInfo(name: string, extraInfo: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| extraInfo | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAccountExtraInfo('ZhangSan', 'Tk002').then(() => { 
  console.info('setAccountExtraInfo Success');
}).catch((err: BusinessError) => {
  console.error(`setAccountExtraInfo err: code is ${err.code}, message is ${err.message}`);
});
```

## setAppAccess

```TypeScript
setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void
```

设置指定应用对特定账号的访问权限。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setAppAccess(name: string, bundleName: string, isAccessible: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| isAccessible | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12400005](../../apis-basic-services-kit/errorcode-account.md#12400005-授权列表已达上限) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400001](../../apis-basic-services-kit/errorcode-account.md#12400001-应用不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true, (err: BusinessError) => {
    if (err) {
      console.error(`setAppAccess failed: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setAppAccess successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

## setAppAccess

```TypeScript
setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>
```

设置指定应用对特定账号的数据访问权限。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>--><!--Device-AppAccountManager-setAppAccess(name: string, bundleName: string, isAccessible: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| bundleName | string | 是 |
| isAccessible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12400005](../../apis-basic-services-kit/errorcode-account.md#12400005-授权列表已达上限) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400001](../../apis-basic-services-kit/errorcode-account.md#12400001-应用不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAppAccess('ZhangSan', 'com.example.accountjsdemo', true).then(() => {
    console.info('setAppAccess successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAppAccess failed: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAppAccess exception: code is ${err.code}, message is ${err.message}`);
}
```

## setAppAccountSyncEnable

```TypeScript
setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void
```

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setDataSyncEnabled](#setdatasyncenabled) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setDataSyncEnabled](#setdatasyncenabled)(name: string, isEnabled: boolean, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-AppAccountManager-setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setAppAccountSyncEnable(name: string, isEnable: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| isEnable | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAppAccountSyncEnable('ZhangSan', true, (err: BusinessError) => {
  if (err) {
    console.error(`setAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAppAccountSyncEnable successful.');
  }
});
```

## setAppAccountSyncEnable

```TypeScript
setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>
```

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setDataSyncEnabled](#setdatasyncenabled)替代 > 。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setDataSyncEnabled](#setdatasyncenabled)(name: string, isEnabled: boolean)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-AppAccountManager-setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>--><!--Device-AppAccountManager-setAppAccountSyncEnable(name: string, isEnable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| isEnable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAppAccountSyncEnable('ZhangSan', true).then(() => { 
  console.info('setAppAccountSyncEnable Success');
}).catch((err: BusinessError) => {
  console.error(`setAppAccountSyncEnable err: code is ${err.code}, message is ${err.message}`);
});
```

## setAssociatedData

```TypeScript
setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void
```

设置指定应用账号的关联数据。使用callback异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setCustomData](#setcustomdata) > 替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCustomData](#setcustomdata)(name: string, key: string, value: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setAssociatedData(name: string, key: string, value: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAssociatedData('ZhangSan', 'k001', 'v001', (err: BusinessError) => {
  if (err) {
    console.error(`setAssociatedData err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setAssociatedData successful.');
  }
});
```

## setAssociatedData

```TypeScript
setAssociatedData(name: string, key: string, value: string): Promise<void>
```

设置指定应用账号的关联数据。使用Promise异步回调。 > **说明：** > > 从API version 7开始支持，从API version 9开始废弃。建议使用 > [setCustomData](#setcustomdata)替代。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [setCustomData](#setcustomdata)(name: string, key: string, value: string)

<!--Device-AppAccountManager-setAssociatedData(name: string, key: string, value: string): Promise<void>--><!--Device-AppAccountManager-setAssociatedData(name: string, key: string, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setAssociatedData('ZhangSan', 'k001', 'v001').then(() => { 
  console.info('setAssociatedData Success');
}).catch((err: BusinessError) => {
  console.error(`setAssociatedData err: code is ${err.code}, message is ${err.message}`);
});
```

## setAuthToken

```TypeScript
setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12400004](../../apis-basic-services-kit/errorcode-account.md#12400004-令牌数量已达上限) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthToken('LiSi', 'getSocialData', 'xxxx', (err: BusinessError) => {
    if (err) {
      console.error(`setAuthToken failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setAuthToken successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

## setAuthToken

```TypeScript
setAuthToken(name: string, authType: string, token: string): Promise<void>
```

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setAuthToken(name: string, authType: string, token: string): Promise<void>--><!--Device-AppAccountManager-setAuthToken(name: string, authType: string, token: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12400004](../../apis-basic-services-kit/errorcode-account.md#12400004-令牌数量已达上限) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthToken('LiSi', 'getSocialData', 'xxxx').then(() => {
    console.info('setAuthToken successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAuthToken failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthToken exception: code is ${err.code}, message is ${err.message}`);
}
```

## setAuthTokenVisibility

```TypeScript
setAuthTokenVisibility(
      name: string,
      authType: string,
      bundleName: string,
      isVisible: boolean,
      callback: AsyncCallback<void>
    ): void
```

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setAuthTokenVisibility(      name: string,      authType: string,      bundleName: string,      isVisible: boolean,      callback: AsyncCallback<void>    ): void--><!--Device-AppAccountManager-setAuthTokenVisibility(      name: string,      authType: string,      bundleName: string,      isVisible: boolean,      callback: AsyncCallback<void>    ): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| isVisible | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12400005](../../apis-basic-services-kit/errorcode-account.md#12400005-授权列表已达上限) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400001](../../apis-basic-services-kit/errorcode-account.md#12400001-应用不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true,
    (err: BusinessError) => {
      if (err) {
        console.error(`setAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('setAuthTokenVisibility successfully');
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

## setAuthTokenVisibility

```TypeScript
setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>
```

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>--><!--Device-AppAccountManager-setAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| isVisible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [12300107](../../apis-basic-services-kit/errorcode-account.md#12300107-认证类型不存在) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12400005](../../apis-basic-services-kit/errorcode-account.md#12400005-授权列表已达上限) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400001](../../apis-basic-services-kit/errorcode-account.md#12400001-应用不存在) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true).then(() => {
    console.info('setAuthTokenVisibility successfully');
  }).catch((err: BusinessError) => {
    console.error(`setAuthTokenVisibility failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthTokenVisibility exception: code is ${err.code}, message is ${err.message}`);
}
```

## setAuthenticatorProperties

```TypeScript
setAuthenticatorProperties(owner: string, callback: AuthCallback): void
```

设置指定应用的认证器属性。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setAuthenticatorProperties(owner: string, callback: AuthCallback): void--><!--Device-AppAccountManager-setAuthenticatorProperties(owner: string, callback: AuthCallback): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setAuthenticatorProperties('com.example.accountjsdemo', {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('setAuthenticatorProperties onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('setAuthenticatorProperties onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('setAuthenticatorProperties onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthenticatorProperties err: code is ${err.code}, message is ${err.message}`);
}
```

## setAuthenticatorProperties

```TypeScript
setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void
```

设置认证器属性。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void--><!--Device-AppAccountManager-setAuthenticatorProperties(owner: string, options: SetPropertiesOptions, callback: AuthCallback): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| owner | string | 是 |
| options | [SetPropertiesOptions](arkts-basicservices-appaccount-setpropertiesoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.SetPropertiesOptions = {
  properties: { prop1: 'value1' }
};
try {
  appAccountManager.setAuthenticatorProperties('com.example.accountjsdemo', options, {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('setAuthenticatorProperties onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('setAuthenticatorProperties onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('setAuthenticatorProperties onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setAuthenticatorProperties err: code is ${err.code}, message is ${err.message}`);
}
```

## setCredential

```TypeScript
setCredential(name: string, credentialType: string, credential: string,
                             callback: AsyncCallback<void>): void
```

设置指定应用账号的凭据。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setCredential(name: string, credentialType: string, credential: string,                             callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setCredential(name: string, credentialType: string, credential: string,                             callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| credential | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCredential('ZhangSan', 'PIN_SIX', 'xxxxxx', (err: BusinessError) => {
    if (err) {
      console.error(`setCredential failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setCredential successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

## setCredential

```TypeScript
setCredential(name: string, credentialType: string, credential: string): Promise<void>
```

设置指定应用账号的凭据。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setCredential(name: string, credentialType: string, credential: string): Promise<void>--><!--Device-AppAccountManager-setCredential(name: string, credentialType: string, credential: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| credentialType | string | 是 |
| credential | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCredential('ZhangSan', 'PIN_SIX', 'xxxxxx').then(() => {
    console.info('setCredential successfully');
  }).catch((err: BusinessError) => {
    console.error(`setCredential failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCredential exception: code is ${err.code}, message is ${err.message}`);
}
```

## setCustomData

```TypeScript
setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void
```

设置指定应用账号的自定义数据。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setCustomData(name: string, key: string, value: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| value | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400003](../../apis-basic-services-kit/errorcode-account.md#12400003-自定义数据的数量已达上限) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCustomData('ZhangSan', 'age', '12', (err: BusinessError) => {
    if (err) {
      console.error(`setCustomData failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setCustomData successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

## setCustomData

```TypeScript
setCustomData(name: string, key: string, value: string): Promise<void>
```

设置指定应用账号的自定义数据。使用Promise异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-setCustomData(name: string, key: string, value: string): Promise<void>--><!--Device-AppAccountManager-setCustomData(name: string, key: string, value: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| key | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12400003](../../apis-basic-services-kit/errorcode-account.md#12400003-自定义数据的数量已达上限) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.setCustomData('ZhangSan', 'age', '12').then(() => {
    console.info('setCustomData successfully');
  }).catch((err: BusinessError) => {
    console.error(`setCustomData failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setCustomData exception: code is ${err.code}, message is ${err.message}`);
}
```

## setDataSyncEnabled

```TypeScript
setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void
```

开启或禁止指定应用账号的数据同步功能。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-AppAccountManager-setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setDataSyncEnabled(name: string, isEnabled: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| isEnabled | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    appAccountManager.setDataSyncEnabled('ZhangSan', true, (err: BusinessError) => { 
        console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
    });
} catch (e) {
    const err = e as BusinessError;
    console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

## setDataSyncEnabled

```TypeScript
setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>
```

开启或禁止指定应用账号的数据同步功能。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-AppAccountManager-setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>--><!--Device-AppAccountManager-setDataSyncEnabled(name: string, isEnabled: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| isEnabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    appAccountManager.setDataSyncEnabled('ZhangSan', true).then(() => { 
        console.info('setDataSyncEnabled Success');
    }).catch((err: BusinessError) => {
        console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
    });
} catch (e) {
    const err = e as BusinessError;
    console.error(`setDataSyncEnabled err: code is ${err.code}, message is ${err.message}`);
}
```

## setOAuthToken

```TypeScript
setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void
```

为指定应用账号设置特定鉴权类型的授权令牌。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [setAuthToken](#setauthtoken) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setAuthToken](#setauthtoken)(name: string, authType: string, token: string, callback: AsyncCallback&lt;void&gt;)

<!--Device-AppAccountManager-setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void--><!--Device-AppAccountManager-setOAuthToken(name: string, authType: string, token: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| token | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthToken('LiSi', 'getSocialData', 'xxxx', (err: BusinessError) => {
  if (err) {
    console.error(`setOAuthToken err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('setOAuthToken successful.');
  }
});
```

## setOAuthToken

```TypeScript
setOAuthToken(name: string, authType: string, token: string): Promise<void>
```

为指定应用账号设置特定鉴权类型的授权令牌。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [setAuthToken](#setauthtoken)替 > 代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setAuthToken](#setauthtoken)(name: string, authType: string, token: string)

<!--Device-AppAccountManager-setOAuthToken(name: string, authType: string, token: string): Promise<void>--><!--Device-AppAccountManager-setOAuthToken(name: string, authType: string, token: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| token | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthToken('LiSi', 'getSocialData', 'xxxx').then(() => {
  console.info('setOAuthToken successfully');
}).catch((err: BusinessError) => {
  console.error(`setOAuthToken err: code is ${err.code}, message is ${err.message}`);
});
```

## setOAuthTokenVisibility

```TypeScript
setOAuthTokenVisibility(
      name: string,
      authType: string,
      bundleName: string,
      isVisible: boolean,
      callback: AsyncCallback<void>
    ): void
```

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用callback异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [setAuthTokenVisibility](#setauthtokenvisibility) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setAuthTokenVisibility](#setauthtokenvisibility)( name: string, authType: string, bundleName: string, isVisible: boolean, callback: AsyncCallback&lt;void&gt; )

<!--Device-AppAccountManager-setOAuthTokenVisibility(      name: string,      authType: string,      bundleName: string,      isVisible: boolean,      callback: AsyncCallback<void>    ): void--><!--Device-AppAccountManager-setOAuthTokenVisibility(      name: string,      authType: string,      bundleName: string,      isVisible: boolean,      callback: AsyncCallback<void>    ): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| isVisible | boolean | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true,
  (err: BusinessError) => {
    if (err) {
      console.error(`setOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOAuthTokenVisibility successful.');
    }
  });
```

## setOAuthTokenVisibility

```TypeScript
setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>
```

设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。使用Promise异步回调。 > **说明：** > > 从API version 8开始支持，从API version 9开始废弃。建议使用 > [setAuthTokenVisibility](#setauthtokenvisibility) > 替代。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setAuthTokenVisibility](#setauthtokenvisibility)(name: string, authType: string, bundleName: string, isVisible: boolean)

<!--Device-AppAccountManager-setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>--><!--Device-AppAccountManager-setOAuthTokenVisibility(name: string, authType: string, bundleName: string, isVisible: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| authType | string | 是 |
| bundleName | string | 是 |
| isVisible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

appAccountManager.setOAuthTokenVisibility('LiSi', 'getSocialData', 'com.example.accountjsdemo', true).then(() => {
  console.info('setOAuthTokenVisibility successfully');
}).catch((err: BusinessError) => {
  console.error(`setOAuthTokenVisibility err: code is ${err.code}, message is ${err.message}`);
});
```

## verifyCredential

```TypeScript
verifyCredential(name: string, owner: string, callback: AuthCallback): void
```

验证指定账号的凭据。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-verifyCredential(name: string, owner: string, callback: AuthCallback): void--><!--Device-AppAccountManager-verifyCredential(name: string, owner: string, callback: AuthCallback): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appAccountManager.verifyCredential('zhangsan', 'com.example.accountjsdemo', {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('verifyCredential onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('verifyCredential onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('verifyCredential onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`verifyCredential err: code is ${err.code}, message is ${err.message}`);
}
```

## verifyCredential

```TypeScript
verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void
```

验证用户凭据。使用callback异步回调。

**起始版本：** 23

<!--Device-AppAccountManager-verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void--><!--Device-AppAccountManager-verifyCredential(name: string, owner: string, options: VerifyCredentialOptions, callback: AuthCallback): void-End-->

**系统能力：** SystemCapability.Account.AppAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| owner | string | 是 |
| options | [VerifyCredentialOptions](arkts-basicservices-appaccount-verifycredentialoptions-i.md) | 是 |
| callback | [AuthCallback](arkts-basicservices-appaccount-authcallback-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [12300010](../../apis-basic-services-kit/errorcode-account.md#12300010-账号服务忙碌) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300114](../../apis-basic-services-kit/errorcode-account.md#12300114-认证服务异常) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| [12300113](../../apis-basic-services-kit/errorcode-account.md#12300113-认证服务不存在) |

**示例**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: appAccount.VerifyCredentialOptions = {
  credentialType: 'pin',
  credential: '123456'
};
try {
  appAccountManager.verifyCredential('zhangsan', 'com.example.accountjsdemo', options, {
    onResult: (resultCode: number, result?: appAccount.AuthResult) => {
      console.info('verifyCredential onResult, resultCode: ' + JSON.stringify(resultCode));
      console.info('verifyCredential onResult, result: ' + JSON.stringify(result));
    },
    onRequestRedirected: (request: Want) => {
      console.info('verifyCredential onRequestRedirected, request: ' + JSON.stringify(request));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`verifyCredential err: code is ${err.code}, message is ${err.message}`);
}
```
