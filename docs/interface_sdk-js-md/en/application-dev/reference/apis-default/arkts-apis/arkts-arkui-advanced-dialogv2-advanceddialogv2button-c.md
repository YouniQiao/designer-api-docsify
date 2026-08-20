# AdvancedDialogV2Button

Declare AdvancedDialogV2Button.

@class AdvancedDialogV2Button

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class AdvancedDialogV2Button--><!--Device-unnamed-export declare class AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options: AdvancedDialogV2ButtonOptions)
```

The constructor used to create a AdvancedDialogV2Button object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-constructor(options: AdvancedDialogV2ButtonOptions)--><!--Device-AdvancedDialogV2Button-constructor(options: AdvancedDialogV2ButtonOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AdvancedDialogV2ButtonOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2buttonoptions-i.md) | Yes | button info. |

## action

```TypeScript
@Trace
  public action?: AdvancedDialogV2ButtonAction
```

Sets the Button Callback.

**Type:** [AdvancedDialogV2ButtonAction](../../apis-arkui/arkts-apis/arkts-arkui-advanceddialogv2buttonaction-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public action?: AdvancedDialogV2ButtonAction--><!--Device-AdvancedDialogV2Button-@Trace  public action?: AdvancedDialogV2ButtonAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## background

```TypeScript
@Trace
  public background?: ColorMetrics
```

Sets the background color of a button.

**Type:** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public background?: ColorMetrics--><!--Device-AdvancedDialogV2Button-@Trace  public background?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
@Trace
  public buttonStyle?: ButtonStyleMode
```

Describes the Button style.

**Type:** ButtonStyleMode

**Default:** ButtonStyleMode.TEXTUAL

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public buttonStyle?: ButtonStyleMode--><!--Device-AdvancedDialogV2Button-@Trace  public buttonStyle?: ButtonStyleMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Trace
  public content: ResourceStr
```

Sets the Display Content of a Button.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public content: ResourceStr--><!--Device-AdvancedDialogV2Button-@Trace  public content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
@Trace
  public defaultFocus?: boolean
```

Set the default focus of a button.

**Type:** boolean

**Default:** { false }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public defaultFocus?: boolean--><!--Device-AdvancedDialogV2Button-@Trace  public defaultFocus?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enabled

```TypeScript
@Trace
  public enabled?: boolean
```

Set the availability of the button.

**Type:** boolean

**Default:** { true }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public enabled?: boolean--><!--Device-AdvancedDialogV2Button-@Trace  public enabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
@Trace
  public fontColor?: ColorMetrics
```

Sets the Button Text Color.

**Type:** [ColorMetrics](arkts-graphics-colormetrics-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public fontColor?: ColorMetrics--><!--Device-AdvancedDialogV2Button-@Trace  public fontColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## role

```TypeScript
@Trace
  public role?: ButtonRole
```

Describes the Button role.

**Type:** ButtonRole

**Default:** ButtonRole.NORMAL

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public role?: ButtonRole--><!--Device-AdvancedDialogV2Button-@Trace  public role?: ButtonRole-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
@Trace
  public textAlign?: TextAlign
```

Set the alignment mode for the button label.

**Type:** TextAlign

**Default:** { TextAlign.Start }

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvancedDialogV2Button-@Trace  public textAlign?: TextAlign--><!--Device-AdvancedDialogV2Button-@Trace  public textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

