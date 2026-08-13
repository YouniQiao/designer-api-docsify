# off_streamChange (System API)

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'streamChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |
