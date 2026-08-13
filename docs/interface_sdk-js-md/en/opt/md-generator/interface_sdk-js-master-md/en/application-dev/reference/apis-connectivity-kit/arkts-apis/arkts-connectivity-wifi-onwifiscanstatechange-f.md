# on_wifiScanStateChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## on_wifiScanStateChange

```TypeScript
function on(type: 'wifiScanStateChange', callback: Callback<number>): void
```

Subscribe Wi-Fi scan status change events.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** wifiScanStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'wifiScanStateChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'wifiScanStateChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'wifiScanStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |
