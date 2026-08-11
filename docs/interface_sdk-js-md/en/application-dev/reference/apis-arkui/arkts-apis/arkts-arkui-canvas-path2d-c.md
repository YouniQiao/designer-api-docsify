# Path2D

2D path object for path drawing

**Inheritance/Implementation:** Path2D extends [CanvasPath](../arkts-components/arkts-arkui-canvaspath-c.md/arkts-arkui-canvaspath-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class Path2D extends CanvasPath--><!--Device-unnamed-export declare class Path2D extends CanvasPath-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addPath

```TypeScript
addPath(path: Path2D, transform?: Matrix2D): void
```

Adds a path according to the specified path variable.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path2D-addPath(path: Path2D, transform?: Matrix2D): void--><!--Device-Path2D-addPath(path: Path2D, transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes | Indicates the path object to be added. |
| transform | [Matrix2D](arkts-arkui-matrix2d-c.md) | No | Transformation matrix of the new trail. The default value is null. |

## constructor

```TypeScript
constructor()
```

Create an empty path object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path2D-constructor()--><!--Device-Path2D-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(unit: LengthMetricsUnit)
```

Create an empty path object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path2D-constructor(unit: LengthMetricsUnit)--><!--Device-Path2D-constructor(unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | Yes | the unit mode |

## constructor

```TypeScript
constructor(path: Path2D)
```

Create a copy of a path object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path2D-constructor(path: Path2D)--><!--Device-Path2D-constructor(path: Path2D)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes | Path object to be copied |

## constructor

```TypeScript
constructor(path: Path2D, unit: LengthMetricsUnit)
```

Create a copy of a path object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path2D-constructor(path: Path2D, unit: LengthMetricsUnit)--><!--Device-Path2D-constructor(path: Path2D, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-viewmodel-path2d-i.md) | Yes | Path object to be copied |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | Yes | the unit mode |

## constructor

```TypeScript
constructor(d: string)
```

Create a new path according to the description.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path2D-constructor(d: string)--><!--Device-Path2D-constructor(d: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | string | Yes | Indicates the path string that compiles with the SVG path description specifications. |

## constructor

```TypeScript
constructor(description: string, unit: LengthMetricsUnit)
```

Create a new path according to the description.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Path2D-constructor(description: string, unit: LengthMetricsUnit)--><!--Device-Path2D-constructor(description: string, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| description | string | Yes | Indicates the path string that compiles with the SVG path description specifications. |
| unit | [LengthMetricsUnit](arkts-arkui-lengthmetricsunit-t.md) | Yes | the unit mode |

