# CustomContentDialogV2

Declare custom content dialog

**Since:** 18

**Deprecated since:** -1

<!--Device-unnamed-export declare struct CustomContentDialogV2--><!--Device-unnamed-export declare struct CustomContentDialogV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AdvancedDialogV2OnCheckedChange, LoadingDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonAction, AlertDialogV2, CustomContentDialogV2, PopoverDialogV2Options, PopoverDialogV2, SelectDialogV2, PopoverDialogV2OnVisibleChange, TipsDialogV2, AdvancedDialogV2ButtonOptions, ConfirmDialogV2 } from '@kit.ArkUI';
```

## buttons

```TypeScript
@Param
  buttons?: AdvancedDialogV2Button[]
```

Sets the CustomContentDialogV2 buttons.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)[]

**Since:** 18

**Deprecated since:** -1

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

**Type:** [LocalizedPadding](arkts-arkui-localizedpadding-i.md)

**Since:** 18

**Deprecated since:** -1

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

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 18

**Deprecated since:** -1

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

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**Deprecated since:** -1

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

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CustomContentDialogV2-@Param  secondaryTitle?: ResourceStr--><!--Device-CustomContentDialogV2-@Param  secondaryTitle?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
