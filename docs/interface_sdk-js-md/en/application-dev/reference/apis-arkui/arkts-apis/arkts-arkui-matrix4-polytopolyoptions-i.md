# PolyToPolyOptions

Set poly to poly point options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-matrix4-export interface PolyToPolyOptions--><!--Device-matrix4-export interface PolyToPolyOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { matrix4 } from '@kit.ArkUI';
```

## dst

```TypeScript
dst: Array<Point>
```

Array of point coordinates for the target polygon.

**Type:** Array&lt;Point&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-dst: Array<Point>--><!--Device-PolyToPolyOptions-dst: Array<Point>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dstIndex

```TypeScript
dstIndex?: int
```

Start index of the target polygon, which defaults to 0.

**Type:** int

**Default:** src.Length/2

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-dstIndex?: int--><!--Device-PolyToPolyOptions-dstIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pointCount

```TypeScript
pointCount?: int
```

The number of points to be used.If it is 0, it returns the identity matrix.If it is 1, it returns a translation matrix that changed before two points.If it is 2-4, it returns a transformation matrix.

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-pointCount?: int--><!--Device-PolyToPolyOptions-pointCount?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src: Array<Point>
```

Array of point coordinates for the source polygon.

**Type:** Array&lt;Point&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-src: Array<Point>--><!--Device-PolyToPolyOptions-src: Array<Point>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## srcIndex

```TypeScript
srcIndex?: int
```

Start point index of the source polygon, which defaults to 0.

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolyToPolyOptions-srcIndex?: int--><!--Device-PolyToPolyOptions-srcIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

