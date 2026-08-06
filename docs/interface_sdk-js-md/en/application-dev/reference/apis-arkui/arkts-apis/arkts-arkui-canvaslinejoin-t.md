# CanvasLineJoin

```TypeScript
export type CanvasLineJoin = 'bevel' | 'miter' | 'round'
```

Sets the attribute of how two connected parts (line segments, arcs, and curves) whose length is not 0are connected together. The following three configurations are supported:'bevel': Fill the ends of the connected sections with an additional triangle-base area,each with its own independent rectangular corner.'miter': (Default) An additional diamond region is formed by extending the outer edges of the connected portions so that they intersect at a point.'round': Draw the shape of the corner by filling in an additional sector with the center at the end of the connected section. The radius of the fillet is the width of the segment.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type CanvasLineJoin = 'bevel' | 'miter' | 'round'--><!--Device-unnamed-export type CanvasLineJoin = 'bevel' | 'miter' | 'round'-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| 'bevel' |  |
| 'miter' |  |
| 'round' |  |

