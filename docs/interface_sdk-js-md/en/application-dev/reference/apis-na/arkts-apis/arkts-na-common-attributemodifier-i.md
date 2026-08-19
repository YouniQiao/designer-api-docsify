# AttributeModifier

Defines the attribute modifier.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface AttributeModifier--><!--Device-unnamed-export declare interface AttributeModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## applyDisabledAttribute

```TypeScript
applyDisabledAttribute(instance: T) : void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-AttributeModifier-applyDisabledAttribute(instance: T) : void--><!--Device-AttributeModifier-applyDisabledAttribute(instance: T) : void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applyFocusedAttribute

```TypeScript
applyFocusedAttribute(instance: T) : void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-AttributeModifier-applyFocusedAttribute(instance: T) : void--><!--Device-AttributeModifier-applyFocusedAttribute(instance: T) : void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applyHoveredAttribute

```TypeScript
applyHoveredAttribute(instance: T) : void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-AttributeModifier-applyHoveredAttribute(instance: T) : void--><!--Device-AttributeModifier-applyHoveredAttribute(instance: T) : void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applyNormalAttribute

```TypeScript
applyNormalAttribute(instance: T) : void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-AttributeModifier-applyNormalAttribute(instance: T) : void--><!--Device-AttributeModifier-applyNormalAttribute(instance: T) : void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applyPressedAttribute

```TypeScript
applyPressedAttribute(instance: T) : void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-AttributeModifier-applyPressedAttribute(instance: T) : void--><!--Device-AttributeModifier-applyPressedAttribute(instance: T) : void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## applySelectedAttribute

```TypeScript
applySelectedAttribute(instance: T) : void
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-AttributeModifier-applySelectedAttribute(instance: T) : void--><!--Device-AttributeModifier-applySelectedAttribute(instance: T) : void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes |  |

## monitoredStates

```TypeScript
monitoredStates(): int
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-AttributeModifier-monitoredStates(): int--><!--Device-AttributeModifier-monitoredStates(): int-End-->

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Specifies the states to be monitored. Override this method to specify which states (Normal, Pressed, Focused, Disabled, Selected) should be monitoredby returning a bitmask of ModifierState enum values.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AttributeModifier-default--><!--Device-AttributeModifier-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

