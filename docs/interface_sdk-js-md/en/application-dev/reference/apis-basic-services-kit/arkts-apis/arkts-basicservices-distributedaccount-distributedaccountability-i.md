# DistributedAccountAbility

Provides APIs for querying and updating the login state of a distributed account. You must obtain a **DistributedAccountAbility** instance first.

**Since:** 7

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { distributedAccount } from 'kits/@kit.BasicServicesKit';
```

## getOsAccountDistributedInfo

```TypeScript
getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void
```

Obtains the distributed account information. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.GET_DISTRIBUTED_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountDistributedInfo

```TypeScript
getOsAccountDistributedInfo(): Promise<DistributedInfo>
```

Obtains the distributed account information. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.GET_DISTRIBUTED_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DistributedInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## queryOsAccountDistributedInfo

```TypeScript
queryOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void
```

Queries the distributed account information. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountDistributedInfo](#getosaccountdistributedinfo)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountDistributedInfo](#getosaccountdistributedinfo)(callback: AsyncCallback&lt;DistributedInfo&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | Yes |

## queryOsAccountDistributedInfo

```TypeScript
queryOsAccountDistributedInfo(): Promise<DistributedInfo>
```

Queries the distributed account information. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountDistributedInfo](#getosaccountdistributedinfo)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountDistributedInfo](#getosaccountdistributedinfo)()

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DistributedInfo & gt; |

## setOsAccountDistributedInfo

```TypeScript
setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

Sets the distributed account information. This API uses an asynchronous callback to return the result. This API can be called only by system applications.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| 12300406 |

## setOsAccountDistributedInfo

```TypeScript
setOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>
```

Sets the distributed account information. This API uses a promise to return the result. This API can be called only by system applications.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| 12300406 |

## updateOsAccountDistributedInfo

```TypeScript
updateOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

Updates the distributed account information. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setOsAccountDistributedInfo](#setosaccountdistributedinfo)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setOsAccountDistributedInfo](#setosaccountdistributedinfo)(accountInfo: DistributedInfo, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## updateOsAccountDistributedInfo

```TypeScript
updateOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>
```

Updates the distributed account information. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setOsAccountDistributedInfo](#setosaccountdistributedinfo)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setOsAccountDistributedInfo](#setosaccountdistributedinfo)(accountInfo: DistributedInfo)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
