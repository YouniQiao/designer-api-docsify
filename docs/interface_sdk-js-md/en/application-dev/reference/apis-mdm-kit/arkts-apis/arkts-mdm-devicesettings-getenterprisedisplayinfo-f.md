# getEnterpriseDisplayInfo

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## getEnterpriseDisplayInfo

```TypeScript
function getEnterpriseDisplayInfo(): DisPlayInfo
```

Obtains enterprise display information.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function getEnterpriseDisplayInfo(): DisPlayInfo--><!--Device-deviceSettings-function getEnterpriseDisplayInfo(): DisPlayInfo-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Return value:**

| Type | Description |
| --- | --- |
| [DisPlayInfo](arkts-mdm-devicesettings-displayinfo-i.md) | This interface is used to obtain enterprise display information in JSON format. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
