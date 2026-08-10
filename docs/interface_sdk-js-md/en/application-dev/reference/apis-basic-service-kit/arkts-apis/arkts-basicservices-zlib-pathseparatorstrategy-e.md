# PathSeparatorStrategy

PathSeparatorStrategy作为[Options](arkts-basicservices-zlib-options-i.md)的一个属性，用于指定解压时目标压缩包内文件路径中分隔符的处理策略。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-zlib-export enum PathSeparatorStrategy--><!--Device-zlib-export enum PathSeparatorStrategy-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## PATH_SEPARATOR_STRATEGY_DEFAULT

```TypeScript
PATH_SEPARATOR_STRATEGY_DEFAULT = 0
```

默认值，压缩包内文件路径中的分隔符不做处理。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PathSeparatorStrategy-PATH_SEPARATOR_STRATEGY_DEFAULT = 0--><!--Device-PathSeparatorStrategy-PATH_SEPARATOR_STRATEGY_DEFAULT = 0-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## PATH_SEPARATOR_STRATEGY_REPLACE_BACKSLASH

```TypeScript
PATH_SEPARATOR_STRATEGY_REPLACE_BACKSLASH = 1
```

压缩包内文件路径中的反斜杠'\'替换为斜杠'/'。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PathSeparatorStrategy-PATH_SEPARATOR_STRATEGY_REPLACE_BACKSLASH = 1--><!--Device-PathSeparatorStrategy-PATH_SEPARATOR_STRATEGY_REPLACE_BACKSLASH = 1-End-->

**System capability:** SystemCapability.BundleManager.Zlib

