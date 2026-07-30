# getApplicationWindowStates

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## getApplicationWindowStates

```TypeScript
function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>
```

Gets the window states of the application.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>--><!--Device-applicationManager-function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-arkui/arkts-apis/arkts-arkui-want-t-sys.md) | Yes | admin indicates the enterprise admin extension ability information. |
| bundleName | string | Yes | bundleName indicates the bundle name of the application. |
| appIndex | number | Yes | appIndex indicates the index of bundle.<br>The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;WindowStateInfo&gt; | Returns the window states information of application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |

**Example**

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Bundle name of the application to be queried. Replace it as required.
let bundleName: string = 'com.example.myapplication';
// Clone index of the queried application. Replace it as required.
let appIndex: number = 0;
try {
  let result: Array<applicationManager.WindowStateInfo> = applicationManager.getApplicationWindowStates(wantTemp, bundleName, appIndex);
  console.info(`Succeeded in getting application window states, result: ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to get application window states. Code: ${err.code}, message: ${err.message}`);
}

```

