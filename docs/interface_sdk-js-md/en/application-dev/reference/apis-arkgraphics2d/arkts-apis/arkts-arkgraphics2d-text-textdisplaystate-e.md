# TextDisplayState

文本显示状态的枚举。表示文本排版后的原生结果，与外部画布裁切、溢出屏幕等外部显示因素无关。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-text-enum TextDisplayState--><!--Device-text-enum TextDisplayState-End-->

**System capability:** SystemCapability.Graphics.Drawing

## UNKNOWN

```TypeScript
UNKNOWN = 0
```

未知显示状态，默认状态。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextDisplayState-UNKNOWN = 0--><!--Device-TextDisplayState-UNKNOWN = 0-End-->

**System capability:** SystemCapability.Graphics.Drawing

## ALL

```TypeScript
ALL = 1
```

完整显示状态，文本无截断、无省略，全部内容正常显示。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextDisplayState-ALL = 1--><!--Device-TextDisplayState-ALL = 1-End-->

**System capability:** SystemCapability.Graphics.Drawing

## CLIP

```TypeScript
CLIP = 2
```

裁剪显示状态，文本超出排版区域的部分被直接裁剪隐藏。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextDisplayState-CLIP = 2--><!--Device-TextDisplayState-CLIP = 2-End-->

**System capability:** SystemCapability.Graphics.Drawing

## OMITTED

```TypeScript
OMITTED = 3
```

省略显示状态，文本超出排版区域后，部分内容以指定字符（如省略号 '...'）替代展示。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TextDisplayState-OMITTED = 3--><!--Device-TextDisplayState-OMITTED = 3-End-->

**System capability:** SystemCapability.Graphics.Drawing

