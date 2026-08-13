# off_hotspotStaJoin (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## off_hotspotStaJoin

```TypeScript
function off(type: 'hotspotStaJoin', callback?: Callback<StationInfo>): void
```

Unsubscribe Wi-Fi hotspot sta join events. &lt;p&gt;All callback functions will be deregistered If there is no specific callback parameter.&lt;/p&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** hotspotStaJoin

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifi-function off(type: 'hotspotStaJoin', callback?: Callback<StationInfo>): void--><!--Device-wifi-function off(type: 'hotspotStaJoin', callback?: Callback<StationInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hotspotStaJoin' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StationInfo&gt; | No |
