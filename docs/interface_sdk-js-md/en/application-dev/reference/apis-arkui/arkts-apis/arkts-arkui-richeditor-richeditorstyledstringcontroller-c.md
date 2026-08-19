# RichEditorStyledStringController

Provides Controller for RichEditor with StyledString.

**Inheritance/Implementation:** RichEditorStyledStringController extends [RichEditorBaseController](arkts-arkui-richeditor-richeditorbasecontroller-c.md) and implements StyledStringController

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class RichEditorStyledStringController--><!--Device-unnamed-export declare class RichEditorStyledStringController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getSelection

```TypeScript
getSelection(): RichEditorRange | undefined
```

Get the selection in the StyledString of the RichEditor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-getSelection(): RichEditorRange | undefined--><!--Device-RichEditorStyledStringController-getSelection(): RichEditorRange | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RichEditorRange](arkts-arkui-richeditor-richeditorrange-i.md) \| undefined |  |

## getStyledString

```TypeScript
getStyledString(): MutableStyledString | undefined
```

Get the StyledString of the RichEditor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-getStyledString(): MutableStyledString | undefined--><!--Device-RichEditorStyledStringController-getStyledString(): MutableStyledString | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MutableStyledString](arkts-arkui-styledstring-mutablestyledstring-c.md) \| undefined |  |

## onContentChanged

```TypeScript
onContentChanged(listener: StyledStringChangedListener): void
```

Register content changed listener

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-onContentChanged(listener: StyledStringChangedListener): void--><!--Device-RichEditorStyledStringController-onContentChanged(listener: StyledStringChangedListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [StyledStringChangedListener](arkts-arkui-textcommon-styledstringchangedlistener-i.md) | Yes | content changed listener. |

## setStyledString

```TypeScript
setStyledString(styledString: StyledString): void
```

Set the StyledString of the RichEditor.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-setStyledString(styledString: StyledString): void--><!--Device-RichEditorStyledStringController-setStyledString(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-styledstring-c.md) | Yes | StyledString. |

