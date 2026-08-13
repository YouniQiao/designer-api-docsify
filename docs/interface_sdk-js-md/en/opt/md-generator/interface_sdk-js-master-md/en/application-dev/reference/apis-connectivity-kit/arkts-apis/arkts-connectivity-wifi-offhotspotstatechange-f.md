# off_hotspotStateChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## off_hotspotStateChange

```TypeScript
function off(type: 'hotspotStateChange', callback?: Callback<number>): void
```

Unsubscribe Wi-Fi hotspot state change events. &lt;p&gt;All callback functions will be deregistered If there is no specific callback parameter.&lt;/p&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** hotspotStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'hotspotStateChange', callback?: Callback<number>): void--><!--Device-wifi-function off(type: 'hotspotStateChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'hotspotStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |
