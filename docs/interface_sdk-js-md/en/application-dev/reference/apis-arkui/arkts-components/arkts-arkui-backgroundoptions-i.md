# BackgroundOptions

Defines background options.

**Since:** 20

<!--Device-unnamed-declare interface BackgroundOptions--><!--Device-unnamed-declare interface BackgroundOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## align

```TypeScript
align?: Alignment
```

Set the alignment of the custom background and component.

Anonymous Object Rectification.

**Type:** Alignment

**Default:** Alignment.Center

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-BackgroundOptions-align?: Alignment--><!--Device-BackgroundOptions-align?: Alignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ignoresLayoutSafeAreaEdges

```TypeScript
ignoresLayoutSafeAreaEdges?: Array<LayoutSafeAreaEdge>
```

The set of edges for which to ignore layout safe area. To respect safe area insets on all edges, explicitly pass empty edge set.

**Type:** Array&lt;LayoutSafeAreaEdge&gt;

**Default:** The default value is LayoutSafeAreaEdge.ALL when background is ResourceColor, otherwise it is an empty
array [].

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-BackgroundOptions-ignoresLayoutSafeAreaEdges?: Array<LayoutSafeAreaEdge>--><!--Device-BackgroundOptions-ignoresLayoutSafeAreaEdges?: Array<LayoutSafeAreaEdge>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

