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

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function off(type: 'notify', callback?: Callback<number>): void--><!--Device-connectedTag-function off(type: 'notify', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'notify' | Yes | The callback type. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | The callback function to be unregistered. |

