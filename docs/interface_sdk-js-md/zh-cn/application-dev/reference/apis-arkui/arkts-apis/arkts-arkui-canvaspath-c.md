# CanvasPath

路径对象，提供基本的路径绘制方法。路径相关API的详细说明请参见CanvasRenderingContext2D中的描述。

**起始版本：** 8

<!--Device-unnamed-declare class CanvasPath--><!--Device-unnamed-declare class CanvasPath-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## arc

```TypeScript
arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void
```

绘制弧线路径。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void--><!--Device-CanvasPath-arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| radius | number | 是 | 弧线的圆半径。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。单位：弧度。 |
| endAngle | number | 是 | 弧线的终止弧度。单位：弧度。 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧。<br>**true**：逆时针方向绘制圆弧。 <br>**false**：顺时针方向绘制圆弧。<br>默认值：**false**，设置**null**或**undefined**按默认值处理。 |

**示例**

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
        .onReady(() => {
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
        .onReady(() => {
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

依据圆弧经过的点和圆弧半径创建圆弧路径。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void--><!--Device-CanvasPath-arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 圆弧经过的第一个点的x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y1 | number | 是 | 圆弧经过的第一个点的y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| x2 | number | 是 | 圆弧经过的第二个点的x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y2 | number | 是 | 圆弧经过的第二个点的y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| radius | number | 是 | 圆弧的圆半径值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |

**示例**

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
        .onReady(() => {
          // 切线
          this.context.beginPath()
          this.context.strokeStyle = '#808080'
          this.context.lineWidth = 1.5;
          this.context.moveTo(360, 20);
          this.context.lineTo(360, 170);
          this.context.lineTo(110, 170);
          this.context.stroke();

          // 圆弧
          this.context.beginPath()
          this.context.strokeStyle = '#000000'
          this.context.lineWidth = 3;
          this.context.moveTo(360, 20)
          this.context.arcTo(360, 170, 110, 170, 150)
          this.context.stroke()

          // 起始点
          this.context.beginPath();
          this.context.fillStyle = '#00ff00';
          this.context.arc(360, 20, 4, 0, 2 * Math.PI);
          this.context.fill();

          // 控制点
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
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)

          // 切线
          offContext.beginPath()
          offContext.strokeStyle = '#808080'
          offContext.lineWidth = 1.5;
          offContext.moveTo(360, 20);
          offContext.lineTo(360, 170);
          offContext.lineTo(110, 170);
          offContext.stroke();

          // 圆弧
          offContext.beginPath()
          offContext.strokeStyle = '#000000'
          offContext.lineWidth = 3;
          offContext.moveTo(360, 20)
          offContext.arcTo(360, 170, 110, 170, 150)
          offContext.stroke()

          // 起始点
          offContext.beginPath();
          offContext.fillStyle = '#00ff00';
          offContext.arc(360, 20, 4, 0, 2 * Math.PI);
          offContext.fill();

          // 控制点
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

创建三次贝塞尔曲线的路径。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void--><!--Device-CanvasPath-bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cp1x | number | 是 | 第一个贝塞尔参数的x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| cp1y | number | 是 | 第一个贝塞尔参数的y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| cp2x | number | 是 | 第二个贝塞尔参数的x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| cp2y | number | 是 | 第二个贝塞尔参数的y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |

**示例**

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
          // 三次贝塞尔曲线
          ctx.beginPath();
          ctx.moveTo(this.start.x, this.start.y);
          ctx.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
          ctx.stroke();

          // 起点和终点
          ctx.fillStyle = 'rgb(39,135,217)';
          ctx.beginPath();
          ctx.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起点
          ctx.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 终点
          ctx.fill();

          // 控制点
          ctx.fillStyle = 'rgb(23,169,141)';
          ctx.beginPath();
          ctx.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // 控制点一
          ctx.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // 控制点二
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
          // 三次贝塞尔曲线
          offContext.beginPath();
          offContext.moveTo(this.start.x, this.start.y);
          offContext.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
          offContext.stroke();

          // 起点和终点
          offContext.fillStyle = 'rgb(39,135,217)';
          offContext.beginPath();
          offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起点
          offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 终点
          offContext.fill();

          // 控制点
          offContext.fillStyle = 'rgb(23,169,141)';
          offContext.beginPath();
          offContext.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // 控制点一
          offContext.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // 控制点二
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

将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-closePath(): void--><!--Device-CanvasPath-closePath(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例**

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
        .onReady(() => {
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
        .onReady(() => {
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

在规定的矩形区域绘制一个椭圆。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-ellipse(    x: number,    y: number,    radiusX: number,    radiusY: number,    rotation: number,    startAngle: number,    endAngle: number,    counterclockwise?: boolean,  ): void--><!--Device-CanvasPath-ellipse(    x: number,    y: number,    radiusX: number,    radiusY: number,    rotation: number,    startAngle: number,    endAngle: number,    counterclockwise?: boolean,  ): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y | number | 是 | 椭圆圆心的y轴坐标。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| radiusX | number | 是 | 椭圆x轴的半径长度。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| radiusY | number | 是 | 椭圆y轴的半径长度。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| rotation | number | 是 | 椭圆的旋转角度。单位：弧度。 |
| startAngle | number | 是 | 椭圆绘制的起始点角度。单位：弧度。 |
| endAngle | number | 是 | 椭圆绘制的结束点角度。单位：弧度。 |
| counterclockwise | boolean | 否 | 是否以逆时针方向绘制椭圆。<br>**true**：逆时针方向绘制椭圆。 <br>**false**：顺时针方向绘制椭圆。<br>默认值：**false**，设置**null**或**undefined**按默认值处理。 |

**示例**

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
        .onReady(() => {
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
        .onReady(() => {
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

从当前点绘制一条直线到目标点。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-lineTo(x: number, y: number): void--><!--Device-CanvasPath-lineTo(x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 目标点X轴坐标。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y | number | 是 | 目标点Y轴坐标。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |

**示例**

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
        .onReady(() => {
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
        .onReady(() => {
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

将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-moveTo(x: number, y: number): void--><!--Device-CanvasPath-moveTo(x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 目标点X轴坐标。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y | number | 是 | 目标点Y轴坐标。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp  > **说明：** >  > API version 18之前，如果没有调用**moveTo**接口或传入无效参数，路径从(0,0)开始。 >  > API version 18及以后，如果没有调用**moveTo**接口或传入无效参数，路径将从第一个有效调用的 > **lineTo**、**arcTo**、**bezierCurveTo**或**quadraticCurveTo**的起始点开始。 |

**示例**

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
        .onReady(() => {
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
        .onReady(() => {
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

创建二次贝塞尔曲线路径。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void--><!--Device-CanvasPath-quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cpx | number | 是 | 贝塞尔参数的x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| cpy | number | 是 | 贝塞尔参数的y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |

**示例**

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
          // 二次贝塞尔曲线
          ctx.beginPath();
          ctx.moveTo(this.start.x, this.start.y);
          ctx.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
          ctx.stroke();

          // 起始点和结束点
          ctx.fillStyle = 'rgb(39,135,217)';
          ctx.beginPath();
          ctx.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起始点
          ctx.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 结束点
          ctx.fill();

          // 控制点
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
          // 二次贝塞尔曲线
          offContext.beginPath();
          offContext.moveTo(this.start.x, this.start.y);
          offContext.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
          offContext.stroke();

          // 起始点和结束点
          offContext.fillStyle = 'rgb(39,135,217)';
          offContext.beginPath();
          offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起始点
          offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 结束点
          offContext.fill();

          // 控制点
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

创建矩形路径。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-rect(x: number, y: number, w: number, h: number): void--><!--Device-CanvasPath-rect(x: number, y: number, w: number, h: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。<br>API version 18之前，设置NaN或Infinity时，整条路径 不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或 undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| w | number | 是 | 指定矩形的宽度。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |
| h | number | 是 | 指定矩形的高度。<br>API version 18之前，设置NaN或Infinity时，整条路径不显示； 设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时 当前接口不生效，其他传入有效参数的路径方法正常绘制。默认单位：vp |

**示例**

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
        .onReady(() => {
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
        .onReady(() => {
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

创建圆角矩形路径，此方法不会直接渲染内容，如需将圆角矩形绘制到画布上，可以使用fill或stroke方法。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void--><!--Device-CanvasPath-roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 矩形左上角x坐标值。<br>设置**null**时，按照**0**处理；设置**undefined**时， 按无效值处理，不进行绘制。<br>绘制完整矩形时，取值范围为[0, 画布宽度)。<br>默认单位：vp |
| y | number | 是 | 矩形左上角y坐标值。<br>设置**null**时，按照**0**处理；设置**undefined**时， 按无效值处理，不进行绘制。<br>绘制完整矩形时，取值范围为[0, 画布高度)。<br>默认单位：vp |
| w | number | 是 | 矩形的宽度。负值表示从右向左绘制矩形。<br>设置**null**时，按照**0**处理； 设置**undefined**时，按无效值处理，不进行绘制。<br>绘制完整矩形时，取值范围为[-x, 画布宽度 - x]。 <br>默认单位：vp |
| h | number | 是 | 矩形的高度。负值表示向上绘制。<br>设置**null**时，按照**0**处理； 设置**undefined**时，按无效值处理，不进行绘制。<br>绘制完整矩形时，取值范围为[-y, 画布高度 - y]。 <br>默认单位：vp |
| radii | number \| Array&lt;number&gt; | 否 | 矩形圆角的圆弧半径值或半径值列表。 <br>参数类型为number时，表示矩形四个角的圆弧半径。 <br>参数类型为Array&lt;number&gt;时，数组包含1到4个数字，含义如下：<br>[矩形四个角的圆弧半径] <br>[矩形左上角和右下角的圆弧半径，矩形右上角和左下角的圆弧半径]<br>[矩形左上角的圆弧半径， 矩形右上角和左下角的圆弧半径，矩形右下角的圆弧半径]<br>[矩形左上角的圆弧半径，矩形右上角的圆弧半径， 矩形右下角的圆弧半径，矩形左下角的圆弧半径]<br>如果**radii**中包含负数或数组元素个数不在[1,4]范围内， 则上报错误码103701。<br>默认值：**0**。设置**null**或**undefined**时按默认值处理。<br>如果圆弧半径超过 矩形的宽度和高度，将按比例缩小以匹配对应尺寸。<br>默认单位：vp |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [103701](../errorcode-canvas.md#103701-参数错误) | 参数错误。可能的原因： <br> 1. 参数radii数组的元素个数为0或超过4个。 <br> 2. 参数radii中包含负数。 |

**示例**

创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边。

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
            // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.context.roundRect(10, 10, 100, 100, 10)
            // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.context.roundRect(120, 10, 100, 100, [10])
            this.context.fill()
            this.context.beginPath()
            // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
            this.context.roundRect(10, 120, 100, 100, [10, 20])
            // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
            this.context.roundRect(120, 120, 100, 100, [10, 20, 30])
            // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            this.context.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
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

创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边。

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
            // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            offContext.roundRect(10, 10, 100, 100, 10)
            // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            offContext.roundRect(120, 10, 100, 100, [10])
            offContext.fill()
            offContext.beginPath()
            // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
            offContext.roundRect(10, 120, 100, 100, [10, 20])
            // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
            offContext.roundRect(120, 120, 100, 100, [10, 20, 30])
            // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            offContext.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            offContext.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
            offContext.stroke()
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
          }
          // 在离屏画布最近渲染的图像上创建一个ImageBitmap对象
          let image = this.offCanvas.transferToImageBitmap()
          // 将创建的ImageBitmap对象显示在Canvas画布上
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边。

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
            // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.pathA.roundRect(10, 10, 100, 100, 10)
            // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.pathA.roundRect(120, 10, 100, 100, [10])
            this.context.fill(this.pathA)
            // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
            this.pathB.roundRect(10, 120, 100, 100, [10, 20])
            // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
            this.pathB.roundRect(120, 120, 100, 100, [10, 20, 30])
            // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            this.pathB.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
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

