# BackgroundOptions

Defines background options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BackgroundOptions--><!--Device-unnamed-export declare interface BackgroundOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## align

```TypeScript
align?: Alignment
```

Set the alignment of the custom background and component.

Anonymous Object Rectification.

**Type:** [Alignment](arkts-arkui-alignment-e.md)

**Default:** Alignment.Center

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundOptions-align?: Alignment--><!--Device-BackgroundOptions-align?: Alignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ignoresLayoutSafeAreaEdges

```TypeScript
ignoresLayoutSafeAreaEdges?: Array<LayoutSafeAreaEdge>
```

The set of edges for which to ignore layout safe area. To respect safe area insets on all edges,explicitly pass empty edge set.

**Type:** Array&lt;LayoutSafeAreaEdge&gt;

**Default:** The default value is LayoutSafeAreaEdge.ALL when background is ResourceColor, otherwise it is an empty array [].

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundOptions-ignoresLayoutSafeAreaEdges?: Array<LayoutSafeAreaEdge>--><!--Device-BackgroundOptions-ignoresLayoutSafeAreaEdges?: Array<LayoutSafeAreaEdge>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

