# DomainServerConfigManager

Provides APIs for domain server configuration and management.

**Since:** 18

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## addServerConfig

```TypeScript
static addServerConfig(parameters: Record<string, Object>): Promise<DomainServerConfig>
```

Adds domain server configuration. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameters | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| 12300211 |
| 12300213 |
| 12300215 |

## getAccountServerConfig

```TypeScript
static getAccountServerConfig(domainAccountInfo: DomainAccountInfo): Promise<DomainServerConfig>
```

Obtains the server configuration of a domain account. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getAllServerConfigs

```TypeScript
static getAllServerConfigs(): Promise<Array<DomainServerConfig>>
```

Obtains the configurations of all domain servers. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getServerConfig

```TypeScript
static getServerConfig(configId: string): Promise<DomainServerConfig>
```

Obtains the domain server configuration. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [configId](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| 12300212 |

## removeServerConfig

```TypeScript
static removeServerConfig(configId: string): Promise<void>
```

Removes domain server configuration. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [configId](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| 12300212 |
| 12300214 |

## updateServerConfig

```TypeScript
static updateServerConfig(configId: string, parameters: Record<string, Object>): Promise<DomainServerConfig>
```

Updates the domain server configuration. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_DOMAIN_ACCOUNT_SERVER_CONFIGS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [configId](../../apis-performance-analysis-kit/arkts-apis/arkts-performanceanalysis-hiappevent-processor-i.md) | string | Yes |
| parameters | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DomainServerConfig](arkts-basicservices-osaccount-domainserverconfig-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| 12300211 |
| 12300212 |
| 12300213 |
| 12300214 |
