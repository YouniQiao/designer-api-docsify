# setHotspotConfig (System API)

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## setHotspotConfig

```TypeScript
function setHotspotConfig(config: HotspotConfig): boolean
```

Sets the hotspot for a device.<p>Only OPEN and WPA2 PSK hotspot can be configured.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setHotspotConfig](arkts-connectivity-wifimanager-sethotspotconfig-f-sys.md)

**Required permissions:** ohos.permission.SET_WIFI_INFO and ohos.permission.GET_WIFI_CONFIG

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [HotspotConfig](arkts-connectivity-wifi-hotspotconfig-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
