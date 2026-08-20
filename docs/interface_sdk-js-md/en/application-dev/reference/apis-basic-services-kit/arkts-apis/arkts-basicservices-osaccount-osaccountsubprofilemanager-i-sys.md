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
createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>
```

Creates an OS account sub-profile.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-createOsAccountSubProfile(osAccountLocalId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | int | Yes | Local ID of the target OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; | Promise used to return the created sub-profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300003](../errorcode-account.md#12300003-account-not-found) | The OS account not found. |
| [12300008](../errorcode-account.md#12300008-restricted-account) | Restricted OS account. |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) | Service busy. Possible causes: The target OS account is being operated. |
| [12300402](../errorcode-account.md#12300402-number-of-os-account-sub-profiles-has-reached-the-upper-limit) | The number of sub-profiles under the OS account has reached limit. |

## deleteOsAccountSubProfile

```TypeScript
deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>
```

Deletes an OS account sub-profile.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>--><!--Device-OsAccountSubProfileManager-deleteOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | int | Yes | Local ID of the target OS account. |
| subProfileId | int | Yes | ID of the sub-profile. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) | Service busy. Possible causes: The OS account or sub-profile is being operated. |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) | Sub-profile not found. |
| [12300403](../errorcode-account.md#12300403-restricted-os-account-sub-profile) | Restricted sub-profile cannot be deleted. |
| [12300404](../errorcode-account.md#12300404-foreground-sub-profile-of-the-os-account-cannot-be-deleted) | The foreground sub-profile cannot be deleted. |

## getOsAccountForegroundSubProfileId

```TypeScript
getOsAccountForegroundSubProfileId(): Promise<int>
```

Gets the foreground sub-profile ID of the OS account to which the caller belongs.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the id of the OS account foreground sub-profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) | Sub-profile not found. |

## getOsAccountForegroundSubProfileId

```TypeScript
getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>
```

Gets the foreground sub-profile ID of a specified OS account.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountForegroundSubProfileId(osAccountLocalId: int): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | int | Yes | Local ID of the OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the id of the OS account foreground sub-profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300003](../errorcode-account.md#12300003-account-not-found) | OS account not found. |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) | The foreground sub-profile not found. |

## getOsAccountLocalIdForSubProfile

```TypeScript
getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>
```

Obtains the local ID of the OS account to which a sub-profile belongs.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>--><!--Device-OsAccountSubProfileManager-getOsAccountLocalIdForSubProfile(subProfileId: int): Promise<int>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subProfileId | int | Yes | ID of the sub-profile. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the local ID of the OS account to which a sub-profile belongs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) | Sub-profile not found. |

## getOsAccountSubProfile

```TypeScript
getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>
```

Gets the sub-profile object information of the OS account to which the caller belongs.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(subProfileId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subProfileId | int | Yes | ID of the sub-profile. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; | Promise used to return the sub-profile object information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) | Sub-profile not found. |

## getOsAccountSubProfile

```TypeScript
getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>
```

Gets the sub-profile object information of the specified OS account.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNTS and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<OsAccountSubProfile>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | int | Yes | Local ID of the OS account. |
| subProfileId | int | Yes | ID of the sub-profile. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[OsAccountSubProfile](arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md)&gt; | Promise used to return the sub-profile object information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) | Sub-profile not found. |

## getOsAccountSubProfileIds

```TypeScript
getOsAccountSubProfileIds(): Promise<int[]>
```

Gets the ID list of sub-profile of the OS account to which the caller belongs.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(): Promise<int[]>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(): Promise<int[]>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int[]&gt; | Promise used to return the ID list of sub-profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |

## getOsAccountSubProfileIds

```TypeScript
getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>
```

Gets the ID list of sub-profile of a specified OS account.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_LOCAL_ACCOUNT_IDENTIFIERS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>--><!--Device-OsAccountSubProfileManager-getOsAccountSubProfileIds(osAccountLocalId: int): Promise<int[]>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | int | Yes | Local ID of the OS account. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int[]&gt; | Promise used to return the ID list of sub-profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300003](../errorcode-account.md#12300003-account-not-found) | OS account not found. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[OsAccountSubProfileEventData](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md)&gt; | No | Callback to be unsubscribed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| events | [OsAccountSubProfileEvent](arkts-basicservices-osaccount-osaccountsubprofileevent-e-sys.md)[] | Yes | Array of events to be subscribed |
| callback | [Callback](arkts-basicservices-callback-t.md)&lt;[OsAccountSubProfileEventData](arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md)&gt; | Yes | Callback invoked when an event occurs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300002](../errorcode-account.md#12300002-invalid-parameter) | Invalid event. |

## switchOsAccountSubProfile

```TypeScript
switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>
```

Switches to an OS account sub-profile.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-OsAccountSubProfileManager-switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>--><!--Device-OsAccountSubProfileManager-switchOsAccountSubProfile(osAccountLocalId: int, subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| osAccountLocalId | int | Yes | Local ID of the OS account. |
| subProfileId | int | Yes | ID of the sub-profile. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [12300001](../errorcode-account.md#12300001-system-service-abnormal) | System service exception. |
| [12300010](../errorcode-account.md#12300010-account-service-not-respond) | Service busy. Possible causes: The OS account or sub-profile is being operated. |
| [12300401](../errorcode-account.md#12300401-os-account-sub-profile-not-found) | Sub-profile not found. |
| [12300403](../errorcode-account.md#12300403-restricted-os-account-sub-profile) | Restricted sub-profile cannot be switched to foreground. |
| [12300405](../errorcode-account.md#12300405-foreground-sub-profile-with-a-logged-in-distributed-account-cannot-be-directly-switched-to-the-background) | The foreground sub-profile bound with a logged-in distributed account cannot be directly switched to background. |

