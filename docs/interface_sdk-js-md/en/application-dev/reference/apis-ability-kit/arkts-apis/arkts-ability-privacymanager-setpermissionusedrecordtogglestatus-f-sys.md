# setPermissionUsedRecordToggleStatus (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## setPermissionUsedRecordToggleStatus

```TypeScript
function setPermissionUsedRecordToggleStatus(status: boolean): Promise<void>
```

Sets whether to record the permission usage of this user. Sets the permission usage record switch for this user. This API uses a promise to return the result.When **status** is **true**, the [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md) API can add usage records normally; when **status** is **false**, the [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md) API does not generate permission usage records, and deletes the current user's historical records.

**Since:** 18

**Required permissions:** ohos.permission.PERMISSION_RECORD_TOGGLE

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |


## setPermissionUsedRecordToggleStatus

```TypeScript
function setPermissionUsedRecordToggleStatus(status: boolean, subProfileId: number): Promise<void>
```

Sets whether permission usage records are collected for a specified sub-profile. A system application can call this API to set the permission usage record switch status for the specified sub-profile. This API uses a promise to return the result.When **status** is **true**, the [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md) API can add usage records normally; when **status** is **false**, the [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md) API does not generate permission usage records, and deletes the historical records of the specified sub-profile.

**Since:** 26.1.0

**Required permissions:** ohos.permission.PERMISSION_RECORD_TOGGLE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| status | boolean | Yes |
| [subProfileId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofileeventdata-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [12100006](../errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
