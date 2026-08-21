# AlertDialogV2

Declare CustomDialog AlertDialogV2.

@struct { AlertDialogV2 }

**Since:** 18

<!--Device-unnamed-export declare struct AlertDialogV2--><!--Device-unnamed-export declare struct AlertDialogV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonOptions, AdvancedDialogV2ButtonAction, AdvancedDialogV2OnCheckedChange, ConfirmDialogV2, LoadingDialogV2, SelectDialogV2, TipsDialogV2, CustomContentDialogV2, PopoverDialogV2, PopoverDialogV2OnVisibleChange, PopoverDialogV2Options } from '@kit.ArkUI';
```

## content

```TypeScript
@Require
  @Param
  content: ResourceStr
```

Sets the AlertDialogV2 content.

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AlertDialogV2-@Require  @Param  content: ResourceStr--><!--Device-AlertDialogV2-@Require  @Param  content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryButton

```TypeScript
@Param
  primaryButton?: AdvancedDialogV2Button
```

Sets the AlertDialogV2 primary button.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkuiadvanceddialogv2-advanceddialogv2button-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AlertDialogV2-@Param  primaryButton?: AdvancedDialogV2Button--><!--Device-AlertDialogV2-@Param  primaryButton?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
@Param
  primaryTitle?: ResourceStr
```

Sets the AlertDialogV2 title.

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AlertDialogV2-@Param  primaryTitle?: ResourceStr--><!--Device-AlertDialogV2-@Param  primaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryButton

```TypeScript
@Param
  secondaryButton?: AdvancedDialogV2Button
```

Sets the AlertDialogV2 secondary button.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkuiadvanceddialogv2-advanceddialogv2button-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AlertDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button--><!--Device-AlertDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
@Param
  secondaryTitle?: ResourceStr
```

Sets the AlertDialogV2 secondary title.

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AlertDialogV2-@Param  secondaryTitle?: ResourceStr--><!--Device-AlertDialogV2-@Param  secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

