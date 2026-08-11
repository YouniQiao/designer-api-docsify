# off (System API)

## Modules to Import

```TypeScript
import { dragInteraction } from 'kits/@kit.ArkUI';
```

## off('drag')

```TypeScript
function off(type: 'drag', callback?: Callback<DragState>): void
```

Disables listening for dragging status changes.

**Since:** 10

<!--Device-dragInteraction-function off(type: 'drag', callback?: Callback<DragState>): void--><!--Device-dragInteraction-function off(type: 'drag', callback?: Callback<DragState>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'drag' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DragState&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
// Unregister a single callback.
function single_callback(event: dragInteraction.DragState) {
  console.info(`Drag interaction event: ${event}`);
  return false;
}
try {
  dragInteraction.on('drag', single_callback);
  dragInteraction.off("drag", single_callback);
} catch (error) {
  console.error(`Execute failed, code: ${error.code}, message: ${error.message}`);
}
```

```TypeScript
// Unregister all callbacks.
function all_callback(event: dragInteraction.DragState) {
  console.info(`Drag interaction event: ${event}`);
  return false;
}
try {
  dragInteraction.on('drag', all_callback);
  dragInteraction.off("drag");
} catch (error) {
  console.error(`Execute failed, code: ${error.code}, message: ${error.message}`);
}
```
