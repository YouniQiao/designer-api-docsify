# on

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## on('selectionCompleted')

```TypeScript
function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void
```

Subscribes to the word selection completion event. This API is used together with   
[off('selectionCompleted')](selectionManager.off(type: 'selectionCompleted', callback?: Callback&lt;SelectionInfo&gt;)).

[off('selectionCompleted')](selectionManager.off(type: 'selectionCompleted', callback?: Callback&lt;SelectionInfo&gt;))is used to unsubscribe from the event.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectionCompleted' | Yes | Event type, which is **'selectionCompleted'**. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;SelectionInfo&gt; | Yes | Callback used to return [SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md). This callback is triggered only when the user selects text using the mouse or touchpad (by double-clicking, triple-clicking, or sliding the left mouse button) and then presses **Ctrl**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600003](../../apis-basic-services-kit/errorcode-selection.md#33600003-api-caller-and-word-selection-application-mismatched) | The application calling the API does not match the application selected in the system settings. |

## Examples

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

try {
  selectionManager.on('selectionCompleted', (info: selectionManager.SelectionInfo) => {
    console.info(`Enter the callback function.`);
  });
} catch (err) {
  console.error(`Failed to register selectionCompleted callback: ${err.code}, error message: ${err.message}`);
}
```

