# TipsDialogV2

Declare CustomDialog TipsDialogV2

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct TipsDialogV2--><!--Device-unnamed-export declare struct TipsDialogV2-End-->

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

## checkTips

```TypeScript
@Param
  checkTips?: ResourceStr
```

Sets the TipsDialogV2 checkbox tips.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  checkTips?: ResourceStr--><!--Device-TipsDialogV2-@Param  checkTips?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## checked

```TypeScript
@Param
  checked?: boolean
```

Sets the TipsDialogV2 checkbox check state.

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  checked?: boolean--><!--Device-TipsDialogV2-@Param  checked?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Param
  content?: ResourceStr
```

Sets the TipsDialogV2 content.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  content?: ResourceStr--><!--Device-TipsDialogV2-@Param  content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageBorderColor

```TypeScript
@Param
  imageBorderColor?: ColorMetrics
```

Sets the borderColor of TipsDialogV2 image.

**Type:** [ColorMetrics](../../apis-na/arkts-apis/arkts-na-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  imageBorderColor?: ColorMetrics--><!--Device-TipsDialogV2-@Param  imageBorderColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageBorderWidth

```TypeScript
@Param
  imageBorderWidth?: LengthMetrics
```

Sets the borderWidth of TipsDialogV2 image.

**Type:** [LengthMetrics](../../apis-na/arkts-apis/arkts-na-graphics-lengthmetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  imageBorderWidth?: LengthMetrics--><!--Device-TipsDialogV2-@Param  imageBorderWidth?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageRes

```TypeScript
@Require
  @Param
  imageRes: ResourceStr | PixelMap
```

Sets the TipsDialogV2 imageRes.

**Type:** ResourceStr \| PixelMap

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Require  @Param  imageRes: ResourceStr | PixelMap--><!--Device-TipsDialogV2-@Require  @Param  imageRes: ResourceStr | PixelMap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## imageSize

```TypeScript
@Param
  imageSize?: SizeOptions
```

Sets the TipsDialogV2 image size.

**Type:** SizeOptions

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  imageSize?: SizeOptions--><!--Device-TipsDialogV2-@Param  imageSize?: SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCheckedChange

```TypeScript
@Param
  onCheckedChange?: AdvancedDialogV2OnCheckedChange
```

Sets the TipsDialogV2 CheckBox Callback.

**Type:** [AdvancedDialogV2OnCheckedChange](arkts-arkui-advanceddialogv2oncheckedchange-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  onCheckedChange?: AdvancedDialogV2OnCheckedChange--><!--Device-TipsDialogV2-@Param  onCheckedChange?: AdvancedDialogV2OnCheckedChange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primaryButton

```TypeScript
@Param
  primaryButton?: AdvancedDialogV2Button
```

Sets the TipsDialogV2 primary button.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  primaryButton?: AdvancedDialogV2Button--><!--Device-TipsDialogV2-@Param  primaryButton?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondaryButton

```TypeScript
@Param
  secondaryButton?: AdvancedDialogV2Button
```

Sets the TipsDialogV2 secondary button.

**Type:** [AdvancedDialogV2Button](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2button-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button--><!--Device-TipsDialogV2-@Param  secondaryButton?: AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
@Param
  title?: ResourceStr
```

Sets the TipsDialogV2 title.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TipsDialogV2-@Param  title?: ResourceStr--><!--Device-TipsDialogV2-@Param  title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

