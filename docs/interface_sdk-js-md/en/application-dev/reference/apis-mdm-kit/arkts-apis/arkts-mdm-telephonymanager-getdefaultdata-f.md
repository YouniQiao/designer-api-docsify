# getDefaultData

## Modules to Import

```TypeScript
import { telephonyManager } from '@kit.MDMKit';
```

## getDefaultData

```TypeScript
function getDefaultData(admin: Want): number
```

Gets the default data traffic card.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function getDefaultData(admin: Want): number--><!--Device-telephonyManager-function getDefaultData(admin: Want): number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-arkui/arkts-apis/arkts-arkui-want-t-sys.md) | Yes | admin indicates the enterprise admin extension ability information.The admin must have the corresponding permission. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Returns the slot ID of the SIM card. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) | This function is prohibited by enterprise management policies. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Failed to call the API due to limited device capabilities. |

**Example**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace the values as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Obtain the slot ID of the SIM card currently used as the default data SIM card.
  let slotId: number = telephonyManager.getDefaultData(wantTemp);
  console.info(`success to get default data SIM ID, current is ${slotId}`);
} catch (err) {
  console.error(`Failed to get default data. Code: ${err.code}, message: ${err.message}`);
}

```

