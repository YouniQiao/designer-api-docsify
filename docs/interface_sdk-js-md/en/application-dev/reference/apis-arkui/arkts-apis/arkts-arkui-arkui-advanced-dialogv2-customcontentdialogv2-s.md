# CustomContentDialogV2

Declare custom content dialog

**Since:** 18

<!--Device-unnamed-export declare struct CustomContentDialogV2--><!--Device-unnamed-export declare struct CustomContentDialogV2-End-->

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

## buttons

```TypeScript
@Param
  buttons?: AdvancedDialogV2Button[]
```

Sets the CustomContentDialogV2 buttons.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)[]

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CustomContentDialogV2-@Param  buttons?: AdvancedDialogV2Button[]--><!--Device-CustomContentDialogV2-@Param  buttons?: AdvancedDialogV2Button[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentAreaPadding

```TypeScript
@Param
  contentAreaPadding?: LocalizedPadding
```

Sets the CustomContentDialogV2 content area padding.

**Type:** LocalizedPadding

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CustomContentDialogV2-@Param  contentAreaPadding?: LocalizedPadding--><!--Device-CustomContentDialogV2-@Param  contentAreaPadding?: LocalizedPadding-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentBuilder

```TypeScript
@BuilderParam
  contentBuilder: CustomBuilder
```

Sets the CustomContentDialogV2 content.

**Type:** CustomBuilder

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CustomContentDialogV2-@BuilderParam  contentBuilder: CustomBuilder--><!--Device-CustomContentDialogV2-@BuilderParam  contentBuilder: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryTitle

```TypeScript
@Param
  primaryTitle?: ResourceStr
```

Sets the CustomContentDialogV2 title.

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CustomContentDialogV2-@Param  primaryTitle?: ResourceStr--><!--Device-CustomContentDialogV2-@Param  primaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryTitle

```TypeScript
@Param
  secondaryTitle?: ResourceStr
```

Sets the CustomContentDialogV2 secondary title.

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CustomContentDialogV2-@Param  secondaryTitle?: ResourceStr--><!--Device-CustomContentDialogV2-@Param  secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

