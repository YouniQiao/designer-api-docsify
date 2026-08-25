# DomainPluginIsAccountTokenValidFunc（系统接口）

```TypeScript
type DomainPluginIsAccountTokenValidFunc = (
    domainAccountInfo: DomainAccountInfo,
    token: Uint8Array,
    callback: AsyncCallback<boolean>
  ) => void
```

检查指定的域账号令牌是否有效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Account.OsAccount

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |
| token | Uint8Array | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**示例**

```TypeScript
import osAccount from '@ohos.account.osAccount';
import { AsyncCallback } from '@ohos.base';
import { BusinessError } from '@kit.BasicServicesKit';

const authFunc: osAccount.DomainPluginAuthFunc = (domainAccountInfo: osAccount.DomainAccountInfo, credential: Uint8Array, callback: osAccount.IUserAuthCallback) => {};
const authWithPopupFunc: osAccount.DomainPluginAuthWithPopupFunc = (domainAccountInfo: osAccount.DomainAccountInfo, callback: osAccount.IUserAuthCallback) => {};
const authWithTokenFunc: osAccount.DomainPluginAuthWithTokenFunc = (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array, callback: osAccount.IUserAuthCallback) =>  {};
const getAccountInfoFunc: osAccount.DomainPluginGetAccountInfoFunc = (options: osAccount.GetDomainAccountInfoPluginOptions, callback: AsyncCallback<osAccount.DomainAccountInfo>) => {};
const getAuthStatusInfoFunc: osAccount.DomainPluginGetAuthStatusInfoFunc = (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<osAccount.AuthStatusInfo>) => {};
const bindAccountFunc: osAccount.DomainPluginBindAccountFunc = (domainAccountInfo: osAccount.DomainAccountInfo, localId: int, callback: AsyncCallback<void>) => {};
const unbindAccountFunc: osAccount.DomainPluginUnbindAccountFunc = (domainAccountInfo: osAccount.DomainAccountInfo, callback: AsyncCallback<void>) => {};
const isAccountTokenValidFunc: osAccount.DomainPluginIsAccountTokenValidFunc = (domainAccountInfo: osAccount.DomainAccountInfo, token: Uint8Array, callback: AsyncCallback<boolean>) => {
  // 模拟检查操作
  // 通知检查结果
  let code: BusinessError = {
    code: 0,
    name: "",
    message: ""
  };
  callback(code, true);
};
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
