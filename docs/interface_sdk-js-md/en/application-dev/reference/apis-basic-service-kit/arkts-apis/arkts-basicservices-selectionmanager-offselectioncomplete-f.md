# offSelectionComplete

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## offSelectionComplete

```TypeScript
function offSelectionComplete(callback?: Callback<SelectionInfo>): void
```

Unregisters the callback used to listen for the word selection completion event. This API uses an asynchronous callback to return the result. **ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void--><!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | No | Callback used to return [SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md#selectioninfo-system-api). If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
import selectionManager from '@ohos.selectionInput.selectionManager';

let selectionChangeCallback = (info: selectionManager.SelectionInfo) => {
  console.info(`Enter the callback function.`);
};

selectionManager.onSelectionComplete(selectionChangeCallback);
try {
  selectionManager.offSelectionComplete(selectionChangeCallback);
} catch (err) {
  console.error(`Failed to unregister selectionComplete: ${err.code}, error message: ${err.message}`);
}
```

