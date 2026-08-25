# AccountManager

Provides APIs for managing OS accounts.

**Since:** 7

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## checkMultiOsAccountEnabled

```TypeScript
checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void
```

Checks whether multiple OS accounts are supported. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## checkMultiOsAccountEnabled

```TypeScript
checkMultiOsAccountEnabled(): Promise<boolean>
```

Checks whether multiple OS accounts are supported. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## checkOsAccountActivated

```TypeScript
checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void
```

Checks whether an OS account is activated. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkOsAccountActivated

```TypeScript
checkOsAccountActivated(localId: number): Promise<boolean>
```

Checks whether an OS account is activated. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkOsAccountConstraintEnabled

```TypeScript
checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void
```

Checks whether the specified constraint is enabled for an OS account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| constraint | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkOsAccountConstraintEnabled

```TypeScript
checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>
```

Checks whether the specified constraint is enabled for an OS account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| constraint | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkOsAccountTestable

```TypeScript
checkOsAccountTestable(callback: AsyncCallback<boolean>): void
```

Checks whether the current OS account is a test account. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## checkOsAccountTestable

```TypeScript
checkOsAccountTestable(): Promise<boolean>
```

Checks whether the current OS account is a test account. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(callback: AsyncCallback<boolean>): void
```

Checks whether the current OS account is unlocked. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. You are advised to use
> [isOsAccountUnlocked](#isosaccountunlocked) instead.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [isOsAccountUnlocked](#isosaccountunlocked)()

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(): Promise<boolean>
```

Checks whether the current OS account has been verified. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. You are advised to use
> [isOsAccountUnlocked](#isosaccountunlocked) instead.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [isOsAccountUnlocked](#isosaccountunlocked)()

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void
```

Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(localId: number): Promise<boolean>
```

Checks whether an OS account has been verified. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getActivatedOsAccountLocalIds

```TypeScript
getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<number>>): void
```

Obtains information about all activated OS accounts. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getActivatedOsAccountLocalIds

```TypeScript
getActivatedOsAccountLocalIds(): Promise<Array<number>>
```

Obtains information about all activated OS accounts. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getCreatedOsAccountsCount

```TypeScript
getCreatedOsAccountsCount(callback: AsyncCallback<number>): void
```

Obtains the number of OS accounts created. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountCount](#getosaccountcount) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountCount](#getosaccountcount)(callback: AsyncCallback&lt;int&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getCreatedOsAccountsCount

```TypeScript
getCreatedOsAccountsCount(): Promise<number>
```

Obtains the number of OS accounts created. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountCount](#getosaccountcount) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountCount](#getosaccountcount)()

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getCurrentOsAccount

```TypeScript
getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void
```

Obtains information about the OS account to which the current process belongs. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** 
- API version 10+: ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS
- API version 9: ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getCurrentOsAccount

```TypeScript
getCurrentOsAccount(): Promise<OsAccountInfo>
```

Obtains information about the OS account to which the current process belongs. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** 
- API version 10+: ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS
- API version 9: ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getDistributedVirtualDeviceId

```TypeScript
getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void
```

Obtains the ID of a distributed virtual device. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)(callback: AsyncCallback&lt;string&gt;)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## getDistributedVirtualDeviceId

```TypeScript
getDistributedVirtualDeviceId(): Promise<string>
```

Queries the ID of a distributed virtual device. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)()

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## getForegroundOsAccountLocalId

```TypeScript
getForegroundOsAccountLocalId(): Promise<number>
```

Obtains the ID of the foreground OS account. This API uses a promise to return the result.

**Since:** 15

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountAllConstraints

```TypeScript
getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void
```

Obtains all constraints enabled for an OS account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## getOsAccountAllConstraints

```TypeScript
getOsAccountAllConstraints(localId: number): Promise<Array<string>>
```

Obtains all constraints enabled for an OS account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## getOsAccountConstraints

```TypeScript
getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void
```

Obtains all constraints enabled for an OS account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getOsAccountConstraints

```TypeScript
getOsAccountConstraints(localId: number): Promise<Array<string>>
```

Obtains all constraints enabled for an OS account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 9 and deprecated since API version 11. The substitute API is available
> only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getOsAccountCount

```TypeScript
getOsAccountCount(callback: AsyncCallback<number>): void
```

Obtains the number of OS accounts created. This API uses an asynchronous callback to return the result. This API can be called only by system applications.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountCount

```TypeScript
getOsAccountCount(): Promise<number>
```

Obtains the number of OS accounts created. This API uses a promise to return the result. This API can be called only by system applications.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountDomainInfo

