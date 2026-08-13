# ScrollSnapOptions

Defines a scroll snapping mode object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface ScrollSnapOptions--><!--Device-unnamed-export declare interface ScrollSnapOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableSnapToEnd

```TypeScript
enableSnapToEnd?: boolean
```

Whether to enable the snap to end feature. When scroll snapping is defined for the &lt;em&gt;Scroll&lt;/em&gt; component, setting this parameter to &lt;em&gt;false&lt;/em&gt; enables the component to scroll between the end and the last page. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. &lt;br&gt;2. This attribute takes effect only when &lt;em&gt;snapPagination&lt;/em&gt; is set to a value of the &lt;em&gt;Array\&lt;Dimension\&gt;&lt;/em&gt; type; it does not work with values of the &lt;em&gt;Dimension&lt;/em&gt; type. &lt;/p&gt;

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapOptions-enableSnapToEnd?: boolean--><!--Device-ScrollSnapOptions-enableSnapToEnd?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableSnapToStart

```TypeScript
enableSnapToStart?: boolean
```

Whether to enable the snap to start feature. When scroll snapping is defined for the &lt;em&gt;Scroll&lt;/em&gt; component, setting this parameter to &lt;em&gt;false&lt;/em&gt; enables the component to scroll between the start and the first page. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. &lt;br&gt;2. This attribute takes effect only when &lt;em&gt;snapPagination&lt;/em&gt; is set to a value of the &lt;em&gt;Array\&lt;Dimension\&gt;&lt;/em&gt; type; it does not work with values of the &lt;em&gt;Dimension&lt;/em&gt; type. &lt;/p&gt;

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapOptions-enableSnapToStart?: boolean--><!--Device-ScrollSnapOptions-enableSnapToStart?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## snapAlign

```TypeScript
snapAlign: ScrollSnapAlign
```

Alignment mode for the scroll snap position.

**Type:** [ScrollSnapAlign](../../apis-arkui/arkts-components/arkts-arkui-scrollsnapalign-e.md)

**Default:** ScrollSnapAlign.NONE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapOptions-snapAlign: ScrollSnapAlign--><!--Device-ScrollSnapOptions-snapAlign: ScrollSnapAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## snapPagination

```TypeScript
snapPagination?: Dimension | Array<Dimension>
```

Pagination points for scroll snapping. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;. &lt;br&gt;1. If the value is of the Dimension type, it indicates the size of each page, and the system will paginat based on this size. &lt;br&gt;2. If the value is of the Array\&lt;Dimension\&gt; type, each &lt;em&gt;Dimension&lt;/em&gt; represents a pagination point, and the system will paginate accordingly. Each &lt;em&gt;Dimension&lt;/em&gt; value must be within the [0, scrollable distance] range. &lt;br&gt;3. If this parameter is not set or &lt;em&gt;Dimension&lt;/em&gt; is set to a value less than or equal to 0, the value is regarded as an invalid value. In this case, there is no scroll snapping. When the value is of the Array\&lt;Dimension\&gt; type, the items in the array must be monotonically increasing. &lt;br&gt;4. When the value is a percentage, the actual size is the product of the viewport of the &lt;em&gt;Scroll&lt;/em&gt; component and the percentage value. &lt;/p&gt;

**Type:** [Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md) \| Array&lt;[Dimension](../../apis-arkui/arkts-apis/arkts-arkui-dimension-t.md)&gt;

**Default:** 100%

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapOptions-snapPagination?: Dimension | Array<Dimension>--><!--Device-ScrollSnapOptions-snapPagination?: Dimension | Array<Dimension>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

