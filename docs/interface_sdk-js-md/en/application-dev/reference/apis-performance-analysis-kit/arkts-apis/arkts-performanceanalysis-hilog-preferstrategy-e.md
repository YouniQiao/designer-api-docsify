# PreferStrategy

偏好策略。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-hilog-enum PreferStrategy--><!--Device-hilog-enum PreferStrategy-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## UNSET_LOGLEVEL

```TypeScript
UNSET_LOGLEVEL = 0
```

清除设置, 实际生效的最低日志级别是系统控制的最低级别。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PreferStrategy-UNSET_LOGLEVEL = 0--><!--Device-PreferStrategy-UNSET_LOGLEVEL = 0-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## PREFER_CLOSE_LOG

```TypeScript
PREFER_CLOSE_LOG = 1
```

实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较大值。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PreferStrategy-PREFER_CLOSE_LOG = 1--><!--Device-PreferStrategy-PREFER_CLOSE_LOG = 1-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

## PREFER_OPEN_LOG

```TypeScript
PREFER_OPEN_LOG = 2
```

实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较小值。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-PreferStrategy-PREFER_OPEN_LOG = 2--><!--Device-PreferStrategy-PREFER_OPEN_LOG = 2-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