```TypeScript
getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>
```

Obtains the domain account information associated with a specified OS account. This API uses a promise to return the result.

**Since:** 15

**Required permissions:** ohos.permission.GET_DOMAIN_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getOsAccountLocalId

```TypeScript
getOsAccountLocalId(callback: AsyncCallback<number>): void
```

Obtains the ID of the OS account to which the current process belongs. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountLocalId

```TypeScript
getOsAccountLocalId(): Promise<number>
```

Obtains the ID of the OS account to which the current process belongs. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountLocalIdBySerialNumber

```TypeScript
getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the SN. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)(serialNumber: long, callback: AsyncCallback&lt;int&gt;)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serialNumber | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getOsAccountLocalIdBySerialNumber

```TypeScript
getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>
```

Obtains the OS account ID based on the SN. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)(serialNumber: long)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serialNumber | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getOsAccountLocalIdForDomain

```TypeScript
getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the domain account information. This API uses an asynchronous callback to return the result. This API can be called only by system applications.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getOsAccountLocalIdForDomain

```TypeScript
getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<number>
```

Obtains the OS account ID based on the domain account information. This API uses a promise to return the result. This API can be called only by system applications.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getOsAccountLocalIdForSerialNumber

```TypeScript
getOsAccountLocalIdForSerialNumber(serialNumber: number, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the SN. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serialNumber | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getOsAccountLocalIdForSerialNumber

```TypeScript
getOsAccountLocalIdForSerialNumber(serialNumber: number): Promise<number>
```

Obtains the OS account ID based on the SN. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| serialNumber | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getOsAccountLocalIdForUid

```TypeScript
getOsAccountLocalIdForUid(uid: number, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the process UID. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## getOsAccountLocalIdForUid

```TypeScript
getOsAccountLocalIdForUid(uid: number): Promise<number>
```

Obtains the OS account ID based on the process UID. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## getOsAccountLocalIdForUidSync

```TypeScript
getOsAccountLocalIdForUidSync(uid: number): number
```

Obtains the OS account ID based on the process UID. The API returns the result synchronously.

**Since:** 10

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## getOsAccountLocalIdFromDomain

```TypeScript
getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the domain account information. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)(domainInfo: DomainAccountInfo, callback: AsyncCallback&lt;int&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getOsAccountLocalIdFromDomain

```TypeScript
getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>
```

Obtains the OS account ID based on the domain account information. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)(domainInfo: DomainAccountInfo)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getOsAccountLocalIdFromProcess

```TypeScript
getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void
```

Obtains the ID of the OS account to which the current process belongs. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountLocalId](#getosaccountlocalid)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalId](#getosaccountlocalid)(callback: AsyncCallback&lt;int&gt;)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getOsAccountLocalIdFromProcess

```TypeScript
getOsAccountLocalIdFromProcess(): Promise<number>
```

Obtains the ID of the OS account to which the current process belongs. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountLocalId](#getosaccountlocalid) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalId](#getosaccountlocalid)()

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getOsAccountLocalIdFromUid

```TypeScript
getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the process UID. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)(uid: int, callback: AsyncCallback&lt;int&gt;)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getOsAccountLocalIdFromUid

```TypeScript
getOsAccountLocalIdFromUid(uid: number): Promise<number>
```

Obtains the OS account ID based on the process UID. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountLocalIdForUid](#getosaccountlocalidforuid) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)(uid: int)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getOsAccountLocalIds

```TypeScript
getOsAccountLocalIds(): Promise<number[]>
```

Obtains the local IDs of all non-system-level OS accounts. Non-system-level OS accounts are visible to users and are usually used for operations such as login. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountName

```TypeScript
getOsAccountName(): Promise<string>
```

Obtains the name of the OS account of the caller. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountNameByLocalId

```TypeScript
getOsAccountNameByLocalId(localId: number): Promise<string>
```

Obtains the name of an OS account based on its local ID. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300008](../errorcode-account.md#12300008-restricted-account) |

## getOsAccountType

```TypeScript
getOsAccountType(callback: AsyncCallback<OsAccountType>): void
```

Obtains the type of the account to which the current process belongs. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountType

```TypeScript
getOsAccountType(): Promise<OsAccountType>
```

Obtains the type of the account to which the current process belongs. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountTypeFromProcess

```TypeScript
getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void
```

Obtains the type of the account to which the current process belongs. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountType](#getosaccounttype)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountType](#getosaccounttype)(callback: AsyncCallback&lt;OsAccountType&gt;)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; | Yes |

## getOsAccountTypeFromProcess

```TypeScript
getOsAccountTypeFromProcess(): Promise<OsAccountType>
```

Obtains the type of the account to which the current process belongs. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountType](#getosaccounttype) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountType](#getosaccounttype)()

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; |

## getSerialNumberByOsAccountLocalId

```TypeScript
getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void
```

Obtains the SN of an OS account based on the account ID. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)(localId: int, callback: AsyncCallback&lt;long&gt;)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getSerialNumberByOsAccountLocalId

