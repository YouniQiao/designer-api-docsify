# CanvasPattern

**CanvasPattern** represents an object, created by the createPattern API, describing an image filling pattern based on the image and repetition mode.

**Since:** 8

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

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transform | [Matrix2D](../arkts-apis/arkts-arkui-canvaspattern-matrix2d-c.md) | No | Transformation matrix.The **undefined** and **null** values are treated as invalid.Default value: **null**. |

**Examples**

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
         .onReady(() => {
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
         .onReady(() => {
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
