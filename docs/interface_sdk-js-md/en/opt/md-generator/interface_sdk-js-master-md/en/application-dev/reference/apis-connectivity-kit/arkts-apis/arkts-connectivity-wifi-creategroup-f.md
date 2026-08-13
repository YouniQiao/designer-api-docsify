# createGroup

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## createGroup

```TypeScript
function createGroup(config: WifiP2PConfig): boolean
```

Creates a P2P group.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** createP2pGroup

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function createGroup(config: WifiP2PConfig): boolean--><!--Device-wifi-function createGroup(config: WifiP2PConfig): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [WifiP2PConfig](arkts-connectivity-wifimanager-wifip2pconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
  let config:wifi.WifiP2PConfig = {
    deviceAddress: "****",
    netId: 0,
    passphrase: "*****",
    groupName: "****",
    goBand: 0
  }
  wifi.createGroup(config);  
  
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
