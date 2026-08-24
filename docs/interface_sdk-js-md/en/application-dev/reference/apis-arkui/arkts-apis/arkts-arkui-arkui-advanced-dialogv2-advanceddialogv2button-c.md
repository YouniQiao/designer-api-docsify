# AdvancedDialogV2Button

Declare AdvancedDialogV2Button.@class AdvancedDialogV2Button

**Since:** 18

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class AdvancedDialogV2Button--><!--Device-unnamed-export declare class AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AlertDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonOptions, AdvancedDialogV2ButtonAction, AdvancedDialogV2OnCheckedChange, ConfirmDialogV2, LoadingDialogV2, SelectDialogV2, TipsDialogV2, CustomContentDialogV2, PopoverDialogV2, PopoverDialogV2OnVisibleChange, PopoverDialogV2Options } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: AdvancedDialogV2ButtonOptions)
```

The constructor used to create a AdvancedDialogV2Button object.

**Since:** 18

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
action?: AdvancedDialogV2ButtonAction
```

Sets the Button Callback.

**Type:** [AdvancedDialogV2ButtonAction](arkts-arkui-advanceddialogv2buttonaction-t.md)

**Since:** 18

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  action?: AdvancedDialogV2ButtonAction--><!--Device-AdvancedDialogV2Button-@Trace  action?: AdvancedDialogV2ButtonAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## background

```TypeScript
background?: ColorMetrics
```

Sets the background color of a button.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  background?: ColorMetrics--><!--Device-AdvancedDialogV2Button-@Trace  background?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
buttonStyle?: ButtonStyleMode
```

Describes the Button style.

**Type:** ButtonStyleMode

**Default:** ButtonStyleMode.TEXTUAL

**Since:** 18

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  buttonStyle?: ButtonStyleMode--><!--Device-AdvancedDialogV2Button-@Trace  buttonStyle?: ButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: ResourceStr
```

Sets the Display Content of a Button.

**Type:** ResourceStr

**Since:** 18

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  content: ResourceStr--><!--Device-AdvancedDialogV2Button-@Trace  content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
defaultFocus?: boolean
```

Set the default focus of a button.

**Type:** boolean

**Default:** { false }

**Since:** 18

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  defaultFocus?: boolean--><!--Device-AdvancedDialogV2Button-@Trace  defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
enabled?: boolean
```

Set the availability of the button.

**Type:** boolean

**Default:** { true }

**Since:** 18

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  enabled?: boolean--><!--Device-AdvancedDialogV2Button-@Trace  enabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ColorMetrics
```

Sets the Button Text Color.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  fontColor?: ColorMetrics--><!--Device-AdvancedDialogV2Button-@Trace  fontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## role

```TypeScript
role?: ButtonRole
```

Describes the Button role.

**Type:** ButtonRole

**Default:** ButtonRole.NORMAL

**Since:** 18

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-@Trace  role?: ButtonRole--><!--Device-AdvancedDialogV2Button-@Trace  role?: ButtonRole-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

Set the alignment mode for the button label.

**Type:** TextAlign

**Default:** { TextAlign.Start }

**Since:** 24

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AdvancedDialogV2Button-@Trace  textAlign?: TextAlign--><!--Device-AdvancedDialogV2Button-@Trace  textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

