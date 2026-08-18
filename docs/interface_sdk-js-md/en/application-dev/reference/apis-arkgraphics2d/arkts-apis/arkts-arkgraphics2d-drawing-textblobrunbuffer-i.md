# TextBlobRunBuffer

Describes a series of consecutive glyphs with the same attributes in a text blob.

**Since:** 23

<!--Device-drawing-interface TextBlobRunBuffer--><!--Device-drawing-interface TextBlobRunBuffer-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## glyph

```TypeScript
glyph: int
```

Index of the glyph. The value is an integer. If a floating point number is passed in, the value is rounded down.

**Type:** int

**Since:** 23

<!--Device-TextBlobRunBuffer-glyph: int--><!--Device-TextBlobRunBuffer-glyph: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

## positionX

```TypeScript
positionX: double
```

X coordinate of the start point of the text blob. The value is a floating point number.

**Type:** double

**Since:** 23

<!--Device-TextBlobRunBuffer-positionX: double--><!--Device-TextBlobRunBuffer-positionX: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## positionY

```TypeScript
positionY: double
```

Y coordinate of the start point of the text blob. The value is a floating point number.

**Type:** double

**Since:** 23

<!--Device-TextBlobRunBuffer-positionY: double--><!--Device-TextBlobRunBuffer-positionY: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

