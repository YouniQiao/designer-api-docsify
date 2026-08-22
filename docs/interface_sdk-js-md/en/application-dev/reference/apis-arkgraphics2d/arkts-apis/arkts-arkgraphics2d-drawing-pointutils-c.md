# PointUtils

This class offers a comprehensive set of operations for handling common2D Point objects.

**Since:** 26.0.0

<!--Device-drawing-class PointUtils--><!--Device-drawing-class PointUtils-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## negate

```TypeScript
static negate(point: common2D.Point): void
```

Negates the point's coordinates.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PointUtils-static negate(point: common2D.Point): void--><!--Device-PointUtils-static negate(point: common2D.Point): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | common2D.Point | Yes | Specifies the point to be negated. |

## offset

```TypeScript
static offset(point: common2D.Point, dx: double, dy: double): void
```

Offsets the point's coordinates by dx, dy.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PointUtils-static offset(point: common2D.Point, dx: double, dy: double): void--><!--Device-PointUtils-static offset(point: common2D.Point, dx: double, dy: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| point | common2D.Point | Yes | Specifies the point to be offset. |
| dx | double | Yes | Indicates the distance to offset on the x-axis in pixels. |
| dy | double | Yes | Indicates the distance to offset on the y-axis in pixels. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const path = new drawing.Path();
path.moveTo(200, 200);
path.lineTo(300, 300);
const dst = path.offset(200, 200);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let rect = drawing.RectUtils.makeLtrb(0, 0, 20, 20);
drawing.RectUtils.offset(rect, 10, 20);
console.info('rect.left:', rect.left);
console.info('rect.top: ', rect.top);
console.info('rect.right: ', rect.right);
console.info('rect.bottom: ', rect.bottom);
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    pen.setColor({
      alpha: 255,
      red: 255,
      green: 0,
      blue: 0
    });
    pen.setStrokeWidth(10);
    canvas.attachPen(pen);
    let region = new drawing.Region();
    region.setRect(100, 100, 400, 400);
    region.offset(10, 20);
    canvas.drawPoint(200, 200);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let roundRect : drawing.RoundRect = new drawing.RoundRect({left: 0, top: 0, right: 300, bottom: 300}, 50, 50);
roundRect.offset(100, 100);
```

