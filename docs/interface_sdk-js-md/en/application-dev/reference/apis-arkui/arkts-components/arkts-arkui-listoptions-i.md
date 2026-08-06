# ListOptions

Defines the options of the **List** component.
    **NOTE**  
    
    To standardize anonymous object definitions, the element definitions here have been revised in API version 18.  
    While historical version information is preserved for anonymous objects, there may be cases where the outer element  
    's @since version number is higher than inner elements'. This does not affect interface usability.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface ListOptions--><!--Device-unnamed-interface ListOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialIndex

```TypeScript
initialIndex?: number
```

Index of the item to be displayed at the start when the list is initially loaded.Anonymous Object Rectification.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If the set value is a negative number or is greater than the index of the last item in the list,the value is invalid. In this case, the default value will be used.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_

**Type:** number

**Default:** 0 [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListOptions-initialIndex?: number--><!--Device-ListOptions-initialIndex?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

Scroller, which can be bound to scrollable components.Anonymous Object Rectification.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_The scroller cannot be bound to other scrollable components.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_

**Type:** Scroller

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListOptions-scroller?: Scroller--><!--Device-ListOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: number | string
```

Spacing between list items along the main axis.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **0**  
\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_If the parameter type is number, the unit is vp.Anonymous Object Rectification.

\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used.\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing.\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ Child components of \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_ whose \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_visibility\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ attribute is set to \_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_None\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_ are not displayed, but the spacing above and below them still takes effect.\_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_

**Type:** number \| string

**Default:** 0 [since 18]

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ListOptions-space?: number | string--><!--Device-ListOptions-space?: number | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spaceWidth

```TypeScript
spaceWidth?: Dimension
```

Spacing between list items along the main axis.

\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ Child components of \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ListItemGroup\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ whose \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_visibility\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_ attribute is set to \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_None\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_are not displayed, but the spacing above and below them still takes effect.\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_ If both spaceWidth and space are set, spaceWidth will take precedence.\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_

**Type:** Dimension

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-ListOptions-spaceWidth?: Dimension--><!--Device-ListOptions-spaceWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

