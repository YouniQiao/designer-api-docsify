# on

## Modules to Import

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## on('selectionCompleted')

```TypeScript
function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void
```

Subscribes to the word selection completion event. This API is used together with off('selectionCompleted').  
off('selectionCompleted') is used to unsubscribe from the event.

**Since:** 24

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'selectionCompleted' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33600003](../errorcode-selection.md#33600003-api-caller-and-word-selection-application-mismatched) |
