# PopoverDialog

Declare struct PopoverDialog

**Since:** 14

**Deprecated since:** -1

<!--Device-unnamed-export declare struct PopoverDialog--><!--Device-unnamed-export declare struct PopoverDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialog, SelectDialog, ButtonOptions, PopoverOptions, TipsDialog, PopoverDialog, LoadingDialog, CustomContentDialog, ConfirmDialog } from '@kit.ArkUI';
```

## popover

```TypeScript
@Require @Prop
  popover: PopoverOptions
```

Sets the PopoverDialog options.

**Type:** [PopoverOptions](arkts-arkui-arkui-advanced-dialog-popoveroptions-i.md)

**Since:** 14

**Deprecated since:** -1

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

**Type:** Callback&lt;void&gt;

**Since:** 14

**Deprecated since:** -1

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PopoverDialog-@Link  visible: boolean--><!--Device-PopoverDialog-@Link  visible: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
