# PathIterator

Implements a path operation iterator. You can read path operation instructions by traversing the iterator.

> **NOTE：**&gt;
> - The initial APIs of this class are supported since API version 18.&gt;
> - This module uses the physical pixel unit, px.&gt;
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 23

<!--Device-drawing-class PathIterator--><!--Device-drawing-class PathIterator-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## constructor

```TypeScript
constructor(path: Path)
```

Creates an iterator and binds it with a path.

**Since:** 23

<!--Device-PathIterator-constructor(path: Path)--><!--Device-PathIterator-constructor(path: Path)-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | Path | Yes | Path** object bound to the iterator. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const brush = new drawing.Brush();
const brushColor: common2D.Color = { alpha: 255, red: 0, green: 255, blue: 0 };
brush.setColor(brushColor);
const newBrush = new drawing.Brush(brush);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
import { image } from '@kit.ImageKit';

const color = new ArrayBuffer(96);
let opts : image.InitializationOptions = {
  editable: true,
  pixelFormat: 3,
  size: {
    height: 4,
    width: 6
  }
}
image.createPixelMap(color, opts).then((pixelMap) => {
  const canvas = new drawing.Canvas(pixelMap);
})
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let matrix = new drawing.Matrix();
let matrix2 = new drawing.Matrix(matrix);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(0, 0);
path.lineTo(0, 700);
path.lineTo(700, 0);
path.close();
let path1: drawing.Path =  new drawing.Path(path);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

const pen = new drawing.Pen();
const penColor: common2D.Color = { alpha: 255, red: 0, green: 255, blue: 0 };
pen.setColor(penColor);
pen.setStrokeWidth(10);
const newPen = new drawing.Pen(pen);
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
    region.setRect(200, 200, 400, 400);
    let region2 = new drawing.Region(region);
    canvas.drawRegion(region2);
    canvas.detachPen();
  }
}
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
    let region = new drawing.Region(100, 100, 200, 200);
    canvas.drawRegion(region);
    canvas.detachPen();
  }
}
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let rect: common2D.Rect = {left : 100, top : 100, right : 500, bottom : 300};
let roundRect = new drawing.RoundRect(rect, 50, 50);
let roundRect2 = new drawing.RoundRect(roundRect);
```

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let rect: common2D.Rect = {left : 100, top : 100, right : 500, bottom : 300};
let roundRect = new drawing.RoundRect(rect, 50, 50);
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const pen = new drawing.Pen();
    let samplingOptions = new drawing.SamplingOptions();
  }
}
```

```TypeScript
import { RenderNode } from '@kit.ArkUI';
import { common2D, drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    let samplingOptions = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
  }
}
```

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
let typeFaceArgument = new drawing.TypefaceArguments();
```

## hasNext

```TypeScript
hasNext(): boolean
```

Checks whether there is any next operation in the path operation iterator.

**Since:** 23

<!--Device-PathIterator-hasNext(): boolean--><!--Device-PathIterator-hasNext(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. **true** means yes; **false** otherwise. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let res = iter.hasNext();
```

## next

```TypeScript
next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb
```

Retrieves the next operation in this path and moves the iterator to that operation.

**Since:** 18

<!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb--><!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| points | Array&lt;common2D.Point&gt; | Yes | Array of coordinate points. The array length must be at least the offset plus 4 to ensure that the array can hold all types of path data. After the operation is executed, this array is overwritten. The number of coordinate points to be filled depends on the operation type. Specifically, for **MOVE**, fill one coordinate; for **LINE**, fill two coordinates; for **QUAD**, fill three coordinates; for **CONIC**, fill three coordinates and one weight value (a total of 3.5 groups); for **CUBIC**, fill four coordinates; for **CLOSE** and **DONE**, do not fill any coordinate points. |
| offset | number | No | Offset from the start of the array where writing begins. The default value is **0**. The value range is [0, size - 4], where **size** is the length of the coordinate point array. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) | Path operation type contained in the iterator. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
path.moveTo(10, 20);
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let verbStr: Array<string> = ["MOVE", "LINE", "QUAD", "CONIC", "CUBIC", "CLOSE", "DONE"];
let pointCount: Array<number> = [1,2,3,4,4,0,0];
let points: Array<common2D.Point> = [{x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}, {x: 0, y: 0}];
let offset = 0;
let verb = iter.next(points, offset);
let outputMessage: string = "pathIteratorNext: ";
outputMessage += "verb =" + verbStr[verb] + "; has " + pointCount[verb] + " pairs: ";
for (let j = 0; j < pointCount[verb] + offset; j++) {
  outputMessage += "[" + points[j].x + ", " + points[j].y + "]";
}
console.info(outputMessage);
```

## next

```TypeScript
next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined
```

Retrieves the next operation in this path and moves the iterator to that operation.

**Since:** 23

<!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined--><!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| points | Array&lt;common2D.Point&gt; | Yes | Indicates the point array. |
| offset | int | No | Indicates the offset into the array where entries should be placed. The default value is 0. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) \| undefined | Returns the next verb in this iterator's path. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

See [next](#next)

## peek

```TypeScript
peek(): PathIteratorVerb
```

Retrieves the next operation in this path, without moving the iterator.

**Since:** 18

<!--Device-PathIterator-peek(): PathIteratorVerb--><!--Device-PathIterator-peek(): PathIteratorVerb-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) | Path operation type contained in the iterator. |

**Examples**

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

let path: drawing.Path = new drawing.Path();
let iter: drawing.PathIterator = new drawing.PathIterator(path);
let res = iter.peek();
```

## peek

```TypeScript
peek(): PathIteratorVerb | undefined
```

Retrieves the next operation in this path, without moving the iterator.

**Since:** 23

<!--Device-PathIterator-peek(): PathIteratorVerb | undefined--><!--Device-PathIterator-peek(): PathIteratorVerb | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) \| undefined | Returns the next verb in the iteration. |

**Examples**

See [peek](#peek)

