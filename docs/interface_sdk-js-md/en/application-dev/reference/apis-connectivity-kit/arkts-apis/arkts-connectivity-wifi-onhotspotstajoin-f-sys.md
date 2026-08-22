# on_hotspotStaJoin (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## on('hotspotStaJoin')

```TypeScript
function on(type: 'hotspotStaJoin', callback: Callback<StationInfo>): void
```

Subscribe Wi-Fi hotspot sta join events.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** hotspotStaJoin

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifi-function on(type: 'hotspotStaJoin', callback: Callback<StationInfo>): void--><!--Device-wifi-function on(type: 'hotspotStaJoin', callback: Callback<StationInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'hotspotStaJoin' | Yes | event name. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StationInfo&gt; | Yes | the callback of on |

