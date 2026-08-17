# EditableLeftIconV2

Declaration of the left icon configuration.

**Since:** 26.0.0

<!--Device-unnamed-export declare class EditableLeftIconV2--><!--Device-unnamed-export declare class EditableLeftIconV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { EditableLeftIconTypeV2 } from 'EditableLeftIconTypeV2';
import { EditableTitleBarV2 } from 'EditableTitleBarV2';
import { EditableLeftIconV2 } from 'EditableLeftIconV2';
import { EditableLeftIconV2Options } from 'EditableLeftIconV2Options';
import { EditableTitleV2 } from 'EditableTitleV2';
import { EditableTitleV2Options } from 'EditableTitleV2Options';
import { EditableTitleBarItemV2 } from 'EditableTitleBarItemV2';
import { EditableTitleBarItemV2Options } from 'EditableTitleBarItemV2Options';
import { EditableTitleBarMenuItemV2 } from 'EditableTitleBarMenuItemV2';
import { EditableTitleBarMenuItemV2Options } from 'EditableTitleBarMenuItemV2Options';
import { EditableSaveButtonV2 } from 'EditableSaveButtonV2';
import { EditableSaveButtonV2Options } from 'EditableSaveButtonV2Options';
import { EditableTitleBarStyleV2 } from 'EditableTitleBarStyleV2';
import { EditableTitleBarStyleV2Options } from 'EditableTitleBarStyleV2Options';
```

## constructor

```TypeScript
constructor(options?: EditableLeftIconV2Options)
```

Constructor of EditableLeftIconV2.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableLeftIconV2-constructor(options?: EditableLeftIconV2Options)--><!--Device-EditableLeftIconV2-constructor(options?: EditableLeftIconV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EditableLeftIconV2Options](../../apis-na/arkts-apis/arkts-na-arkui-advanced-editabletitlebarv2-editablelefticonv2options-i.md) | No | The options of the left icon |

## defaultFocus

```TypeScript
@Trace
  public defaultFocus: boolean
```

Whether to get focus by default.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableLeftIconV2-@Trace  public defaultFocus: boolean--><!--Device-EditableLeftIconV2-@Trace  public defaultFocus: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconType

```TypeScript
@Trace
  public iconType: EditableLeftIconTypeV2
```

Icon type, Back or Cancel.

**Type:** [EditableLeftIconTypeV2](../../apis-na/arkts-apis/arkts-na-arkui-advanced-editabletitlebarv2-editablelefticontypev2-e.md)

**Default:** EditableLeftIconTypeV2.Back

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableLeftIconV2-@Trace  public iconType: EditableLeftIconTypeV2--><!--Device-EditableLeftIconV2-@Trace  public iconType: EditableLeftIconTypeV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAction

```TypeScript
@Trace
  public onAction?: OnActionCallback
```

Callback function when click on the left icon.

**Type:** [OnActionCallback](../../apis-na/arkts-apis/arkts-na-onactioncallback-t.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableLeftIconV2-@Trace  public onAction?: OnActionCallback--><!--Device-EditableLeftIconV2-@Trace  public onAction?: OnActionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

