# getControlPanelTopToggleListForAccount

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## getControlPanelTopToggleListForAccount

```TypeScript
function getControlPanelTopToggleListForAccount(accountId: number): Promise<Array<ControlPanelTopToggleType>>
```

Queries the control panel top toggle list (1*2 area) whitelist for a specified account. If no whitelist is configured or the configured whitelist is an empty array, an empty array is returned.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function getControlPanelTopToggleListForAccount(accountId: number): Promise<Array<ControlPanelTopToggleType>>--><!--Device-deviceSettings-function getControlPanelTopToggleListForAccount(accountId: number): Promise<Array<ControlPanelTopToggleType>>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. The specified user must exist. You can call [getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) to obtain the user ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[ControlPanelTopToggleType](arkts-mdm-devicesettings-controlpaneltoptoggletype-e.md)&gt;&gt; | Promise used to return the control panel 1*2 area toggle whitelist. An empty array means no whitelist is configured or all croppable icons in the area are hidden. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200006](../errorcode-enterpriseDeviceManager.md#9200006-invalid-user-id) | The specified account ID is invalid. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
