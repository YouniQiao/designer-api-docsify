# onHotspotStaJoin (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## onHotspotStaJoin

```TypeScript
function onHotspotStaJoin(callback: Callback<StationInfo>): void
```

Subscribe Wi-Fi hotspot sta join events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function onHotspotStaJoin(callback: Callback<StationInfo>): void--><!--Device-wifiManager-function onHotspotStaJoin(callback: Callback<StationInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StationInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) |
