# CanvasElement

&lt;canvas&gt; provides a rectangular canvas component for drawing graphics on the screen.You can control each pixel to draw on the canvas.&lt;canvas&gt; offers a variety of functions for drawing paths, rectangles, circles, text, and allows for adding images to it.

**继承/实现关系：** CanvasElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface CanvasElement extends Element--><!--Device-unnamed-export interface CanvasElement extends Element-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getContext

```TypeScript
getContext(type: "2d", options?: ContextAttrOptions): CanvasRenderingContext2D
```

Obtains the context of 2D canvas drawing.Only parameters related to 2D canvas drawing are supported.The return value is a 2D drawing object that provides specific 2D drawing operations.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CanvasElement-getContext(type: "2d", options?: ContextAttrOptions): CanvasRenderingContext2D--><!--Device-CanvasElement-getContext(type: "2d", options?: ContextAttrOptions): CanvasRenderingContext2D-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "2d" | 是 | identifier defining the drawing context associated to the canvas. |
| options | [ContextAttrOptions](arkts-arkui-viewmodel-contextattroptions-i.md) | 否 | use this context attributes to creating rendering context. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) |  |

## getContext

```TypeScript
getContext(type: "webgl", options?: WebGLContextAttributes): WebGLRenderingContext
```

Obtains the context of webgl canvas drawing.Only parameters related to webgl canvas drawing are supported.The return value is a webgl drawing object that provides specific webgl drawing operations.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CanvasElement-getContext(type: "webgl", options?: WebGLContextAttributes): WebGLRenderingContext--><!--Device-CanvasElement-getContext(type: "webgl", options?: WebGLContextAttributes): WebGLRenderingContext-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "webgl" | 是 | identifier defining the drawing context associated to the canvas. |
| options | [WebGLContextAttributes](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-webgl-webglcontextattributes-i.md) | 否 | use this context attributes to creating rendering context. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebGLRenderingContext](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-webgl-webglrenderingcontext-i.md) |  |

## getContext

```TypeScript
getContext(type: "webgl2", options?: WebGLContextAttributes): WebGL2RenderingContext
```

Obtains the context of webgl2 canvas drawing.Only parameters related to webgl2 canvas drawing are supported.The return value is a webgl2 drawing object that provides specific webgl2 drawing operations.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CanvasElement-getContext(type: "webgl2", options?: WebGLContextAttributes): WebGL2RenderingContext--><!--Device-CanvasElement-getContext(type: "webgl2", options?: WebGLContextAttributes): WebGL2RenderingContext-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | "webgl2" | 是 | identifier defining the drawing context associated to the canvas. |
| options | [WebGLContextAttributes](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-webgl-webglcontextattributes-i.md) | 否 | use this context attributes to creating rendering context. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebGL2RenderingContext](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-webgl2-webgl2renderingcontext-i.md) |  |

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: number): string
```

Creates a data URI that contains the image display.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CanvasElement-toDataURL(type?: string, quality?: number): string--><!--Device-CanvasElement-toDataURL(type?: string, quality?: number): string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 否 | A DOMString indicating the image format. The default type is image/png. |
| quality | number | 否 | A Number between 0 and 1 indicating image quality if the type option is image/jpeg or image/webp. If this argument is anything else, the default value for image quality is used. Other arguments are ignored. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

