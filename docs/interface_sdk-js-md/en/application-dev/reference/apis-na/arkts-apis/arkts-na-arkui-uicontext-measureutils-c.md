# MeasureUtils

class MeasureUtils

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class MeasureUtils--><!--Device-unnamed-export declare class MeasureUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getParagraphs

```TypeScript
getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>
```

Get layout info of the styled string.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MeasureUtils-getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>--><!--Device-MeasureUtils-getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | StyledString | Yes | The styled string value. |
| options | TextLayoutOptions | No | The layout options. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Paragraph&gt; | paragraph result |

## measureText

```TypeScript
measureText(options: MeasureOptions): double
```

Obtains the width of the specified text in a single line layout.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MeasureUtils-measureText(options: MeasureOptions): double--><!--Device-MeasureUtils-measureText(options: MeasureOptions): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [MeasureOptions](../../apis-arkui/arkts-apis/arkts-arkui-measure-measureoptions-i.md) | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| double |  |

## measureTextSize

```TypeScript
measureTextSize(options: MeasureOptions): SizeOptions
```

Obtains the width and height of the specified text in a single line layout.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MeasureUtils-measureTextSize(options: MeasureOptions): SizeOptions--><!--Device-MeasureUtils-measureTextSize(options: MeasureOptions): SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [MeasureOptions](../../apis-arkui/arkts-apis/arkts-arkui-measure-measureoptions-i.md) | Yes | Options of measure area occupied by text. |

**Return value:**

| Type | Description |
| --- | --- |
| SizeOptions | width and height for text to display |

