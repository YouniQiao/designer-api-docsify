# LayoutCallbacks

Defining interface of LayoutCallbacks for custom component, when decorate with @Layoutable.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface LayoutCallbacks--><!--Device-unnamed-export interface LayoutCallbacks-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPlaceChildren

```TypeScript
onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void
```

Custom component override this method to layout each of its sub components.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LayoutCallbacks-onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void--><!--Device-LayoutCallbacks-onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selfLayoutInfo | [GeometryInfo](../../apis-arkui/arkts-components/arkts-arkui-geometryinfo-i.md) | Yes |  |
| children | Array&lt;[Layoutable](../../apis-arkui/arkts-components/arkts-arkui-layoutable-i.md)&gt; | Yes |  |
| constraint | [ConstraintSizeOptions](../../apis-arkui/arkts-apis/arkts-arkui-constraintsizeoptions-i.md) | Yes |  |

