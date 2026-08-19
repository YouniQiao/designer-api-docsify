# on_hotspotStaLeave (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## on_hotspotStaLeave('hotspotStaLeave')

```TypeScript
function on(type: 'hotspotStaLeave', callback: Callback<StationInfo>): void
```

Subscribe Wi-Fi hotspot sta leave events.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** hotspotStaLeave

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifi-function on(type: 'hotspotStaLeave', callback: Callback<StationInfo>): void--><!--Device-wifi-function on(type: 'hotspotStaLeave', callback: Callback<StationInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hotspotStaLeave' | Yes | event name. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StationInfo&gt; | Yes | the callback of on |

