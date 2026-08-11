# DomainServerConfigManager

域服务器配置管理类。

**起始版本：** 18

<!--Device-osAccount-class DomainServerConfigManager--><!--Device-osAccount-class DomainServerConfigManager-End-->

**系统能力：** SystemCapability.Account.OsAccount

## addServerConfig

```TypeScript
static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>
```

添加域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

<!--Device-DomainServerConfigManager-static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>--><!--Device-DomainServerConfigManager-static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameters | Record&lt;string, Object&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;DomainServerConfig&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 12300211 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| 12300215 |
| 12300213 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add server configuration successfully, the return config: ' + JSON.stringify(serverConfig));
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

## getAccountServerConfig

```TypeScript
static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>
```

获取目标域账号的服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

<!--Device-DomainServerConfigManager-static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>--><!--Device-DomainServerConfigManager-static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| domainAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;DomainServerConfig&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-账号不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountInfo: osAccount.DomainAccountInfo = {
  'accountName': 'demoName',
  'domain': 'demoDomain'
};
osAccount.DomainServerConfigManager.getAccountServerConfig(accountInfo).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('get account server configuration successfully, the return config: ' + JSON.stringify(serverConfig));
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

## getAllServerConfigs

```TypeScript
static getAllServerConfigs(): Promise<Array<DomainServerConfig>>
```

获取所有域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

<!--Device-DomainServerConfigManager-static getAllServerConfigs(): Promise<Array<DomainServerConfig>>--><!--Device-DomainServerConfigManager-static getAllServerConfigs(): Promise<Array<DomainServerConfig>>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;DomainServerConfig&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.getAllServerConfigs().then((data: Array<osAccount.DomainServerConfig>) => {
    console.info('get all domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`get all domain server configuration failed, code is ${err.code}, message is ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

## getServerConfig

```TypeScript
static getServerConfig(configId: string): Promise<DomainServerConfig>
```

获取域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

<!--Device-DomainServerConfigManager-static getServerConfig(configId: string): Promise<DomainServerConfig>--><!--Device-DomainServerConfigManager-static getServerConfig(configId: string): Promise<DomainServerConfig>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;DomainServerConfig&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| 12300212 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.getServerConfig(serverConfig.id).then((data: osAccount.DomainServerConfig) => {
    console.info('get domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`get domain server configuration failed, code is ${err.code}, message is ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

## removeServerConfig

```TypeScript
static removeServerConfig(configId: string): Promise<void>
```

删除域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

<!--Device-DomainServerConfigManager-static removeServerConfig(configId: string): Promise<void>--><!--Device-DomainServerConfigManager-static removeServerConfig(configId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| 12300214 |
| 12300212 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.removeServerConfig(serverConfig.id);
  console.info('remove domain server configuration successfully');
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```

## updateServerConfig

```TypeScript
static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>
```

更新域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

<!--Device-DomainServerConfigManager-static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>--><!--Device-DomainServerConfigManager-static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>-End-->

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| configId | string | 是 |
| parameters | Record&lt;string, Object&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;DomainServerConfig&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| 12300211 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-无效参数) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-系统服务异常) |
| 12300214 |
| 12300213 |
| 12300212 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let configParams: Record<string, Object> = {
  'uri': 'test.example.com',
  'port': 100
};
osAccount.DomainServerConfigManager.addServerConfig(configParams).then((
  serverConfig: osAccount.DomainServerConfig) => {
  console.info('add domain server configuration successfully, the added config: ' + JSON.stringify(serverConfig));
  osAccount.DomainServerConfigManager.updateServerConfig(serverConfig.id, configParams).then((data) => {
    console.info('update domain server configuration successfully, return config: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`update domain server configuration failed, code is ${err.code}, message is ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`add server configuration failed, code is ${err.code}, message is ${err.message}`);
});
```
