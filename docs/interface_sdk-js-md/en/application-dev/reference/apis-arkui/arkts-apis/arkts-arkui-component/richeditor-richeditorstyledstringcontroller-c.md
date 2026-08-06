# RichEditorStyledStringController

Provides Controller for RichEditor with StyledString.

**Inheritance/Implementation:** RichEditorStyledStringController extends [RichEditorBaseController](richeditor-richeditorbasecontroller-c.md) and implements [StyledStringController](textcommon-styledstringcontroller-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RichEditorStyledStringController extends RichEditorBaseController    implements StyledStringController--><!--Device-unnamed-export declare class RichEditorStyledStringController extends RichEditorBaseController    implements StyledStringController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getSelection

```TypeScript
getSelection(): RichEditorRange | undefined
```

Get the selection in the StyledString of the RichEditor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-getSelection(): RichEditorRange | undefined--><!--Device-RichEditorStyledStringController-getSelection(): RichEditorRange | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## getStyledString

```TypeScript
getStyledString(): MutableStyledString | undefined
```

Get the StyledString of the RichEditor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-getStyledString(): MutableStyledString | undefined--><!--Device-RichEditorStyledStringController-getStyledString(): MutableStyledString | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

## onContentChanged

```TypeScript
onContentChanged(listener: StyledStringChangedListener): void
```

Register content changed listener

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-onContentChanged(listener: StyledStringChangedListener): void--><!--Device-RichEditorStyledStringController-onContentChanged(listener: StyledStringChangedListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | content changed listener. |

## setStyledString

```TypeScript
setStyledString(styledString: StyledString): void
```

Set the StyledString of the RichEditor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-setStyledString(styledString: StyledString): void--><!--Device-RichEditorStyledStringController-setStyledString(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | StyledString. |

