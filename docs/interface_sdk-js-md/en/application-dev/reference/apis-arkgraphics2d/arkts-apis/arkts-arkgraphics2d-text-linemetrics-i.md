# LineMetrics

Describes the measurement information of a single line of text in the text layout.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-interface LineMetrics--><!--Device-text-interface LineMetrics-End-->

**System capability:** SystemCapability.Graphics.Drawing

## ascent

```TypeScript
ascent: double
```

Text ascent height, which refers to the distance from the baseline to the top of characters, in physical pixels (px).

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-ascent: double--><!--Device-LineMetrics-ascent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## baseline

```TypeScript
baseline: double
```

Y coordinate of the baseline in the line relative to the top of the paragraph, in physical pixels (px).

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-baseline: double--><!--Device-LineMetrics-baseline: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## descent

```TypeScript
descent: double
```

Text descent height, which refers to the distance from the baseline to the bottom of characters, in physical pixels (px).

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-descent: double--><!--Device-LineMetrics-descent: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## endIndex

```TypeScript
endIndex: int
```

End index of the line in the text buffer.

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-endIndex: int--><!--Device-LineMetrics-endIndex: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

## height

```TypeScript
height: double
```

Height of the current line, in physical pixels (px). The calculation method is \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-height: double--><!--Device-LineMetrics-height: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## left

```TypeScript
left: double
```

Left edge position of a line, in physical pixels (px). The right edge is the value of **left** plus the value of  
**width**.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-left: double--><!--Device-LineMetrics-left: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## lineNumber

```TypeScript
lineNumber: int
```

Line number, starting from 0.

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-lineNumber: int--><!--Device-LineMetrics-lineNumber: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

## runMetrics

```TypeScript
runMetrics: Map<int, RunMetrics>
```

Mapping between the text index range and the associated font measurement information.

**Type:** Map&lt;int, RunMetrics&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-runMetrics: Map<int, RunMetrics>--><!--Device-LineMetrics-runMetrics: Map<int, RunMetrics>-End-->

**System capability:** SystemCapability.Graphics.Drawing

## startIndex

```TypeScript
startIndex: int
```

Start index of the line in the text buffer.

**Type:** int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-startIndex: int--><!--Device-LineMetrics-startIndex: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

## topHeight

```TypeScript
topHeight: double
```

Height from the top to the current line, in physical pixels (px).

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-topHeight: double--><!--Device-LineMetrics-topHeight: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

## width

```TypeScript
width: double
```

Width of a line, in physical pixels (px).

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-LineMetrics-width: double--><!--Device-LineMetrics-width: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

