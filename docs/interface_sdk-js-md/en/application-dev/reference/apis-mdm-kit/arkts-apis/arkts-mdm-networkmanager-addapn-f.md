# addApn

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## addApn

```TypeScript
function addApn(admin: Want, apnInfo: Record<string, string>): void
```

Adds an access point name (APN).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APN

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function addApn(admin: Want, apnInfo: Record<string, string>): void--><!--Device-networkManager-function addApn(admin: Want, apnInfo: Record<string, string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| apnInfo | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt; | Yes | APN information to be added. After the setting, the system uses these parameters to configure the mobile data network access point, affecting the network connection method and data transmission path. &lt;br&gt;- **apnName**: APN identifier, which is mandatory. &lt;br&gt;- **mcc**: 3-digit mobile country code (MCC), which is mandatory. &lt;br&gt;- **mnc**: 2-digit or 3-digit mobile network code (MNC), which is mandatory. &lt;br&gt;- **apn**: access point name, which is mandatory. &lt;br&gt;- **type**: APN service type, which is optional. &lt;br&gt;- **user**: user name for APN authentication, which is optional. &lt;br&gt;- **password**: password for APN authentication, which is optional. &lt;br&gt;- **proxy**: address of the proxy server for a common data connection, which is optional. &lt;br&gt;- **mmsproxy**: dedicated proxy address of the MMS service, which is optional. &lt;br&gt;- **authType**: authentication protocol type of the APN, which is optional. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { networkManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility',
};
let apnInfo: Record<string, string> = {
  // Replace with actual values.
  "apnName": "CTNET",
  "apn": "CTNET",
  "mnc": "11",
  "mcc": "460",
};
try {
  networkManager.addApn(wantTemp, apnInfo);
  console.info(`Succeeded in adding apn.`);
} catch (err) {
  console.error(`Failed to add apn. Code: ${err.code}, message: ${err.message}`);
}
```

