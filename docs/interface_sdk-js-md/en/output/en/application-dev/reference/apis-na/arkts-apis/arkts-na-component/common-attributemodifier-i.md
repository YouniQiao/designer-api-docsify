# AttributeModifier

Defines the attribute modifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AttributeModifier<T>--><!--Device-unnamed-export declare interface AttributeModifier<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyDisabledAttribute

```TypeScript
default applyDisabledAttribute(instance: T) : void
```

Defines the disabled update attribute function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttributeModifier-default applyDisabledAttribute(instance: T) : void--><!--Device-AttributeModifier-default applyDisabledAttribute(instance: T) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applyFocusedAttribute

```TypeScript
default applyFocusedAttribute(instance: T) : void
```

Defines the focused update attribute function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttributeModifier-default applyFocusedAttribute(instance: T) : void--><!--Device-AttributeModifier-default applyFocusedAttribute(instance: T) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applyHoveredAttribute

```TypeScript
default applyHoveredAttribute(instance: T) : void
```

Defines the function that updates the hovered attribute.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttributeModifier-default applyHoveredAttribute(instance: T) : void--><!--Device-AttributeModifier-default applyHoveredAttribute(instance: T) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applyNormalAttribute

```TypeScript
default applyNormalAttribute(instance: T) : void
```

Defines the normal update attribute function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttributeModifier-default applyNormalAttribute(instance: T) : void--><!--Device-AttributeModifier-default applyNormalAttribute(instance: T) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applyPressedAttribute

```TypeScript
default applyPressedAttribute(instance: T) : void
```

Defines the pressed update attribute function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttributeModifier-default applyPressedAttribute(instance: T) : void--><!--Device-AttributeModifier-default applyPressedAttribute(instance: T) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applySelectedAttribute

```TypeScript
default applySelectedAttribute(instance: T) : void
```

Defines the selected update attribute function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttributeModifier-default applySelectedAttribute(instance: T) : void--><!--Device-AttributeModifier-default applySelectedAttribute(instance: T) : void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## monitoredStates

```TypeScript
default monitoredStates(): int
```

Specifies the states to be monitored. Override this method to specify which states (Normal, Pressed, Focused, Disabled, Selected) should be monitoredby returning a bitmask of ModifierState enum values.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttributeModifier-default monitoredStates(): int--><!--Device-AttributeModifier-default monitoredStates(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | - Bitmask combination of states to be monitored |

