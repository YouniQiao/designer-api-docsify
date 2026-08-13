# ListOptions

Defines the options of the &lt;em&gt;List&lt;/em&gt; component. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: &lt;br&gt;- The default value of the universal attribute clip is &lt;em&gt;true&lt;/em&gt; for the &lt;em&gt;List&lt;/em&gt; component. &lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface ListOptions--><!--Device-unnamed-export interface ListOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialIndex

```TypeScript
initialIndex?: int
```

Index of the item to be displayed at the start when the list is initially loaded. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. The value should be an integer. &lt;br&gt;If the set value is a negative number or is greater than the index of the last item in the list, the value is invalid. In this case, the default value will be used. &lt;/p&gt;

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-initialIndex?: int--><!--Device-ListOptions-initialIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller?: Scroller
```

Scroller, which can be bound to scrollable components. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. &lt;br&gt;The scroller cannot be bound to other scrollable components. &lt;/p&gt;

**Type:** [Scroller](../../apis-arkui/arkts-components/arkts-arkui-scroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-scroller?: Scroller--><!--Device-ListOptions-scroller?: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: double | string
```

Spacing between list items along the main axis. Anonymous Object Rectification. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. &lt;br&gt;If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used. &lt;br&gt;If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing. &lt;br&gt; Child components of &lt;em&gt;List&lt;/em&gt; whose &lt;em&gt;visibility&lt;/em&gt; attribute is set to &lt;em&gt;None&lt;/em&gt; are not displayed, but the spacing above and below them still takes effect. &lt;/p&gt;

**Type:** double \| string

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-space?: double | string--><!--Device-ListOptions-space?: double | string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## spaceWidth

```TypeScript
spaceWidth?: Dimension
```

Spacing between list items along the main axis. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. &lt;br&gt;If this parameter is set to a negative number or a value greater than or equal to the length of the list content area, the default value is used. &lt;br&gt;If this parameter is set to a value less than the width of the list divider, the width of the list divider is used as the spacing. &lt;br&gt; Child components of &lt;em&gt;List&lt;/em&gt; whose &lt;em&gt;visibility&lt;/em&gt; attribute is set to &lt;em&gt;None&lt;/em&gt; are not displayed, but the spacing above and below them still takes effect. &lt;br&gt; If both spaceWidth and space are set, spaceWidth will take precedence. &lt;/p&gt;

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListOptions-spaceWidth?: Dimension--><!--Device-ListOptions-spaceWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

