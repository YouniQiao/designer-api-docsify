# onSelectionComplete

## Modules to Import

```TypeScript
import { selectionManager } from 'selectionManager';
```

## onSelectionComplete

```TypeScript
function onSelectionComplete(callback: Callback<SelectionInfo>): void
```

Registers a callback to listen for the word selection completion event. This API uses an asynchronous callback to return the result. **ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | Yes | Callback used to return the word selection information. This callback is triggered only when the user selects text using the mouse or touchpad (by double-clicking, triple-clicking, or pressing and sliding the left mouse button) and then presses **Ctrl**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33600003](../../apis-basic-services-kit/errorcode-selection.md#33600003-api-caller-and-word-selection-application-mismatched) | The application calling the API does not match the application selected in the system settings. |

## Examples

```TypeScript
import selectionManager from '@ohos.selectionInput.selectionManager';

try {
  selectionManager.onSelectionComplete((info: selectionManager.SelectionInfo) => {
    console.info(`SelectionInfo: ${JSON.stringify(info)}`);
  });
} catch (err) {
  console.error(`Failed to register selectionCompleted callback: ${err.code}, error message: ${err.message}}`);
}
```

