# AccountManager

Provides APIs for managing OS accounts.

**Since:** 23

<!--Device-osAccount-interface AccountManager--><!--Device-osAccount-interface AccountManager-End-->

**System capability:** SystemCapability.Account.OsAccount

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
import { osAccount } from '@kit.BasicServicesKit';
```

## checkMultiOsAccountEnabled

```TypeScript
checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void
```

Checks whether multiple OS accounts are supported. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-checkMultiOsAccountEnabled(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means multiple OS accounts are supported; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkMultiOsAccountEnabled((err: BusinessError, isEnabled: boolean) => {
    if (err) {
      console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkMultiOsAccountEnabled successfully, isEnabled: ' + isEnabled);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
}
```

## checkMultiOsAccountEnabled

```TypeScript
checkMultiOsAccountEnabled(): Promise<boolean>
```

Checks whether multiple OS accounts are supported. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-checkMultiOsAccountEnabled(): Promise<boolean>--><!--Device-AccountManager-checkMultiOsAccountEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means multiple OS accounts are supported; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  accountManager.checkMultiOsAccountEnabled().then((isEnabled: boolean) => {
    console.info('checkMultiOsAccountEnabled successfully, isEnabled: ' + isEnabled);
  }).catch((err: BusinessError) => {
    console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkMultiOsAccountEnabled failed, code is ${err.code}, message is ${err.message}`);
}
```

## checkOsAccountActivated

```TypeScript
checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void
```

Checks whether an OS account is activated. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-checkOsAccountActivated(localId: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the account is activated; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## checkOsAccountActivated

```TypeScript
checkOsAccountActivated(localId: number): Promise<boolean>
```

Checks whether an OS account is activated. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-checkOsAccountActivated(localId: number): Promise<boolean>--><!--Device-AccountManager-checkOsAccountActivated(localId: number): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the account is activated; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## checkOsAccountConstraintEnabled

```TypeScript
checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void
```

Checks whether the specified constraint is enabled for an OS account. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-checkOsAccountConstraintEnabled(localId: number, constraint: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| constraint | string | Yes | [Constraint](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) to check. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId or constraint. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## checkOsAccountConstraintEnabled

```TypeScript
checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>
```

Checks whether the specified constraint is enabled for an OS account. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>--><!--Device-AccountManager-checkOsAccountConstraintEnabled(localId: number, constraint: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| constraint | string | Yes | [Constraint](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) to check. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId or constraint. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## checkOsAccountTestable

```TypeScript
checkOsAccountTestable(callback: AsyncCallback<boolean>): void
```

Checks whether this OS account is a test account. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-checkOsAccountTestable(callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-checkOsAccountTestable(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the account is a test account; the value **false** means the opposite; the default value is **false**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountTestable((err: BusinessError, isTestable: boolean) => {
    if (err) {
      console.error(`checkOsAccountTestable failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOsAccountTestable successfully, isTestable: ' + isTestable);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountTestable code is ${err.code}, message is ${err.message}`);
}
```

## checkOsAccountTestable

```TypeScript
checkOsAccountTestable(): Promise<boolean>
```

Checks whether this OS account is a test account. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-checkOsAccountTestable(): Promise<boolean>--><!--Device-AccountManager-checkOsAccountTestable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the account is a test account; the value **false** means the opposite; the default value is **false**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountTestable().then((isTestable: boolean) => {
    console.info('checkOsAccountTestable successfully, isTestable: ' + isTestable);
  }).catch((err: BusinessError) => {
    console.error(`checkOsAccountTestable failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountTestable exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(callback: AsyncCallback<boolean>): void
```

Checks whether this OS account is unlocked. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. You are advised to use > [isOsAccountUnlocked](#isosaccountunlocked) instead.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [isOsAccountUnlocked](#isosaccountunlocked)()

<!--Device-AccountManager-checkOsAccountVerified(callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-checkOsAccountVerified(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the OS account has been verified; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountVerified((err: BusinessError, isVerified: boolean) => {
    if (err) {
      console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(): Promise<boolean>
```

Checks whether this OS account has been verified. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. You are advised to use > [isOsAccountUnlocked](#isosaccountunlocked) instead.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [isOsAccountUnlocked](#isosaccountunlocked)()

<!--Device-AccountManager-checkOsAccountVerified(): Promise<boolean>--><!--Device-AccountManager-checkOsAccountVerified(): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the OS account has been verified; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.checkOsAccountVerified().then((isVerified: boolean) => {
    console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void
```

Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-checkOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the OS account has been verified; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountVerified(localId, (err: BusinessError, isVerified: boolean) => {
    if (err) {
      console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
}
```

## checkOsAccountVerified

```TypeScript
checkOsAccountVerified(localId: number): Promise<boolean>
```

Checks whether an OS account has been verified. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-checkOsAccountVerified(localId: number): Promise<boolean>--><!--Device-AccountManager-checkOsAccountVerified(localId: number): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. If this parameter is not specified, this API checks whether the current OS account has been verified. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the OS account has been verified; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
try {
  accountManager.checkOsAccountVerified(localId).then((isVerified: boolean) => {
    console.info('checkOsAccountVerified successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(`checkOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`checkOsAccountVerified exception: code is ${err.code}, message is ${err.message}`);
}
```

## getActivatedOsAccountLocalIds

```TypeScript
getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<int>>): void
```

Obtains information about all activated OS accounts. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<int>>): void--><!--Device-AccountManager-getActivatedOsAccountLocalIds(callback: AsyncCallback<Array<int>>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;int&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is a list of activated OS accounts. Otherwise, **data** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getActivatedOsAccountLocalIds((err: BusinessError, idArray: number[])=>{
    if (err) {
      console.error(`getActivatedOsAccountLocalIds code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getActivatedOsAccountLocalIds idArray length:' + idArray.length);
      for(let i=0;i<idArray.length;i++) {
        console.info('activated os account id: ' + idArray[i]);
      }
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getActivatedOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}`);
}
```

## getActivatedOsAccountLocalIds

```TypeScript
getActivatedOsAccountLocalIds(): Promise<Array<int>>
```

Obtains information about all activated OS accounts. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-getActivatedOsAccountLocalIds(): Promise<Array<int>>--><!--Device-AccountManager-getActivatedOsAccountLocalIds(): Promise<Array<int>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;int&gt;&gt; | Promise used to return the information about all activated OS accounts. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getActivatedOsAccountLocalIds().then((idArray: number[]) => {
    console.info('getActivatedOsAccountLocalIds, idArray: ' + idArray);
  }).catch((err: BusinessError) => {
    console.error(`getActivatedOsAccountLocalIds err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getActivatedOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}`);
}
```

## getCreatedOsAccountsCount

```TypeScript
getCreatedOsAccountsCount(callback: AsyncCallback<number>): void
```

Obtains the number of OS accounts created. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [getOsAccountCount](#getosaccountcount) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountCount](#getosaccountcount)(callback: AsyncCallback&lt;int&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getCreatedOsAccountsCount(callback: AsyncCallback<number>): void--><!--Device-AccountManager-getCreatedOsAccountsCount(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the number of created OS accounts. If the operation fails, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getCreatedOsAccountsCount((err: BusinessError, count: number)=>{
  if (err) {
    console.error(`getCreatedOsAccountsCount failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getCreatedOsAccountsCount successfully, count: ' + count);
  }
});
```

## getCreatedOsAccountsCount

```TypeScript
getCreatedOsAccountsCount(): Promise<number>
```

Obtains the number of OS accounts created. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [getOsAccountCount](#getosaccountcount) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountCount](#getosaccountcount)()

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getCreatedOsAccountsCount(): Promise<number>--><!--Device-AccountManager-getCreatedOsAccountsCount(): Promise<number>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the number of created OS accounts. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getCreatedOsAccountsCount().then((count: number) => {
  console.info('getCreatedOsAccountsCount successfully, count: ' + count);
}).catch((err: BusinessError) => {
  console.error(`getCreatedOsAccountsCount failed, code is ${err.code}, message is ${err.message}`);
});
```

## getCurrentOsAccount

```TypeScript
getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void
```

Obtains information about the OS account to which the current process belongs. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** 
- API version 10+: ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS
- API version 9: ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void--><!--Device-AccountManager-getCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account information obtained. Otherwise, **data** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getCurrentOsAccount((err: BusinessError, curAccountInfo: osAccount.OsAccountInfo)=>{
    if (err) {
      console.error(`getCurrentOsAccount code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getCurrentOsAccount curAccountInfo:' + JSON.stringify(curAccountInfo));
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCurrentOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## getCurrentOsAccount

```TypeScript
getCurrentOsAccount(): Promise<OsAccountInfo>
```

Obtains information about the OS account to which the current process belongs. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** 
- API version 10+: ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.GET_LOCAL_ACCOUNTS
- API version 9: ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getCurrentOsAccount(): Promise<OsAccountInfo>--><!--Device-AccountManager-getCurrentOsAccount(): Promise<OsAccountInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Promise used to return the OS account information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getCurrentOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
    console.info('getCurrentOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
  }).catch((err: BusinessError) => {
    console.error(`getCurrentOsAccount err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getCurrentOsAccount exception: code is ${err.code}, message is ${err.message}`);
}
```

## getDistributedVirtualDeviceId

```TypeScript
getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void
```

Obtains the ID of a distributed virtual device. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid) > instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)(callback: AsyncCallback&lt;string&gt;)

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void--><!--Device-AccountManager-getDistributedVirtualDeviceId(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the distributed virtual device ID obtained. Otherwise, **data** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getDistributedVirtualDeviceId((err: BusinessError, virtualID: string) => {
  if (err) {
    console.error(`getDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getDistributedVirtualDeviceId virtualID: ' + virtualID);
  }
});
```

## getDistributedVirtualDeviceId

```TypeScript
getDistributedVirtualDeviceId(): Promise<string>
```

Obtains the ID of this distributed virtual device. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [queryDistributedVirtualDeviceId](#querydistributedvirtualdeviceid)()

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getDistributedVirtualDeviceId(): Promise<string>--><!--Device-AccountManager-getDistributedVirtualDeviceId(): Promise<string>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the distributed virtual device ID obtained. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getDistributedVirtualDeviceId().then((virtualID: string) => {
  console.info('getDistributedVirtualDeviceId, virtualID: ' + virtualID);
}).catch((err: BusinessError) => {
  console.error(`getDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
});
```

## getForegroundOsAccountLocalId

```TypeScript
getForegroundOsAccountLocalId(): Promise<int>
```

Obtains the ID of the foreground OS account. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-getForegroundOsAccountLocalId(): Promise<int>--><!--Device-AccountManager-getForegroundOsAccountLocalId(): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the ID of the foreground OS account. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getForegroundOsAccountLocalId().then((localId: number) => {
    console.info('getForegroundOsAccountLocalId, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getForegroundOsAccountLocalId err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getForegroundOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountAllConstraints

```TypeScript
getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void
```

Obtains all constraints enabled for an OS account. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountConstraints](#getosaccountconstraints)(localId: number, callback: AsyncCallback&lt;Array&lt;string&gt;&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void--><!--Device-AccountManager-getOsAccountAllConstraints(localId: number, callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is a list of all [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) enabled for the OS account. Otherwise, **err** is an error object. |

## getOsAccountAllConstraints

```TypeScript
getOsAccountAllConstraints(localId: number): Promise<Array<string>>
```

Obtains all constraints enabled for an OS account. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountConstraints](#getosaccountconstraints)(localId: number)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountAllConstraints(localId: number): Promise<Array<string>>--><!--Device-AccountManager-getOsAccountAllConstraints(localId: number): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return all the [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) enabled for the OS account. |

## getOsAccountConstraints

```TypeScript
getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void
```

Obtains all constraints enabled for an OS account. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void--><!--Device-AccountManager-getOsAccountConstraints(localId: number, callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is all [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getOsAccountConstraints

```TypeScript
getOsAccountConstraints(localId: number): Promise<Array<string>>
```

Obtains all constraints enabled for an OS account. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 9 and deprecated since API version 11. The substitute API is available > only to system applications.

**Since:** 9

**Deprecated since:** 11

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountConstraints(localId: number): Promise<Array<string>>--><!--Device-AccountManager-getOsAccountConstraints(localId: number): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return all the [constraints](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) enabled for the OS account. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getOsAccountCount

```TypeScript
getOsAccountCount(callback: AsyncCallback<int>): void
```

Obtains the number of OS accounts created. This API uses an asynchronous callback to return the result. This API can be called only by system applications.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountCount(callback: AsyncCallback<int>): void--><!--Device-AccountManager-getOsAccountCount(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the number of created OS accounts. If the operation fails, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountCount((err: BusinessError, count: number) => {
    if (err) {
      console.error(`getOsAccountCount failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountCount successfully, count: ' + count);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountCount exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountCount

```TypeScript
getOsAccountCount(): Promise<int>
```

Obtains the number of OS accounts created. This API uses a promise to return the result. This API can be called only by system applications.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountCount(): Promise<int>--><!--Device-AccountManager-getOsAccountCount(): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the number of created OS accounts. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountCount().then((count: number) => {
    console.info('getOsAccountCount successfully, count: ' + count);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountCount failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountCount exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountDomainInfo

```TypeScript
getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>
```

Obtains the domain account information associated with a specified OS account. This API uses a promise to return the result.

**Since:** 15

**Required permissions:** ohos.permission.GET_DOMAIN_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>--><!--Device-AccountManager-getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md)&gt; | Promise used to return the domain account information obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | OS account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.getOsAccountDomainInfo(localId).then((domainAccountInfo: osAccount.DomainAccountInfo) => {
  if (domainAccountInfo === null) {
    console.info('The target OS account is not a domain account.')
  } else {
    console.info('getOsAccountDomainInfo domain: ' + domainAccountInfo.domain);
    console.info('getOsAccountDomainInfo accountName: ' + domainAccountInfo.accountName);
  }
}).catch((err: BusinessError) => {
  console.error(`getOsAccountDomainInfo err: code is ${err.code}, message is ${err.message}`);
})
```

## getOsAccountDomainInfo

```TypeScript
getOsAccountDomainInfo(localId: int): Promise<DomainAccountInfo | null>
```

Obtains the domain account information associated with a specified OS account. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_DOMAIN_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountDomainInfo(localId: int): Promise<DomainAccountInfo | null>--><!--Device-AccountManager-getOsAccountDomainInfo(localId: int): Promise<DomainAccountInfo | null>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | int | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) \| null&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | OS account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getOsAccountLocalId

```TypeScript
getOsAccountLocalId(callback: AsyncCallback<int>): void
```

Obtains the ID of the OS account to which the current process belongs. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountLocalId(callback: AsyncCallback<int>): void--><!--Device-AccountManager-getOsAccountLocalId(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account ID obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalId((err: BusinessError, localId: number) => {
    if (err) {
      console.error(`getOsAccountLocalId failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountLocalId successfully, localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountLocalId

```TypeScript
getOsAccountLocalId(): Promise<int>
```

Obtains the ID of the OS account to which the current process belongs. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountLocalId(): Promise<int>--><!--Device-AccountManager-getOsAccountLocalId(): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the OS account ID obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalId().then((localId: number) => {
    console.info('getOsAccountLocalId successfully, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalId failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalId exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountLocalIdBySerialNumber

```TypeScript
getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the SN. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)(serialNumber: long, callback: AsyncCallback&lt;int&gt;)

<!--Device-AccountManager-getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void--><!--Device-AccountManager-getOsAccountLocalIdBySerialNumber(serialNumber: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| serialNumber | number | Yes | Account SN. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account ID obtained. Otherwise, **err** is an error object. |

## getOsAccountLocalIdBySerialNumber

```TypeScript
getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>
```

Obtains the OS account ID based on the SN. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForSerialNumber](#getosaccountlocalidforserialnumber)(serialNumber: long)

<!--Device-AccountManager-getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>--><!--Device-AccountManager-getOsAccountLocalIdBySerialNumber(serialNumber: number): Promise<number>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| serialNumber | number | Yes | Account SN. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the OS account ID obtained. |

## getOsAccountLocalIdForDomain

```TypeScript
getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<int>): void
```

Obtains the OS account ID based on the domain account information. This API uses an asynchronous callback to return the result. This API can be called only by system applications.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<int>): void--><!--Device-AccountManager-getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Domain account information. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the ID of the OS account associated with the domain account. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Domain account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid domainInfo. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalIdForDomain(domainInfo, (err: BusinessError, localId: number) => {
    if (err) {
      console.error(`getOsAccountLocalIdForDomain failed, code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountLocalIdForDomain successfully, localId: ' + localId);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForDomain exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountLocalIdForDomain

```TypeScript
getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<int>
```

Obtains the OS account ID based on the domain account information. This API uses a promise to return the result. This API can be called only by system applications.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<int>--><!--Device-AccountManager-getOsAccountLocalIdForDomain(domainInfo: DomainAccountInfo): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Domain account information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the ID of the OS account associated with the domain account. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Domain account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid domainInfo. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
try {
  accountManager.getOsAccountLocalIdForDomain(domainInfo).then((localId: number) => {
    console.info('getOsAccountLocalIdForDomain successfully, localId: ' + localId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalIdForDomain failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForDomain exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountLocalIdForSerialNumber

```TypeScript
getOsAccountLocalIdForSerialNumber(serialNumber: long, callback: AsyncCallback<int>): void
```

Obtains the OS account ID based on the SN. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountLocalIdForSerialNumber(serialNumber: long, callback: AsyncCallback<int>): void--><!--Device-AccountManager-getOsAccountLocalIdForSerialNumber(serialNumber: long, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| serialNumber | long | Yes | Account SN. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account ID obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | The account indicated by serialNumber does not exist. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid serialNumber. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getOsAccountLocalIdForSerialNumber

```TypeScript
getOsAccountLocalIdForSerialNumber(serialNumber: long): Promise<int>
```

Obtains the OS account ID based on the SN. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountLocalIdForSerialNumber(serialNumber: long): Promise<int>--><!--Device-AccountManager-getOsAccountLocalIdForSerialNumber(serialNumber: long): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| serialNumber | long | Yes | Account SN. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the OS account ID obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | The account indicated by serialNumber does not exist. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid serialNumber. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getOsAccountLocalIdForUid

```TypeScript
getOsAccountLocalIdForUid(uid: int, callback: AsyncCallback<int>): void
```

Obtains the OS account ID based on the process UID. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountLocalIdForUid(uid: int, callback: AsyncCallback<int>): void--><!--Device-AccountManager-getOsAccountLocalIdForUid(uid: int, callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | int | Yes | Process UID. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account ID obtained. Otherwise, **data** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid uid. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getOsAccountLocalIdForUid

```TypeScript
getOsAccountLocalIdForUid(uid: int): Promise<int>
```

Obtains the OS account ID based on the process UID. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountLocalIdForUid(uid: int): Promise<int>--><!--Device-AccountManager-getOsAccountLocalIdForUid(uid: int): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | int | Yes | Process UID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the OS account ID obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid uid. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getOsAccountLocalIdForUidSync

```TypeScript
getOsAccountLocalIdForUidSync(uid: int): int
```

Obtains the OS account ID based on the process UID. The API returns the result synchronously.

**Since:** 23

<!--Device-AccountManager-getOsAccountLocalIdForUidSync(uid: int): int--><!--Device-AccountManager-getOsAccountLocalIdForUidSync(uid: int): int-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | int | Yes | Process UID. |

**Return value:**

| Type | Description |
| --- | --- |
| int | OS account ID obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid uid. |

## getOsAccountLocalIdFromDomain

```TypeScript
getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the domain account information. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)(domainInfo: DomainAccountInfo, callback: AsyncCallback&lt;int&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void--><!--Device-AccountManager-getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Domain account information. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account ID obtained. Otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromDomain(domainInfo, (err: BusinessError, localId: number) => {
  if (err) {
    console.error(`getOsAccountLocalIdFromDomain failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOsAccountLocalIdFromDomain successfully, localId: ' + localId);
  }
});
```

## getOsAccountLocalIdFromDomain

```TypeScript
getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>
```

Obtains the OS account ID based on the domain account information. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForDomain](#getosaccountlocalidfordomain)(domainInfo: DomainAccountInfo)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>--><!--Device-AccountManager-getOsAccountLocalIdFromDomain(domainInfo: DomainAccountInfo): Promise<number>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domainInfo | [DomainAccountInfo](arkts-basicservices-osaccount-domainaccountinfo-i.md) | Yes | Domain account information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the ID of the OS account associated with the domain account. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let domainInfo: osAccount.DomainAccountInfo = {domain: 'testDomain', accountName: 'testAccountName'};
accountManager.getOsAccountLocalIdFromDomain(domainInfo).then((localId: number) => {
  console.info('getOsAccountLocalIdFromDomain successfully, localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountLocalIdFromDomain failed, code is ${err.code}, message is ${err.message}`);
});
```

## getOsAccountLocalIdFromProcess

```TypeScript
getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void
```

Obtains the ID of the OS account to which the current process belongs. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [getOsAccountLocalId](#getosaccountlocalid) > instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalId](#getosaccountlocalid)(callback: AsyncCallback&lt;int&gt;)

<!--Device-AccountManager-getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void--><!--Device-AccountManager-getOsAccountLocalIdFromProcess(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account ID obtained. Otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromProcess((err: BusinessError, localId: number) => {
  if (err) {
    console.error(`getOsAccountLocalIdFromProcess failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOsAccountLocalIdFromProcess id:: ' + localId);
  }
});
```

## getOsAccountLocalIdFromProcess

```TypeScript
getOsAccountLocalIdFromProcess(): Promise<number>
```

Obtains the ID of the OS account to which the current process belongs. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [getOsAccountLocalId](#getosaccountlocalid) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalId](#getosaccountlocalid)()

<!--Device-AccountManager-getOsAccountLocalIdFromProcess(): Promise<number>--><!--Device-AccountManager-getOsAccountLocalIdFromProcess(): Promise<number>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the OS account ID obtained. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountLocalIdFromProcess().then((localId: number) => {
  console.info('getOsAccountLocalIdFromProcess successfully, localId: ' + localId);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountLocalIdFromProcess failed, code is ${err.code}, message is ${err.message}`);
});
```

## getOsAccountLocalIdFromUid

```TypeScript
getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void
```

Obtains the OS account ID based on the process UID. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [getOsAccountLocalIdForUid](#getosaccountlocalidforuid) > instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)(uid: int, callback: AsyncCallback&lt;int&gt;)

<!--Device-AccountManager-getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void--><!--Device-AccountManager-getOsAccountLocalIdFromUid(uid: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | Process UID. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account ID obtained. Otherwise, **data** is an error object. |

## getOsAccountLocalIdFromUid

```TypeScript
getOsAccountLocalIdFromUid(uid: number): Promise<number>
```

Obtains the OS account ID based on the process UID. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [getOsAccountLocalIdForUid](#getosaccountlocalidforuid) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountLocalIdForUid](#getosaccountlocalidforuid)(uid: int)

<!--Device-AccountManager-getOsAccountLocalIdFromUid(uid: number): Promise<number>--><!--Device-AccountManager-getOsAccountLocalIdFromUid(uid: number): Promise<number>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | Process UID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the OS account ID obtained. |

## getOsAccountLocalIds

```TypeScript
getOsAccountLocalIds(): Promise<int[]>
```

Obtains the local IDs of all non-system-level OS accounts. Non-system-level OS accounts are visible to users and are usually used for operations such as login. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccountManager-getOsAccountLocalIds(): Promise<int[]>--><!--Device-AccountManager-getOsAccountLocalIds(): Promise<int[]>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int[]&gt; | Promise used to return the local IDs of all non-system-level OS accounts. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountLocalIds().then((localIds: number[]) => {
    console.info('getOsAccountLocalIds localIds: ' + localIds);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalIds failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIds exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountName

```TypeScript
getOsAccountName(): Promise<string>
```

Obtains the name of the OS account of the caller. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountName(): Promise<string>--><!--Device-AccountManager-getOsAccountName(): Promise<string>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the OS account name obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountName().then((name: string) => {
    console.info('getOsAccountName, name: ' + name);
  }).catch((err: BusinessError) => {
    console.error('getOsAccountName err: ' + err);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountName exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountNameByLocalId

```TypeScript
getOsAccountNameByLocalId(localId: int): Promise<string>
```

Obtains the name of an OS account based on its local ID. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccountManager-getOsAccountNameByLocalId(localId: int): Promise<string>--><!--Device-AccountManager-getOsAccountNameByLocalId(localId: int): Promise<string>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | int | Yes | Local ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the name of the target OS account. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300008](../../apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) | Restricted Account. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getOsAccountType

```TypeScript
getOsAccountType(callback: AsyncCallback<OsAccountType>): void
```

Obtains the type of the account to which the current process belongs. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountType(callback: AsyncCallback<OsAccountType>): void--><!--Device-AccountManager-getOsAccountType(callback: AsyncCallback<OsAccountType>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account type obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountType((err: BusinessError, accountType: osAccount.OsAccountType) => {
    if (err) {
      console.error(`getOsAccountType err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('getOsAccountType accountType: ' + accountType);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountType exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountType

```TypeScript
getOsAccountType(): Promise<OsAccountType>
```

Obtains the type of the account to which the current process belongs. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-getOsAccountType(): Promise<OsAccountType>--><!--Device-AccountManager-getOsAccountType(): Promise<OsAccountType>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; | Promise used to return the OS account type obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.getOsAccountType().then((accountType: osAccount.OsAccountType) => {
    console.info('getOsAccountType, accountType: ' + accountType);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountType err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountType exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountTypeFromProcess

```TypeScript
getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void
```

Obtains the type of the account to which the current process belongs. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [getOsAccountType](#getosaccounttype) > instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountType](#getosaccounttype)(callback: AsyncCallback&lt;OsAccountType&gt;)

<!--Device-AccountManager-getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void--><!--Device-AccountManager-getOsAccountTypeFromProcess(callback: AsyncCallback<OsAccountType>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account type obtained. Otherwise, **err** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountTypeFromProcess((err: BusinessError, accountType: osAccount.OsAccountType) => {
  if (err) {
    console.error(`getOsAccountTypeFromProcess err: code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('getOsAccountTypeFromProcess accountType: ' + accountType);
  }
});
```

## getOsAccountTypeFromProcess

```TypeScript
getOsAccountTypeFromProcess(): Promise<OsAccountType>
```

Obtains the type of the account to which the current process belongs. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [getOsAccountType](#getosaccounttype) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getOsAccountType](#getosaccounttype)()

<!--Device-AccountManager-getOsAccountTypeFromProcess(): Promise<OsAccountType>--><!--Device-AccountManager-getOsAccountTypeFromProcess(): Promise<OsAccountType>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OsAccountType](arkts-basicservices-osaccount-osaccounttype-e.md)&gt; | Promise used to return the OS account type obtained. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.getOsAccountTypeFromProcess().then((accountType: osAccount.OsAccountType) => {
  console.info('getOsAccountTypeFromProcess, accountType: ' + accountType);
}).catch((err: BusinessError) => {
  console.error(`getOsAccountTypeFromProcess err: code is ${err.code}, message is ${err.message}`);
});
```

## getSerialNumberByOsAccountLocalId

```TypeScript
getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void
```

Obtains the SN of an OS account based on the account ID. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)(localId: int, callback: AsyncCallback&lt;long&gt;)

<!--Device-AccountManager-getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void--><!--Device-AccountManager-getSerialNumberByOsAccountLocalId(localId: number, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the SN obtained. Otherwise, **err** is an error object. |

## getSerialNumberByOsAccountLocalId

```TypeScript
getSerialNumberByOsAccountLocalId(localId: number): Promise<number>
```

Obtains the SN of an OS account based on the account ID. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSerialNumberForOsAccountLocalId](#getserialnumberforosaccountlocalid)(localId: int)

<!--Device-AccountManager-getSerialNumberByOsAccountLocalId(localId: number): Promise<number>--><!--Device-AccountManager-getSerialNumberByOsAccountLocalId(localId: number): Promise<number>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the SN obtained. |

## getSerialNumberForOsAccountLocalId

```TypeScript
getSerialNumberForOsAccountLocalId(localId: int, callback: AsyncCallback<long>): void
```

Obtains the SN of an OS account based on the account ID. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AccountManager-getSerialNumberForOsAccountLocalId(localId: int, callback: AsyncCallback<long>): void--><!--Device-AccountManager-getSerialNumberForOsAccountLocalId(localId: int, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | int | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the SN obtained. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## getSerialNumberForOsAccountLocalId

```TypeScript
getSerialNumberForOsAccountLocalId(localId: int): Promise<long>
```

Obtains the SN of an OS account based on the account ID. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-getSerialNumberForOsAccountLocalId(localId: int): Promise<long>--><!--Device-AccountManager-getSerialNumberForOsAccountLocalId(localId: int): Promise<long>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | int | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the SN obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300003](../../apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) | Account not found. |
| [12300002](../../apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) | Invalid localId. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## isMultiOsAccountEnable

```TypeScript
isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void
```

Checks whether multiple OS accounts are supported. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [checkMultiOsAccountEnabled](#checkmultiosaccountenabled) > instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)(callback: AsyncCallback&lt;boolean&gt;)

<!--Device-AccountManager-isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-isMultiOsAccountEnable(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means multiple OS accounts are supported; the value **false** means the opposite. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isMultiOsAccountEnable((err: BusinessError, isEnabled: boolean) => {
  if (err) {
    console.error(`isMultiOsAccountEnable failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isMultiOsAccountEnable successfully, isEnabled: ' + isEnabled);
  }
});
```

## isMultiOsAccountEnable

```TypeScript
isMultiOsAccountEnable(): Promise<boolean>
```

Checks whether multiple OS accounts are supported. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [checkMultiOsAccountEnabled](#checkmultiosaccountenabled) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkMultiOsAccountEnabled](#checkmultiosaccountenabled)()

<!--Device-AccountManager-isMultiOsAccountEnable(): Promise<boolean>--><!--Device-AccountManager-isMultiOsAccountEnable(): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means multiple OS accounts are supported; the value **false** means the opposite. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isMultiOsAccountEnable().then((isEnabled: boolean) => {
  console.info('isMultiOsAccountEnable successfully, isEnabled: ' + isEnabled);
}).catch((err: BusinessError) => {
  console.error(`isMultiOsAccountEnable failed, code is ${err.code}, message is ${err.message}`);
});
```

## isOsAccountActived

```TypeScript
isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void
```

Checks whether an OS account is activated. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountActivated](#checkosaccountactivated)(localId: number, callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-isOsAccountActived(localId: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the account is activated; the value **false** means the opposite. |

## isOsAccountActived

```TypeScript
isOsAccountActived(localId: number): Promise<boolean>
```

Checks whether an OS account is activated. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountActivated](#checkosaccountactivated)(localId: number)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountActived(localId: number): Promise<boolean>--><!--Device-AccountManager-isOsAccountActived(localId: number): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the account is activated; the value **false** means the opposite. |

## isOsAccountConstraintEnable

```TypeScript
isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void
```

Checks whether the specified constraint is enabled for an OS account. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountConstraintEnabled](#checkosaccountconstraintenabled)(localId: number, constraint: string, callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-isOsAccountConstraintEnable(localId: number, constraint: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| constraint | string | Yes | [Constraint](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) to check. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

## isOsAccountConstraintEnable

```TypeScript
isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>
```

Checks whether the specified constraint is enabled for an OS account. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountConstraintEnabled](#checkosaccountconstraintenabled)(localId: number, constraint: string)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>--><!--Device-AccountManager-isOsAccountConstraintEnable(localId: number, constraint: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| constraint | string | Yes | [Constraint](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) to check. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

## isOsAccountConstraintEnabled

```TypeScript
isOsAccountConstraintEnabled(constraint: string): Promise<boolean>
```

Checks whether a constraint is enabled for this OS account. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-isOsAccountConstraintEnabled(constraint: string): Promise<boolean>--><!--Device-AccountManager-isOsAccountConstraintEnabled(constraint: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| constraint | string | Yes | [Constraint](arkts-basicservices-osaccount-osaccountinfo-i.md#constraints) to check. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the specified constraint is enabled; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

## isOsAccountUnlocked

```TypeScript
isOsAccountUnlocked(): Promise<boolean>
```

Checks whether this OS account is unlocked. This API uses a promise to return the result.

**Since:** 23

<!--Device-AccountManager-isOsAccountUnlocked(): Promise<boolean>--><!--Device-AccountManager-isOsAccountUnlocked(): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the OS account has been verified; the value **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.isOsAccountUnlocked().then((isVerified: boolean) => {
    console.info('isOsAccountUnlocked successfully, isVerified: ' + isVerified);
  }).catch((err: BusinessError) => {
    console.error(`isOsAccountUnlocked failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`isOsAccountUnlocked exception: code is ${err.code}, message is ${err.message}`);
}
```

## isOsAccountVerified

```TypeScript
isOsAccountVerified(callback: AsyncCallback<boolean>): void
```

Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [checkOsAccountVerified](#checkosaccountverified) > instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountVerified](#checkosaccountverified)(callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountVerified(callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-isOsAccountVerified(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the OS account has been verified; the value **false** means the opposite. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isOsAccountVerified((err: BusinessError, isVerified: boolean) => {
  if (err) {
    console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
  }
});
```

## isOsAccountVerified

```TypeScript
isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void
```

Checks whether an OS account has been verified. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountVerified](#checkosaccountverified)(localId: number, callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-isOsAccountVerified(localId: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | Yes | ID of the target OS account. |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the OS account has been verified; the value **false** means the opposite. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
let localId: number = 100;
accountManager.isOsAccountVerified(localId, (err: BusinessError, isVerified: boolean) => {
  if (err) {
    console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
  }
});
```

## isOsAccountVerified

```TypeScript
isOsAccountVerified(localId?: number): Promise<boolean>
```

Checks whether an OS account has been verified. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountVerified](#checkosaccountverified)(localId: number)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS or ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-AccountManager-isOsAccountVerified(localId?: number): Promise<boolean>--><!--Device-AccountManager-isOsAccountVerified(localId?: number): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| localId | number | No | ID of the target OS account. If this parameter is not specified, this API checks whether the current OS account has been verified. The default value is **-1**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the OS account has been verified; the value **false** means the opposite. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isOsAccountVerified().then((isVerified: boolean) => {
  console.info('isOsAccountVerified successfully, isVerified: ' + isVerified);
}).catch((err: BusinessError) => {
  console.error(`isOsAccountVerified failed, code is ${err.code}, message is ${err.message}`);
});
```

## isTestOsAccount

```TypeScript
isTestOsAccount(callback: AsyncCallback<boolean>): void
```

Checks whether this OS account is a test account. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [checkOsAccountTestable](#checkosaccounttestable) > instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountTestable](#checkosaccounttestable)(callback: AsyncCallback&lt;boolean&gt;)

<!--Device-AccountManager-isTestOsAccount(callback: AsyncCallback<boolean>): void--><!--Device-AccountManager-isTestOsAccount(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means the account is a test account; the value **false** means the opposite. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.isTestOsAccount((err: BusinessError, isTestable: boolean) => {
  if (err) {
    console.error(`isTestOsAccount failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('isTestOsAccount successfully, isTestable: ' + isTestable);
  }
});
```

## isTestOsAccount

```TypeScript
isTestOsAccount(): Promise<boolean>
```

Checks whether this OS account is a test account. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. You are advised to use > [checkOsAccountTestable](#checkosaccounttestable) instead.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [checkOsAccountTestable](#checkosaccounttestable)()

<!--Device-AccountManager-isTestOsAccount(): Promise<boolean>--><!--Device-AccountManager-isTestOsAccount(): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means the account is a test account; the value **false** means the opposite. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  accountManager.isTestOsAccount().then((isTestable: boolean) => {
    console.info('isTestOsAccount successfully, isTestable: ' + isTestable);
  }).catch((err: BusinessError) => {
    console.error(`isTestOsAccount failed, code is ${err.code}, message is ${err.message}`);
});
```

## queryActivatedOsAccountIds

```TypeScript
queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void
```

Obtains information about all activated OS accounts. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids) > instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)(callback: AsyncCallback&lt;Array&lt;int&gt;&gt;)

<!--Device-AccountManager-queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void--><!--Device-AccountManager-queryActivatedOsAccountIds(callback: AsyncCallback<Array<number>>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is a list of activated OS accounts. Otherwise, **data** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryActivatedOsAccountIds((err: BusinessError, idArray: number[]) => {
  if (err) {
    console.error(`queryActivatedOsAccountIds code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('queryActivatedOsAccountIds idArray length:' + idArray.length);
    for (let i = 0; i < idArray.length; i++) {
      console.info('activated os account id: ' + idArray[i]);
    }
  }
});
```

## queryActivatedOsAccountIds

```TypeScript
queryActivatedOsAccountIds(): Promise<Array<number>>
```

Obtains information about all activated OS accounts. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 8 and deprecated since API version 9. You are advised to use > [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids) instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getActivatedOsAccountLocalIds](#getactivatedosaccountlocalids)()

<!--Device-AccountManager-queryActivatedOsAccountIds(): Promise<Array<number>>--><!--Device-AccountManager-queryActivatedOsAccountIds(): Promise<Array<number>>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;number&gt;&gt; | Promise used to return the information about all activated OS accounts. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryActivatedOsAccountIds().then((idArray: number[]) => {
  console.info('queryActivatedOsAccountIds, idArray: ' + idArray);
}).catch((err: BusinessError) => {
  console.error(`queryActivatedOsAccountIds err: code is ${err.code}, message is ${err.message}`);
});
```

## queryCurrentOsAccount

```TypeScript
queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void
```

Obtains information about the OS account to which the current process belongs. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCurrentOsAccount](#getcurrentosaccount)(callback: AsyncCallback&lt;OsAccountInfo&gt;)

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void--><!--Device-AccountManager-queryCurrentOsAccount(callback: AsyncCallback<OsAccountInfo>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the OS account information obtained. Otherwise, **data** is an error object. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryCurrentOsAccount((err: BusinessError, curAccountInfo: osAccount.OsAccountInfo)=>{
  if (err) {
    console.error(`queryCurrentOsAccount code is ${err.code}, message is ${err.message}`);
  } else {
    console.info('queryCurrentOsAccount curAccountInfo:' + JSON.stringify(curAccountInfo));
  }
});
```

## queryCurrentOsAccount

```TypeScript
queryCurrentOsAccount(): Promise<OsAccountInfo>
```

Obtains information about the OS account to which the current process belongs. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 7 and deprecated since API version 9. The substitute API is available > only to system applications.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCurrentOsAccount](#getcurrentosaccount)()

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-queryCurrentOsAccount(): Promise<OsAccountInfo>--><!--Device-AccountManager-queryCurrentOsAccount(): Promise<OsAccountInfo>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OsAccountInfo](arkts-basicservices-osaccount-osaccountinfo-i.md)&gt; | Promise used to return the OS account information obtained. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
accountManager.queryCurrentOsAccount().then((accountInfo: osAccount.OsAccountInfo) => {
  console.info('queryCurrentOsAccount, accountInfo: ' + JSON.stringify(accountInfo));
}).catch((err: BusinessError) => {
  console.error(`queryCurrentOsAccount err: code is ${err.code}, message is ${err.message}`);
});
```

## queryDistributedVirtualDeviceId

```TypeScript
queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void
```

Queries the ID of a distributed virtual device. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void--><!--Device-AccountManager-queryDistributedVirtualDeviceId(callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **null** and **data** is the distributed virtual device ID obtained. Otherwise, **data** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryDistributedVirtualDeviceId((err: BusinessError, virtualID: string) => {
    if (err) {
      console.error(`queryDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
    } else {
      console.info('queryDistributedVirtualDeviceId virtualID: ' + virtualID);
    }
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryDistributedVirtualDeviceId exception: code is ${err.code}, message is ${err.message}`);
}
```

## queryDistributedVirtualDeviceId

```TypeScript
queryDistributedVirtualDeviceId(): Promise<string>
```

Queries the ID of this distributed virtual device. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC or ohos.permission.MANAGE_LOCAL_ACCOUNTS

<!--Device-AccountManager-queryDistributedVirtualDeviceId(): Promise<string>--><!--Device-AccountManager-queryDistributedVirtualDeviceId(): Promise<string>-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the distributed virtual device ID obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [12300001](../../apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) | The system service works abnormally. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
try {
  accountManager.queryDistributedVirtualDeviceId().then((virtualID: string) => {
    console.info('queryDistributedVirtualDeviceId, virtualID: ' + virtualID);
  }).catch((err: BusinessError) => {
    console.error(`queryDistributedVirtualDeviceId err: code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`queryDistributedVirtualDeviceId exception: code is ${err.code}, message is ${err.message}`);
}
```

