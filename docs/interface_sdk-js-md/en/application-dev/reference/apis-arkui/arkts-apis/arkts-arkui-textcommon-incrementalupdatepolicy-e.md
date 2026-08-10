# IncrementalUpdatePolicy

文本渲染的增量更新策略。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare enum IncrementalUpdatePolicy--><!--Device-unnamed-export declare enum IncrementalUpdatePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

不启用增量更新，采用全量布局渲染。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IncrementalUpdatePolicy-NONE = 0--><!--Device-IncrementalUpdatePolicy-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PARAGRAPH_CACHE

```TypeScript
PARAGRAPH_CACHE = 1
```

启用增量更新，使用段落级缓存。该策略生效的前提是文本绑定的属性字符串对象保持不变，若属性字符串对象发生变化则无法命中缓存。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IncrementalUpdatePolicy-PARAGRAPH_CACHE = 1--><!--Device-IncrementalUpdatePolicy-PARAGRAPH_CACHE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

