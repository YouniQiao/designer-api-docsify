# on_notify

## Modules to Import

```TypeScript
import { connectedTag } from 'connectedTag';
```

## on_notify

```TypeScript
function on(type: 'notify', callback: Callback<number>): void
```

Subscribes NFC RF status change events.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** -1

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function on(type: 'notify', callback: Callback<number>): void--><!--Device-connectedTag-function on(type: 'notify', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'notify' | Yes | The callback type. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | The callback function to be registered. |

