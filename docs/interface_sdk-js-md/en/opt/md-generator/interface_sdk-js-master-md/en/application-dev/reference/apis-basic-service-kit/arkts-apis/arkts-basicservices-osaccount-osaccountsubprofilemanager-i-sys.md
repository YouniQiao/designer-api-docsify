# OsAccountSubProfileManager (System API)

Defines the OS account sub-profile manager class.

**Since:** 26.0.0

<!--Device-osAccount-interface OsAccountSubProfileManager--><!--Device-osAccount-interface OsAccountSubProfileManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## createOsAccountSubProfile

```TypeScript
createOsAccountSubProfile(osAccountLocalId: number): Promise<OsAccountSubProfile>
```

Creates an OS account sub-profile.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| osAccountLocalId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300008](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300008-restricted-account) |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [12300402](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300402-number-of-os-account-subprofiles-has-reached-the-upper-limit) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Create an OS account sub-profile whose ID is 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
try {
  subProfileManager.createOsAccountSubProfile(osAccountLocalId).then((subProfile: osAccount.OsAccountSubProfile) => {
    console.info('createOsAccountSubProfile successfully, subProfileId: ' + subProfile.id);
  }).catch((err: BusinessError) => {
    console.error(`createOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`createOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## deleteOsAccountSubProfile

```TypeScript
deleteOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<void>
```

Deletes an OS account sub-profile.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>--><!--Device-OsAccountSubProfileManager-deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| osAccountLocalId | number | Yes |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300403](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300403-restricted-os-account-subprofile) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300401-os-account-subprofile-not-found) |
| [12300404](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300404-foreground-subprofile-of-the-os-account-cannot-be-deleted) |

## Examples

Delete the sub-profile whose ID is 100001 from OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
let subProfileId: number = 100001;
try {
  subProfileManager.deleteOsAccountSubProfile(osAccountLocalId, subProfileId).then(() => {
    console.info('deleteOsAccountSubProfile successfully');
  }).catch((err: BusinessError) => {
    console.error(`deleteOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`deleteOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountForegroundSubProfileId

```TypeScript
getOsAccountForegroundSubProfileId(): Promise<number>
```

Gets the foreground sub-profile ID of the OS account to which the caller belongs.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(): Promise<int>-End-->

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
| [12300401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300401-os-account-subprofile-not-found) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
try {
  subProfileManager.getOsAccountForegroundSubProfileId().then((subProfileId: number) => {
    console.info('getOsAccountForegroundSubProfileId successfully, subProfileId: ' + subProfileId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountForegroundSubProfileId failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountForegroundSubProfileId exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountForegroundSubProfileId

```TypeScript
getOsAccountForegroundSubProfileId(osAccountLocalId: number): Promise<number>
```

Gets the foreground sub-profile ID of a specified OS account.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| osAccountLocalId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300401-os-account-subprofile-not-found) |

## Examples

Obtain the foreground sub-profile ID of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
try {
  subProfileManager.getOsAccountForegroundSubProfileId(osAccountLocalId).then((subProfileId: number) => {
    console.info('getOsAccountForegroundSubProfileId successfully, subProfileId: ' + subProfileId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountForegroundSubProfileId failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountForegroundSubProfileId exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountLocalIdForSubProfile

```TypeScript
getOsAccountLocalIdForSubProfile(subProfileId: number): Promise<number>
```

Obtains the local ID of the OS account to which a sub-profile belongs.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300401-os-account-subprofile-not-found) |

## Examples

Obtains the local ID of the OS account of the sub-profile whose ID is 100001.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let subProfileId: number = 100001;
try {
  subProfileManager.getOsAccountLocalIdForSubProfile(subProfileId).then((osAccountLocalId: number) => {
    console.info('getOsAccountLocalIdForSubProfile successfully, osAccountLocalId: ' + osAccountLocalId);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountLocalIdForSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountLocalIdForSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountSubProfile

```TypeScript
getOsAccountSubProfile(subProfileId: number): Promise<OsAccountSubProfile>
```

Gets the sub-profile object information of the OS account to which the caller belongs.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300401-os-account-subprofile-not-found) |

## Examples

Obtains the sub-profile whose ID is 100001.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let subProfileId: number = 100001;
try {
  subProfileManager.getOsAccountSubProfile(subProfileId).then((subProfile: osAccount.OsAccountSubProfile) => {
    console.info('getOsAccountSubProfile successfully, subProfile: ' + JSON.stringify(subProfile));
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountSubProfile

```TypeScript
getOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<OsAccountSubProfile>
```

Gets the sub-profile object information of the specified OS account.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| osAccountLocalId | number | Yes |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300401-os-account-subprofile-not-found) |

## Examples

Obtain the sub-profile whose ID is 100001 of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
let subProfileId: number = 100001;
try {
  subProfileManager.getOsAccountSubProfile(osAccountLocalId, subProfileId).then((subProfile: osAccount.OsAccountSubProfile) => {
    console.info('getOsAccountSubProfile successfully, subProfile: ' + JSON.stringify(subProfile));
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountSubProfileIds

```TypeScript
getOsAccountSubProfileIds(): Promise<number[]>
```

Gets the ID list of sub-profile of the OS account to which the caller belongs.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(): Promise<int[]>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(): Promise<int[]>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
try {
  subProfileManager.getOsAccountSubProfileIds().then((subProfileIds: number[]) => {
    console.info('getOsAccountSubProfileIds successfully, subProfileIds: ' + subProfileIds);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountSubProfileIds failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountSubProfileIds exception: code is ${err.code}, message is ${err.message}`);
}
```

## getOsAccountSubProfileIds

```TypeScript
getOsAccountSubProfileIds(osAccountLocalId: number): Promise<number[]>
```

Gets the ID list of sub-profile of a specified OS account.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| osAccountLocalId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300003-account-not-found) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Obtain the sub-profile IDs of OS account 100.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
try {
  subProfileManager.getOsAccountSubProfileIds(osAccountLocalId).then((subProfileIds: number[]) => {
    console.info('getOsAccountSubProfileIds successfully, subProfileIds: ' + subProfileIds);
  }).catch((err: BusinessError) => {
    console.error(`getOsAccountSubProfileIds failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`getOsAccountSubProfileIds exception: code is ${err.code}, message is ${err.message}`);
}
```

## offOsAccountSubProfileEvent

```TypeScript
offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void
```

Unsubscribes from OS account sub-profile events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void--><!--Device-OsAccountSubProfileManager-offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSubProfileEventData](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
try {
  subProfileManager.offOsAccountSubProfileEvent();
} catch (e) {
  const err = e as BusinessError;
  console.error(`offOsAccountSubProfileEvent failed, code is ${err.code}, message is ${err.message}`);
}
```

## onOsAccountSubProfileEvent

```TypeScript
onOsAccountSubProfileEvent(
      events: OsAccountSubProfileEvent[],
      callback: Callback<OsAccountSubProfileEventData>): void
```

Subscribes to OS account sub-profile events.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-onOsAccountSubProfileEvent(      events: OsAccountSubProfileEvent[],      callback: Callback<OsAccountSubProfileEventData>): void--><!--Device-OsAccountSubProfileManager-onOsAccountSubProfileEvent(      events: OsAccountSubProfileEvent[],      callback: Callback<OsAccountSubProfileEventData>): void-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| events | [OsAccountSubProfileEvent](arkts-basicservices-osaccount-osaccountsubprofileevent-e-sys.md)[] | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSubProfileEventData](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12300002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300002-invalid-parameter) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |

## Examples

Subscribe to an OS account sub-profile creation event.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let events: osAccount.OsAccountSubProfileEvent[] = [osAccount.OsAccountSubProfileEvent.CREATED];
try {
  subProfileManager.onOsAccountSubProfileEvent(events, (data: osAccount.OsAccountSubProfileEventData) => {
    console.info('onOsAccountSubProfileEvent, event: ' + data.event + ', localId: ' + data.osAccountLocalId);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`onOsAccountSubProfileEvent failed, code is ${err.code}, message is ${err.message}`);
}
```

## switchOsAccountSubProfile

```TypeScript
switchOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<void>
```

Switches to an OS account sub-profile.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>--><!--Device-OsAccountSubProfileManager-switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| osAccountLocalId | number | Yes |
| [subProfileId](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12300010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300010-account-service-not-respond) |
| [12300403](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300403-restricted-os-account-subprofile) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300401-os-account-subprofile-not-found) |
| [12300405](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-account.md#12300405-foreground-subprofile-with-a-loggedin-distributed-account-cannot-be-directly-switched-to-the-background) |

## Examples

Switch from the current sub-profile of OS account 100 to the sub-profile whose ID is 100001.

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
let osAccountLocalId: number = 100;
let subProfileId: number = 100001;
try {
  subProfileManager.switchOsAccountSubProfile(osAccountLocalId, subProfileId).then(() => {
    console.info('switchOsAccountSubProfile successfully');
  }).catch((err: BusinessError) => {
    console.error(`switchOsAccountSubProfile failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`switchOsAccountSubProfile exception: code is ${err.code}, message is ${err.message}`);
}
```
