# setPermissionUsedRecordToggleStatus (System API)

## Modules to Import

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
```

## setPermissionUsedRecordToggleStatus

```TypeScript
function setPermissionUsedRecordToggleStatus(status: boolean): Promise<void>
```

Sets whether to record the permission usage of this user. Sets the permission usage record switch for this user.This API uses a promise to return the result.

When **status** is **true**, the [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord) API can add usage records normally; when **status** is **false**, the  
[addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord) API does not generate permission usage records, and deletes the current user's historical records.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PERMISSION_RECORD_TOGGLE

<!--Device-privacyManager-function setPermissionUsedRecordToggleStatus(status: boolean): Promise<void>--><!--Device-privacyManager-function setPermissionUsedRecordToggleStatus(status: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| status | boolean | Yes | Setting of the permission usage record switch. The value **true** means the switch is toggled on; the value **false** means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [12100009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100009-internal-service-error) | Common inner error. Possible causes: 1. Database error. 2. Failed to query all applications under the user. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_RECORD_TOGGLE". |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | Operation not allowed. The toggle status of the specified permission has already been set by [setPermissionUsedRecordToggleStatus](#setPermissionUsedRecordToggleStatus-1).<br>**Applicable version:** 26.1.0 and later |
| [12100007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

privacyManager.setPermissionUsedRecordToggleStatus(true).then(() => {
  console.info('setPermissionUsedRecordToggleStatus success');
}).catch((err: BusinessError) => {
  console.error(`setPermissionUsedRecordToggleStatus fail, code: ${err.code}, message: ${err.message}`);
});
```


## setPermissionUsedRecordToggleStatus

```TypeScript
function setPermissionUsedRecordToggleStatus(status: boolean, subProfileId: int): Promise<void>
```

Sets whether permission usage records are collected for a specified sub-profile. A system application can call this API to set the permission usage record switch status for the specified sub-profile. This API uses a promise to return the result.

When **status** is **true**, the [addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord) API can add usage records normally; when **status** is **false**, the  
[addPermissionUsedRecord](arkts-ability-privacymanager-addpermissionusedrecord-f-sys.md#addPermissionUsedRecord) API does not generate permission usage records, and deletes the historical records of the specified sub-profile.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.PERMISSION_RECORD_TOGGLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-privacyManager-function setPermissionUsedRecordToggleStatus(status: boolean, subProfileId: int): Promise<void>--><!--Device-privacyManager-function setPermissionUsedRecordToggleStatus(status: boolean, subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| status | boolean | Yes | Setting of the permission usage record switch. The value **true** means the switch is toggled on; the value **false** means the opposite. |
| subProfileId | int | Yes | ID of the sub-profile. It can be obtained from [OsAccountSubProfile.id](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md#id). &lt;br&gt;The value should be an integer. Value constraint: This parameter must be an integer greater than 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [12100009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100009-internal-service-error) | Common inner error. Possible causes: 1. Database error. 2. Failed to query all applications under the user. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_RECORD_TOGGLE". |
| [12100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100001-invalid-parameters) | Invalid parameter. The specified subProfileId does not exist for the current user. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system app. Interface caller is not a system app. |
| [12100006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100006-permission-granting-or-revocation-not-supported) | Operation not allowed. The toggle status of the specified permission has already been set by [setPermissionUsedRecordToggleStatus](#setPermissionUsedRecordToggleStatus). |
| [12100007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-access-token.md#12100007-system-service-not-working-properly) | Service exception. |

