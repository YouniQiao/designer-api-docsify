# AlertDialogV2

Declare CustomDialog AlertDialogV2.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct AlertDialogV2--><!--Device-unnamed-export declare struct AlertDialogV2-End-->

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

## content

```TypeScript
@Require
  @Param
  content: ResourceStr
```

Sets the AlertDialogV2 content.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AlertDialogV2-@Param  secondaryTitle?: ResourceStr--><!--Device-AlertDialogV2-@Param  secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

