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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void--><!--Device-selectionManager-function offSelectionComplete(callback?: Callback<SelectionInfo>): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md)&gt; | No |
