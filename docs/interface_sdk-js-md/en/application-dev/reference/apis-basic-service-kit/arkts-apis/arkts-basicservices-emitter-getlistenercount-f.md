# getListenerCount

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## getListenerCount

```TypeScript
function getListenerCount(eventId: long | string): long
```

获取指定事件的订阅数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-emitter-function getListenerCount(eventId: long | string): long--><!--Device-emitter-function getListenerCount(eventId: long | string): long-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | ArkTS-Dyn: number \| string  <br>ArkTS-Sta：long \| string | Yes | 事件ID，由开发者定义，用于辨别事件。 string类型：不可为空字符串，大小不超过10240字节，超出部分会被截断。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 指定事件的订阅数。 |

## Examples

```TypeScript
let count: number = emitter.getListenerCount('eventId');
```

