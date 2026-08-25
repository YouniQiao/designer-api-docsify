# ListOptions

Defines the options of the &lt;em&gt;List&lt;/em&gt; component.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>- The default value of the universal attribute clip is &lt;em&gt;true&lt;/em&gt; for the &lt;em&gt;List&lt;/em&gt; component. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialIndex

```TypeScript
initialIndex?: int
```

Index of the item to be displayed at the start when the list is initially loaded. Anonymous Object Rectification. <p>&lt;strong&gt;NOTE&lt;/strong&gt;. The value should be an integer. <br>If the set value is a negative number or is greater than the index of the last item in the list, the value is invalid. In this case, the default value will be used. </p>

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

Scroller, which can be bound to scrollable components. Anonymous Object Rectification. <p>&lt;strong&gt;NOTE&lt;/strong&gt;. <br>The scroller cannot be bound to other scrollable components. </p>

**Type:** [Scroller](../arkts-components/arkts-arkui-scroller-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: double | string
```

Spacing between list items along the main axis. Anonymous Object Rectification. <p>&lt;strong&gt;NOTE&lt;/strong&gt;. <br>If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used. <br>If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing. <br> Child components of &lt;em&gt;List&lt;/em&gt; whose &lt;em&gt;visibility&lt;/em&gt; attribute is set to &lt;em&gt;None&lt;/em&gt; are not displayed, but the spacing above and below them still takes effect. </p>

**Type:** double \| string

**Default:** 0

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spaceWidth

```TypeScript
spaceWidth?: Dimension
```

Spacing between list items along the main axis. <p>&lt;strong&gt;NOTE&lt;/strong&gt;. <br>If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used. <br>If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing. <br> Child components of &lt;em&gt;List&lt;/em&gt; whose &lt;em&gt;visibility&lt;/em&gt; attribute is set to &lt;em&gt;None&lt;/em&gt; are not displayed, but the spacing above and below them still takes effect. <br> If both spaceWidth and space are set, spaceWidth will take precedence. </p>

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
