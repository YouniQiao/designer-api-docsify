# createGroup

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## createGroup

```TypeScript
function createGroup(config: WifiP2PConfig): void
```

Create a P2P group.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function createGroup(config: WifiP2PConfig): void--><!--Device-wifiManager-function createGroup(config: WifiP2PConfig): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [WifiP2PConfig](arkts-connectivity-wifimanager-wifip2pconfig-i.md) | Yes | Indicates the configuration for a group. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid parameters. Possible causes: 1.Incorrect parameter types. 2.Parameter verification failed. |
| 801 | Capability not supported. |
| 2801000 | Operation failed. |
| 2801001 | Wi-Fi STA disabled. |
| 201 | Permission denied. |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let config:wifiManager.WifiP2PConfig = {
      deviceAddress: "****",
      netId: 0,
      passphrase: "*****",
      groupName: "****",
      goBand: 0
    }
    wifiManager.createGroup(config);  
    
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```

