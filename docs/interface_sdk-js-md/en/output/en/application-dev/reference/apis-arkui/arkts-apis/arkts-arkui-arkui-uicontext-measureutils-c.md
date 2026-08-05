# MeasureUtils

class MeasureUtils

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class MeasureUtils--><!--Device-unnamed-export declare class MeasureUtils-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getParagraphs

```TypeScript
getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>
```

Get layout info of the styled string.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MeasureUtils-getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>--><!--Device-MeasureUtils-getParagraphs(styledString: StyledString, options?: TextLayoutOptions): Array<Paragraph>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The styled string value. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The layout options. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | paragraph result |

## measureText

```TypeScript
measureText(options: MeasureOptions): double
```

Obtains the width of the specified text in a single line layout.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MeasureUtils-measureText(options: MeasureOptions): double--><!--Device-MeasureUtils-measureText(options: MeasureOptions): double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options. |

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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MeasureUtils-measureTextSize(options: MeasureOptions): SizeOptions--><!--Device-MeasureUtils-measureTextSize(options: MeasureOptions): SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options of measure area occupied by text. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | width and height for text to display |

