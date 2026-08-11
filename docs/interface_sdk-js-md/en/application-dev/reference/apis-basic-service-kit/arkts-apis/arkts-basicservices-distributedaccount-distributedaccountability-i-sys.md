# DistributedAccountAbility

Provides APIs for querying and updating the login state of a distributed account. You must obtain a  
**DistributedAccountAbility** instance first.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-distributedAccount-interface DistributedAccountAbility--><!--Device-distributedAccount-interface DistributedAccountAbility-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { distributedAccount } from 'kits/@kit.BasicServicesKit';
```

## getOsAccountDistributedInfoByLocalId

ArkTS-Dyn:
```TypeScript
getOsAccountDistributedInfoByLocalId(localId: number, callback: AsyncCallback<DistributedInfo>): void
```

ArkTS-Sta:
```TypeScript
getOsAccountDistributedInfoByLocalId(localId: int, callback: AsyncCallback<DistributedInfo>): void
```

Obtains distributed information about an OS account. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or (ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.GET_DISTRIBUTED_ACCOUNTS)
- API version 10 - 19: ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-DistributedAccountAbility-getOsAccountDistributedInfoByLocalId(localId: int, callback: AsyncCallback<DistributedInfo>): void--><!--Device-DistributedAccountAbility-getOsAccountDistributedInfoByLocalId(localId: int, callback: AsyncCallback<DistributedInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;DistributedInfo&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the distributed account information obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | System service exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
try {
  accountAbility.getOsAccountDistributedInfoByLocalId(100,
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

ArkTS-Dyn:
```TypeScript
getOsAccountDistributedInfoByLocalId(localId: number): Promise<DistributedInfo>
```

ArkTS-Sta:
```TypeScript
getOsAccountDistributedInfoByLocalId(localId: int): Promise<DistributedInfo>
```

Obtains distributed information about an OS account. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 20+: ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or (ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS and ohos.permission.GET_DISTRIBUTED_ACCOUNTS)
- API version 10 - 19: ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-DistributedAccountAbility-getOsAccountDistributedInfoByLocalId(localId: int): Promise<DistributedInfo>--><!--Device-DistributedAccountAbility-getOsAccountDistributedInfoByLocalId(localId: int): Promise<DistributedInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DistributedInfo&gt; | Promise used to return the distributed account information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | System service exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
try {
  accountAbility.getOsAccountDistributedInfoByLocalId(100).then((
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

ArkTS-Dyn:
```TypeScript
setOsAccountDistributedInfoByLocalId(localId: number, distributedInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo, callback: AsyncCallback<void>): void
```

Sets the distributed information for an OS account. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

<!--Device-DistributedAccountAbility-setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo, callback: AsyncCallback<void>): void--><!--Device-DistributedAccountAbility-setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the target OS account. |
| distributedInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes | Distributed account information to set. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the distributed information is set successfully, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| [12300008](../../apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) | Restricted OS account. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account identified by localId or by distributedInfo not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid distributedInfo. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| 12300406 | The distributed account information has already been bound to a sub-profile of the target OS account.<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
try {
  accountAbility.setOsAccountDistributedInfoByLocalId(100, accountInfo, (err: BusinessError) => {
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

ArkTS-Dyn:
```TypeScript
setOsAccountDistributedInfoByLocalId(localId: number, distributedInfo: DistributedInfo): Promise<void>
```

ArkTS-Sta:
```TypeScript
setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo): Promise<void>
```

Sets the distributed information for an OS account. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

<!--Device-DistributedAccountAbility-setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo): Promise<void>--><!--Device-DistributedAccountAbility-setOsAccountDistributedInfoByLocalId(localId: int, distributedInfo: DistributedInfo): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the target OS account. |
| distributedInfo | [DistributedInfo](arkts-basicservices-distributedaccount-distributedinfo-i.md) | Yes | Distributed account information to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameter types. |
| [12300008](../../apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) | Restricted OS account. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account identified by localId or by distributedInfo not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid distributedInfo. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| 12300406 | The distributed account information has already been bound to a sub-profile of the target OS account.<br>**Applicable version:** 26.0.0 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountAbility: distributedAccount.DistributedAccountAbility = distributedAccount.getDistributedAccountAbility();
let accountInfo: distributedAccount.DistributedInfo =
  { id: '12345', name: 'ZhangSan', event: 'Ohos.account.event.LOGIN' };
try {
  accountAbility.setOsAccountDistributedInfoByLocalId(100, accountInfo).then(() => {
    console.info('setOsAccountDistributedInfoByLocalId successfully');
  }).catch((err: BusinessError) => {
    console.error(`setOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountDistributedInfoByLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

