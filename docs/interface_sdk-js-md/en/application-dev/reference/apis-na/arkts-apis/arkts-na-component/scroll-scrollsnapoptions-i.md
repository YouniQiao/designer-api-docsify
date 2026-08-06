# ScrollSnapOptions

Defines a scroll snapping mode object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ScrollSnapOptions--><!--Device-unnamed-export declare interface ScrollSnapOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableSnapToEnd

```TypeScript
enableSnapToEnd?: boolean
```

Whether to enable the snap to end feature. When scroll snapping is defined for the \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Scroll\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ component, setting this parameter to \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_false\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ enables the component to scroll between the end and the last page. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_2. This attribute takes effect only when \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_snapPagination\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_ is set to a value of the \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_Array\&lt;Dimension\&gt;\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ type; it does not work with values of the \_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_Dimension\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_ type. \_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapOptions-enableSnapToEnd?: boolean--><!--Device-ScrollSnapOptions-enableSnapToEnd?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableSnapToStart

```TypeScript
enableSnapToStart?: boolean
```

Whether to enable the snap to start feature. When scroll snapping is defined for the \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Scroll\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ component, setting this parameter to \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_false\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ enables the component to scroll between the start and the first page. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_2. This attribute takes effect only when \_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_snapPagination\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_ is set to a value of the \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_Array\&lt;Dimension\&gt;\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ type; it does not work with values of the \_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_Dimension\_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_ type. \_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapOptions-enableSnapToStart?: boolean--><!--Device-ScrollSnapOptions-enableSnapToStart?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## snapAlign

```TypeScript
snapAlign: ScrollSnapAlign
```

Alignment mode for the scroll snap position.

**Type:** ScrollSnapAlign

**Default:** ScrollSnapAlign.NONE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapOptions-snapAlign: ScrollSnapAlign--><!--Device-ScrollSnapOptions-snapAlign: ScrollSnapAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## snapPagination

```TypeScript
snapPagination?: Dimension | Array<Dimension>
```

Pagination points for scroll snapping. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_1. If the value is of the Dimension type, it indicates the size of each page, and the system will paginat based on this size. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_2. If the value is of the Array\&lt;Dimension\&gt; type, each \_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_Dimension\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_ represents a pagination point, and the system will paginate accordingly. Each \_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_Dimension\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_ value must be within the [0, scrollable distance] range. \_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_3. If this parameter is not set or \_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_Dimension\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_ is set to a value less than or equal to 0, the value is regarded as an invalid value. In this case, there is no scroll snapping. When the value is of the Array\&lt;Dimension\&gt; type, the items in the array must be monotonically increasing. \_\_\_HTML\_TAG\_DESC\_USD\_12\_\_\_4. When the value is a percentage, the actual size is the product of the viewport of the \_\_\_HTML\_TAG\_DESC\_USD\_13\_\_\_Scroll\_\_\_HTML\_TAG\_DESC\_USD\_14\_\_\_ component and the percentage value. \_\_\_HTML\_TAG\_DESC\_USD\_15\_\_\_

**Type:** Dimension \| Array&lt;Dimension&gt;

**Default:** 100%

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollSnapOptions-snapPagination?: Dimension | Array<Dimension>--><!--Device-ScrollSnapOptions-snapPagination?: Dimension | Array<Dimension>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

