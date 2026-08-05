# LayoutCallbacks

Defining interface of LayoutCallbacks for custom component, when decorate with @Layoutable.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface LayoutCallbacks {  /**   * Custom component override this method to layout each of its sub components.   *   *******/  onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void--><!--Device-unnamed-export interface LayoutCallbacks {  /**   * Custom component override this method to layout each of its sub components.   *   *******/  onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPlaceChildren

```TypeScript
onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void
```

Custom component override this method to layout each of its sub components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayoutCallbacks-onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void--><!--Device-LayoutCallbacks-onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selfLayoutInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |
| children | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | Yes |  |
| constraint | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

