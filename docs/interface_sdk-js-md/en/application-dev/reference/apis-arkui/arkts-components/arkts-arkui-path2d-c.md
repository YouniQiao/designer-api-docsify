# Path2D

*Path2D** allows you to describe a path through an existing path. This path can be drawn through the **stroke** or **fill** API of **Canvas**.

> **NOTE：**
> 
> The Path2D object does not support the resetting of an existing path. If a new path
> is required, you can create an empty Path2D object.
> 
> The methods of the Path2D object do not take effect for the paths set in the
> [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md)
> and
> [OffscreenCanvasRenderingContext2D](arkts-arkui-offscreencanvasrenderingcontext2d-c.md)
> objects.

@extends CanvasPath

**Inheritance/Implementation:** Path2D extends [CanvasPath](arkts-arkui-canvaspath-c.md)

**Since:** 8

<!--Device-unnamed-declare class Path2D--><!--Device-unnamed-declare class Path2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## addPath

```TypeScript
addPath(path: Path2D, transform?: Matrix2D): void
```

Adds a path to this path.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Path2D-addPath(path: Path2D, transform?: Matrix2D): void--><!--Device-Path2D-addPath(path: Path2D, transform?: Matrix2D): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-path2d-c.md) | Yes | Path to be added to this path. Unit: px.<br> The **undefined** and **null** values are treated as invalid. |
| transform | Matrix2D | No | Transformation matrix of the new path.<br> The **undefined** and **null** values are treated as invalid.<br> Default value: **null**. |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct AddPath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private path2Da: Path2D = new Path2D("M250 150 L150 350 L350 350 Z");
  private path2Db: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Db.addPath(this.path2Da)
          this.context.stroke(this.path2Db)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## constructor

```TypeScript
constructor()
```

Constructs an empty **Path2D** object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Path2D-constructor()--><!--Device-Path2D-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

The following example shows how to specify the unit mode during the creation of a CanvasRenderingContext2D object. The default unit mode is LengthMetricsUnit.DEFAULT, which corresponds to the default unit vp. Once set, this unit mode cannot be changed dynamically. For details, see LengthMetricsUnit.

```TypeScript
// xxx.ets
import { LengthMetricsUnit } from '@kit.ArkUI'

@Entry
@Component
struct LengthMetricsUnitDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private contextPX: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX);
  private contextVP: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.contextPX)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextPX.fillRect(10,10,100,100)
          this.contextPX.clearRect(10,10,50,50)
        })

      Canvas(this.contextVP)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextVP.fillRect(10,10,100,100)
          this.contextVP.clearRect(10,10,50,50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## constructor

```TypeScript
constructor(unit: LengthMetricsUnit)
```

Constructs an empty Path2D object. The unit mode of the Path2D object can be configured.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Path2D-constructor(unit: LengthMetricsUnit)--><!--Device-Path2D-constructor(unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unit | LengthMetricsUnit | Yes | Unit mode of the Path2D object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md).<br> Invalid values **NaN** and **Infinity** are treated as the default value.<br> Default value: **DEFAULT |

**Examples**

See [constructor](#constructor)

## constructor

```TypeScript
constructor(path: Path2D)
```

Constructs a Path2D object using a path object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Path2D-constructor(path: Path2D)--><!--Device-Path2D-constructor(path: Path2D)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-path2d-c.md) | Yes | Path** object. |

**Examples**

See [constructor](#constructor)

## constructor

```TypeScript
constructor(path: Path2D, unit: LengthMetricsUnit)
```

When a path object is used to construct a Path2D object, the unit mode of the Path2D object can be configured.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Path2D-constructor(path: Path2D, unit: LengthMetricsUnit)--><!--Device-Path2D-constructor(path: Path2D, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path2D](arkts-arkui-path2d-c.md) | Yes | Path** object. |
| unit | LengthMetricsUnit | Yes | Unit mode of the Path2D object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md).<br> Invalid values **NaN** and **Infinity** are treated as the default value.<br> Default value: **DEFAULT |

**Examples**

See [constructor](#constructor)

## constructor

```TypeScript
constructor(d: string)
```

Constructs a Path2D object using a path string that complies with the SVG path description specifications.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-Path2D-constructor(d: string)--><!--Device-Path2D-constructor(d: string)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | string | Yes | Path that complies with the [SVG path syntax](#path2d). Invalid values are treated as invalid inputs. |

**Examples**

See [constructor](#constructor)

## constructor

```TypeScript
constructor(description: string, unit: LengthMetricsUnit)
```

Constructs a Path2D object using a path string that complies with the SVG path specifications. The unit mode of the Path2D object can be configured.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-Path2D-constructor(description: string, unit: LengthMetricsUnit)--><!--Device-Path2D-constructor(description: string, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| description | string | Yes | Path that complies with the [SVG path syntax](#path2d). Invalid values are treated as invalid inputs. |
| unit | LengthMetricsUnit | Yes | Unit mode of the Path2D object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md).<br> Invalid values **NaN** and **Infinity** are treated as the default value.<br> Default value: **DEFAULT |

**Examples**

See [constructor](#constructor)

