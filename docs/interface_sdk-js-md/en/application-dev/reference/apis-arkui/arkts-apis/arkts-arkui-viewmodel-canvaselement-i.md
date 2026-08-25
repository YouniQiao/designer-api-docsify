# CanvasElement

&lt;canvas&gt; provides a rectangular canvas component for drawing graphics on the screen. You can control each pixel to draw on the canvas. &lt;canvas&gt; offers a variety of functions for drawing paths, rectangles, circles, text, and allows for adding images to it.@extends Element @interface CanvasElement

**Inheritance/Implementation:** CanvasElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**Since:** 4

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getContext("2d")

```TypeScript
getContext(type: "2d", options?: ContextAttrOptions): CanvasRenderingContext2D
```

Obtains the context of 2D canvas drawing. Only parameters related to 2D canvas drawing are supported. The return value is a 2D drawing object that provides specific 2D drawing operations.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "2d" | Yes |
| options | [ContextAttrOptions](arkts-arkui-viewmodel-contextattroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CanvasRenderingContext2D](arkts-arkui-viewmodel-canvasrenderingcontext2d-i.md) |

## getContext("webgl")

```TypeScript
getContext(type: "webgl", options?: WebGLContextAttributes): WebGLRenderingContext
```

Obtains the context of webgl canvas drawing. Only parameters related to webgl canvas drawing are supported. The return value is a webgl drawing object that provides specific webgl drawing operations.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "webgl" | Yes |
| options | [WebGLContextAttributes](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-webgl-webglcontextattributes-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebGLRenderingContext](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-webgl-webglrenderingcontext-i.md) |

## getContext("webgl2")

```TypeScript
getContext(type: "webgl2", options?: WebGLContextAttributes): WebGL2RenderingContext
```

Obtains the context of webgl2 canvas drawing. Only parameters related to webgl2 canvas drawing are supported. The return value is a webgl2 drawing object that provides specific webgl2 drawing operations.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "webgl2" | Yes |
| options | [WebGLContextAttributes](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-webgl-webglcontextattributes-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebGL2RenderingContext](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-webgl2-webgl2renderingcontext-i.md) |

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: number): string
```

Creates a data URI that contains the image display.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | string | No |
| quality | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
