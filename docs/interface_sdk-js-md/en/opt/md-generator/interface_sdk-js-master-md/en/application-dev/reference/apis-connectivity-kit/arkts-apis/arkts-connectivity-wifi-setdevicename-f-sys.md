# setDeviceName (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## setDeviceName

```TypeScript
function setDeviceName(devName: string): boolean
```

Sets the name of the Wi-Fi P2P device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** setP2pDeviceName

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function setDeviceName(devName: string): boolean--><!--Device-wifi-function setDeviceName(devName: string): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| devName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
    let name = "****";
    wifi.setDeviceName(name);    
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```
