# getDeviceMacAddress (System API)

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## getDeviceMacAddress

```TypeScript
function getDeviceMacAddress(): string[]
```

Obtains the MAC address of a Wi-Fi device. Wi-Fi must be enabled. &lt;p&gt;The MAC address is unique and cannot be changed.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getDeviceMacAddress](arkts-connectivity-wifimanager-getdevicemacaddress-f.md#getdevicemacaddress)

**Required permissions:** ohos.permission.GET_WIFI_LOCAL_MAC and ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getDeviceMacAddress(): string[]--><!--Device-wifi-function getDeviceMacAddress(): string[]-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string[] | Returns the MAC address of the Wi-Fi device. |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let ret = wifi.getDeviceMacAddress();
    console.info("deviceMacAddress:" + JSON.stringify(ret));
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```

