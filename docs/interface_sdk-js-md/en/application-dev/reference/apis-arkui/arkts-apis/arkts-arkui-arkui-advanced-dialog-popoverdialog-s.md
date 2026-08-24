# PopoverDialog

Declare struct PopoverDialog

**Since:** 14

**Decorator:** @Component

<!--Device-unnamed-export declare struct PopoverDialog--><!--Device-unnamed-export declare struct PopoverDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialog, ButtonOptions, ConfirmDialog, LoadingDialog, SelectDialog, TipsDialog, CustomContentDialog, PopoverDialog, PopoverOptions } from '@kit.ArkUI';
```

## popover

```TypeScript
popover: PopoverOptions
```

Sets the PopoverDialog options.

**Type:** [PopoverOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-dialog-popoveroptions-i.md)

**Since:** 14

**Decorator:** @Require, @Prop

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PopoverDialog-@Require @Prop  popover: PopoverOptions--><!--Device-PopoverDialog-@Require @Prop  popover: PopoverOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetBuilder

```TypeScript
targetBuilder: Callback<void>
```

Sets the targetBuilder content.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt;

**Since:** 14

**Decorator:** @Require, @BuilderParam

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PopoverDialog-@Require @BuilderParam   targetBuilder: Callback<void>--><!--Device-PopoverDialog-@Require @BuilderParam   targetBuilder: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
visible: boolean
```

Sets the PopoverDialog Visible Status.

**Type:** boolean

**Since:** 14

**Decorator:** @Link

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-PopoverDialog-@Link  visible: boolean--><!--Device-PopoverDialog-@Link  visible: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

