# off_notify

## Modules to Import

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
```

## off_notify

```TypeScript
function off(type: 'notify', callback?: Callback<number>): void
```

Unsubscribes NFC RF status change events. &lt;p&gt;All callback functions will be unregistered If there is no specific callback parameter.&lt;/p&gt;

**Since:** 8

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function off(type: 'notify', callback?: Callback<number>): void--><!--Device-connectedTag-function off(type: 'notify', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'notify' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |
