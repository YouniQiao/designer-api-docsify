# ComposeTitleBarV2MenuItem

Declaration of the menu item on the right side.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare class ComposeTitleBarV2MenuItem--><!--Device-unnamed-export declare class ComposeTitleBarV2MenuItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ComposeTitleBarV2 } from 'ComposeTitleBarV2';
import { ComposeTitleBarV2MenuItem } from 'ComposeTitleBarV2MenuItem';
import { ComposeTitleBarV2MenuItemParams } from 'ComposeTitleBarV2MenuItemParams';
```

## constructor

```TypeScript
constructor(params?: ComposeTitleBarV2MenuItemParams)
```

Constructor of ComposeTitleBarV2MenuItem.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-constructor(params?: ComposeTitleBarV2MenuItemParams)--><!--Device-ComposeTitleBarV2MenuItem-constructor(params?: ComposeTitleBarV2MenuItemParams)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ComposeTitleBarV2MenuItemParams](../../apis-na/arkts-apis/arkts-na-arkui-advanced-composetitlebarv2-composetitlebarv2menuitemparams-i.md) | No | Parameters for creating a menu item instance |

## accessibilityDescription

```TypeScript
@Trace
  accessibilityDescription?: ResourceStr
```

The accessibilityDescription of this menu item.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-@Trace  accessibilityDescription?: ResourceStr--><!--Device-ComposeTitleBarV2MenuItem-@Trace  accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
@Trace
  accessibilityLevel?: string
```

The accessibilityLevel of this menu item.

**Type:** string

**Default:** auto .The options are as follows:<br/> "auto":The value is converted to "yes" or "no" based on the component. "yes": the current component is selectable for the accessibility service. "no": The current component is not selectable for the accessibility service. "no-hide-descendants":The current component and all its child components are not selectable<br/> for the accessibility service.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-@Trace  accessibilityLevel?: string--><!--Device-ComposeTitleBarV2MenuItem-@Trace  accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
@Trace
  accessibilityText?: ResourceStr
```

The accessibilityText of this menu item.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-@Trace  accessibilityText?: ResourceStr--><!--Device-ComposeTitleBarV2MenuItem-@Trace  accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
@Trace
  action?: OnActionCallback
```

Callback function when click on this menu item.

**Type:** [OnActionCallback](../../apis-na/arkts-apis/arkts-na-onactioncallback-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-@Trace  action?: OnActionCallback--><!--Device-ComposeTitleBarV2MenuItem-@Trace  action?: OnActionCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isEnabled

```TypeScript
@Trace
  isEnabled?: boolean
```

Whether to enable this menu item.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-@Trace  isEnabled?: boolean--><!--Device-ComposeTitleBarV2MenuItem-@Trace  isEnabled?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## label

```TypeScript
@Trace
  label?: ResourceStr
```

Icon label for this menu item.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-@Trace  label?: ResourceStr--><!--Device-ComposeTitleBarV2MenuItem-@Trace  label?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolStyle

```TypeScript
@Trace
  symbolStyle?: SymbolGlyphModifier
```

Symbol icon resource for this menu item, which has higher priority than value.

**Type:** [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-@Trace  symbolStyle?: SymbolGlyphModifier--><!--Device-ComposeTitleBarV2MenuItem-@Trace  symbolStyle?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
@Trace
  value: ResourceStr
```

Icon resource for this menu item.

**Type:** ResourceStr

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ComposeTitleBarV2MenuItem-@Trace  value: ResourceStr--><!--Device-ComposeTitleBarV2MenuItem-@Trace  value: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

