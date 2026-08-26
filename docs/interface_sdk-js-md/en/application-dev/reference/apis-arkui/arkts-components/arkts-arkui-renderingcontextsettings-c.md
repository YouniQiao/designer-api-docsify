# RenderingContextSettings

Configures the settings of a **CanvasRenderingContext2D** object, including whether to enable anti-aliasing.

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(antialias?: boolean)
```

Constructs a **CanvasRenderingContext2D** object. Anti-aliasing can be enabled.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| antialias | boolean | No | Whether to enable anti-aliasing. A value of **undefined** is treated as the default value.    **false**: Disable anti-aliasing. **true**: Enable anti-aliasing. Default value: **false**    **NOTE：**Anti-aliasing is enabled by default for text drawing. The **antialias** attribute of **RenderingContextSettings** does not affect the anti-aliasing effect of the drawn text. |

**Examples**

The following example shows how to specify the unit mode during the creation of a CanvasRenderingContext2D object. The default unit mode is LengthMetricsUnit.DEFAULT, which corresponds to the default unit vp. Once set, this unit mode cannot be changed dynamically. For details, see LengthMetricsUnit.

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
          // Draw graphics in px unit mode.
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

## antialias

```TypeScript
antialias?: boolean
```

Indicates whether anti-aliasing is enabled for canvas. A value of **undefined** is treated as the default value.   
**false**: Disable anti-aliasing. **true**: Enable anti-aliasing. Default value: **false**   
**NOTE：**Anti-aliasing is enabled by default for text drawing. The **antialias** attribute of **RenderingContextSettings** does not affect the anti-aliasing effect of the drawn text. To adjust the anti-aliasing effect for text, use the [antialias](#antialias) API.

**Type:** boolean

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct AntialiasDemoOff {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings);
          let anti = offContext.antialias;
          console.info(`current antialias is ${anti}`);
          // Set antialias to false.
          offContext.antialias = false;
          offContext.strokeStyle = 'rgb(0,0,0)';
          offContext.lineWidth = 2;
          offContext.beginPath();
          offContext.arc(150, 150, 100, 0, Math.PI);
          offContext.stroke();
          offContext.font = 'normal bold 30vp monospace';
          offContext.fillText("Hello World", 20, 100);
          anti = offContext.antialias;
          console.info(`current antialias is ${anti}`);

          // Set antialias to true.
          offContext.antialias = true;
          offContext.beginPath();
          offContext.arc(150, 350, 100, 0, Math.PI);
          offContext.stroke();
          offContext.font = 'normal bold 30vp monospace';
          offContext.fillText("Hello World", 20, 300);
          anti = offContext.antialias;
          console.info(`current antialias is ${anti}`);
          let image = this.offCanvas.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
