# DomainServerConfigManager

域服务器配置管理类。

**起始版本：** 18

**系统能力：** SystemCapability.Account.OsAccount

## 导入模块

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## addServerConfig

```TypeScript
static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>
```

添加域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameters | Record & lt;string, Object & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| 12300211 |
| 12300213 |
| 12300215 |

## getAccountServerConfig

```TypeScript
static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>
```

获取目标域账号的服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300003](../errorcode-account.md#12300003-账号不存在) |

## getAllServerConfigs

```TypeScript
static getAllServerConfigs(): Promise<Array<DomainServerConfig>>
```

获取所有域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**系统能力：** SystemCapability.Account.OsAccount

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |

## getServerConfig

```TypeScript
static getServerConfig(configId: string): Promise<DomainServerConfig>
```

获取域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [configId](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| 12300212 |

## removeServerConfig

```TypeScript
static removeServerConfig(configId: string): Promise<void>
```

删除域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [configId](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| 12300212 |
| 12300214 |

## updateServerConfig

```TypeScript
static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>
```

更新域服务器配置。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**系统能力：** SystemCapability.Account.OsAccount

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [configId](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | 是 |
| parameters | Record & lt;string, Object & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [12300001](../errorcode-account.md#12300001-系统服务异常) |
| [12300002](../errorcode-account.md#12300002-无效参数) |
| 12300211 |
| 12300212 |
| 12300213 |
| 12300214 |
