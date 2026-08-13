# EditableSaveButtonV2

Declaration of the save button configuration.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare class EditableSaveButtonV2--><!--Device-unnamed-export declare class EditableSaveButtonV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { EditableSaveButtonV2, EditableTitleBarStyleV2Options, EditableTitleBarStyleV2, EditableTitleBarItemV2, EditableLeftIconV2Options, EditableTitleBarMenuItemV2, EditableTitleBarV2, EditableTitleBarMenuItemV2Options, EditableSaveButtonV2Options, EditableTitleBarItemV2Options, EditableTitleV2Options, EditableTitleV2, EditableLeftIconV2, EditableLeftIconTypeV2 } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: EditableSaveButtonV2Options)
```

Constructor of EditableSaveButtonV2.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableSaveButtonV2-constructor(options?: EditableSaveButtonV2Options)--><!--Device-EditableSaveButtonV2-constructor(options?: EditableSaveButtonV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EditableSaveButtonV2Options](arkts-arkui-arkui-advanced-editabletitlebarv2-editablesavebuttonv2options-i.md) | No | The options of the save button |

## defaultFocus

```TypeScript
@Trace
  public defaultFocus: boolean
```

Whether to get focus by default.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableSaveButtonV2-@Trace  public defaultFocus: boolean--><!--Device-EditableSaveButtonV2-@Trace  public defaultFocus: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isRequired

```TypeScript
@Trace
  public isRequired: boolean
```

Whether to show the save button.

**Type:** boolean

**Default:** true

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableSaveButtonV2-@Trace  public isRequired: boolean--><!--Device-EditableSaveButtonV2-@Trace  public isRequired: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAction

```TypeScript
@Trace
  public onAction?: OnActionCallback
```

Callback function when click on the save button.

**Type:** [OnActionCallback](arkts-arkui-onactioncallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableSaveButtonV2-@Trace  public onAction?: OnActionCallback--><!--Device-EditableSaveButtonV2-@Trace  public onAction?: OnActionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

