# RenderingContextOptions

Defines the specific configuration parameters for the rendering context.

**Since:** 23

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## antialias

```TypeScript
antialias?: boolean
```

Indicates whether to enable anti-aliasing for the **RenderingContext**. A value of **undefined** is treated as the default value.   
**true**: Enable anti-aliasing. **false**: Disable anti-aliasing. Default value: **false**

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

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
