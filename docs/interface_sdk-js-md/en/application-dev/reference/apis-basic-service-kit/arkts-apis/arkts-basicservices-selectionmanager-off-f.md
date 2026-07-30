# off

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## off('selectionCompleted')

```TypeScript
function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void
```

Unregisters the callback used to listen for the word selection completion event. This API uses an asynchronous callback to return the result.

**Since:** 24

<!--Device-selectionManager-function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void--><!--Device-selectionManager-function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectionCompleted' | Yes | Event type, which is **'selectionCompleted'**. |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;SelectionInfo&gt; | No | Callback used to return SelectionInfo. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

// Define a callback used to listen for the word selection completion event, which will be registered and unregistered.
let selectionChangeCallback = (info: selectionManager.SelectionInfo) => {
  console.info('Enter the callback function.');
};

// Register a callback used to listen for the word selection completion event, preparing for subsequent unsubscription.
selectionManager.on('selectionCompleted', selectionChangeCallback);
try {
  // Unsubscribe from the word selection completion event.
  selectionManager.off('selectionCompleted', selectionChangeCallback);
} catch (err) {
  console.error(`Failed to unregister selectionCompleted. Error code: ${err.code}, error message: ${err.message}`);
}

```

