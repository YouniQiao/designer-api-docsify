# getAllowedWifiList

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## getAllowedWifiList

```TypeScript
function getAllowedWifiList(admin: Want): Array<WifiAccessInfo>
```

Obtains Wi-Fi networks from the allowed list.

**Since:** 19

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_WIFI

**Model restriction:** This API can be used only in the stage model.

<!--Device-wifiManager-function getAllowedWifiList(admin: Want): Array<WifiAccessInfo>--><!--Device-wifiManager-function getAllowedWifiList(admin: Want): Array<WifiAccessInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;WifiAccessInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |


## getAllowedWifiList

```TypeScript
function getAllowedWifiList(admin: Want | null): Array<WifiAccessInfo>
```

Obtains Wi-Fi networks from the allowed list.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_WIFI

**Model restriction:** This API can be used only in the stage model.

<!--Device-wifiManager-function getAllowedWifiList(admin: Want | null): Array<WifiAccessInfo>--><!--Device-wifiManager-function getAllowedWifiList(admin: Want | null): Array<WifiAccessInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;WifiAccessInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
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
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: Array<wifiManager.WifiAccessInfo> = wifiManager.getAllowedWifiList(wantTemp);
  console.info(`Succeeded in getting allowed Wi-Fi list. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get allowed Wi-Fi list. Code: ${err.code}, message: ${err.message}`);
}
```
