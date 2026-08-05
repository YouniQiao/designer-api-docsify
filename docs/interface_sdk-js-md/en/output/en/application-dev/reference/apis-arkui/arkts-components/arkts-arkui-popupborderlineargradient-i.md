# PopupBorderLinearGradient

Sets the color and direction of the linear gradient for the outlines.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare interface PopupBorderLinearGradient--><!--Device-unnamed-declare interface PopupBorderLinearGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colors

```TypeScript
colors: Array<[ResourceColor, number]>
```

Array of color stops, each of which consists of a color and its stop position. Invalid colors are automatically skipped. **NOTE** For details about how to set colors, see [ResourceColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. Colors that are not within the types of [ResourceColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ are invalid. If the color in the array is set to **undefined** or **null**, the default color is black. When using the **colors** parameter, take note of the following: [ResourceColor]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ indicates the color, and **number** indicates the color's position, which ranges from 0 to 1.0: **0** indicates the start of the gradient color container, and **1.0** indicates the end of the container. To create a gradient with multiple color stops, you are advised to set the **number** values in ascending order. If a value of **number** in an array is smaller than that in the previous one, the value of **number** in the previous array is used.

**Type:** Array&lt;[ResourceColor, number]&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PopupBorderLinearGradient-colors: Array<[ResourceColor, number]>--><!--Device-PopupBorderLinearGradient-colors: Array<[ResourceColor, number]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: GradientDirection
```

Direction of the linear gradient. Default value: **GradientDirection.Bottom** **NOTE** When the direction is set to **GradientDirection.None**, the default value is used.

**Type:** GradientDirection

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PopupBorderLinearGradient-direction?: GradientDirection--><!--Device-PopupBorderLinearGradient-direction?: GradientDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

