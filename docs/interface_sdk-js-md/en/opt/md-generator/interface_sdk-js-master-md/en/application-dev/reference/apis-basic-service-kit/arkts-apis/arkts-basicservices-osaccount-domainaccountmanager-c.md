# DomainAccountManager

Provides APIs for domain account management.

**Since:** 23

**Deprecated since:** -1

<!--Device-osAccount-class DomainAccountManager--><!--Device-osAccount-class DomainAccountManager-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## updateAccountInfo

```TypeScript
static updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>
```

Updates information of a domain account. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.MANAGE_DOMAIN_ACCOUNTS

<!--Device-DomainAccountManager-static updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>--><!--Device-DomainAccountManager-static updateAccountInfo(oldAccountInfo: DomainAccountInfo, newAccountInfo: DomainAccountInfo): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oldAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| newAccountInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300004](../../apis-basic-services-kit/errorcode-account.md#12300004-account-already-exists) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let oldDomainInfo: osAccount.DomainAccountInfo =
  {domain: 'testDomain', accountName: 'oldtestAccountName'};
let newDomainInfo: osAccount.DomainAccountInfo =
  {domain: 'testDomain', accountName: 'newtestAccountName'};
try {
  osAccount.DomainAccountManager.updateAccountInfo(oldDomainInfo, newDomainInfo).then(() => {
    console.info('updateAccountInfo, success');
  }).catch((err: BusinessError) => {
    console.error('updateAccountInfo err: ' + err);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`updateAccountInfo exception: code is ${err.code}, message is ${err.message}`);
}
```
