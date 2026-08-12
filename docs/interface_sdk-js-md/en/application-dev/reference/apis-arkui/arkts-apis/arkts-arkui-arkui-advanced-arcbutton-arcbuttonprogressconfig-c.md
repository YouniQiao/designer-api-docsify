# ArcButtonProgressConfig

The class used for configuring ArcButton to support progress bar display.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class ArcButtonProgressConfig--><!--Device-unnamed-export declare class ArcButtonProgressConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcButtonPosition, ArcButton, ArcButtonStatus, ArcButtonStyleMode, ArcButtonOptions, ArcButtonProgressConfig } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(value: double, total?: double, color?: ResourceColor)
```

Constructor of the ArcButtonProgressConfig.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-constructor(value: double, total?: double, color?: ResourceColor)--><!--Device-ArcButtonProgressConfig-constructor(value: double, total?: double, color?: ResourceColor)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | sets the value of progress. &lt;br&gt;Value range:[0, total] &lt;br&gt;When setting a value less than 0, it is set to 0; when setting a value greater than total, it is set to total. |
| total | double | No | sets the total of progress. |
| color | ResourceColor | No | sets the foreground color of progress. |

## color

```TypeScript
public color?: ResourceColor
```

Sets the foreground color of Progress.

**Type:** ResourceColor

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-public color?: ResourceColor--><!--Device-ArcButtonProgressConfig-public color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## total

```TypeScript
public total?: double
```

Sets the total of Progress.

Range value: [0, 2147483647].

**Type:** double

**Default:** 100

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-public total?: double--><!--Device-ArcButtonProgressConfig-public total?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## value

```TypeScript
public value: double
```

Sets the value of Progress.

Range value: [0, total].

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-public value: double--><!--Device-ArcButtonProgressConfig-public value: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

