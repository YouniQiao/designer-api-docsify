# CanvasFillRule

```TypeScript
declare type CanvasFillRule = "evenodd" | "nonzero"
```

Defines the fill pattern algorithm used to determine whether a point is inside or outside a path. The value type is a union of the types listed in the table below.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-unnamed-declare type CanvasFillRule = "evenodd" | "nonzero"--><!--Device-unnamed-declare type CanvasFillRule = "evenodd" | "nonzero"-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| "evenodd" | The inside part of a shape is determined based on whether the counting result is an odd number or not. This rule determines whether a point is inside a shape by casting a ray from the point on the canvas in any direction and counting the number of intersections between the ray and the shape path. If the number of intersections is odd, the point is inside the shape. Otherwise, the point is outside the shape. |
| "nonzero" | The inside part of a shape is determined based on whether the counting result is zero or not. This rule determines whether a point is inside a shape by casting a ray from the point on the canvas in any direction and checking the intersections between the ray and the shape path. The initial count is **0**: assign a direction value to each segment of the path, add 1 each time the path crosses the ray from left to right, and subtract 1 each time it crosses the ray from right to left. If the final result is **0**, the point is outside the shape. Otherwise, the point is inside the shape. |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213, 213, 213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.font = '60px sans-serif'
          offContext.fillStyle = 'rgb(39, 135, 217)';
          // Non-zero rule (nonzero).
          offContext.beginPath();
          offContext.arc(100, 100, 60, 0, Math.PI * 2);
          offContext.arc(100, 100, 20, 0, Math.PI * 2);
          offContext.fill('nonzero'); // Use the non-zero rule.
          offContext.fillText('nonzero', 65, 200)
          // Even-odd rule (evenodd).
          offContext.beginPath();
          offContext.arc(250, 100, 60, 0, Math.PI * 2);
          offContext.arc(250, 100, 20, 0, Math.PI * 2);
          offContext.fill('evenodd'); // Use the even-odd rule.
          offContext.fillText('evenodd', 215, 200)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