```TypeScript
getSerialNumberByOsAccountLocalId(localId: number): Promise<number>
```

Obtains the SN of an OS account based on the account ID. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)(localId: int)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getSerialNumberForOsAccountLocalId

```TypeScript
getSerialNumberForOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void
```

Obtains the SN of an OS account based on the account ID. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## getSerialNumberForOsAccountLocalId

```TypeScript
getSerialNumberForOsAccountLocalId(localId: number): Promise<number>
```

Obtains the SN of an OS account based on the account ID. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## isMultiOsAccountEnable

```TypeScript
isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void
```

Checks whether multiple OS accounts are supported. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)(callback: AsyncCallback&lt;boolean&gt;)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isMultiOsAccountEnable

```TypeScript
isMultiOsAccountEnable(): Promise<boolean>
```

Checks whether multiple OS accounts are supported. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [checkMultiOsAccountEnabled](#checkmultiosaccountenabled) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)()

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isOsAccountActived

```TypeScript
isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void
```

Checks whether an OS account is activated. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isOsAccountActived

```TypeScript
isOsAccountActived(localId: number): Promise<boolean>
```

Checks whether an OS account is activated. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isOsAccountConstraintEnable

```TypeScript
isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void
```

Checks whether the specified constraint is enabled for an OS account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| constraint | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isOsAccountConstraintEnable

```TypeScript
isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>
```

Checks whether the specified constraint is enabled for an OS account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| constraint | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isOsAccountConstraintEnabled

```TypeScript
isOsAccountConstraintEnabled(constraint: string): Promise<boolean>
```

Checks whether a constraint is enabled for the current OS account. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| constraint | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## isOsAccountUnlocked

```TypeScript
isOsAccountUnlocked(): Promise<boolean>
```

Checks whether the current OS account has been unlocked. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## isOsAccountVerified

```TypeScript
isOsAccountVerified(callback: AsyncCallback<boolean>): void
```

Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [checkOsAccountVerified](#checkosaccountverified)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountVerified](#checkosaccountverified)(callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isOsAccountVerified

```TypeScript
isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void
```

Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isOsAccountVerified

```TypeScript
isOsAccountVerified(localId?: number): Promise<boolean>
```

Checks whether an OS account has been verified. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## isTestOsAccount

```TypeScript
isTestOsAccount(callback: AsyncCallback<boolean>): void
```

Checks whether the current OS account is a test account. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [checkOsAccountTestable](#checkosaccounttestable)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountTestable](#checkosaccounttestable)(callback: AsyncCallback&lt;boolean&gt;)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## isTestOsAccount

```TypeScript
isTestOsAccount(): Promise<boolean>
```

Checks whether the current OS account is a test account. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [checkOsAccountTestable](#checkosaccounttestable) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountTestable](#checkosaccounttestable)()

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## queryActivatedOsAccountIds

```TypeScript
queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void
```

Obtains information about all activated OS accounts. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)(callback: AsyncCallback&lt;Array&lt;int&gt;&gt;)

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | Yes |

## queryActivatedOsAccountIds

```TypeScript
queryActivatedOsAccountIds(): Promise<Array<number>>
```

Obtains information about all activated OS accounts. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 8 and deprecated since API version 9. You are advised to use
> [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)()

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

## queryCurrentOsAccount

```TypeScript
queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void
```

Obtains information about the OS account to which the current process belongs. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Yes |

## queryCurrentOsAccount

```TypeScript
queryCurrentOsAccount(): Promise<OsAccountInfo>
```

Obtains information about the OS account to which the current process belongs. This API uses a promise to return the result.

> **NOTE：**&gt;
> This API is supported since API version 7 and deprecated since API version 9. The substitute API is available
> only to system applications.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

## queryDistributedVirtualDeviceId

```TypeScript
queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void
```

Queries the ID of a distributed virtual device. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## queryDistributedVirtualDeviceId

```TypeScript
queryDistributedVirtualDeviceId(): Promise<string>
```

Queries the ID of this distributed virtual device. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
