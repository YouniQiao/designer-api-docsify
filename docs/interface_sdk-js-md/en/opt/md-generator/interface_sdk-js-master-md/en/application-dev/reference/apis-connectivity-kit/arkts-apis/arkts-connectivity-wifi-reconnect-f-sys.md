# reconnect (System API)

## Modules to Import

```TypeScript
```

## reconnect

```TypeScript
function reconnect(): boolean
```

Re-connects to current network.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reconnect](arkts-connectivity-wifimanager-reconnect-f-sys.md#reconnect-system-api)

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function reconnect(): boolean--><!--Device-wifi-function reconnect(): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

try {
    wifi.reconnect();
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```
