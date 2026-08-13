# on_selectionCompleted (System API)

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## on_selectionCompleted

```TypeScript
function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void
```

Subscribes to the word selection completion event. This API is used together with [off('selectionCompleted')](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#off_selectionCompleted). [off('selectionCompleted')](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#off_selectionCompleted) is used to unsubscribe from the event.

**Since:** 20

**Deprecated since:** -1

<!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'selectionCompleted' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33600003](../../apis-basic-services-kit/errorcode-selection.md#33600003-api-caller-and-word-selection-application-mismatched) |

## Examples

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

try {
  // Subscribe to the word selection completion event.
  selectionManager.on('selectionCompleted', (info: selectionManager.SelectionInfo) => {
    console.info('Enter the callback function.');
  });
} catch (err) {
  console.error(`Failed to register selectionCompleted callback. Error code: ${err.code}, error message: ${err.message}`);
}
```
