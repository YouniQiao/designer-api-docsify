# SelectDialogV2

Declare CustomDialog SelectDialogV2

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct SelectDialogV2--><!--Device-unnamed-export declare struct SelectDialogV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialogV2 } from 'AlertDialogV2';
import { AdvancedDialogV2Button } from 'AdvancedDialogV2Button';
import { AdvancedDialogV2ButtonOptions } from 'AdvancedDialogV2ButtonOptions';
import { AdvancedDialogV2ButtonAction } from 'AdvancedDialogV2ButtonAction';
import { AdvancedDialogV2OnCheckedChange } from 'AdvancedDialogV2OnCheckedChange';
import { ConfirmDialogV2 } from 'ConfirmDialogV2';
import { LoadingDialogV2 } from 'LoadingDialogV2';
import { SelectDialogV2 } from 'SelectDialogV2';
import { TipsDialogV2 } from 'TipsDialogV2';
import { CustomContentDialogV2 } from 'CustomContentDialogV2';
import { PopoverDialogV2 } from 'PopoverDialogV2';
import { PopoverDialogV2OnVisibleChange } from 'PopoverDialogV2OnVisibleChange';
import { PopoverDialogV2Options } from 'PopoverDialogV2Options';
```

## confirm

```TypeScript
@Param
  confirm?: AdvancedDialogV2Button
```

Sets the SelectDialogV2 confirm button.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Param  confirm?: AdvancedDialogV2Button--><!--Device-SelectDialogV2-@Param  confirm?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Param
  content?: ResourceStr
```

Sets the SelectDialogV2 content.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Param  content?: ResourceStr--><!--Device-SelectDialogV2-@Param  content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radioContent

```TypeScript
@Require
  @Param
  radioContent: SheetInfo[]
```

Sets the SelectDialog sheets.

**Type:** SheetInfo[]

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Require  @Param  radioContent: SheetInfo[]--><!--Device-SelectDialogV2-@Require  @Param  radioContent: SheetInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
@Param
  selectedIndex?: number
```

Sets the SelectDialogV2 selected index.

**Type:** number

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Param  selectedIndex?: number--><!--Device-SelectDialogV2-@Param  selectedIndex?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
@Require
  @Param
  title: ResourceStr
```

Sets the SelectDialogV2 title.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Require  @Param  title: ResourceStr--><!--Device-SelectDialogV2-@Require  @Param  title: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

