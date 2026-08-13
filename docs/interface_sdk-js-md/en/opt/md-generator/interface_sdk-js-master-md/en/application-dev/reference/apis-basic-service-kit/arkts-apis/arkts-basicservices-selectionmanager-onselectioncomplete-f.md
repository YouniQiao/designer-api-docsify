# onSelectionComplete

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## onSelectionComplete

```TypeScript
function onSelectionComplete(callback: Callback<SelectionInfo>): void
```

Registers a callback to listen for the word selection completion event. This API uses an asynchronous callback to return the result. **ArkTS mode:** This API applies only to ArkTS-Sta.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void--><!--Device-selectionManager-function onSelectionComplete(callback: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33600003](../../apis-basic-services-kit/errorcode-selection.md#33600003-api-caller-and-word-selection-application-mismatched) |
