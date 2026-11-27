# setControlPanelRestricted

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## setControlPanelRestricted

```TypeScript
function setControlPanelRestricted(restricted: boolean): Promise<void>
```

Sets whether to enable the control panel restricted mode. When enabled, the control panel displays only the toggles in the whitelist. If no whitelist is configured, all croppable icons in the area are hidden. When disabled, the whitelist does not take effect.

This API is a device-level setting. It takes effect for all users and persists after a restart. If multiple administrators call this API, the last successful setting takes effect.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setControlPanelRestricted(restricted: boolean): Promise<void>--><!--Device-deviceSettings-function setControlPanelRestricted(restricted: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| restricted | boolean | Yes | Whether to enable control panel restricted mode. The value **true** means enabling; the value **false** means disabling. |

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
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
