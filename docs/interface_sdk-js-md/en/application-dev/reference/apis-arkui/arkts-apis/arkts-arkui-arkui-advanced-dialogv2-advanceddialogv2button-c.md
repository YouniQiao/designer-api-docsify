# AdvancedDialogV2Button

Declare AdvancedDialogV2Button.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare class AdvancedDialogV2Button--><!--Device-unnamed-export declare class AdvancedDialogV2Button-End-->

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

## constructor

```TypeScript
constructor(options: AdvancedDialogV2ButtonOptions)
```

The constructor used to create a AdvancedDialogV2Button object.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-constructor(options: AdvancedDialogV2ButtonOptions)--><!--Device-AdvancedDialogV2Button-constructor(options: AdvancedDialogV2ButtonOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AdvancedDialogV2ButtonOptions](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2buttonoptions-i.md) | Yes | button info. |

## action

```TypeScript
@Trace
  action?: AdvancedDialogV2ButtonAction
```

Sets the Button Callback.

**Type:** [AdvancedDialogV2ButtonAction](arkts-arkui-advanceddialogv2buttonaction-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  action?: AdvancedDialogV2ButtonAction--><!--Device-AdvancedDialogV2Button-@Trace  action?: AdvancedDialogV2ButtonAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## background

```TypeScript
@Trace
  background?: ColorMetrics
```

Sets the background color of a button.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  background?: ColorMetrics--><!--Device-AdvancedDialogV2Button-@Trace  background?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
@Trace
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

<!--Device-AdvancedDialogV2Button-@Trace  buttonStyle?: ButtonStyleMode--><!--Device-AdvancedDialogV2Button-@Trace  buttonStyle?: ButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Trace
  content: ResourceStr
```

Sets the Display Content of a Button.

**Type:** ResourceStr

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  content: ResourceStr--><!--Device-AdvancedDialogV2Button-@Trace  content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
@Trace
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

<!--Device-AdvancedDialogV2Button-@Trace  defaultFocus?: boolean--><!--Device-AdvancedDialogV2Button-@Trace  defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
@Trace
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

<!--Device-AdvancedDialogV2Button-@Trace  enabled?: boolean--><!--Device-AdvancedDialogV2Button-@Trace  enabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
@Trace
  fontColor?: ColorMetrics
```

Sets the Button Text Color.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  fontColor?: ColorMetrics--><!--Device-AdvancedDialogV2Button-@Trace  fontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## role

```TypeScript
@Trace
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

<!--Device-AdvancedDialogV2Button-@Trace  role?: ButtonRole--><!--Device-AdvancedDialogV2Button-@Trace  role?: ButtonRole-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
@Trace
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

<!--Device-AdvancedDialogV2Button-@Trace  textAlign?: TextAlign--><!--Device-AdvancedDialogV2Button-@Trace  textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

