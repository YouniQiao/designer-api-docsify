# setEnterpriseDisplayInfo

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## setEnterpriseDisplayInfo

```TypeScript
function setEnterpriseDisplayInfo(displayInfo: DisPlayInfo): void
```

Set enterprise display information.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setEnterpriseDisplayInfo(displayInfo: DisPlayInfo): void--><!--Device-deviceSettings-function setEnterpriseDisplayInfo(displayInfo: DisPlayInfo): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayInfo | [DisPlayInfo](arkts-mdm-devicesettings-displayinfo-i.md) | Yes | Specifies the enterprise information to be displayed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
