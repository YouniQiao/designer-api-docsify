# removeDevice

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## removeDevice

```TypeScript
function removeDevice(id: number): void
```

Remove a Wi-Fi DeviceConfig with networkId.After a Wi-Fi DeviceConfig is removed, its configuration will be deleted from the list of Wi-Fi configurations.If the Wi-Fi DeviceConfig is being connected, the connection will be interrupted.The application can only delete Wi-Fi DeviceConfig it has created.

**Since:** 15

**Required permissions:** ohos.permission.SET_WIFI_INFO and (ohos.permission.MANAGE_WIFI_CONNECTION or ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION)

<!--Device-wifiManager-function removeDevice(id: int): void--><!--Device-wifiManager-function removeDevice(id: int): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../errorcode-wifi.md#2501001-sta-disabled) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
  
    try {
      let id = 0;
      wifiManager.removeDevice(id);  
    }catch(error){
      console.error("failed:" + JSON.stringify(error));
    }
```
