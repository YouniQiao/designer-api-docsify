# BlurType

Enumerates the blur types of a mask filter. | Name | Value| Description | Diagram | | ------ | - | ------------------ | -------- | | NORMAL | 0 | Both the outer edges and the inner solid parts are blurred.|| | SOLID | 1 | The inner solid part remains unchanged, while only the outer edges are blurred.|| | OUTER | 2 | Only the outer edges are blurred, with the inner solid part being fully transparent.|| | INNER | 3 | Only the inner solid part is blurred, while the outer edges remain sharp.||

**Since:** 23

<!--Device-drawing-enum BlurType--><!--Device-drawing-enum BlurType-End-->

**System capability:** SystemCapability.Graphics.Drawing

## NORMAL

```TypeScript
NORMAL = 0
```

Both the outer edges and the inner solid parts are blurred.

**Since:** 23

<!--Device-BlurType-NORMAL = 0--><!--Device-BlurType-NORMAL = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## SOLID

```TypeScript
SOLID = 1
```

The inner solid part remains unchanged, while only the outer edges are blurred.

**Since:** 23

<!--Device-BlurType-SOLID = 1--><!--Device-BlurType-SOLID = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

## OUTER

```TypeScript
OUTER = 2
```

Only the outer edges are blurred, with the inner solid part being fully transparent.

**Since:** 23

<!--Device-BlurType-OUTER = 2--><!--Device-BlurType-OUTER = 2-End-->

**System capability:** SystemCapability.Graphics.Drawing

## INNER

```TypeScript
INNER = 3
```

Only the inner solid part is blurred, while the outer edges remain sharp.

**Since:** 23

<!--Device-BlurType-INNER = 3--><!--Device-BlurType-INNER = 3-End-->

**System capability:** SystemCapability.Graphics.Drawing

