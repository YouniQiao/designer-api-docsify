# ArcButtonProgressConfig

The class used for configuring ArcButton to support progress bar display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class ArcButtonProgressConfig--><!--Device-unnamed-export declare class ArcButtonProgressConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(value: double, total?: double, color?: ResourceColor)
```

Constructor of the ArcButtonProgressConfig.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-constructor(value: double, total?: double, color?: ResourceColor)--><!--Device-ArcButtonProgressConfig-constructor(value: double, total?: double, color?: ResourceColor)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | sets the value of progress. <br>Value range:[0, total] <br>When setting a value less than 0, it is set to 0; when setting a value greater than total, it is set to total. |
| total | double | No | sets the total of progress. |
| color | ResourceColor | No | sets the foreground color of progress. |

## color

```TypeScript
@Trace
  public color?: ResourceColor
```

Sets the foreground color of Progress.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-@Trace  public color?: ResourceColor--><!--Device-ArcButtonProgressConfig-@Trace  public color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## total

```TypeScript
@Trace
  public total?: double
```

Sets the total of Progress.

Range value: [0, 2147483647].

**Type:** double

**Default:** 100

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-@Trace  public total?: double--><!--Device-ArcButtonProgressConfig-@Trace  public total?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## value

```TypeScript
@Trace
  public value: double
```

Sets the value of Progress.

Range value: [0, total].

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-@Trace  public value: double--><!--Device-ArcButtonProgressConfig-@Trace  public value: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

