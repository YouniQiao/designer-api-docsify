# addAllowedWifiList

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## addAllowedWifiList

```TypeScript
function addAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void
```

Adds allowed Wi-Fi networks. The current device can only connect to the allowed Wi-Fi networks. This API is applicable to enterprise security management scenarios, for example, restricting employees' devices to connect only to Wi-Fi networks authorized by the enterprise, preventing connection to insecure external Wi-Fi networks and ensuring enterprise network and data security.

A policy conflict is reported when this API is called in the following scenarios:

1. The device Wi-Fi capability has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy).You can resolve the conflict by enabling Wi-Fi via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy).2. Disallowed Wi-Fi networks have been added by calling [addDisallowedWifiList](arkts-mdm-wifimanager-adddisallowedwifilist-f.md#adddisallowedwifilist).You can resolve the conflict by removing the disallowed Wi-Fi networks through [removeDisallowedWifiList](arkts-mdm-wifimanager-removedisallowedwifilist-f.md#removedisallowedwifilist).

**Since:** 19

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_WIFI

**Model restriction:** This API can be used only in the stage model.

<!--Device-wifiManager-function addAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void--><!--Device-wifiManager-function addAllowedWifiList(admin: Want, list: Array<WifiAccessInfo>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| list | Array&lt;WifiAccessInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.edmtest',
  abilityName: 'com.example.edmtest.EnterpriseAdminAbility'
};
try {
  let wifiIds: Array<wifiManager.WifiAccessInfo> = [{
    // Replace with actual values.
    ssid: "wifi_name",
    bssid: "68:77:24:77:A6:D8"
  }];
  wifiManager.addAllowedWifiList(wantTemp, wifiIds);
  console.info(`Succeeded in adding allowed Wi-Fi list.`);
} catch (err) {
  console.error(`Failed to add allowed Wi-Fi list. Code: ${err.code}, message: ${err.message}`);
}
```
