# AdvancedDialogV2Button

Declare AdvancedDialogV2Button.

**Since:** 18

**Deprecated since:** -1

<!--Device-unnamed-export declare class AdvancedDialogV2Button--><!--Device-unnamed-export declare class AdvancedDialogV2Button-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AdvancedDialogV2OnCheckedChange, LoadingDialogV2, AdvancedDialogV2Button, AdvancedDialogV2ButtonAction, AlertDialogV2, CustomContentDialogV2, PopoverDialogV2Options, PopoverDialogV2, SelectDialogV2, PopoverDialogV2OnVisibleChange, TipsDialogV2, AdvancedDialogV2ButtonOptions, ConfirmDialogV2 } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: AdvancedDialogV2ButtonOptions)
```

The constructor used to create a AdvancedDialogV2Button object.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AdvancedDialogV2Button-constructor(options: AdvancedDialogV2ButtonOptions)--><!--Device-AdvancedDialogV2Button-constructor(options: AdvancedDialogV2ButtonOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AdvancedDialogV2ButtonOptions](arkts-arkui-arkui-advanced-dialogv2-advanceddialogv2buttonoptions-i.md) | Yes |

## action

```TypeScript
@Trace
  action?: AdvancedDialogV2ButtonAction
```

Sets the Button Callback.

**Type:** [AdvancedDialogV2ButtonAction](arkts-arkui-advanceddialogv2buttonaction-t.md)

**Since:** 18

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

**Type:** ColorMetrics

**Since:** 18

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

**Type:** [ButtonStyleMode](../arkts-components/arkts-arkui-buttonstylemode-e.md)

**Default:** ButtonStyleMode.TEXTUAL

**Since:** 18

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

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

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

**Type:** ColorMetrics

**Since:** 18

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

**Type:** [ButtonRole](../arkts-components/arkts-arkui-buttonrole-e.md)

**Default:** ButtonRole.NORMAL

**Since:** 18

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AdvancedDialogV2Button-@Trace  textAlign?: TextAlign--><!--Device-AdvancedDialogV2Button-@Trace  textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
