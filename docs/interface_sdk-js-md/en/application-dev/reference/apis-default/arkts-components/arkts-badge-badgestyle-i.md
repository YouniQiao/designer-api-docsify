# BadgeStyle

Describes the badge style. It includes the font color, font size, badge color, badge size, etc.

> **NOTE：**
> 
> - When **borderWidth** is set to a value greater than 0 and **borderColor** is different from **badgeColor**, the &gt; badge is drawn before the border. Edge pixels are anti-aliased, which produces semi-transparent pixels. This causes &gt; the border in **badgeColor** to become visible at the four corners. To implement related scenarios, it is &gt; recommended that you use the Text component with its &gt; outline attribute instead of the **Badge** component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface BadgeStyle--><!--Device-unnamed-export declare interface BadgeStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## badgeColor

```TypeScript
badgeColor?: ResourceColor
```

Badge color. Default value: Color.Red .

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.Red

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-badgeColor?: ResourceColor--><!--Device-BadgeStyle-badgeColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## badgeSize

```TypeScript
badgeSize?: double | ResourceStr
```

Size of a badge. Default value: 16vp.

**Type:** double \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-badgeSize?: double | ResourceStr--><!--Device-BadgeStyle-badgeSize?: double | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor
```

Border color of the background. Default value: Color.Red.

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.Red

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-borderColor?: ResourceColor--><!--Device-BadgeStyle-borderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Length
```

Baseplate stroke thickness. The percentage cannot be set. When the percentage is set, the default value is used. Unit: vp. Default value: 1.

**Type:** [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md)

**Default:** 1

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-borderWidth?: Length--><!--Device-BadgeStyle-borderWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

Font color. Default value: Color.White.

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.White

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-color?: ResourceColor--><!--Device-BadgeStyle-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableAutoAvoidance

```TypeScript
enableAutoAvoidance?: boolean
```

Enable auto-avoidance for text in badge. Default value: false. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: 1. The avoidance effect is that the text of the corner mark extends to the interior of the component. 2. When the width of the outer stroke is greater than 0, the extension start point of the corner mark is the inner side of the outer stroke. 3. When position is set to a specific coordinate value, corner marks are not avoided.

**Type:** boolean

**Default:** false

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-enableAutoAvoidance?: boolean--><!--Device-BadgeStyle-enableAutoAvoidance?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: double | ResourceStr
```

Text size. Default value: 10vp.

**Type:** double \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-fontSize?: double | ResourceStr--><!--Device-BadgeStyle-fontSize?: double | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: int | FontWeight | ResourceStr
```

Define the font weight of the badge. Default value: FontWeight.Normal. <br>Value range of the number type: [100, 900], with an interval of 100. A larger value indicates a thicker font. If the number type is out of the value range, the default value 400 is used. The value of the string type must be a string of values of the number type, for example, 400. The values of bold, bolter, lighter, regular, and medium correspond to the corresponding enumerated values in FontWeight, respectively.

**Type:** int \| [FontWeight](../../apis-arkui/arkts-apis/arkts-arkui-fontweight-e.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-fontWeight?: int | FontWeight | ResourceStr--><!--Device-BadgeStyle-fontWeight?: int | FontWeight | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outerBorderColor

```TypeScript
outerBorderColor?: ResourceColor
```

Outer border color of the background. Default value: Color.White.

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.White

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-outerBorderColor?: ResourceColor--><!--Device-BadgeStyle-outerBorderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outerBorderWidth

```TypeScript
outerBorderWidth?: LengthMetrics
```

Outer border width of the background. Default value: 0 Unit: vp The percentage cannot be set. When the percentage is set, the default value is used.

**Type:** [LengthMetrics](../../apis-arkui/arkts-apis/arkts-arkui-lengthmetrics-t.md)

**Default:** 0

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-outerBorderWidth?: LengthMetrics--><!--Device-BadgeStyle-outerBorderWidth?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

