# OffscreenCanvasRenderingContext2DInterface

使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。 离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到Canvas上。 离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。

> **说明：**&gt;
> OffscreenCanvasRenderingContext2D无法在ServiceExtensionAbility中使用，
> ServiceExtensionAbility中建议使用
> [Drawing模块](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-drawing.md)
> 进行离屏绘制。&gt;
> beginPath、moveTo、lineTo、closePath、bezierCurveTo、quadraticCurveTo、arc、arcTo、ellipse、rect和
> roundRect接口只能对OffscreenCanvasRenderingContext2D中的路径生效，无法对
> [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md)
> 和[Path2D](arkts-arkui-path2d-c.md)
> 对象中设置的路径生效。

**起始版本：** 8

<!--Device-unnamed-declare interface OffscreenCanvasRenderingContext2DInterface--><!--Device-unnamed-declare interface OffscreenCanvasRenderingContext2DInterface-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

**起始版本：** 8

<!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 |  |
| height | number | 是 |  |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
**示例**

以下示例展示了配置CanvasRenderingContext2D对象的单位模式，默认单位模式为LengthMetricsUnit.DEFAULT，对应默认单位vp，配置后无法动态更改。详细说明见LengthMetricsUnit。

```TypeScript
// xxx.ets
import { LengthMetricsUnit } from '@kit.ArkUI'

@Entry
@Component
struct LengthMetricsUnitDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private contextPX: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX);
  private contextVP: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.contextPX)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextPX.fillRect(10, 10, 100, 100)
          this.contextPX.clearRect(10, 10, 50, 50)
        })

      Canvas(this.contextVP)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextVP.fillRect(10, 10, 100, 100)
          this.contextVP.clearRect(10, 10, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## constructor

```TypeScript
(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D
```

**起始版本：** 12

<!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvasRenderingContext2DInterface-(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit): OffscreenCanvasRenderingContext2D-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 |  |
| height | number | 是 |  |
| settings | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | 否 |  |
| unit | LengthMetricsUnit | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
**示例**

参见 [constructor](#constructor)

