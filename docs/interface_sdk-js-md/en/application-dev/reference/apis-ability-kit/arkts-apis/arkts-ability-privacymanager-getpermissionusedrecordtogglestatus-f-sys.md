# getPermissionUsedRecordToggleStatus (System API)

## Modules to Import

```TypeScript
import { privacyManager } from 'kits/@kit.AbilityKit';
```

## getPermissionUsedRecordToggleStatus

```TypeScript
function getPermissionUsedRecordToggleStatus(): Promise<boolean>
```

系统应用调用此接口，可以获取当前用户的权限使用记录开关状态，例如在权限管理界面展示当前开关设置状态。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function getPermissionUsedRecordToggleStatus(): Promise<boolean>--><!--Device-privacyManager-function getPermissionUsedRecordToggleStatus(): Promise<boolean>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回true，表示当前用户的开关状态值为开启。返回false，表示当前用户的开关状态值为关闭。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| 202 | Not system app. Interface caller is not a system app. |
| 12100004 | This API must be used together with [setPermissionUsedRecordToggleStatus](arkts-ability-privacymanager-setpermissionusedrecordtogglestatus-f-sys.md#setpermissionusedrecordtogglestatus).<br>**Applicable version:** 26.1.0 and later |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Query permission usage record switch status
privacyManager.getPermissionUsedRecordToggleStatus().then((status) => {
  console.info('getPermissionUsedRecordToggleStatus success');
  if (status == true) {
    console.info('get status is TRUE');
  } else {
    console.info('get status is FALSE');
  }
}).catch((err: BusinessError): void => {
  console.error(`getPermissionUsedRecordToggleStatus fail, code: ${err.code}, message: ${err.message}`);
});
```


## getPermissionUsedRecordToggleStatus

```TypeScript
function getPermissionUsedRecordToggleStatus(subProfileId: int): Promise<boolean>
```

系统应用调用此接口，可以获取指定子身份资料的权限使用记录开关状态，例如在权限管理界面展示当前开关设置状态。使用Promise异步回调。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.PERMISSION_USED_STATS

**Model restriction:** This API can be used only in the stage model.

<!--Device-privacyManager-function getPermissionUsedRecordToggleStatus(subProfileId: int): Promise<boolean>--><!--Device-privacyManager-function getPermissionUsedRecordToggleStatus(subProfileId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| subProfileId | int | Yes | 子身份资料的标识符。可以通过[OsAccountSubProfile.id](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md#id)获取。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回true，表示指定子身份资料的开关状态值为开启。返回false，表示指定子身份资料的开关状态值为关闭 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.PERMISSION_USED_STATS". |
| 12100001 | Invalid parameter. The specified subProfileId does not exist for the current user. |
| 202 | Not system app. Interface caller is not a system app. |
| 12100007 | Service exception. |

