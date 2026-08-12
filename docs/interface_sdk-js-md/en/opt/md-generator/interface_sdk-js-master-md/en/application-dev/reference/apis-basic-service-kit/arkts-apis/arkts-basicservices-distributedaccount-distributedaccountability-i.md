# DistributedAccountAbility

Provides APIs for querying and updating the login state of a distributed account. You must obtain a  
**DistributedAccountAbility** instance first.

**Since:** 7

<!--Device-distributedAccount-interface DistributedAccountAbility--><!--Device-distributedAccount-interface DistributedAccountAbility-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { distributedAccount } from '@kit.BasicServicesKit';
```

## getOsAccountDistributedInfo

```TypeScript
getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void
```

Obtains the distributed account information. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.GET_DISTRIBUTED_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DistributedAccountAbility-getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void--><!--Device-DistributedAccountAbility-getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
try {
  accountAbility.getOsAccountDistributedInfo(
    (err: BusinessError, data: distributedAccount.DistributedInfo) => {
      if (err) {
        console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('distributed information: ' + JSON.stringify(data));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountDistributedInfo

```TypeScript
getOsAccountDistributedInfo(): Promise<DistributedInfo>
```

Obtains the distributed account information. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.GET_DISTRIBUTED_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DistributedAccountAbility-getOsAccountDistributedInfo(): Promise<DistributedInfo>--><!--Device-DistributedAccountAbility-getOsAccountDistributedInfo(): Promise<DistributedInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DistributedInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
try {
  accountAbility.getOsAccountDistributedInfo().then((data: distributedAccount.DistributedInfo) => {
    console.info('distributed information: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryOsAccountDistributedInfo

```TypeScript
queryOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void
```

Queries the distributed account information. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountDistributedInfo](#getOsAccountDistributedInfo)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountDistributedInfo](distributedAccount.DistributedAccountAbility.getOsAccountDistributedInfo(callback:)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DistributedAccountAbility-queryOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void--><!--Device-DistributedAccountAbility-queryOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
accountAbility.queryOsAccountDistributedInfo(
  (err: BusinessError, data: distributedAccount.DistributedInfo) => {
    if (err) {
      console.error(`queryOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('distributed information: ' + JSON.stringify(data));
    }
  });
```

## queryOsAccountDistributedInfo

```TypeScript
queryOsAccountDistributedInfo(): Promise<DistributedInfo>
```

Queries the distributed account information. This API uses a promise to return the result.

> **NOTE：**
> 
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [getOsAccountDistributedInfo](#getOsAccountDistributedInfo)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountDistributedInfo](#getOsAccountDistributedInfo)()

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-DistributedAccountAbility-queryOsAccountDistributedInfo(): Promise<DistributedInfo>--><!--Device-DistributedAccountAbility-queryOsAccountDistributedInfo(): Promise<DistributedInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DistributedInfo & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
accountAbility.queryOsAccountDistributedInfo().then((data: distributedAccount.DistributedInfo) => {
  console.info('distributed information: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`queryOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
});
```

## setOsAccountDistributedInfo

```TypeScript
setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

Sets the distributed account information. This API uses an asynchronous callback to return the result.This API can be called only by system applications.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

<!--Device-DistributedAccountAbility-setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void--><!--Device-DistributedAccountAbility-setOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300406 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
// This is an example. Replace it with the actual distributed account information obtained using getOsAccountDistributedInfo.
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
try {
  accountAbility.setOsAccountDistributedInfo(accountInfo, (err: BusinessError) => {
    if (err) {
      console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOsAccountDistributedInfo successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountDistributedInfo

```TypeScript
setOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>
```

Sets the distributed account information. This API uses a promise to return the result.This API can be called only by system applications.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

<!--Device-DistributedAccountAbility-setOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>--><!--Device-DistributedAccountAbility-setOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300406 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
// This is an example. Replace it with the actual distributed account information obtained using getOsAccountDistributedInfo.
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
try {
  accountAbility.setOsAccountDistributedInfo(accountInfo).then(() => {
    console.info('setOsAccountDistributedInfo successfully');
  }).catch((err: BusinessError) => {
    console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
}
```

## updateOsAccountDistributedInfo

```TypeScript
updateOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

Updates the distributed account information. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setOsAccountDistributedInfo](#setOsAccountDistributedInfo)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setOsAccountDistributedInfo](distributedAccount.DistributedAccountAbility.setOsAccountDistributedInfo(accountInfo:)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-DistributedAccountAbility-updateOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void--><!--Device-DistributedAccountAbility-updateOsAccountDistributedInfo(accountInfo: DistributedInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
// This is an example. Replace it with the actual distributed account information obtained using getOsAccountDistributedInfo.
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
accountAbility.updateOsAccountDistributedInfo(accountInfo, (err: BusinessError) => {
  if (err) {
    console.error(`updateOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('updateOsAccountDistributedInfo successfully');
  }
});
```

## updateOsAccountDistributedInfo

```TypeScript
updateOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>
```

Updates the distributed account information. This API uses a promise to return the result.

> **NOTE：**
> 
> This API is supported since API version 7 and deprecated since API version 9. You are advised to use
> [setOsAccountDistributedInfo](#setOsAccountDistributedInfo-1)
> instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setOsAccountDistributedInfo](distributedAccount.DistributedAccountAbility.setOsAccountDistributedInfo(accountInfo:)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-DistributedAccountAbility-updateOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>--><!--Device-DistributedAccountAbility-updateOsAccountDistributedInfo(accountInfo: DistributedInfo): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain a DistributedAccountAbility instance.
const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
// This is an example. Replace it with the actual distributed account information obtained using getOsAccountDistributedInfo.
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
accountAbility.updateOsAccountDistributedInfo(accountInfo).then(() => {
  console.info('updateOsAccountDistributedInfo successfully');
}).catch((err: BusinessError) => {
  console.error(`updateOsAccountDistributedInfo exception: code is ${err.code}, message is ${err.message}`);
});
```
