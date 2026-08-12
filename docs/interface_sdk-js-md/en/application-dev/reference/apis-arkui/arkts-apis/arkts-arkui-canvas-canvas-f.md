# Canvas

## Canvas

```TypeScript
export declare function Canvas(
  context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions
): CanvasAttribute
```

Canvas is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Canvas(  context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions): CanvasAttribute--><!--Device-unnamed-export declare function Canvas(  context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions): CanvasAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](arkts-arkui-canvas-canvasrenderingcontext2d-c.md) \| [DrawingRenderingContext](arkts-arkui-canvas-drawingrenderingcontext-c.md) | No | Canvas context object. |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | No | Options for AI analyzer. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) | The attribute of the Canvas. |


## Canvas

```TypeScript
export declare function Canvas(
  params: CanvasParams
): CanvasAttribute
```

Create a canvas component using { @link CanvasParams }.This canvas component will not respond to drawing commands when invisible for memory optimization,You can get a rendering context in { @link onReady }.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Canvas(  params: CanvasParams): CanvasAttribute--><!--Device-unnamed-export declare function Canvas(  params: CanvasParams): CanvasAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [CanvasParams](arkts-arkui-canvas-canvasparams-i.md) | Yes | Parameters for creating Canvas. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) | The attribute of the Canvas. |


## Canvas

```TypeScript
export declare function Canvas(
    style_: CustomBuilderT<CanvasAttribute>
): CanvasAttribute
```

Defines Canvas Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Canvas(    style_: CustomBuilderT<CanvasAttribute>): CanvasAttribute--><!--Device-unnamed-export declare function Canvas(    style_: CustomBuilderT<CanvasAttribute>): CanvasAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md)&gt; | Yes | Canvas attribute instance. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) |  |

