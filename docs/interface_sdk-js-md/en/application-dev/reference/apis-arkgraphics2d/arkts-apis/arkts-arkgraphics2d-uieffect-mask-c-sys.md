# Mask (System API)

Mask effect class, used as input for Filter and VisualEffect. Different types of Mask provide different grayscale distribution patterns, such as wave ring masks, radial gradients, pixel map masks, etc.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,
      fillColor?: Color): Mask
```

Creates a Mask instance with scaling effect by inputting a pixelMap, the area of the pixelMap to be drawn, the drawing area of the mounted node, and the color to fill outside the drawing area.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelMap | image.PixelMap | Yes |
| srcRect | common2D.Rect | Yes |
| dstRect | common2D.Rect | Yes |
| fillColor | [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap): Mask
```

Creates a Mask instance by inputting a pixelMap. This interface does not perform scaling on the input pixelMap.

**Since:** 22

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelMap | image.PixelMap | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## createRadialGradientMask

```TypeScript
static createRadialGradientMask(center: common2D.Point, radiusX: number, radiusY: number,
      gradients: Array<[number, number]>): Mask
```

Creates an elliptical mask Mask instance by inputting the center position of the ellipse, the semi-major and semi-minor axes, and shape parameters.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| center | common2D.Point | Yes |
| radiusX | number | Yes |
| radiusY | number | Yes |
| gradients | Array & lt;[number, number] & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## createRippleMask

```TypeScript
static createRippleMask(center: common2D.Point, radius: number, width: number, offset?: number): Mask
```

Creates a wave ring mask Mask instance by inputting the center position, radius, and width of the wave ring.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| center | common2D.Point | Yes |
| radius | number | Yes |
| width | number | Yes |
| offset | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## createUseEffectMask

```TypeScript
static createUseEffectMask(useEffect: boolean): Mask
```

Creates and sets a Mask instance indicating whether to use blur caching. This Mask instance is specifically designed for the useEffectMask parameter of the liquidMaterial method, used to declare whether the material effect uses blur caching to improve performance. When this Mask instance is used with other Filter or VisualEffect methods, the useEffect property may not take effect.

**Since:** 22

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [useEffect](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## createWaveGradientMask

```TypeScript
static createWaveGradientMask(center: common2D.Point, width: number, propagationRadius: number,
      blurRadius: number, turbulenceStrength?: number): Mask
```

Creates a single-wave mask Mask instance by inputting the wave source center position and single-wave parameters.

**Since:** 20

**System capability:** SystemCapability.Graphics.Drawing

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| center | common2D.Point | Yes |
| width | number | Yes |
| propagationRadius | number | Yes |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | Yes |
| turbulenceStrength | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
