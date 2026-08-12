# PathEffect

Implements a path effect.

> **NOTE：**
> 
> - The initial APIs of this class are supported since API version 12.
> 
> - This module uses the physical pixel unit, px.
> 
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class PathEffect--><!--Device-drawing-class PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## createComposePathEffect

```TypeScript
static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect
```

Creates a path effect by sequentially applying the inner effect and then the outer effect.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect--><!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outer | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | Path effect that is applied second, overlaying the first effect. |
| inner | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | Inner path effect that is applied first. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect** object created. |

## createComposePathEffect

```TypeScript
static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect | undefined
```

Creates a path effect by sequentially applying the inner effect and then the outer effect.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect | undefined--><!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outer | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | Path effect that is applied second, overlaying the first effect. |
| inner | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | Inner path effect that is applied first. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect object. |

## createCornerPathEffect

```TypeScript
static createCornerPathEffect(radius: number): PathEffect
```

Creates a path effect that transforms the sharp angle between line segments into a rounded corner with the specified radius.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-PathEffect-static createCornerPathEffect(radius: number): PathEffect--><!--Device-PathEffect-static createCornerPathEffect(radius: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | number | Yes | Radius of the rounded corner. The value must be greater than 0. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createCornerPathEffect

```TypeScript
static createCornerPathEffect(radius: double): PathEffect | undefined
```

Creates a path effect that transforms the sharp angle between line segments into a rounded corner with the specified radius.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createCornerPathEffect(radius: double): PathEffect | undefined--><!--Device-PathEffect-static createCornerPathEffect(radius: double): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | double | Yes | Radius of the rounded corner. The value must be greater than 0. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createDashPathEffect

```TypeScript
static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect
```

Creates a **PathEffect** object that converts a path into a dotted line.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-PathEffect-static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect--><!--Device-PathEffect-static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intervals | Array&lt;number&gt; | Yes | Array of the lengths of the ON (solid line) and OFF (blank) parts of the dashed path. The number of elements in the array must be an even number and greater than or equal to 2. The value of this parameter is a positive integer. |
| phase | number | Yes | Offset used during drawing. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createDashPathEffect

```TypeScript
static createDashPathEffect(intervals: Array<double>, phase: double): PathEffect | undefined
```

Creates a PathEffect object that converts a path into a dotted line.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createDashPathEffect(intervals: Array<double>, phase: double): PathEffect | undefined--><!--Device-PathEffect-static createDashPathEffect(intervals: Array<double>, phase: double): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intervals | Array&lt;double&gt; | Yes | Array of ON and OFF lengths of dotted lines. The number of arrays must be an even number and be greater than or equal to 2. |
| phase | double | Yes | Offset used during drawing. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createDiscretePathEffect

```TypeScript
static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect
```

Creates an effect that segments the path and scatters the segments in an irregular pattern along the path.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-PathEffect-static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect--><!--Device-PathEffect-static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| segLength | number | Yes | Distance along the path at which each segment is fragmented. The value is a floating point number. If a negative number or the value **0** is passed in, no effect is created. |
| dev | number | Yes | Maximum amount by which the end points of the segments can be randomly displaced during rendering. The value is a floating-point number. |
| seedAssist | number | No | Optional parameter to assist in generating a pseudo-random seed for the effect. The default value is **0**, and the value is a 32-bit unsigned integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect** object created. |

## createDiscretePathEffect

```TypeScript
static createDiscretePathEffect(segLength: double, dev: double, seedAssist?: int): PathEffect | undefined
```

Creates an effect that segments the path and scatters the segments in an irregular pattern along the path.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createDiscretePathEffect(segLength: double, dev: double, seedAssist?: int): PathEffect | undefined--><!--Device-PathEffect-static createDiscretePathEffect(segLength: double, dev: double, seedAssist?: int): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| segLength | double | Yes | Distance along the path at which each segment is fragmented. The value is a floating point number. If a negative number or the value 0 is passed in, no effect is created. |
| dev | double | Yes | Maximum amount by which the end points of the segments can be randomly displaced during rendering. The value is a floating-point number. |
| seedAssist | int | No | Optional parameter to assist in generating a pseudo-random seed for the effect. The default value is 0, and the value is a 32-bit unsigned integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect object. |

## createPathDashEffect

```TypeScript
static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect
```

Creates a dashed path effect based on the shape described by a path.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-PathEffect-static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect--><!--Device-PathEffect-static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | Path | Yes | Path that defines the shape to be used for filling each dash in the pattern. |
| advance | number | Yes | Distance between two consecutive dashes. The value is a floating point number greater than 0. Otherwise, an error code is thrown. |
| phase | number | Yes | Starting offset of the dash pattern. The value is a floating point number. The actual offset used is the absolute value of this value modulo the value of **advance**. |
| style | [PathDashStyle](arkts-arkgraphics2d-drawing-pathdashstyle-e.md) | Yes | Style of the dashed path effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect** object created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createPathDashEffect

```TypeScript
static createPathDashEffect(path: Path, advance: double, phase: double, style: PathDashStyle): PathEffect | undefined
```

Creates a dashed path effect based on the shape described by a path.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createPathDashEffect(path: Path, advance: double, phase: double, style: PathDashStyle): PathEffect | undefined--><!--Device-PathEffect-static createPathDashEffect(path: Path, advance: double, phase: double, style: PathDashStyle): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | Path | Yes | Path that defines the shape to be used for filling each dash in the pattern. |
| advance | double | Yes | Distance between two consecutive dashes. The value is a floating point number greater than 0. Otherwise, an error code is thrown. |
| phase | double | Yes | Starting offset of the dash pattern. The value is a floating point number. The actual offset used is the absolute value of this value modulo the value of advance. |
| style | [PathDashStyle](arkts-arkgraphics2d-drawing-pathdashstyle-e.md) | Yes | Style of the dashed path effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createSumPathEffect

```TypeScript
static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect
```

Creates an overlay path effect based on two distinct path effects. Different from **createComposePathEffect**,this API applies each effect separately and then displays them as a simple overlay.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect--><!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | First path effect. |
| secondPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | Second path effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect** object created. |

## createSumPathEffect

```TypeScript
static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect | undefined
```

Creates an overlay path effect based on two distinct path effects.Different from createComposePathEffect,this API applies each effect separately and then displays them as a simple overlay.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect | undefined--><!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | First path effect. |
| secondPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | Second path effect. |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | PathEffect object. |

