# EllipsisMode

省略号类型枚举。

EllipsisMode.START和EllipsisMode.MIDDLE仅在单行超长文本生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-enum EllipsisMode--><!--Device-text-enum EllipsisMode-End-->

**System capability:** SystemCapability.Graphics.Drawing

## START

```TypeScript
START = 0
```

开头省略号，该枚举值只在[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)中设置maxLines为1时生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-EllipsisMode-START = 0--><!--Device-EllipsisMode-START = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## MIDDLE

```TypeScript
MIDDLE = 1
```

中间省略号，该枚举值只在[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)中设置maxLines为1时生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-EllipsisMode-MIDDLE = 1--><!--Device-EllipsisMode-MIDDLE = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

## END

```TypeScript
END = 2
```

末尾省略号，该枚举值在[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)中maxLines设置为任何值时均有效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-EllipsisMode-END = 2--><!--Device-EllipsisMode-END = 2-End-->

**System capability:** SystemCapability.Graphics.Drawing

## MULTILINE_START

```TypeScript
MULTILINE_START = 3
```

开头省略号，该枚举值在[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)中maxLines设置为任何值时均有效。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-EllipsisMode-MULTILINE_START = 3--><!--Device-EllipsisMode-MULTILINE_START = 3-End-->

**System capability:** SystemCapability.Graphics.Drawing

## MULTILINE_MIDDLE

```TypeScript
MULTILINE_MIDDLE = 4
```

中间省略号，该枚举值在[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)中maxLines设置为任何值时均有效。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-EllipsisMode-MULTILINE_MIDDLE = 4--><!--Device-EllipsisMode-MULTILINE_MIDDLE = 4-End-->

**System capability:** SystemCapability.Graphics.Drawing

