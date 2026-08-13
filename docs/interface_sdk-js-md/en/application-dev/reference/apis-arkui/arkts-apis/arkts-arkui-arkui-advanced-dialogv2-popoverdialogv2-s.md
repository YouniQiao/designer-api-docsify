# PopoverDialogV2

Declare struct PopoverDialogV2

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct PopoverDialogV2--><!--Device-unnamed-export declare struct PopoverDialogV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AdvancedDialogV2OnCheckedChange, LoadingDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonAction, AlertDialogV2, CustomContentDialogV2, PopoverDialogV2Options, PopoverDialogV2, SelectDialogV2, PopoverDialogV2OnVisibleChange, TipsDialogV2, AdvancedDialogV2ButtonOptions, ConfirmDialogV2 } from '@kit.ArkUI';
```

## $visible

```TypeScript
@Event
  $visible?: PopoverDialogV2OnVisibleChange
```

Sets the callback when visibility changed.

**Type:** [PopoverDialogV2OnVisibleChange](arkts-arkui-popoverdialogv2onvisiblechange-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PopoverDialogV2-@Event  $visible?: PopoverDialogV2OnVisibleChange--><!--Device-PopoverDialogV2-@Event  $visible?: PopoverDialogV2OnVisibleChange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## popover

```TypeScript
@Require
  @Param
  popover: PopoverDialogV2Options
```

Sets the PopoverDialogV2 options.

**Type:** [PopoverDialogV2Options](arkts-arkui-arkui-advanced-dialogv2-popoverdialogv2options-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PopoverDialogV2-@Require  @Param  popover: PopoverDialogV2Options--><!--Device-PopoverDialogV2-@Require  @Param  popover: PopoverDialogV2Options-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetBuilder

```TypeScript
@BuilderParam
  targetBuilder: CustomBuilder
```

Sets the targetBuilder content.

**Type:** CustomBuilder

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PopoverDialogV2-@BuilderParam  targetBuilder: CustomBuilder--><!--Device-PopoverDialogV2-@BuilderParam  targetBuilder: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
@Require
  @Param
  visible: boolean
```

Sets the PopoverDialogV2 Visible Status.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PopoverDialogV2-@Require  @Param  visible: boolean--><!--Device-PopoverDialogV2-@Require  @Param  visible: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

