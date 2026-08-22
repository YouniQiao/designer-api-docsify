# CanvasPattern

*CanvasPattern** represents an object, created by the createPattern API, describing an image filling pattern based on the image and repetition mode.

**Since:** 8

<!--Device-unnamed-declare interface CanvasPattern--><!--Device-unnamed-declare interface CanvasPattern-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## setTransform

```TypeScript
setTransform(transform?: Matrix2D): void
```

Uses a **Matrix2D** object as a parameter to perform matrix transformation on the current **CanvasPattern** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasPattern-setTransform(transform?: Matrix2D): void--><!--Device-CanvasPattern-setTransform(transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transform | Matrix2D | No | Transformation matrix.<br>The **undefined** and **null** values are treated as invalid.<br>Default value: **null**. |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct SetTransform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillStyle = 'rgb(112,112,112)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(23,169,141)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.setTransform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(39,135,217)'
          this.context.fillRect(0, 0, 100, 100)
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
struct TransFormDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('context1');
      Canvas(this.context1)
        .width('230vp')
        .height('160vp')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context1.fillRect(100, 20, 50, 50);
          this.context1.setTransform(1, 0.5, -0.5, 1, 10, 10);
          this.context1.fillRect(100, 20, 50, 50);
        })
      Text('context2');
      Canvas(this.context2)
        .width('230vp')
        .height('160vp')
        .backgroundColor('#0ffff0')
        .onReady(() =>{
          this.context2.fillRect(100, 20, 50, 50);
          let storedTransform = this.context1.getTransform();
          this.context2.setTransform(storedTransform);
          this.context2.fillRect(100, 20, 50, 50);
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
struct SetTransform {
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
          offContext.fillStyle = 'rgb(255,0,0)'
          offContext.fillRect(0, 0, 100, 100)
          offContext.setTransform(1,0.5, -0.5, 1, 10, 10)
          offContext.fillStyle = 'rgb(0,0,255)'
          offContext.fillRect(0, 0, 100, 100)
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
 struct TransFormDemo {
   private settings: RenderingContextSettings = new RenderingContextSettings(true);
   private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
   private offcontext1: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 200, this.settings);
   private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
   private offcontext2: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 200, this.settings);

   build() {
     Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
       Text('context1');
       Canvas(this.context1)
         .width('230vp')
         .height('160vp')
         .backgroundColor('#ffff00')
         .onReady(() =>{
           this.offcontext1.fillRect(100, 20, 50, 50);
           this.offcontext1.setTransform(1, 0.5, -0.5, 1, 10, 10);
           this.offcontext1.fillRect(100, 20, 50, 50);
           let image = this.offcontext1.transferToImageBitmap();
           this.context1.transferFromImageBitmap(image);
         })
       Text('context2');
       Canvas(this.context2)
         .width('230vp')
         .height('160vp')
         .backgroundColor('#0ffff0')
         .onReady(() =>{
           this.offcontext2.fillRect(100, 20, 50, 50);
           let storedTransform = this.offcontext1.getTransform();
           this.offcontext2.setTransform(storedTransform);
           this.offcontext2.fillRect(100, 20, 50, 50);
           let image = this.offcontext2.transferToImageBitmap();
           this.context2.transferFromImageBitmap(image);
         })
     }
     .width('100%')
     .height('100%')
   }
 }
```

