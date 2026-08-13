# addPermissionUsedRecord (System API)

## Modules to Import

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
```

## addPermissionUsedRecord

```TypeScript
function addPermissionUsedRecord(
    tokenID: number,
    permissionName: Permissions,
    successCount: number,
    failCount: number,
    options?: AddPermissionUsedRecordOptions
  ): Promise<void>
```

When an application protected by a permission is called by another service or application, this API can be used to add a permission usage record. It is recommended to call this API after accessing a sensitive permission, so that the system records the corresponding sensitive permission access event. This API uses a promise to return the result. The permission usage record includes the application identity of the caller, the name of the application permission, and the number of successful and failed accesses to this application by the caller. > **NOTE：**> The permission usage record is controlled by the toggle status set by [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus-(System-API)). When the toggle is off, calling this API will not generate a permission usage record.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    options?: AddPermissionUsedRecordOptions  ): Promise<void>--><!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    options?: AddPermissionUsedRecordOptions  ): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| successCount | number | Yes |
| failCount | number | Yes |
| options | [AddPermissionUsedRecordOptions](arkts-ability-privacymanager-addpermissionusedrecordoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // Obtained from the accessTokenId field of ApplicationInfo in the BundleInfo of the application.
// Add permission usage record
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0).then(() => {
  console.info('addPermissionUsedRecord success');
}).catch((err: BusinessError): void => {
  console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
});
// with options param
let options: privacyManager.AddPermissionUsedRecordOptions = {
  usedType: privacyManager.PermissionUsedType.PICKER_TYPE,
  enhancedIdentity: 'test'
};
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0, options).then(() => {
  console.info('addPermissionUsedRecord success');
}).catch((err: BusinessError): void => {
  console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
});
```


## addPermissionUsedRecord

```TypeScript
function addPermissionUsedRecord(
    tokenID: number,
    permissionName: Permissions,
    successCount: number,
    failCount: number,
    callback: AsyncCallback<void>
  ): void
```

When an application protected by a permission is called by another service or application, this API can be used to add a permission usage record. It is recommended to call this API after accessing a sensitive permission, so that the system records the corresponding sensitive permission access event. This API uses an asynchronous callback to return the result. The permission usage record includes the application identity of the caller, the name of the application permission used, and the number of successful and failed accesses to this application by the caller. The permission usage record is controlled by the toggle status set by [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setPermissionUsedRecordToggleStatus-(System-API)). When the toggle is off, calling this API will not generate a permission usage record.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    callback: AsyncCallback<void>  ): void--><!--Device-privacyManager-function addPermissionUsedRecord(    tokenID: int,    permissionName: Permissions,    successCount: int,    failCount: int,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tokenID | number | Yes |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes |
| successCount | number | Yes |
| failCount | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-out-of-memory) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12100009](../errorcode-access-token.md#12100009-internal-service-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12100001](../errorcode-access-token.md#12100001-invalid-parameters) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [12100002](../errorcode-access-token.md#12100002-tokenid-not-exist) |
| [12100003](../errorcode-access-token.md#12100003-permission-not-exist) |
| [12100007](../errorcode-access-token.md#12100007-system-service-not-working-properly) |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // Obtained from the accessTokenId field of ApplicationInfo in the BundleInfo of the application.
// Add permission usage record
privacyManager.addPermissionUsedRecord(tokenID, 'ohos.permission.READ_AUDIO', 1, 0, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`addPermissionUsedRecord fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('addPermissionUsedRecord success');
  }
});
```
