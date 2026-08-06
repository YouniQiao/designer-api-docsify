# ListOptions

Defines the options of the \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ component.

\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_:\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_- The default value of the universal attribute clip is \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_true\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ for the \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_ component.\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ListOptions--><!--Device-unnamed-export interface ListOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialIndex

```TypeScript
initialIndex?: int
```

Index of the item to be displayed at the start when the list is initially loaded.Anonymous Object Rectification.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_.The value should be an integer.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If the set value is a negative number or is greater than the index of the last item in the list,the value is invalid. In this case, the default value will be used.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-initialIndex?: int--><!--Device-ListOptions-initialIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

Scroller, which can be bound to scrollable components.Anonymous Object Rectification.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_The scroller cannot be bound to other scrollable components.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_

**Type:** Scroller

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-scroller?: Scroller--><!--Device-ListOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: double | string
```

Spacing between list items along the main axis.Anonymous Object Rectification.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ Child components of \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ whose \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_visibility\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_ attribute is set to \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_None\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ are not displayed, but the spacing above and below them still takes effect.\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_

**Type:** double \| string

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-space?: double | string--><!--Device-ListOptions-space?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spaceWidth

```TypeScript
spaceWidth?: Dimension
```

Spacing between list items along the main axis.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used.\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing.\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_ Child components of \_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_List\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_ whose \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_visibility\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_ attribute is set to \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_None\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ are not displayed, but the spacing above and below them still takes effect.\_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_ If both spaceWidth and space are set, spaceWidth will take precedence.\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_

**Type:** Dimension

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-spaceWidth?: Dimension--><!--Device-ListOptions-spaceWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

