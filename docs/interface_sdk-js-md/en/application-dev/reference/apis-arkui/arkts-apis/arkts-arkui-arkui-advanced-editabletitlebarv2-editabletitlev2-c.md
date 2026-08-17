# EditableTitleV2

Declaration of the title configuration.

**Since:** 26.0.0

<!--Device-unnamed-export declare class EditableTitleV2--><!--Device-unnamed-export declare class EditableTitleV2-End-->

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
constructor(options?: EditableTitleV2Options)
```

Constructor of EditableTitleV2.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleV2-constructor(options?: EditableTitleV2Options)--><!--Device-EditableTitleV2-constructor(options?: EditableTitleV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EditableTitleV2Options](../../apis-na/arkts-apis/arkts-na-arkui-advanced-editabletitlebarv2-editabletitlev2options-i.md) | No | The options of the title |

## mainTitle

```TypeScript
@Trace
  public mainTitle: ResourceStr
```

Main title content.

**Type:** ResourceStr

**Default:** ''

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleV2-@Trace  public mainTitle: ResourceStr--><!--Device-EditableTitleV2-@Trace  public mainTitle: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subTitle

```TypeScript
@Trace
  public subTitle?: ResourceStr
```

Subtitle content.

**Type:** ResourceStr

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-EditableTitleV2-@Trace  public subTitle?: ResourceStr--><!--Device-EditableTitleV2-@Trace  public subTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

