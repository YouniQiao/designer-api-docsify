# TextMetrics

Size information of the text.

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## actualBoundingBoxAscent

```TypeScript
readonly actualBoundingBoxAscent: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the top of the bounding rectangle used to render the text. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## actualBoundingBoxDescent

```TypeScript
readonly actualBoundingBoxDescent: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the bottom of the bounding rectangle used to render the text. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## actualBoundingBoxLeft

```TypeScript
readonly actualBoundingBoxLeft: number
```

Distance parallel to the baseline from the alignment point determined by the [CanvasRenderingContext2D.textAlign](arkts-arkui-canvastextalign-t.md) attribute to the left side of the bounding rectangle of the text. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## actualBoundingBoxRight

```TypeScript
readonly actualBoundingBoxRight: number
```

Distance parallel to the baseline from the alignment point determined by the [CanvasRenderingContext2D.textAlign](arkts-arkui-canvastextalign-t.md) attribute to the right side of the bounding rectangle of the text. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alphabeticBaseline

```TypeScript
readonly alphabeticBaseline: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the alphabetic baseline of the line box. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## emHeightAscent

```TypeScript
readonly emHeightAscent: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the top of the em square in the line box. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## emHeightDescent

```TypeScript
readonly emHeightDescent: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the bottom of the em square in the line box. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontBoundingBoxAscent

```TypeScript
readonly fontBoundingBoxAscent: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the top of the bounding rectangle of all the fonts used to render the text. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontBoundingBoxDescent

```TypeScript
readonly fontBoundingBoxDescent: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the bottom of the bounding rectangle of all the fonts used to render the text. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hangingBaseline

```TypeScript
readonly hangingBaseline: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the hanging baseline of the line box. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
readonly height: number
```

Height of the text. Read-only.Default unit: vp.If the unit mode of the **CanvasRenderingContext2D** object is set to px, the unit is px.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct OffscreenCanvasPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(200, 300);

  build() {
    Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .borderWidth(5)
          .borderColor('#057D02')
          .backgroundColor('#FFFFFF')
          .onReady(() => {
            let offContext = this.offCanvas.getContext("2d", this.settings)
            offContext.fillStyle = '#CDCDCD'
            offContext.fillRect(0, 0, 100, this.offCanvas.height)
            let image = this.offCanvas.transferToImageBitmap()
            this.context.setTransform(1, 0, 0, 1, 50, 200)
            this.context.transferFromImageBitmap(image)
          })
      }
    }.width('100%').height('100%')
  }
}
```

## ideographicBaseline

```TypeScript
readonly ideographicBaseline: number
```

Distance from the horizontal line specified by the [CanvasRenderingContext2D.textBaseline](arkts-arkui-canvastextbaseline-t.md) attribute to the ideographic baseline of the line box. Read-only.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
readonly width: number
```

Width of the text. Read-only.Default unit: vp.If the unit mode of the **CanvasRenderingContext2D** object is set to px, the unit is px.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct OffscreenCanvasPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(200, 300);

  build() {
    Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .borderWidth(5)
          .borderColor('#057D02')
          .backgroundColor('#FFFFFF')
          .onReady(() => {
            let offContext = this.offCanvas.getContext("2d", this.settings)
            offContext.fillStyle = '#CDCDCD'
            offContext.fillRect(0, 0, this.offCanvas.width, 150)
            let image = this.offCanvas.transferToImageBitmap()
            this.context.setTransform(1, 0, 0, 1, 50, 200)
            this.context.transferFromImageBitmap(image)
          })
      }
    }.width('100%').height('100%')
  }
}
```
