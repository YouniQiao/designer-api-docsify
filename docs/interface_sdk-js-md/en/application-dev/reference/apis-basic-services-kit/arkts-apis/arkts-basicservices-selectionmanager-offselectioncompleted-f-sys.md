# off_selectionCompleted (System API)

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## off_selectionCompleted('selectionCompleted')

```TypeScript
function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void
```

Unsubscribes from the word selection completion event. This API is used together with [on('selectionCompleted')](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#on_selectioncompletedselectioncompleted).

**Since:** 20

<!--Device-selectionManager-function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void--><!--Device-selectionManager-function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectionCompleted' | Yes | Type of the event to unsubscribe from. The value is fixed to **'selectionCompleted'**. |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | No | Callback to be unregistered, which the callback instance registered using **on**. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';

let selectionChangeCallback = (info: selectionManager.SelectionInfo) => {
  console.info(`Enter the callback function.`);
};

selectionManager.on('selectionCompleted', selectionChangeCallback);
try {
  selectionManager.off('selectionCompleted', selectionChangeCallback);
} catch (err) {
  console.error(`Failed to unregister selectionCompleted: ${err.code}, error message: ${err.message}`);
}
```

