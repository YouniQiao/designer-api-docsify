# DistributedAccountAbility

Provides APIs for querying and updating the login state of a distributed account. You must obtain a  
**DistributedAccountAbility** instance first.

**Since:** 7

<!--Device-distributedAccount-interface DistributedAccountAbility--><!--Device-distributedAccount-interface DistributedAccountAbility-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { distributedAccount } from 'kits/@kit.BasicServicesKit';
```

## getOsAccountDistributedInfoByLocalId

```TypeScript
getOsAccountDistributedInfoByLocalId(localId: number, callback: AsyncCallback<DistributedInfo>): void
```

Obtains distributed information about an OS account. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or (ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.GET_DISTRIBUTED_ACCOUNTS)
- API version 10 - 19: ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-DistributedAccountAbility-getOsAccountDistributedInfoByLocalId(localId: int, callback: AsyncCallback<DistributedInfo>): void--><!--Device-DistributedAccountAbility-getOsAccountDistributedInfoByLocalId(localId: int, callback: AsyncCallback<DistributedInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
try {
  let localId: number = 100; // This is an example. Replace it with an actual OS account ID.
  accountAbility.getOsAccountDistributedInfoByLocalId(localId,
    (err: BusinessError, data: distributedAccount.DistributedInfo) => {
      if (err) {
        console.error(`getOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
      } else {
        console.info('distributed information: ' + JSON.stringify(data));
      }
    });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountDistributedInfoByLocalId

```TypeScript
getOsAccountDistributedInfoByLocalId(localId: number): Promise<DistributedInfo>
```

Obtains distributed information about an OS account. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or (ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.GET_DISTRIBUTED_ACCOUNTS)
- API version 10 - 19: ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-DistributedAccountAbility-getOsAccountDistributedInfoByLocalId(localId: int): Promise<DistributedInfo>--><!--Device-DistributedAccountAbility-getOsAccountDistributedInfoByLocalId(localId: int): Promise<DistributedInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;DistributedInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
try {
  let localId: number = 100; // This is an example. Replace it with an actual OS account ID.
  accountAbility.getOsAccountDistributedInfoByLocalId(localId).then((
    data: distributedAccount.DistributedInfo) => {
    console.info('distributed information: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountDistributedInfoByLocalId

```TypeScript
setOsAccountDistributedInfoByLocalId(localId: number, distributedInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

Sets the distributed information for an OS account. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

<!--Device-DistributedAccountAbility-setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo, callback: AsyncCallback<void>): void--><!--Device-DistributedAccountAbility-setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| distributedInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300406 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
try {
  let localId: number = 100; // This is an example. Replace it with an actual OS account ID.
  accountAbility.setOsAccountDistributedInfoByLocalId(localId, accountInfo, (err: BusinessError) => {
    if (err) {
      console.error(`setOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOsAccountDistributedInfoByLocalId successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountDistributedInfoByLocalId

```TypeScript
setOsAccountDistributedInfoByLocalId(localId: number, distributedInfo: DistributedInfo): Promise<void>
```

Sets the distributed information for an OS account. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

<!--Device-DistributedAccountAbility-setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo): Promise<void>--><!--Device-DistributedAccountAbility-setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| distributedInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| 12300406 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
try {
  let localId: number = 100; // This is an example. Replace it with an actual OS account ID.
  accountAbility.setOsAccountDistributedInfoByLocalId(localId, accountInfo).then(() => {
    console.info('setOsAccountDistributedInfoByLocalId successfully');
  }).catch((err: BusinessError) => {
    console.error(`setOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```
