# getApplicationWindowStates

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## getApplicationWindowStates

```TypeScript
function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>
```

Queries the window state information list of the specified application. It can retrieve information such as whether the application is in the bottom dock and whether the application window is currently displayed in the foreground.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>--><!--Device-applicationManager-function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the application. |
| appIndex | number | Yes | Index of the application clone. The value is an integer greater than or equal to 0. &lt;br&gt; You can call [getAppCloneIdentity](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getappcloneidentity-f.md#getAppCloneIdentity) of @ohos.bundle.bundleManager to obtain the index. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[WindowStateInfo](arkts-mdm-applicationmanager-windowstateinfo-i.md)&gt; | Array of the application window state information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

