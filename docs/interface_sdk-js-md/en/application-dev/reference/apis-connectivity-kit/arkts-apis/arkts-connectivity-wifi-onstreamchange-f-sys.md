# on_streamChange (System API)

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## on_streamChange

```TypeScript
function on(type: 'streamChange', callback: Callback<number>): void
```

Subscribe Wi-Fi stream change events.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** streamChange

**Required permissions:** ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function on(type: 'streamChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'streamChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'streamChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | the callback of on, 1: stream down, 2: stream up, 3: stream bidirectional |

