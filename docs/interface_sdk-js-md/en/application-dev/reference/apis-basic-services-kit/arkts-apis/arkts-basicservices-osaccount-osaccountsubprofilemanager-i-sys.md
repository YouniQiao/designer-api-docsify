# OsAccountSubProfileManager (System API)

Defines an OS account sub-profile manager.

**Since:** 26.0.0

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## createOsAccountSubProfile

```TypeScript
createOsAccountSubProfile(osAccountLocalId: number): Promise<OsAccountSubProfile>
```

Creates an OS account sub-profile. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300008](../errorcode-account.md#12300008-restricted-account) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300402](../errorcode-account.md#12300402-number-of-os-account-sub-profiles-has-reached-the-upper-limit) |

## deleteOsAccountSubProfile

```TypeScript
deleteOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<void>
```

Deletes an OS account sub-profile. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) |
| [12300403](../errorcode-account.md#12300403-restricted-os-account-sub-profile) |
| [12300404](../errorcode-account.md#12300404-foreground-sub-profile-of-the-os-account-cannot-be-deleted) |

## getOsAccountForegroundSubProfileId

```TypeScript
getOsAccountForegroundSubProfileId(): Promise<number>
```

Obtains the foreground sub-profile ID of the OS account of the caller. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) |

## getOsAccountForegroundSubProfileId

```TypeScript
getOsAccountForegroundSubProfileId(osAccountLocalId: number): Promise<number>
```

Obtains the foreground sub-profile ID of the specified OS account. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) |

## getOsAccountLocalIdForSubProfile

```TypeScript
getOsAccountLocalIdForSubProfile(subProfileId: number): Promise<number>
```

Obtains the local ID of the OS account of a sub-profile. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) |

## getOsAccountSubProfile

```TypeScript
getOsAccountSubProfile(subProfileId: number): Promise<OsAccountSubProfile>
```

Obtains the sub-profile of the OS account of the caller. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) |

## getOsAccountSubProfile

```TypeScript
getOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<OsAccountSubProfile>
```

Obtains the sub-profile of the specified OS account. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) |

## getOsAccountSubProfileIds

```TypeScript
getOsAccountSubProfileIds(): Promise<number[]>
```

Obtains the sub-profile IDs of the OS account of the caller. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number[] & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## getOsAccountSubProfileIds

```TypeScript
getOsAccountSubProfileIds(osAccountLocalId: number): Promise<number[]>
```

Obtains the sub-profile IDs of the specified OS account. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300003](../errorcode-account.md#12300003-account-not-found) |

## offOsAccountSubProfileEvent

```TypeScript
offOsAccountSubProfileEvent(callback?: Callback<OsAccountSubProfileEventData>): void
```

Unsubscribes from OS account sub-profile events. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[OsAccountSubProfileEventData](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |

## onOsAccountSubProfileEvent

```TypeScript
onOsAccountSubProfileEvent(
      events: OsAccountSubProfileEvent[],
      callback: Callback<OsAccountSubProfileEventData>): void
```

Subscribes to OS account sub-profile events. This API uses an asynchronous callback to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

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
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) |

## switchOsAccountSubProfile

```TypeScript
switchOsAccountSubProfile(osAccountLocalId: number, subProfileId: number): Promise<void>
```

Switches to an OS account sub-profile. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) |
| [12300403](../errorcode-account.md#12300403-restricted-os-account-sub-profile) |
| [12300405](../errorcode-account.md#12300405-foreground-sub-profile-with-a-logged-in-distributed-account-cannot-be-directly-switched-to-the-background) |
