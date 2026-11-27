# setControlPanelTopToggleListForAccount

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## setControlPanelTopToggleListForAccount

```TypeScript
function setControlPanelTopToggleListForAccount(toggleList: Array<ControlPanelTopToggleType>,
    accountId: number): Promise<void>
```

Sets the control panel top toggle list (1*2 area) whitelist for a specified account. The whitelist takes effect only when the restricted mode is enabled. If the restricted mode is disabled, the whitelist is still saved but does not crop icons. The new list overwrites the existing list. An empty array means all croppable icons in the area are hidden.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setControlPanelTopToggleListForAccount(toggleList: Array<ControlPanelTopToggleType>,    accountId: number): Promise<void>--><!--Device-deviceSettings-function setControlPanelTopToggleListForAccount(toggleList: Array<ControlPanelTopToggleType>,    accountId: number): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toggleList | Array&lt;[ControlPanelTopToggleType](arkts-mdm-devicesettings-controlpaneltoptoggletype-e.md)&gt; | Yes | Toggle list whitelist for the 1*2 area. An empty array means all croppable icons in the area are hidden. |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. The specified user must exist. You can call [getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) to obtain the user ID. Whether cross-user setting is supported depends on the administrator type and the device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200006](../errorcode-enterpriseDeviceManager.md#9200006-invalid-user-id) | The specified account ID is invalid. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
