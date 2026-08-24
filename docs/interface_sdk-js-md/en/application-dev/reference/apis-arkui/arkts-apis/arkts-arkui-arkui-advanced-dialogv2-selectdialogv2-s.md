# SelectDialogV2

Declare CustomDialog SelectDialogV2@struct { SelectDialogV2 }

**Since:** 18

**Decorator:** @ComponentV2

<!--Device-unnamed-export declare struct SelectDialogV2--><!--Device-unnamed-export declare struct SelectDialogV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonOptions, AdvancedDialogV2ButtonAction, AdvancedDialogV2OnCheckedChange, ConfirmDialogV2, LoadingDialogV2, SelectDialogV2, TipsDialogV2, CustomContentDialogV2, PopoverDialogV2, PopoverDialogV2OnVisibleChange, PopoverDialogV2Options } from '@kit.ArkUI';
```

## confirm

```TypeScript
confirm?: AdvancedDialogV2Button
```

Sets the SelectDialogV2 confirm button.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Param  confirm?: AdvancedDialogV2Button--><!--Device-SelectDialogV2-@Param  confirm?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content?: ResourceStr
```

Sets the SelectDialogV2 content.

**Type:** ResourceStr

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Param  content?: ResourceStr--><!--Device-SelectDialogV2-@Param  content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## radioContent

```TypeScript
radioContent: SheetInfo[]
```

Sets the SelectDialog sheets.

**Type:** SheetInfo[]

**Since:** 18

**Decorator:** @Require, @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Require  @Param  radioContent: SheetInfo[]--><!--Device-SelectDialogV2-@Require  @Param  radioContent: SheetInfo[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndex

```TypeScript
selectedIndex?: number
```

Sets the SelectDialogV2 selected index.

**Type:** number

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Param  selectedIndex?: number--><!--Device-SelectDialogV2-@Param  selectedIndex?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title: ResourceStr
```

Sets the SelectDialogV2 title.

**Type:** ResourceStr

**Since:** 18

**Decorator:** @Require, @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SelectDialogV2-@Require  @Param  title: ResourceStr--><!--Device-SelectDialogV2-@Require  @Param  title: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

