# offSelectionComplete

## offSelectionComplete

```TypeScript
function offSelectionComplete(callback?: Callback<SelectionInfo>): void
```

Unregisters the callback used to listen for the word selection completion event. This API uses an asynchronous callback to return the result.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void--><!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SelectionInfo&gt; | No | Callback used to return SelectionInfo. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Example**

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

