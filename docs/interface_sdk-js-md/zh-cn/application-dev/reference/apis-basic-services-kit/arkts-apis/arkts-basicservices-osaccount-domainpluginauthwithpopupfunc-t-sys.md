# DomainPluginAuthWithPopupFunc（系统接口）

```TypeScript
type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,
    callback: IUserAuthCallback) => void
```

弹窗认证指定的域账号。

**起始版本：** 23

<!--Device-osAccount-type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,    callback: IUserAuthCallback) => void--><!--Device-osAccount-type DomainPluginAuthWithPopupFunc = (domainAccountInfo: DomainAccountInfo,    callback: IUserAuthCallback) => void-End-->

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 | 表示域账号信息。 |
| callback | IUserAuthCallback | 是 | 表示认证结果回调。 |

**示例**

```TypeScript
import osAccount from '@ohos.account.osAccount';
import { AsyncCallback } from '@ohos.base';
import { BusinessError } from '@kit.BasicServicesKit';

const authFunc: osAccount.DomainPluginAuthFunc = (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array, callback: osAccount.IUserAuthCallback) => {};
const authWithPopupFunc: osAccount.DomainPluginAuthWithPopupFunc = (domainAccountInfo: osAccount.DomainAccountInfo, callback: osAccount.IUserAuthCallback) => {
  // 模拟认证
  // 通知认证结果
  let result: osAccount.AuthResult = {
    token: new Uint8Array([0]),
    remainTimes: 5,
    freezingTime: 0
  };
  callback.onResult(0, result);
};
const authWithTokenFunc: osAccount.DomainPluginAuthWithTokenFunc = (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array, callback: osAccount.IUserAuthCallback) =>  {};
const getAccountInfoFunc: osAccount.DomainPluginGetAccountInfoFunc = (options: osAccount.GetDomainAccountInfoPluginOptions, callback: AsyncCallback<osAccount.DomainAccountInfo>) => {};
const getAuthStatusInfoFunc: osAccount.DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<osAccount.AuthStatusInfo>) => {};
const bindAccountFunc: osAccount.DomainPluginBindAccountFunc = (domainAccountInfo: osAccount.DomainAccountInfo, localId: int, callback: AsyncCallback<void>) => {};
const unbindAccountFunc: osAccount.DomainPluginUnbindAccountFunc = (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {};
const isAccountTokenValidFunc: osAccount.DomainPluginIsAccountTokenValidFunc = (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array, callback: AsyncCallback<boolean>) => {};
const getAccessTokenFunc: osAccount.DomainPluginGetAccessTokenFunc = (options: osAccount.GetDomainAccessTokenOptions, callback: AsyncCallback<Uint8Array>) => {};

let plugin: osAccount.DomainPlugin = {
  auth: authFunc,
  authWithPopup: authWithPopupFunc,
  authWithToken: authWithTokenFunc,
  getAccountInfo: getAccountInfoFunc,
  getAuthStatusInfo: getAuthStatusInfoFunc,
  bindAccount: bindAccountFunc,
  unbindAccount: unbindAccountFunc,
  isAccountTokenValid: isAccountTokenValidFunc,
  getAccessToken: getAccessTokenFunc
}

try {
  osAccount.DomainAccountManager.registerPlugin(plugin);
  console.info('registerPlugin success.');
} catch(e: Error) {
  const err = e as BusinessError;
  console.error(`registerPlugin code is ${err.code}, message is ${err.message}`);
}
```

