# TipsDialogV2

Declare CustomDialog TipsDialogV2@struct { TipsDialogV2 }

**Since:** 18

**Decorator:** @ComponentV2

<!--Device-unnamed-export declare struct TipsDialogV2--><!--Device-unnamed-export declare struct TipsDialogV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonOptions, AdvancedDialogV2ButtonAction, AdvancedDialogV2OnCheckedChange, ConfirmDialogV2, LoadingDialogV2, SelectDialogV2, TipsDialogV2, CustomContentDialogV2, PopoverDialogV2, PopoverDialogV2OnVisibleChange, PopoverDialogV2Options } from '@kit.ArkUI';
```

## checked

```TypeScript
checked?: boolean
```

Sets the TipsDialogV2 checkbox check state.

**Type:** boolean

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  checked?: boolean--><!--Device-TipsDialogV2-@Param  checked?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## checkTips

```TypeScript
checkTips?: ResourceStr
```

Sets the TipsDialogV2 checkbox tips.

**Type:** ResourceStr

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  checkTips?: ResourceStr--><!--Device-TipsDialogV2-@Param  checkTips?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content?: ResourceStr
```

Sets the TipsDialogV2 content.

**Type:** ResourceStr

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  content?: ResourceStr--><!--Device-TipsDialogV2-@Param  content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageBorderColor

```TypeScript
imageBorderColor?: ColorMetrics
```

Sets the borderColor of TipsDialogV2 image.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  imageBorderColor?: ColorMetrics--><!--Device-TipsDialogV2-@Param  imageBorderColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageBorderWidth

```TypeScript
imageBorderWidth?: LengthMetrics
```

Sets the borderWidth of TipsDialogV2 image.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  imageBorderWidth?: LengthMetrics--><!--Device-TipsDialogV2-@Param  imageBorderWidth?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageRes

```TypeScript
imageRes: ResourceStr | PixelMap
```

Sets the TipsDialogV2 imageRes.

**Type:** ResourceStr \| PixelMap

**Since:** 18

**Decorator:** @Require, @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Require  @Param  imageRes: ResourceStr | PixelMap--><!--Device-TipsDialogV2-@Require  @Param  imageRes: ResourceStr | PixelMap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSize

```TypeScript
imageSize?: SizeOptions
```

Sets the TipsDialogV2 image size.

**Type:** SizeOptions

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  imageSize?: SizeOptions--><!--Device-TipsDialogV2-@Param  imageSize?: SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCheckedChange

```TypeScript
onCheckedChange?: AdvancedDialogV2OnCheckedChange
```

Sets the TipsDialogV2 CheckBox Callback.

**Type:** [AdvancedDialogV2OnCheckedChange](arkts-arkui-advanceddialogv2oncheckedchange-t.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  onCheckedChange?: AdvancedDialogV2OnCheckedChange--><!--Device-TipsDialogV2-@Param  onCheckedChange?: AdvancedDialogV2OnCheckedChange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryButton

```TypeScript
primaryButton?: AdvancedDialogV2Button
```

Sets the TipsDialogV2 primary button.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  primaryButton?: AdvancedDialogV2Button--><!--Device-TipsDialogV2-@Param  primaryButton?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryButton

```TypeScript
secondaryButton?: AdvancedDialogV2Button
```

Sets the TipsDialogV2 secondary button.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button--><!--Device-TipsDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: ResourceStr
```

Sets the TipsDialogV2 title.

**Type:** ResourceStr

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  title?: ResourceStr--><!--Device-TipsDialogV2-@Param  title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

