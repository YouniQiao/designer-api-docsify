# connectToNetwork (System API)

## Modules to Import

```TypeScript
```

## connectToNetwork

```TypeScript
function connectToNetwork(networkId: number): boolean
```

Connects to Wi-Fi network.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [connectToNetwork](arkts-connectivity-wifimanager-connecttonetwork-f.md#connecttonetwork)

**Required permissions:** ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function connectToNetwork(networkId: number): boolean--><!--Device-wifi-function connectToNetwork(networkId: number): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let networkId = 0;
    wifi.connectToNetwork(networkId);
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```
