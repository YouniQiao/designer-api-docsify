# off_streamChange (System API)

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## off_streamChange

```TypeScript
function off(type: 'streamChange', callback?: Callback<number>): void
```

Unsubscribe Wi-Fi stream change events. &lt;p&gt;All callback functions will be deregistered If there is no specific callback parameter.&lt;/p&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** streamChange

**Required permissions:** ohos.permission.MANAGE_WIFI_CONNECTION

<!--Device-wifi-function off(type: 'streamChange', callback?: Callback<number>): void--><!--Device-wifi-function off(type: 'streamChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'streamChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | the callback of on, 1: stream down, 2: stream up, 3: stream bidirectional |

