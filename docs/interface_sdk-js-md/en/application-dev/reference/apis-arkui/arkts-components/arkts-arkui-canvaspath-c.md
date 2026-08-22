# CanvasPath

Path object, which provides basic methods for drawing paths. For details about the path-related APIs, see the description in **CanvasRenderingContext2D**.

**Since:** 8

<!--Device-unnamed-declare class CanvasPath--><!--Device-unnamed-declare class CanvasPath-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## arc

```TypeScript
arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void
```

Draws an arc on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void--><!--Device-CanvasPath-arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | X-coordinate of the center point of the arc.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y | number | Yes | Y-coordinate of the center point of the arc.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| radius | number | Yes | Radius of the arc.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| startAngle | number | Yes | Start radian of the arc.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Unit: radian |
| endAngle | number | Yes | End radian of the arc.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Unit: radian |
| counterclockwise | boolean | No | Whether to draw the arc counterclockwise.<br>**true**: Draw the arc counterclockwise.<br>**false**: Draw the arc clockwise.<br>The default value is **false**. If this parameter is set to **null** or **undefined**, the default value is used. |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct Arc {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.arc(100, 75, 50, 0, 6.28)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct Arc {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.arc(100, 75, 50, 0, 6.28)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct Arc {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.arc(100, 75, 50, 0, 6.28)
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## arcTo

```TypeScript
arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void
```

Creates a circular arc using the given control points and radius.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void--><!--Device-CanvasPath-arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x1 | number | Yes | X-coordinate of the first control point.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y1 | number | Yes | Y-coordinate of the first control point.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| x2 | number | Yes | X-coordinate of the second control point.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y2 | number | Yes | Y-coordinate of the second control point.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| radius | number | Yes | Radius of the arc.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct ArcTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          // Tangent
          this.context.beginPath()
          this.context.strokeStyle = '#808080'
          this.context.lineWidth = 1.5;
          this.context.moveTo(360, 20);
          this.context.lineTo(360, 170);
          this.context.lineTo(110, 170);
          this.context.stroke();
          
          // Arc
          this.context.beginPath()
          this.context.strokeStyle = '#000000'
          this.context.lineWidth = 3;
          this.context.moveTo(360, 20)
          this.context.arcTo(360, 170, 110, 170, 150)
          this.context.stroke()
          
          // Start point
          this.context.beginPath();
          this.context.fillStyle = '#00ff00';
          this.context.arc(360, 20, 4, 0, 2 * Math.PI);
          this.context.fill();
          
          // Control points
          this.context.beginPath();
          this.context.fillStyle = '#ff0000';
          this.context.arc(360, 170, 4, 0, 2 * Math.PI);
          this.context.arc(110, 170, 4, 0, 2 * Math.PI);
          this.context.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct ArcTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)

          // Tangent
          offContext.beginPath()
          offContext.strokeStyle = '#808080'
          offContext.lineWidth = 1.5;
          offContext.moveTo(360, 20);
          offContext.lineTo(360, 170);
          offContext.lineTo(110, 170);
          offContext.stroke();

          // Arc
          offContext.beginPath()
          offContext.strokeStyle = '#000000'
          offContext.lineWidth = 3;
          offContext.moveTo(360, 20)
          offContext.arcTo(360, 170, 110, 170, 150)
          offContext.stroke()

          // Start point
          offContext.beginPath();
          offContext.fillStyle = '#00ff00';
          offContext.arc(360, 20, 4, 0, 2 * Math.PI);
          offContext.fill();

          // Control points
          offContext.beginPath();
          offContext.fillStyle = '#ff0000';
          offContext.arc(360, 170, 4, 0, 2 * Math.PI);
          offContext.arc(110, 170, 4, 0, 2 * Math.PI);
          offContext.fill();

          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct ArcTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(0, 0)
          this.path2Db.arcTo(150, 20, 150, 70, 50)
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## bezierCurveTo

```TypeScript
bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void
```

Draws a cubic Bezier curve on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void--><!--Device-CanvasPath-bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cp1x | number | Yes | X-coordinate of the first parameter of the Bezier curve.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| cp1y | number | Yes | Y-coordinate of the first parameter of the Bezier curve.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| cp2x | number | Yes | X-coordinate of the second parameter of the Bezier curve.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| cp2y | number | Yes | Y-coordinate of the second parameter of the Bezier curve.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| x | number | Yes | X-coordinate of the end point on the Bezier curve.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y | number | Yes | Y-coordinate of the end point on the Bezier curve.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |

**Examples**

```TypeScript
// xxx.ets
import { Point } from '@kit.TestKit';

@Entry
@Component
struct BezierCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private start: Point = { x: 50, y: 50 };
  private end: Point = { x: 250, y: 100 };
  private cp1: Point = { x: 200, y: 30 };
  private cp2: Point = { x: 130, y: 80 };

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let ctx = this.context;
          // Cubic Bezier curve
          ctx.beginPath();
          ctx.moveTo(this.start.x, this.start.y);
          ctx.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
          ctx.stroke();

          // Start point and end point
          ctx.fillStyle = 'rgb(39,135,217)';
          ctx.beginPath();
          ctx.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // Start point
          ctx.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // End point
          ctx.fill();

          // Control points
          ctx.fillStyle = 'rgb(23,169,141)';
          ctx.beginPath();
          ctx.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // Control point 1
          ctx.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // Control point 2
          ctx.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
import { Point } from '@kit.TestKit';

@Entry
@Component
struct BezierCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
  private start: Point = { x: 50, y: 50 };
  private end: Point = { x: 250, y: 100 };
  private cp1: Point = { x: 200, y: 30 };
  private cp2: Point = { x: 130, y: 80 };

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          // Cubic Bezier curve
          offContext.beginPath();
          offContext.moveTo(this.start.x, this.start.y);
          offContext.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
          offContext.stroke();

          // Start point and end point.
          offContext.fillStyle = 'rgb(39,135,217)';
          offContext.beginPath();
          offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // Start point
          offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // End point
          offContext.fill();

          // Control points
          offContext.fillStyle = 'rgb(23,169,141)';
          offContext.beginPath();
          offContext.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // Control point 1
          offContext.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // Control point 2
          offContext.fill();
          let image = this.offCanvas.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct BezierCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(10, 10)
          this.path2Db.bezierCurveTo(20, 100, 200, 100, 200, 20)
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## closePath

```TypeScript
closePath(): void
```

Moves the current point of the path back to the start point of the path, and draws a straight line between the current point and the start point. If the shape has already been closed or has only one point, this method does nothing.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-closePath(): void--><!--Device-CanvasPath-closePath(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct ClosePath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
            this.context.beginPath()
            this.context.moveTo(30, 30)
            this.context.lineTo(110, 30)
            this.context.lineTo(70, 90)
            this.context.closePath()
            this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct ClosePath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
            let offContext = this.offCanvas.getContext("2d", this.settings)
            offContext.beginPath()
            offContext.moveTo(30, 30)
            offContext.lineTo(110, 30)
            offContext.lineTo(70, 90)
            offContext.closePath()
            offContext.stroke()
            let image = this.offCanvas.transferToImageBitmap()
            this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct ClosePath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(200, 100)
          this.path2Db.lineTo(300, 100)
          this.path2Db.lineTo(200, 200)
          this.path2Db.closePath()
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## ellipse

```TypeScript
ellipse(
    x: number,
    y: number,
    radiusX: number,
    radiusY: number,
    rotation: number,
    startAngle: number,
    endAngle: number,
    counterclockwise?: boolean,
  ): void
```

Draws an ellipse in the specified rectangular region on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-ellipse(    x: number,    y: number,    radiusX: number,    radiusY: number,    rotation: number,    startAngle: number,    endAngle: number,    counterclockwise?: boolean,  ): void--><!--Device-CanvasPath-ellipse(    x: number,    y: number,    radiusX: number,    radiusY: number,    rotation: number,    startAngle: number,    endAngle: number,    counterclockwise?: boolean,  ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | X-coordinate of the ellipse center.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y | number | Yes | Y-coordinate of the ellipse center.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| radiusX | number | Yes | Radius of the ellipse on the x-axis.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| radiusY | number | Yes | Radius of the ellipse on the y-axis.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| rotation | number | Yes | Rotation angle of the ellipse.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Unit: radian |
| startAngle | number | Yes | Angle of the start point for drawing the ellipse.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Unit: radian |
| endAngle | number | Yes | Angle of the end point for drawing the ellipse.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Unit: radian |
| counterclockwise | boolean | No | Whether to draw the ellipse counterclockwise.<br>**true**: Draw the ellipse counterclockwise.<br>**false**: Draw the ellipse clockwise.<br>The default value is **false**. If this parameter is set to **null** or **undefined**, the default value is used. |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, false)
          this.context.stroke()
          this.context.beginPath()
          this.context.ellipse(200, 300, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, true)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, false)
          offContext.stroke()
          offContext.beginPath()
          offContext.ellipse(200, 300, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, true)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.ellipse(200, 200, 50, 100, 0, Math.PI * 1, Math.PI * 2)
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## lineTo

```TypeScript
lineTo(x: number, y: number): void
```

Connects the current point to a target position using a line.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-lineTo(x: number, y: number): void--><!--Device-CanvasPath-lineTo(x: number, y: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | X-coordinate of the target position.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y | number | Yes | Y-coordinate of the target position.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct LineTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.lineTo(280, 160)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct LineTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.moveTo(10, 10)
          offContext.lineTo(280, 160)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct LineTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(100, 100)
          this.path2Db.lineTo(100, 200)
          this.path2Db.lineTo(200, 200)
          this.path2Db.lineTo(200, 100)
          this.path2Db.closePath()
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## moveTo

```TypeScript
moveTo(x: number, y: number): void
```

Moves a drawing path from the current position to a target position on the canvas.   
> **NOTE：**
> 
> In versions earlier than API version 18, if the **moveTo** API is not called or invalid arguments
> are passed to it, the path starts from (0,0).
> 
> Starting from API version 18, if the **moveTo** API is not executed or invalid arguments are passed
> to it, the path will begin at the start point of the first valid call to **lineTo**, **arcTo**,
> **bezierCurveTo**, or **quadraticCurveTo**.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-moveTo(x: number, y: number): void--><!--Device-CanvasPath-moveTo(x: number, y: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | X-coordinate of the target position.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y | number | Yes | Y-coordinate of the target position.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct MoveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.lineTo(280, 160)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct MoveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.moveTo(10, 10)
          offContext.lineTo(280, 160)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct MoveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(50, 100)
          this.path2Db.lineTo(250, 100)
          this.path2Db.lineTo(150, 200)
          this.path2Db.closePath()
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## quadraticCurveTo

```TypeScript
quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void
```

Creates a path for a quadratic Bezier curve.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void--><!--Device-CanvasPath-quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cpx | number | Yes | X-coordinate of the Bezier curve parameter.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| cpy | number | Yes | Y-coordinate of the Bezier curve parameter.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| x | number | Yes | X-coordinate of the end point on the Bezier curve.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y | number | Yes | Y-coordinate of the end point on the Bezier curve.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |

**Examples**

```TypeScript
// xxx.ets
import { Point } from '@kit.TestKit';

@Entry
@Component
struct QuadraticCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private start: Point = { x: 50, y: 20 };
  private end: Point = { x: 50, y: 100 };
  private cp: Point = { x: 230, y: 30 };

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let ctx = this.context;
          // Quadratic Bezier curve
          ctx.beginPath();
          ctx.moveTo(this.start.x, this.start.y);
          ctx.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
          ctx.stroke();

          // Start point and end point
          ctx.fillStyle = 'rgb(39,135,217)';
          ctx.beginPath();
          ctx.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // Start point
          ctx.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // End point
          ctx.fill();

          // Control point
          ctx.fillStyle = 'rgb(23,169,141)';
          ctx.beginPath();
          ctx.arc(this.cp.x, this.cp.y, 5, 0, 2 * Math.PI);
          ctx.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
import { Point } from '@kit.TestKit';

@Entry
@Component
struct QuadraticCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
  private start: Point = { x: 50, y: 20 };
  private end: Point = { x: 50, y: 100 };
  private cp: Point = { x: 230, y: 30 };

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings);
          // Quadratic Bezier curve
          offContext.beginPath();
          offContext.moveTo(this.start.x, this.start.y);
          offContext.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
          offContext.stroke();

          // Start point and end point
          offContext.fillStyle = 'rgb(39,135,217)';
          offContext.beginPath();
          offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // Start point
          offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // End point
          offContext.fill();

          // Control points
          offContext.fillStyle = 'rgb(23,169,141)';
          offContext.beginPath();
          offContext.arc(this.cp.x, this.cp.y, 5, 0, 2 * Math.PI);
          offContext.fill();

          let image = this.offCanvas.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct QuadraticCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.moveTo(10, 10)
          this.path2Db.quadraticCurveTo(100, 100, 200, 20)
          this.context.stroke(this.path2Db)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## rect

```TypeScript
rect(x: number, y: number, w: number, h: number): void
```

Creates a rectangle on the canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPath-rect(x: number, y: number, w: number, h: number): void--><!--Device-CanvasPath-rect(x: number, y: number, w: number, h: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | X-coordinate of the rectangle's top-left corner.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| y | number | Yes | Y-coordinate of the rectangle's top-left corner.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| w | number | Yes | Width of the rectangle.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |
| h | number | Yes | Height of the rectangle.<br>In versions earlier than API version 18, **NaN** or **Infinity** value prevents the entire path from rendering, and **null** or **undefined** value causes the current API to have no effect. Since API version 18, **NaN**, **Infinity**, **null**, or **undefined** causes the current API to have no effect, and other path APIs with valid arguments continue to render correctly.<br>Default unit: vp |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.rect(20, 20, 100, 100);
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## roundRect

```TypeScript
roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void
```

Creates a rounded rectangle path. This API does not directly render content. To draw the rounded rectangle on the canvas, use **fill** or **stroke**.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-CanvasPath-roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void--><!--Device-CanvasPath-roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | X-coordinate of the rectangle's top-left corner.<br>The value **null** is treated as **0**, and **undefined** is treated as an invalid value, indicating no rendering.<br> To draw a complete rectangle, the value range is [0, Canvas width).<br>Default unit: vp |
| y | number | Yes | Y-coordinate of the rectangle's top-left corner.<br>The value **null** is treated as **0**, and **undefined** is treated as an invalid value, indicating no rendering.<br>To draw a complete rectangle, the value range is [0, Canvas height).<br>Default unit: vp |
| w | number | Yes | Width of the rectangle. A negative value indicates that the rectangle is drawn from right to left.<br>The value **null** is treated as **0**, and **undefined** is treated as an invalid value, indicating no rendering.<br>To draw a complete rectangle, the value range is [-x, Canvas width - x].<br>Default unit: vp |
| h | number | Yes | Height of the rectangle. A negative value indicates upward drawing.<br>The value **null** is treated as **0**, and **undefined** is treated as an invalid value, indicating no rendering.<br>To draw a complete rectangle, the value range is [-y, Canvas height - y].<br> Default unit: vp |
| radii | number \| Array&lt;number&gt; | No | Number or list of arc radii used for the rectangle corners. <br>If the parameter type is number, it applies to the arc radius of all rectangle corners. <br>If the parameter type is Array&lt;number&gt;, the array contains 1 to 4 numbers, interpreted as follows:<br>[Arc radius of all rectangle corners]<br>[Arc radius of the top-left and bottom-right rectangle corners, and arc radius of the top-right and bottom-left rectangle corners]<br>[Arc radius of the top-left rectangle corner, arc radius of the top-right and bottom-left rectangle corners, and arc radius of the bottom-right rectangle corner]<br>[Arc radius of the top-left rectangle corner, arc radius of the top-right rectangle corner, arc radius of the bottom-right rectangle corner, and arc radius of the bottom-left rectangle corner]<br>If **radii** contains a negative number or the number of items in the list is not within [1,4], error code 103701 is reported.<br>Default value: **0**. **null** and **undefined** are treated as the default value.<br>If the arc radius exceeds the width and height of the rectangle, it will be proportionally scaled down to match the corresponding dimensions.<br>Default unit: vp |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) | Parameter error. Possible causes: <br> 1. The param radii is a list that has zero or more than four elements. <br> 2. The param radii contains negative value. |

**Examples**

Create a rounded rectangle with the start point at (220 vp, 330 vp), width and height of -100 vp, and the radius of the top-left, top-right, bottom-right, and bottom-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively. Then, stroke the rectangle.

```TypeScript
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          try {
            this.context.fillStyle = '#707070'
            this.context.beginPath()
            // Create a rounded rectangle with the start point at (10 vp, 10 vp), width and height of 100 vp, and arc radius of 10 vp for the four rectangle corners.
            this.context.roundRect(10, 10, 100, 100, 10)
            // Create a rounded rectangle with the start point at (120 vp, 10 vp), width and height of 100 vp, and arc radius of 10 vp for the four rectangle corners.
            this.context.roundRect(120, 10, 100, 100, [10])
            this.context.fill()
            this.context.beginPath()
            // Create a rounded rectangle with the start point at (10 vp, 120 vp), width and height of 100 vp, arc radius of 10 vp for the top-left and bottom-right rectangle corners, and arc radius of 20 vp for the top-right and bottom-left rectangle corners.
            this.context.roundRect(10, 120, 100, 100, [10, 20])
            // Create a rounded rectangle with the start point at (120 vp, 120 vp), width and height of 100 vp, arc radius of 10 vp for the top-left rectangle corner, arc radius of 20 vp for the top-right and bottom-left rectangle corners, and arc radius of 30 vp for the bottom-right rectangle corner.
            this.context.roundRect(120, 120, 100, 100, [10, 20, 30])
            // Create a rounded rectangle with the start point at (10 vp, 230 vp), width and height of 100 vp, and the radius of the top-left, top-right, bottom-right, and bottom-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively.
            this.context.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // Create a rounded rectangle with the start point at (220 vp, 330 vp), width and height of -100 vp, and the radius of the top-left, top-right, bottom-right, and bottom-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively.
            this.context.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
            this.context.stroke()
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

Create a rounded rectangle with the start point at (220 vp, 330 vp), width and height of -100 vp, and the radius of the upper-left, upper-right, lower-right, and lower-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively. Then, stroke the rectangle.

```TypeScript
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          try {
            offContext.fillStyle = '#707070'
            offContext.beginPath()
            // Create a rounded rectangle with the start point at (10 vp, 10 vp), width and height of 100 vp, and arc radius of 10 vp for the four rectangle corners.
            offContext.roundRect(10, 10, 100, 100, 10)
            // Create a rounded rectangle with the start point at (120 vp, 10 vp), width and height of 100 vp, and arc radius of 10 vp for the four rectangle corners.
            offContext.roundRect(120, 10, 100, 100, [10])
            offContext.fill()
            offContext.beginPath()
            // Create a rounded rectangle with the start point at (10 vp, 120 vp), width and height of 100 vp, arc radius of 10 vp for the upper-left and lower-right rectangle corners, arc radius of 20 vp for the upper-right and lower-left rectangle corners.
            offContext.roundRect(10, 120, 100, 100, [10, 20])
            // Create a rounded rectangle with the start point at (120 vp, 120 vp), width and height of 100 vp, arc radius of 10 vp for the upper-left rectangle corner, arc radius of 20 vp for the upper-right and lower-left rectangle corners, arc radius of 30 vp for the lower-right rectangle corner.
            offContext.roundRect(120, 120, 100, 100, [10, 20, 30])
            // Create a rounded rectangle with the start point at (10 vp, 230 vp), width and height of 100 vp, and the radius of the upper-left, upper-right, lower-right, and lower-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively.
            offContext.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // Create a rounded rectangle with the start point at (220 vp, 330 vp), width and height of -100 vp, and the radius of the upper-left, upper-right, lower-right, and lower-left rounded corners of 10 vp, 20 vp, 30 vp, and 40 vp, respectively.
            offContext.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
            offContext.stroke()
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
          }
          // Creates an ImageBitmap object from the most recently rendered image of the offscreen canvas.
          let image = this.offCanvas.transferToImageBitmap()
          // Display the created ImageBitmap object on the canvas.
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

Creates a rounded rectangle with the start point (220vp, 330vp), width and height of -100 vp, and the radius of the upper-left rounded corner of 10 vp, the radius of the upper-right rounded corner of 20 vp, the radius of the lower-right rounded corner of 30 vp, and the radius of the lower-left rounded corner of 40 vp. The rounded rectangle is outlined.

```TypeScript
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private pathA: Path2D = new Path2D();
  private pathB: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          try {
            this.context.fillStyle = '#707070'
            // Create a rounded rectangle with the start point (10vp, 10vp), width and height of 100 vp, and four rounded corners with a radius of 10 vp.
            this.pathA.roundRect(10, 10, 100, 100, 10)
            // Create a rounded rectangle with the start point (120vp, 10vp), width and height of 100 vp, and four rounded corners with a radius of 10 vp.
            this.pathA.roundRect(120, 10, 100, 100, [10])
            this.context.fill(this.pathA)
            // Create a rounded rectangle with the start point (10vp, 120vp), width and height of 100 vp, and four rounded corners with a radius of 10 vp in the upper left and lower right corners, and a radius of 20 vp in the upper right and lower left corners.
            this.pathB.roundRect(10, 120, 100, 100, [10, 20])
            // Create a rounded rectangle with the start point (120vp, 120vp), width and height of 100 vp, and four rounded corners with a radius of 10 vp in the upper left corner, a radius of 20 vp in the upper right and lower left corners, and a radius of 30 vp in the lower right corner.
            this.pathB.roundRect(120, 120, 100, 100, [10, 20, 30])
            // Create a rounded rectangle with the start point (10vp, 230vp), width and height of 100 vp, and four rounded corners with a radius of 10 vp in the upper left corner, a radius of 20 vp in the upper right corner, a radius of 30 vp in the lower right corner, and a radius of 40 vp in the lower left corner.
            this.pathB.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // Create a rounded rectangle with the start point (220vp, 330vp), width and height of -100 vp, and four rounded corners with a radius of 10 vp in the upper left corner, a radius of 20 vp in the upper right corner, a radius of 30 vp in the lower right corner, and a radius of 40 vp in the lower left corner.
            this.pathB.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
            this.context.stroke(this.pathB)
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

