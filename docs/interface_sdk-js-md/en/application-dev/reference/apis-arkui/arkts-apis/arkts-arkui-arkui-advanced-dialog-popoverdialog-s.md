# PopoverDialog

Declare struct PopoverDialog

**Since:** 14

<!--Device-unnamed-export declare struct PopoverDialog--><!--Device-unnamed-export declare struct PopoverDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialog, ButtonOptions, ConfirmDialog, LoadingDialog, SelectDialog, TipsDialog, CustomContentDialog, PopoverDialog, PopoverOptions } from '@kit.ArkUI';
import { AlertDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonOptions, AdvancedDialogV2ButtonAction, AdvancedDialogV2OnCheckedChange, ConfirmDialogV2, LoadingDialogV2, SelectDialogV2, TipsDialogV2, CustomContentDialogV2, PopoverDialogV2, PopoverDialogV2OnVisibleChange, PopoverDialogV2Options } from '@kit.ArkUI';
```

## popover

```TypeScript
@Require @Prop
  popover: PopoverOptions
```

Sets the PopoverDialog options.

**Type:** [PopoverOptions](arkts-arkui-arkui-advanced-dialog-popoveroptions-i.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PopoverDialog-@Require @Prop  popover: PopoverOptions--><!--Device-PopoverDialog-@Require @Prop  popover: PopoverOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetBuilder

```TypeScript
@Require @BuilderParam 
  targetBuilder: Callback<void>
```

Sets the targetBuilder content.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PopoverDialog-@Require @BuilderParam   targetBuilder: Callback<void>--><!--Device-PopoverDialog-@Require @BuilderParam   targetBuilder: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
@Link
  visible: boolean
```

Sets the PopoverDialog Visible Status.

**Type:** boolean

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PopoverDialog-@Link  visible: boolean--><!--Device-PopoverDialog-@Link  visible: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

