# AdvancedDialogV2ButtonOptions

Declare the options of AdvancedDialogV2Button

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface AdvancedDialogV2ButtonOptions--><!--Device-unnamed-export declare interface AdvancedDialogV2ButtonOptions-End-->

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

## action

```TypeScript
action?: AdvancedDialogV2ButtonAction
```

Sets the Button Callback.

**Type:** [AdvancedDialogV2ButtonAction](arkts-arkui-advanceddialogv2buttonaction-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2ButtonOptions-action?: AdvancedDialogV2ButtonAction--><!--Device-AdvancedDialogV2ButtonOptions-action?: AdvancedDialogV2ButtonAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## background

```TypeScript
background?: ColorMetrics
```

Sets the background color of a button.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2ButtonOptions-background?: ColorMetrics--><!--Device-AdvancedDialogV2ButtonOptions-background?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
buttonStyle?: ButtonStyleMode
```

Describes the Button style.

**Type:** ButtonStyleMode

**Default:** ButtonStyleMode.TEXTUAL

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2ButtonOptions-buttonStyle?: ButtonStyleMode--><!--Device-AdvancedDialogV2ButtonOptions-buttonStyle?: ButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: ResourceStr
```

Sets the Display Content of a Button.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2ButtonOptions-content: ResourceStr--><!--Device-AdvancedDialogV2ButtonOptions-content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
defaultFocus?: boolean
```

Set the default focus of a button.

**Type:** boolean

**Default:** { false }

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2ButtonOptions-defaultFocus?: boolean--><!--Device-AdvancedDialogV2ButtonOptions-defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
enabled?: boolean
```

Set the availability of the button.

**Type:** boolean

**Default:** { true }

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2ButtonOptions-enabled?: boolean--><!--Device-AdvancedDialogV2ButtonOptions-enabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ColorMetrics
```

Sets the Button Text Color.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2ButtonOptions-fontColor?: ColorMetrics--><!--Device-AdvancedDialogV2ButtonOptions-fontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## role

```TypeScript
role?: ButtonRole
```

Describes the Button role.

**Type:** ButtonRole

**Default:** ButtonRole.NORMAL

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2ButtonOptions-role?: ButtonRole--><!--Device-AdvancedDialogV2ButtonOptions-role?: ButtonRole-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

Set the alignment mode for the button label.

**Type:** TextAlign

**Default:** { TextAlign.Start }

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AdvancedDialogV2ButtonOptions-textAlign?: TextAlign--><!--Device-AdvancedDialogV2ButtonOptions-textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

