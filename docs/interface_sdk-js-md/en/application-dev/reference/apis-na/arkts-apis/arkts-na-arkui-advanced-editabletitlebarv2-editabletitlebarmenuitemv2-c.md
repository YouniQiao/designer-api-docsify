# EditableTitleBarMenuItemV2

Declaration of the menu item on the right side.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare class EditableTitleBarMenuItemV2--><!--Device-unnamed-export declare class EditableTitleBarMenuItemV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options?: EditableTitleBarMenuItemV2Options)
```

Constructor of EditableTitleBarMenuItemV2.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-constructor(options?: EditableTitleBarMenuItemV2Options)--><!--Device-EditableTitleBarMenuItemV2-constructor(options?: EditableTitleBarMenuItemV2Options)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EditableTitleBarMenuItemV2Options](arkts-na-arkui-advanced-editabletitlebarv2-editabletitlebarmenuitemv2options-i.md) | No | The options of the menu item |

## accessibilityDescription

```TypeScript
@Trace
  public accessibilityDescription?: ResourceStr
```

Accessibility description.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public accessibilityDescription?: ResourceStr--><!--Device-EditableTitleBarMenuItemV2-@Trace  public accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  public accessibilityLevel: string
```

Accessibility level, options: 'auto', 'yes', 'no'.

**Type:** string

**Default:** 'auto'

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public accessibilityLevel: string--><!--Device-EditableTitleBarMenuItemV2-@Trace  public accessibilityLevel: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  public accessibilityText?: ResourceStr
```

Accessibility text for screen reader.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public accessibilityText?: ResourceStr--><!--Device-EditableTitleBarMenuItemV2-@Trace  public accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
@Trace
  public action?: OnActionCallback
```

Callback function when click on this menu item.

**Type:** [OnActionCallback](arkts-na-onactioncallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public action?: OnActionCallback--><!--Device-EditableTitleBarMenuItemV2-@Trace  public action?: OnActionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## defaultFocus

```TypeScript
@Trace
  public defaultFocus: boolean
```

Whether to get focus by default.

**Type:** boolean

**Default:** false

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public defaultFocus: boolean--><!--Device-EditableTitleBarMenuItemV2-@Trace  public defaultFocus: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isEnabled

```TypeScript
@Trace
  public isEnabled: boolean
```

Whether to enable this menu item.

**Type:** boolean

**Default:** true

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public isEnabled: boolean--><!--Device-EditableTitleBarMenuItemV2-@Trace  public isEnabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
@Trace
  public label?: ResourceStr
```

Label text for long press dialog.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public label?: ResourceStr--><!--Device-EditableTitleBarMenuItemV2-@Trace  public label?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
@Trace
  public symbolStyle?: SymbolGlyphModifier
```

Symbol icon style modifier.

**Type:** SymbolGlyphModifier

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public symbolStyle?: SymbolGlyphModifier--><!--Device-EditableTitleBarMenuItemV2-@Trace  public symbolStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
@Trace
  public value: ResourceStr
```

Icon resource, supports Symbol or Image.

**Type:** ResourceStr

**Default:** ''

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditableTitleBarMenuItemV2-@Trace  public value: ResourceStr--><!--Device-EditableTitleBarMenuItemV2-@Trace  public value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

