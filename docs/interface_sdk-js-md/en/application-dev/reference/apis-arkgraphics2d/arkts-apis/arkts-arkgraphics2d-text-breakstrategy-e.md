# BreakStrategy

断行策略枚举。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-enum BreakStrategy--><!--Device-text-enum BreakStrategy-End-->

**System capability:** SystemCapability.Graphics.Drawing

## GREEDY

```TypeScript
GREEDY = 0
```

尽可能将当前行填满，不会自动添加连词符。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-BreakStrategy-GREEDY = 0--><!--Device-BreakStrategy-GREEDY = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## HIGH_QUALITY

```TypeScript
HIGH_QUALITY = 1
```

布局优化，必要时会自动添加连词符。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-BreakStrategy-HIGH_QUALITY = 1--><!--Device-BreakStrategy-HIGH_QUALITY = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

## BALANCED

```TypeScript
BALANCED = 2
```

保证一个段落的每一行的宽度相同，必要时会添加连词符。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-BreakStrategy-BALANCED = 2--><!--Device-BreakStrategy-BALANCED = 2-End-->

**System capability:** SystemCapability.Graphics.Drawing

