# MeasureText

Defines the Measure interface.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class MeasureText--><!--Device-unnamed-declare class MeasureText-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { MeasureOptions } from 'MeasureOptions';
```

## measureText

```TypeScript
static measureText(options: MeasureOptions): double
```

Displays the textWidth.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MeasureText-static measureText(options: MeasureOptions): double--><!--Device-MeasureText-static measureText(options: MeasureOptions): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## measureTextSize

```TypeScript
static measureTextSize(options: MeasureOptions): SizeOptions
```

Displays the text width and height.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-MeasureText-static measureTextSize(options: MeasureOptions): SizeOptions--><!--Device-MeasureText-static measureTextSize(options: MeasureOptions): SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [MeasureOptions](arkts-arkui-measure-measureoptions-i.md) | Yes | Options of measure area occupied by text. |

**Return value:**

| Type | Description |
| --- | --- |
| SizeOptions | width and height for text to display \ |

