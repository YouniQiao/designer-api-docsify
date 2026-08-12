# AccountManager

Provides APIs for managing OS accounts.

**Since:** 7

<!--Device-osAccount-interface AccountManager--><!--Device-osAccount-interface AccountManager-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## activateOsAccount

```TypeScript
activateOsAccount(localId: number, callback: AsyncCallback<void>): void
```

Activates an OS account. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-activateOsAccount(localId: int, callback: AsyncCallback<void>): void--><!--Device-AccountManager-activateOsAccount(localId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300009-account-already-activated) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300016](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300016-login-accounts-reached-the-limit) |

## Examples

Activate OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.activateOsAccount(localId, (err: BusinessError)=>{
    if (err) {
      console.error(`activateOsAccount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('activateOsAccount successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`activateOsAccount failed, code is ${err.code}, message is ${err.message}`);
}
```

## activateOsAccount

```TypeScript
activateOsAccount(localId: number): Promise<void>
```

Activates an OS account. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-activateOsAccount(localId: int): Promise<void>--><!--Device-AccountManager-activateOsAccount(localId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300009](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300009-account-already-activated) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300016](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300016-login-accounts-reached-the-limit) |

## Examples

Activate OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.activateOsAccount(localId).then(() => {
    console.info('activateOsAccount successfully');
  }).catch((err: BusinessError) => {
    console.error(`activateOsAccount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`activateOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## activateOsAccount

```TypeScript
activateOsAccount(localId: number, displayId: number): Promise<void>
```

Activates (Starts on the foreground or switches to) the target OS account on the specified logical display.This API uses a promise to return the result.Currently, cross-logical-display activation is not supported. That is, you cannot activate an OS account that is already running on the foreground of another logical display on the specified logical display.

**Since:** 23

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-activateOsAccount(localId: int, displayId: long): Promise<void>--><!--Device-AccountManager-activateOsAccount(localId: int, displayId: long): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [12300019](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300019-crossdisplay-activation-not-supported) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300018](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300018-logical-display-not-found) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300016](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300016-login-accounts-reached-the-limit) |

## Examples

Activate the OS account 100 on the logical screen 0.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let displayId: number = 0;
try {
  accountManager.activateOsAccount(localId, displayId).then(() => {
    console.info('activateOsAccount with displayId successfully');
  }).catch((err: BusinessError) => {
    console.error(`activateOsAccount with displayId failed, err: ${err.code} ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`activateOsAccount with displayId exception: ${err.code} ${err.message}`);
}
```

## bindDomainAccount

```TypeScript
bindDomainAccount(localId: number, domainAccountInfo: DomainAccountInfo): Promise<void>
```

Binds a domain account to an OS account. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-bindDomainAccount(localId: int, domainAccountInfo: DomainAccountInfo): Promise<void>--><!--Device-AccountManager-bindDomainAccount(localId: int, domainAccountInfo: DomainAccountInfo): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| [domainAccountInfo](arkts-basicservices-osaccount-getdomainaccesstokenoptions-i-sys.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300022](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300022-domain-account-already-bound) |
| [12300021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300021-os-account-already-bound) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  let localId: number = 100;
  let domainInfo: osAccount.DomainAccountInfo =
    { domain: 'testDomain', accountName: 'testAccountName' };
  accountManager.bindDomainAccount(localId, domainInfo).then(() => {
    console.info('bindDomainAccount success.');
  }).catch((error: BusinessError) => {
    console.error(`bindDomainAccount failed, errCode=${error.code}, errMsg=${error.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`bindDomainAccount error, errCode=${err.code}, errMsg=${err.message}`);
}
```

## createOsAccount

```TypeScript
createOsAccount(localName: string, type: OsAccountType, callback: AsyncCallback<OsAccountInfo>): void
```

Creates an OS account. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-createOsAccount(localName: string, type: OsAccountType, callback: AsyncCallback<OsAccountInfo>): void--><!--Device-AccountManager-createOsAccount(localName: string, type: OsAccountType, callback: AsyncCallback<OsAccountInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localName | string | Yes |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |
| [12300007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300007-account-count-reached-the-limit) |
| [12300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300023-accounts-of-a-specified-type-reached-the-limit) |
| [12300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300006-unsupported-account-type) |
| [12300005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300005-multiple-users-not-supported) |
| [12300004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300004-account-already-exists) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.createOsAccount('testName', osAccount.OsAccountType.NORMAL,
    (err: BusinessError, osAccountInfo: osAccount.OsAccountInfo)=>{
    if (err) {
      console.error(`createOsAccount exception:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('createOsAccount osAccountInfo:' + JSON.stringify(osAccountInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## createOsAccount

```TypeScript
createOsAccount(localName: string, type: OsAccountType, options?: CreateOsAccountOptions): Promise<OsAccountInfo>
```

Creates an OS account. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-createOsAccount(localName: string, type: OsAccountType, options?: CreateOsAccountOptions): Promise<OsAccountInfo>--><!--Device-AccountManager-createOsAccount(localName: string, type: OsAccountType, options?: CreateOsAccountOptions): Promise<OsAccountInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localName | string | Yes |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | Yes |
| options | [CreateOsAccountOptions](arkts-basicservices-osaccount-createosaccountoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300015](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300015-duplicate-short-name) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |
| [12300007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300007-account-count-reached-the-limit) |
| [12300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300023-accounts-of-a-specified-type-reached-the-limit) |
| [12300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300006-unsupported-account-type) |
| [12300005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300005-multiple-users-not-supported) |
| [12300004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300004-account-already-exists) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let options: osAccount.CreateOsAccountOptions = {
  shortName: 'myShortName',
  disallowedPreinstalledBundles: [],
  allowedPreinstalledBundles: [],
}
try {
  accountManager.createOsAccount('testAccountName', osAccount.OsAccountType.NORMAL, options).then(
    (accountInfo: osAccount.OsAccountInfo) => {
    console.info('createOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
  }).catch((err: BusinessError) => {
    console.error(`createOsAccount err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## createOsAccountForDomain

```TypeScript
createOsAccountForDomain(
      type: OsAccountType,
      domainInfo: DomainAccountInfo,
      callback: AsyncCallback<OsAccountInfo>
    ): void
```

Creates an OS account and associates it with the specified domain account. This API uses an asynchronous callback to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-createOsAccountForDomain(      type: OsAccountType,      domainInfo: DomainAccountInfo,      callback: AsyncCallback<OsAccountInfo>    ): void--><!--Device-AccountManager-createOsAccountForDomain(      type: OsAccountType,      domainInfo: DomainAccountInfo,      callback: AsyncCallback<OsAccountInfo>    ): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | Yes |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |
| [12300007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300007-account-count-reached-the-limit) |
| [12300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300023-accounts-of-a-specified-type-reached-the-limit) |
| [12300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300006-unsupported-account-type) |
| [12300005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300005-multiple-users-not-supported) |
| [12300004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300004-account-already-exists) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let domainInfo: osAccount.DomainAccountInfo =
  {domain: 'testDomain', accountName: 'testAccountName'};
try {
  accountManager.createOsAccountForDomain(osAccount.OsAccountType.NORMAL, domainInfo,
    (err: BusinessError, osAccountInfo: osAccount.OsAccountInfo)=>{
    if (err) {
      console.error(`createOsAccountForDomain exception:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('createOsAccountForDomain osAccountInfo:' + JSON.stringify(osAccountInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createOsAccountForDomain exception: code is ${err.code}, message is ${err.message}`);
}
```

## createOsAccountForDomain

```TypeScript
createOsAccountForDomain(type: OsAccountType, domainInfo: DomainAccountInfo, options?: CreateOsAccountForDomainOptions): Promise<OsAccountInfo>
```

Creates an OS account and associates it with the specified domain account. This API uses a promise to return the result.

**Since:** 8

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-createOsAccountForDomain(type: OsAccountType, domainInfo: DomainAccountInfo, options?: CreateOsAccountForDomainOptions): Promise<OsAccountInfo>--><!--Device-AccountManager-createOsAccountForDomain(type: OsAccountType, domainInfo: DomainAccountInfo, options?: CreateOsAccountForDomainOptions): Promise<OsAccountInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | Yes |
| [domainInfo](arkts-basicservices-osaccount-osaccountinfo-i.md) | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes |
| options | [CreateOsAccountForDomainOptions](arkts-basicservices-osaccount-createosaccountfordomainoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [12300015](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300015-duplicate-short-name) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |
| [12300007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300007-account-count-reached-the-limit) |
| [12300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300023-accounts-of-a-specified-type-reached-the-limit) |
| [12300006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300006-unsupported-account-type) |
| [12300005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300005-multiple-users-not-supported) |
| [12300004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300004-account-already-exists) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let domainInfo: osAccount.DomainAccountInfo =
  {domain: 'testDomain', accountName: 'testAccountName'};
let options: osAccount.CreateOsAccountForDomainOptions = {
  shortName: 'myShortName'
}
try {
  accountManager.createOsAccountForDomain(osAccount.OsAccountType.NORMAL, domainInfo, options).then(
    (accountInfo: osAccount.OsAccountInfo) => {
    console.info('createOsAccountForDomain, account info: ' + JSON.stringify(accountInfo));
  }).catch((err: BusinessError) => {
    console.error(`createOsAccountForDomain err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createOsAccountForDomain exception: code is ${err.code}, message is ${err.message}`);
}
```

## deactivateOsAccount

```TypeScript
deactivateOsAccount(localId: number): Promise<void>
```

Deactivates (logs out of) an OS account. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-deactivateOsAccount(localId: int): Promise<void>--><!--Device-AccountManager-deactivateOsAccount(localId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Deactivate OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.deactivateOsAccount(localId).then(() => {
    console.info('deactivateOsAccount successfully');
  }).catch((err: BusinessError) => {
    console.error(`deactivateOsAccount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deactivateOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## getBundleIdForUid

```TypeScript
getBundleIdForUid(uid: number, callback: AsyncCallback<number>): void
```

Obtains the bundle ID based on the specified UID. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-AccountManager-getBundleIdForUid(uid: int, callback: AsyncCallback<int>): void--><!--Device-AccountManager-getBundleIdForUid(uid: int, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
// uid indicates the application process UID, which can be obtained from the application information.
let testUid: number = 1000000;
try {
  accountManager.getBundleIdForUid(testUid, (err: BusinessError, bundleId: number) => {
    if (err) {
      console.error(`getBundleIdForUid errInfo:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getBundleIdForUid bundleId:' + JSON.stringify(bundleId));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getBundleIdForUid exception: code is ${err.code}, message is ${err.message}`);
}
```

## getBundleIdForUid

```TypeScript
getBundleIdForUid(uid: number): Promise<number>
```

Obtains the bundle ID based on the specified UID. This API uses a promise to return the result.

**Since:** 9

<!--Device-AccountManager-getBundleIdForUid(uid: int): Promise<int>--><!--Device-AccountManager-getBundleIdForUid(uid: int): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let testUid: number = 1000000;
try {
  accountManager.getBundleIdForUid(testUid).then((result: number) => {
    console.info('getBundleIdForUid bundleId:' + JSON.stringify(result));
  }).catch((err: BusinessError) => {
    console.error(`getBundleIdForUid errInfo:code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getBundleIdForUid exception: code is ${err.code}, message is ${err.message}`);
}
```

## getBundleIdForUidSync

```TypeScript
getBundleIdForUidSync(uid: number): number
```

Obtains the bundle ID based on the specified UID. The API returns the result synchronously.

**Since:** 10

<!--Device-AccountManager-getBundleIdForUidSync(uid: int): int--><!--Device-AccountManager-getBundleIdForUidSync(uid: int): int-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let testUid: number = 1000000;
try {
  let bundleId : number = accountManager.getBundleIdForUidSync(testUid);
  console.info('getBundleIdForUidSync bundleId:' + bundleId);
} catch (e) {
  const err = e as BusinessError;
  console.error(`getBundleIdForUidSync exception: code is ${err.code}, message is ${err.message}`);
}
```

## getEnabledOsAccountConstraints

```TypeScript
getEnabledOsAccountConstraints(localId: number): Promise<Array<string>>
```

Obtains all the enabled constraints of an OS account. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-getEnabledOsAccountConstraints(localId: int): Promise<Array<string>>--><!--Device-AccountManager-getEnabledOsAccountConstraints(localId: int): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Obtain all constraints of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getEnabledOsAccountConstraints(localId).then((constraints: string[]) => {
    console.info('getEnabledOsAccountConstraints, constraints: ' + constraints);
  }).catch((err: BusinessError) => {
    console.error(`getEnabledOsAccountConstraints err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getEnabledOsAccountConstraints exception: code is ${err.code}, message is ${err.message}`);
}
```

## getForegroundOsAccountDisplayId

```TypeScript
getForegroundOsAccountDisplayId(localId: number): Promise<number>
```

Obtains the logical display ID of the specified foreground OS account. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-getForegroundOsAccountDisplayId(localId: int): Promise<long>--><!--Device-AccountManager-getForegroundOsAccountDisplayId(localId: int): Promise<long>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

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
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300017](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300017-foreground-os-account-not-found) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getForegroundOsAccountDisplayId(localId).then((displayId: number) => {
    console.info('account ' + localId + ' foreground displayId: ' + displayId);
  }).catch((err: BusinessError) => {
    console.error(`getForegroundOsAccountDisplayId failed: ${err.code} ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getForegroundOsAccountDisplayId exception: ${err.code} ${err.message}`);
}
```

## getForegroundOsAccountLocalId

```TypeScript
getForegroundOsAccountLocalId(displayId: number): Promise<number>
```

Obtains the ID of the foreground OS account running on a specified logical display. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-getForegroundOsAccountLocalId(displayId: long): Promise<int>--><!--Device-AccountManager-getForegroundOsAccountLocalId(displayId: long): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300017](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300017-foreground-os-account-not-found) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let displayId: number = 0;
try {
  accountManager.getForegroundOsAccountLocalId(displayId).then((localId: number) => {
    console.info('foreground account on display ' + displayId + ' is ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getForegroundOsAccountLocalId failed: ${err.code} ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getForegroundOsAccountLocalId exception: ${err.code} ${err.message}`);
}
```

## getOsAccountConstraintSourceTypes

```TypeScript
getOsAccountConstraintSourceTypes(localId: number, constraint: string, callback: AsyncCallback<Array<ConstraintSourceTypeInfo>>): void
```

Obtains the constraint source information of an OS account. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountConstraintSourceTypes(localId: int, constraint: string, callback: AsyncCallback<Array<ConstraintSourceTypeInfo>>): void--><!--Device-AccountManager-getOsAccountConstraintSourceTypes(localId: int, constraint: string, callback: AsyncCallback<Array<ConstraintSourceTypeInfo>>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| constraint | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ConstraintSourceTypeInfo](arkts-basicservices-osaccount-constraintsourcetypeinfo-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountConstraintSourceTypes(100, 'constraint.wifi',
    (err: BusinessError,sourceTypeInfos: osAccount.ConstraintSourceTypeInfo[])=>{
    if (err) {
      console.error(`getOsAccountConstraintSourceTypes errInfo:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountConstraintSourceTypes sourceTypeInfos:' + JSON.stringify(sourceTypeInfos));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountConstraintSourceTypes exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountConstraintSourceTypes

```TypeScript
getOsAccountConstraintSourceTypes(localId: number, constraint: string): Promise<Array<ConstraintSourceTypeInfo>>
```

Obtains the constraint source information of an OS account. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountConstraintSourceTypes(localId: int, constraint: string): Promise<Array<ConstraintSourceTypeInfo>>--><!--Device-AccountManager-getOsAccountConstraintSourceTypes(localId: int, constraint: string): Promise<Array<ConstraintSourceTypeInfo>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| constraint | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ConstraintSourceTypeInfo](arkts-basicservices-osaccount-constraintsourcetypeinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountConstraintSourceTypes(100, 'constraint.wifi').then(
    (result: osAccount.ConstraintSourceTypeInfo[]) => {
    console.info('getOsAccountConstraintSourceTypes sourceTypeInfos:' + JSON.stringify(result));
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountConstraintSourceTypes errInfo:code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountConstraintSourceTypes exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountProfilePhoto

```TypeScript
getOsAccountProfilePhoto(localId: number, callback: AsyncCallback<string>): void
```

Obtains the profile photo of an OS account. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountProfilePhoto(localId: int, callback: AsyncCallback<string>): void--><!--Device-AccountManager-getOsAccountProfilePhoto(localId: int, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Obtain the profile photo of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getOsAccountProfilePhoto(localId, (err: BusinessError, photo: string)=>{
    if (err) {
      console.error(`getOsAccountProfilePhoto exception:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('get photo:' + photo + ' by localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountProfilePhoto exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountProfilePhoto

```TypeScript
getOsAccountProfilePhoto(localId: number): Promise<string>
```

Obtains the profile photo of an OS account. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountProfilePhoto(localId: int): Promise<string>--><!--Device-AccountManager-getOsAccountProfilePhoto(localId: int): Promise<string>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Obtain the profile photo of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.getOsAccountProfilePhoto(localId).then((photo: string) => {
    console.info('getOsAccountProfilePhoto: ' + photo);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountProfilePhoto err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountProfilePhoto exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountType

```TypeScript
getOsAccountType(localId: number): Promise<OsAccountType>
```

Obtains the type of a specified OS account. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountType(localId: int): Promise<OsAccountType>--><!--Device-AccountManager-getOsAccountType(localId: int): Promise<OsAccountType>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  let localId: number = 100;
  accountManager.getOsAccountType(localId).then((type: osAccount.OsAccountType) => {
    console.info('getOsAccountType Type:' + type);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountType errInfo:code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountType exception: code is ${err.code}, message is ${err.message}`);
}
```

## isMainOsAccount

```TypeScript
isMainOsAccount(callback: AsyncCallback<boolean>): void
```

Checks whether the current process belongs to the main OS account. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-isMainOsAccount(callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-isMainOsAccount(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.isMainOsAccount((err: BusinessError,result: boolean)=>{
    if (err) {
      console.error(`isMainOsAccount errInfo:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('isMainOsAccount result:' + JSON.stringify(result));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`isMainOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## isMainOsAccount

```TypeScript
isMainOsAccount(): Promise<boolean>
```

Checks whether the current process belongs to the main OS account. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-isMainOsAccount(): Promise<boolean>--><!--Device-AccountManager-isMainOsAccount(): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.isMainOsAccount().then((result: boolean) => {
    console.info('isMainOsAccount result:' + JSON.stringify(result));
  }).catch((err: BusinessError) => {
    console.error(`isMainOsAccount errInfo:code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`isMainOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## isOsAccountActivated

```TypeScript
isOsAccountActivated(localId: number): Promise<boolean>
```

Checks whether an OS account is activated. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountActivated(localId: int): Promise<boolean>--><!--Device-AccountManager-isOsAccountActivated(localId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Check whether OS account 100 is activated.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.isOsAccountActivated(localId).then((isActivated: boolean) => {
    console.info('isOsAccountActivated successfully, isActivated: ' + isActivated);
  }).catch((err: BusinessError) => {
    console.error(`isOsAccountActivated failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`isOsAccountActivated exception: code is ${err.code}, message is ${err.message}`);
}
```

## isOsAccountConstraintEnabled

```TypeScript
isOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>
```

Checks whether a constraint is enabled for an OS account. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountConstraintEnabled(localId: int, constraint: string): Promise<boolean>--><!--Device-AccountManager-isOsAccountConstraintEnabled(localId: int, constraint: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Check whether OS account 100 is forbidden to use Wi-Fi.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
try {
  accountManager.isOsAccountConstraintEnabled(localId, constraint).then((isEnabled: boolean) => {
    console.info('isOsAccountConstraintEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(`isOsAccountConstraintEnabled failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`isOsAccountConstraintEnabled exception: code is ${err.code}, message is ${err.message}`);
}
```

## isOsAccountUnlocked

```TypeScript
isOsAccountUnlocked(localId: number): Promise<boolean>
```

Checks whether an OS account has been verified. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountUnlocked(localId: int): Promise<boolean>--><!--Device-AccountManager-isOsAccountUnlocked(localId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.isOsAccountUnlocked(localId).then((isVerified: boolean) => {
    console.info('isOsAccountUnlocked successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(`isOsAccountUnlocked failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`isOsAccountUnlocked exception: code is ${err.code}, message is ${err.message}`);
}
```

## off('activate' | 'activating')

```TypeScript
off(type: 'activate' | 'activating', name: string, callback?: Callback<number>): void
```

Unsubscribes from the OS account activation states, including the states of the account being activated and the account with activation completed. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-off(type: 'activate' | 'activating', name: string, callback?: Callback<int>): void--><!--Device-AccountManager-off(type: 'activate' | 'activating', name: string, callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activate' \| 'activating' | Yes |
| name | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();

function offCallback(){
  console.info('off enter')
}

try {
  accountManager.off('activating', 'osAccountOnOffNameA', offCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`off exception: code is ${err.code}, message is ${err.message}`);
}
```

## off('activate' | 'activating')

```TypeScript
off(type: 'activate' | 'activating', name: string, callback?: Callback<number>): void
```

Unsubscribes from the OS account activation states, including the states of the account being activated and the account with activation completed. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-off(type: 'activate' | 'activating', name: string, callback?: Callback<int>): void--><!--Device-AccountManager-off(type: 'activate' | 'activating', name: string, callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activate' \| 'activating' | Yes |
| name | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();

function offCallback(){
  console.info('off enter')
}

try {
  accountManager.off('activating', 'osAccountOnOffNameA', offCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`off exception: code is ${err.code}, message is ${err.message}`);
}
```

## off('switching')

```TypeScript
off(type: 'switching', callback?: Callback<OsAccountSwitchEventData>): void
```

Unsubscribes from the switchover between a foreground OS account and a background OS account in progress. This API uses an asynchronous callback to return the result.

**Since:** 12

**Required permissions:** 
- API version 23+: ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
- API version 12 - 22: ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-off(type: 'switching', callback?: Callback<OsAccountSwitchEventData>): void--><!--Device-AccountManager-off(type: 'switching', callback?: Callback<OsAccountSwitchEventData>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'switching' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.off('switching');
} catch (e) {
  const err = e as BusinessError;
  console.error(`off exception: code is ${err.code}, message is ${err.message}`);
}
```

## off('switched')

```TypeScript
off(type: 'switched', callback?: Callback<OsAccountSwitchEventData>): void
```

Unsubscribes from the end of a switchover between a foreground OS account and a background OS account.This API uses an asynchronous callback to return the result.

**Since:** 12

**Required permissions:** 
- API version 23+: ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
- API version 12 - 22: ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-off(type: 'switched', callback?: Callback<OsAccountSwitchEventData>): void--><!--Device-AccountManager-off(type: 'switched', callback?: Callback<OsAccountSwitchEventData>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'switched' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.off('switched');
} catch (e) {
  const err = e as BusinessError;
  console.error(`off exception: code is ${err.code}, message is ${err.message}`);
}
```

## offConstraintChanged

```TypeScript
offConstraintChanged(callback?: Callback<ConstraintChangeInfo>): void
```

Unsubscribes from constraint change events associated with the specified callback. If no callback is specified,this API unsubscribes from all subscription records.

**Since:** 23

<!--Device-AccountManager-offConstraintChanged(callback?: Callback<ConstraintChangeInfo>): void--><!--Device-AccountManager-offConstraintChanged(callback?: Callback<ConstraintChangeInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ConstraintChangeInfo](arkts-basicservices-osaccount-constraintchangeinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let constraint: string = 'constraint.wifi';
const callback:Callback<osAccount.ConstraintChangeInfo> = (data: osAccount.ConstraintChangeInfo): void => {
  console.info(`ConstraintChangeInfo received, constraint: ${data.constraint} isEnabled: ${data.isEnabled}`);
};

try {
  accountManager.onConstraintChanged([constraint], callback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`onConstraintChanged exception: code is ${err.code}, message is ${err.message}`);
}

try {
  accountManager.offConstraintChanged(callback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`offConstraintChanged exception: code is ${err.code}, message is ${err.message}`);
}
```

## on('activate' | 'activating')

```TypeScript
on(type: 'activate' | 'activating', name: string, callback: Callback<number>): void
```

Subscribes to the OS account activation states, including the states of the account being activated and the account with activation completed. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-on(type: 'activate' | 'activating', name: string, callback: Callback<int>): void--><!--Device-AccountManager-on(type: 'activate' | 'activating', name: string, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activate' \| 'activating' | Yes |
| name | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();

function onCallback(receiveLocalId: number){
  console.info('receive localId:' + receiveLocalId);
}

try {
  accountManager.on('activating', 'osAccountOnOffNameA', onCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`receive localId exception: code is ${err.code}, message is ${err.message}`);
}
```

## on('activate' | 'activating')

```TypeScript
on(type: 'activate' | 'activating', name: string, callback: Callback<number>): void
```

Subscribes to the OS account activation states, including the states of the account being activated and the account with activation completed. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-on(type: 'activate' | 'activating', name: string, callback: Callback<int>): void--><!--Device-AccountManager-on(type: 'activate' | 'activating', name: string, callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'activate' \| 'activating' | Yes |
| name | string | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();

function onCallback(receiveLocalId: number){
  console.info('receive localId:' + receiveLocalId);
}

try {
  accountManager.on('activating', 'osAccountOnOffNameA', onCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`receive localId exception: code is ${err.code}, message is ${err.message}`);
}
```

## on('switching')

```TypeScript
on(type: 'switching', callback: Callback<OsAccountSwitchEventData>): void
```

Subscribes to the switchover between a foreground OS account and a background OS account in progress.This API uses an asynchronous callback to return the result.

**Since:** 12

**Required permissions:** 
- API version 23+: ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
- API version 12 - 22: ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-on(type: 'switching', callback: Callback<OsAccountSwitchEventData>): void--><!--Device-AccountManager-on(type: 'switching', callback: Callback<OsAccountSwitchEventData>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'switching' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();

function onSwitchingCallback(eventData: osAccount.OsAccountSwitchEventData){
  console.info('receive eventData:' + JSON.stringify(eventData));
}

try {
  accountManager.on('switching', onSwitchingCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`receive eventData exception: code is ${err.code}, message is ${err.message}`);
}
```

## on('switched')

```TypeScript
on(type: 'switched', callback: Callback<OsAccountSwitchEventData>): void
```

Subscribes to the end of a switchover between a foreground OS account and a background OS account. This API uses an asynchronous callback to return the result.

**Since:** 12

**Required permissions:** 
- API version 23+: ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
- API version 12 - 22: ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-on(type: 'switched', callback: Callback<OsAccountSwitchEventData>): void--><!--Device-AccountManager-on(type: 'switched', callback: Callback<OsAccountSwitchEventData>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'switched' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSwitchEventData](arkts-basicservices-osaccount-osaccountswitcheventdata-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();

function onSwitchedCallback(eventData: osAccount.OsAccountSwitchEventData){
  console.info('receive eventData:' + JSON.stringify(eventData));
}

try {
  accountManager.on('switched', onSwitchedCallback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`receive eventData exception: code is ${err.code}, message is ${err.message}`);
}
```

## onConstraintChanged

```TypeScript
onConstraintChanged(constraints: string[], callback: Callback<ConstraintChangeInfo>): void
```

Subscribes to one or more constraint change events of the OS account to which the caller belongs. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-onConstraintChanged(constraints: string[], callback: Callback<ConstraintChangeInfo>): void--><!--Device-AccountManager-onConstraintChanged(constraints: string[], callback: Callback<ConstraintChangeInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md) | string[] | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ConstraintChangeInfo](arkts-basicservices-osaccount-constraintchangeinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let constraint: string = 'constraint.wifi';
const callback:Callback<osAccount.ConstraintChangeInfo> = (data: osAccount.ConstraintChangeInfo): void => {
  console.info(`ConstraintChangeInfo received, constraint: ${data.constraint} isEnabled: ${data.isEnabled}`);
};

try {
  accountManager.onConstraintChanged([constraint], callback);
} catch (e) {
  const err = e as BusinessError;
  console.error(`onConstraintChanged exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryAllCreatedOsAccounts

```TypeScript
queryAllCreatedOsAccounts(callback: AsyncCallback<Array<OsAccountInfo>>): void
```

Queries information about all the OS accounts created. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-queryAllCreatedOsAccounts(callback: AsyncCallback<Array<OsAccountInfo>>): void--><!--Device-AccountManager-queryAllCreatedOsAccounts(callback: AsyncCallback<Array<OsAccountInfo>>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryAllCreatedOsAccounts((err: BusinessError, accountArr: osAccount.OsAccountInfo[])=>{
    if (err) {
      console.error(`queryAllCreatedOsAccounts exception:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('queryAllCreatedOsAccounts accountArr:' + JSON.stringify(accountArr));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryAllCreatedOsAccounts exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryAllCreatedOsAccounts

```TypeScript
queryAllCreatedOsAccounts(): Promise<Array<OsAccountInfo>>
```

Queries information about all the OS accounts created. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-queryAllCreatedOsAccounts(): Promise<Array<OsAccountInfo>>--><!--Device-AccountManager-queryAllCreatedOsAccounts(): Promise<Array<OsAccountInfo>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryAllCreatedOsAccounts().then((accountArr: osAccount.OsAccountInfo[]) => {
    console.info('queryAllCreatedOsAccounts, accountArr: ' + JSON.stringify(accountArr));
  }).catch((err: BusinessError) => {
    console.error(`queryAllCreatedOsAccounts err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryAllCreatedOsAccounts exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryMaxLoggedInOsAccountNumber

```TypeScript
queryMaxLoggedInOsAccountNumber(): Promise<number>
```

Queries the maximum number of OS accounts allowed to log in to the system. This API uses a promise to return the result.

**Since:** 12

<!--Device-AccountManager-queryMaxLoggedInOsAccountNumber(): Promise<int>--><!--Device-AccountManager-queryMaxLoggedInOsAccountNumber(): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryMaxLoggedInOsAccountNumber().then((maxNum: number) => {
    console.info('queryMaxLoggedInOsAccountNumber successfully, maxNum: ' + maxNum);
  }).catch((err: BusinessError) => {
    console.error(`queryMaxLoggedInOsAccountNumber failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryMaxLoggedInOsAccountNumber exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryMaxOsAccountNumber

```TypeScript
queryMaxOsAccountNumber(callback: AsyncCallback<number>): void
```

Queries the maximum number of OS accounts that can be created. This API uses an asynchronous callback to return the result.

**Since:** 7

<!--Device-AccountManager-queryMaxOsAccountNumber(callback: AsyncCallback<int>): void--><!--Device-AccountManager-queryMaxOsAccountNumber(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryMaxOsAccountNumber((err: BusinessError, maxCnt: number) => {
    if (err) {
      console.error(`queryMaxOsAccountNumber failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('queryMaxOsAccountNumber successfully, maxCnt:' + maxCnt);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryMaxOsAccountNumber exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryMaxOsAccountNumber

```TypeScript
queryMaxOsAccountNumber(): Promise<number>
```

Queries the maximum number of OS accounts that can be created. This API uses a promise to return the result.

**Since:** 7

<!--Device-AccountManager-queryMaxOsAccountNumber(): Promise<int>--><!--Device-AccountManager-queryMaxOsAccountNumber(): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryMaxOsAccountNumber().then((maxCnt: number) => {
    console.info('queryMaxOsAccountNumber successfully, maxCnt: ' + maxCnt);
  }).catch((err: BusinessError) => {
    console.error(`queryMaxOsAccountNumber failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryMaxOsAccountNumber exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryOsAccount

```TypeScript
queryOsAccount(): Promise<OsAccountInfo>
```

Obtains information about the OS account to which the current process belongs. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS

<!--Device-AccountManager-queryOsAccount(): Promise<OsAccountInfo>--><!--Device-AccountManager-queryOsAccount(): Promise<OsAccountInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
    console.info('queryOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
  }).catch((err: BusinessError) => {
    console.error(`queryOsAccount err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryOsAccountById

```TypeScript
queryOsAccountById(localId: number, callback: AsyncCallback<OsAccountInfo>): void
```

Queries information about the OS account of the given ID. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-queryOsAccountById(localId: int, callback: AsyncCallback<OsAccountInfo>): void--><!--Device-AccountManager-queryOsAccountById(localId: int, callback: AsyncCallback<OsAccountInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Query information about OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.queryOsAccountById(localId, (err: BusinessError, accountInfo: osAccount.OsAccountInfo)=>{
    if (err) {
      console.error(`queryOsAccountById exception:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('queryOsAccountById accountInfo:' + JSON.stringify(accountInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryOsAccountById exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryOsAccountById

```TypeScript
queryOsAccountById(localId: number): Promise<OsAccountInfo>
```

Queries information about the OS account of the given ID. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS_EXTENSION

<!--Device-AccountManager-queryOsAccountById(localId: int): Promise<OsAccountInfo>--><!--Device-AccountManager-queryOsAccountById(localId: int): Promise<OsAccountInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Query information about OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.queryOsAccountById(localId).then((accountInfo: osAccount.OsAccountInfo) => {
    console.info('queryOsAccountById, accountInfo: ' + JSON.stringify(accountInfo));
  }).catch((err: BusinessError) => {
    console.error(`queryOsAccountById err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryOsAccountById exception: code is ${err.code}, message is ${err.message}`);
}
```

## removeOsAccount

```TypeScript
removeOsAccount(localId: number, callback: AsyncCallback<void>): void
```

Removes an OS account. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-removeOsAccount(localId: int, callback: AsyncCallback<void>): void--><!--Device-AccountManager-removeOsAccount(localId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let accountName: string = 'testAccountName';
try {
  accountManager.createOsAccount(accountName, osAccount.OsAccountType.NORMAL,
    (err: BusinessError, osAccountInfo: osAccount.OsAccountInfo) => {
      accountManager.removeOsAccount(osAccountInfo.localId, (err: BusinessError)=>{
        if (err) {
          console.error(`removeOsAccount failed, code is ${err.code}, message is ${err.message}`);
        } else {
          console.info('removeOsAccount successfully');
        }
    });
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## removeOsAccount

```TypeScript
removeOsAccount(localId: number): Promise<void>
```

Removes an OS account. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-removeOsAccount(localId: int): Promise<void>--><!--Device-AccountManager-removeOsAccount(localId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let accountName: string = 'testAccountName';
try {
  accountManager.createOsAccount(accountName, osAccount.OsAccountType.NORMAL,
    (err: BusinessError, osAccountInfo: osAccount.OsAccountInfo)=>{
      accountManager.removeOsAccount(osAccountInfo.localId).then(() => {
        console.info('removeOsAccount successfully');
      }).catch((err: BusinessError) => {
        console.error(`removeOsAccount failed, code is ${err.code}, message is ${err.message}`);
      });
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## removeOsAccount

```TypeScript
removeOsAccount(localId: number, options: RemoveOsAccountOptions): Promise<void>
```

Removes a specified OS account based on the options. This API uses a promise to return the result.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-removeOsAccount(localId: int, options: RemoveOsAccountOptions): Promise<void>--><!--Device-AccountManager-removeOsAccount(localId: int, options: RemoveOsAccountOptions): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| options | [RemoveOsAccountOptions](arkts-basicservices-osaccount-removeosaccountoptions-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let accountName: string = 'testAccountName';
let token: Uint8Array = new Uint8Array([0]);
let options: osAccount.RemoveOsAccountOptions = {
  token: token,
}
try {
  accountManager.createOsAccount(accountName, osAccount.OsAccountType.NORMAL,
    (err: BusinessError, osAccountInfo: osAccount.OsAccountInfo)=>{
      accountManager.removeOsAccount(osAccountInfo.localId, options).then(() => {
        console.info('removeOsAccount successfully');
      }).catch((err: BusinessError) => {
        console.error(`removeOsAccount failed, code is ${err.code}, message is ${err.message}`);
      });
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`removeOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountConstraints

```TypeScript
setOsAccountConstraints(localId: number, constraints: Array<string>, enable: boolean, callback: AsyncCallback<void>): void
```

Sets or removes constraints for an OS account. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-setOsAccountConstraints(localId: int, constraints: Array<string>, enable: boolean, callback: AsyncCallback<void>): void--><!--Device-AccountManager-setOsAccountConstraints(localId: int, constraints: Array<string>, enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md) | Array & lt;string & gt; | Yes |
| enable | boolean | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Disable Wi-Fi for OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let constraint: string = 'constraint.wifi';
try {
  accountManager.setOsAccountConstraints(localId, [constraint], true, (err: BusinessError) => {
    if (err) {
      console.error(`setOsAccountConstraints failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOsAccountConstraints successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountConstraints exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountConstraints

```TypeScript
setOsAccountConstraints(localId: number, constraints: Array<string>, enable: boolean): Promise<void>
```

Sets or removes constraints for an OS account. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-setOsAccountConstraints(localId: int, constraints: Array<string>, enable: boolean): Promise<void>--><!--Device-AccountManager-setOsAccountConstraints(localId: int, constraints: Array<string>, enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md) | Array & lt;string & gt; | Yes |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Remove the constraint on the use of Wi-Fi for OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.setOsAccountConstraints(localId, ['constraint.location.set'], false).then(() => {
    console.info('setOsAccountConstraints successfully');
  }).catch((err: BusinessError) => {
    console.error(`setOsAccountConstraints failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountConstraints exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountName

```TypeScript
setOsAccountName(localId: number, localName: string, callback: AsyncCallback<void>): void
```

Sets the name of an OS account. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-setOsAccountName(localId: int, localName: string, callback: AsyncCallback<void>): void--><!--Device-AccountManager-setOsAccountName(localId: int, localName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| localName | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Set the name of OS account 100 to demoName.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let name: string = 'demoName';
try {
  accountManager.setOsAccountName(localId, name, (err: BusinessError) => {
    if (err) {
      console.error(`setOsAccountName failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOsAccountName successfully');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountName exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountName

```TypeScript
setOsAccountName(localId: number, localName: string): Promise<void>
```

Sets the name of an OS account. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-setOsAccountName(localId: int, localName: string): Promise<void>--><!--Device-AccountManager-setOsAccountName(localId: int, localName: string): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| localName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Set the name of OS account 100 to demoName.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let name: string = 'testName';
try {
  accountManager.setOsAccountName(localId, name).then(() => {
    console.info('setOsAccountName successfully');
  }).catch((err: BusinessError) => {
    console.error(`setOsAccountName failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountName exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountProfilePhoto

```TypeScript
setOsAccountProfilePhoto(localId: number, photo: string, callback: AsyncCallback<void>): void
```

Sets a profile photo for an OS account. This API uses an asynchronous callback to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-setOsAccountProfilePhoto(localId: int, photo: string, callback: AsyncCallback<void>): void--><!--Device-AccountManager-setOsAccountProfilePhoto(localId: int, photo: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| photo | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Set a profile photo for OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let photo: string = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPCAYAAAA/I0V3AAAAAXNSR0IArs4c6QAAAARnQU1BAA'+
'Cxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACwSURBVDhPvZLBDYMwDEV/ugsXRjAT0EHCOuFIBwkbdIRewi6unbiAyoGgSn1SFH85+Y'+
'q/4ljARW62X+LHS8uIzjm4dXUYF+utzBikB52Jo5e5iEPKqpACk7R9NM2RvWm5tIkD2czLCUFNKLD6IjdMHFHDzws285MgGrT0xCtp3WOKHo'+
'+7q0mP0DZW9pNmoEFUzrQjp5cCnaen2kSJXLFD8ghbXyZCMQf/8e8Ns1XVAG/XAgqKzVnJFAAAAABJRU5ErkJggg=='
try {
  accountManager.setOsAccountProfilePhoto(localId, photo, (err: BusinessError)=>{
    if (err) {
      console.error(`setOsAccountProfilePhoto exception:code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('setOsAccountProfilePhoto successful.');
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountProfilePhoto exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountProfilePhoto

```TypeScript
setOsAccountProfilePhoto(localId: number, photo: string): Promise<void>
```

Sets a profile photo for an OS account. This API uses a promise to return the result.

**Since:** 7

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-setOsAccountProfilePhoto(localId: int, photo: string): Promise<void>--><!--Device-AccountManager-setOsAccountProfilePhoto(localId: int, photo: string): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| photo | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Set a profile photo for OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let photo: string = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPCAYAAAA/I0V3AAAAAXNSR0IArs4c6QAAAARnQU1BAA'+
'Cxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACwSURBVDhPvZLBDYMwDEV/ugsXRjAT0EHCOuFIBwkbdIRewi6unbiAyoGgSn1SFH85+Y'+
'q/4ljARW62X+LHS8uIzjm4dXUYF+utzBikB52Jo5e5iEPKqpACk7R9NM2RvWm5tIkD2czLCUFNKLD6IjdMHFHDzws285MgGrT0xCtp3WOKHo'+
'+7q0mP0DZW9pNmoEFUzrQjp5cCnaen2kSJXLFD8ghbXyZCMQf/8e8Ns1XVAG/XAgqKzVnJFAAAAABJRU5ErkJggg=='
try {
  accountManager.setOsAccountProfilePhoto(localId, photo).then(() => {
    console.info('setOsAccountProfilePhoto success');
  }).catch((err: BusinessError) => {
    console.error(`setOsAccountProfilePhoto err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountProfilePhoto exception: code is ${err.code}, message is ${err.message}`);
}
```

## setOsAccountType

```TypeScript
setOsAccountType(localId: number, type: OsAccountType, options?: SetOsAccountTypeOptions): Promise<void>
```

Sets the type of a specified OS account. This API uses a promise to return the result.

**Since:** 24

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-setOsAccountType(localId: int, type: OsAccountType, options?: SetOsAccountTypeOptions): Promise<void>--><!--Device-AccountManager-setOsAccountType(localId: int, type: OsAccountType, options?: SetOsAccountTypeOptions): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| localId | number | Yes |
| type | [OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md) | Yes |
| options | [SetOsAccountTypeOptions](arkts-basicservices-osaccount-setosaccounttypeoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [204](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#204-access-denied-by-user-access-control-policy) |
| [12300023](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300023-accounts-of-a-specified-type-reached-the-limit) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
let type: osAccount.OsAccountType = osAccount.OsAccountType.ADMIN;
let options: osAccount.SetOsAccountTypeOptions = {
  token: new Uint8Array([0, 1, 2, 3])
};
try {
  accountManager.setOsAccountType(localId, type, options).then(() => {
    console.info('setOsAccountType successfully');
  }).catch((err: BusinessError) => {
    console.error(`setOsAccountType failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`setOsAccountType exception: code is ${err.code}, message is ${err.message}`);
}
```
