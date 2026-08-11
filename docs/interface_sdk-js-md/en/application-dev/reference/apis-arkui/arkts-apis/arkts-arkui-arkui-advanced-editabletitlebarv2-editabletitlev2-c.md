# EditableTitleV2

Declaration of the title configuration.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class EditableTitleV2--><!--Device-unnamed-export declare class EditableTitleV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { EditableSaveButtonV2, EditableTitleBarStyleV2Options, EditableTitleBarStyleV2, EditableTitleBarItemV2, EditableLeftIconV2Options, EditableTitleBarMenuItemV2, EditableTitleBarV2, EditableTitleBarMenuItemV2Options, EditableSaveButtonV2Options, EditableTitleBarItemV2Options, EditableTitleV2Options, EditableTitleV2, EditableLeftIconV2, EditableLeftIconTypeV2 } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: EditableTitleV2Options)
```

Constructor of EditableTitleV2.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleV2-constructor(options?: EditableTitleV2Options)--><!--Device-EditableTitleV2-constructor(options?: EditableTitleV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EditableTitleV2Options](arkts-arkui-arkui-advanced-editabletitlebarv2-editabletitlev2options-i.md) | No | The options of the title |

## mainTitle

```TypeScript
public mainTitle: ResourceStr
```

Main title content.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Default:** ''

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleV2-public mainTitle: ResourceStr--><!--Device-EditableTitleV2-public mainTitle: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subTitle

```TypeScript
public subTitle?: ResourceStr
```

Subtitle content.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleV2-public subTitle?: ResourceStr--><!--Device-EditableTitleV2-public subTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

