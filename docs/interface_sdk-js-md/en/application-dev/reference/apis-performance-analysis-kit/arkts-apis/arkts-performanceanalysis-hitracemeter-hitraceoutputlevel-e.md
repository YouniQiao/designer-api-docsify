# HiTraceOutputLevel

枚举，跟踪输出级别。

低于系统跟踪输出级别阈值的打点将不会生效。log版本阈值为INFO；nolog版本阈值为COMMERCIAL。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-hiTraceMeter-enum HiTraceOutputLevel--><!--Device-hiTraceMeter-enum HiTraceOutputLevel-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## DEBUG

```TypeScript
DEBUG = 0
```

仅用于调试的输出级别，优先级最低。低于系统跟踪输出级别阈值时打点不会生效。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-HiTraceOutputLevel-DEBUG = 0--><!--Device-HiTraceOutputLevel-DEBUG = 0-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## INFO

```TypeScript
INFO = 1
```

用于log版本的输出级别，log版本阈值为INFO。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-HiTraceOutputLevel-INFO = 1--><!--Device-HiTraceOutputLevel-INFO = 1-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## CRITICAL

```TypeScript
CRITICAL = 2
```

用于log版本的输出级别，优先级高于INFO，用于需要重点关注的trace事件。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-HiTraceOutputLevel-CRITICAL = 2--><!--Device-HiTraceOutputLevel-CRITICAL = 2-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## COMMERCIAL

```TypeScript
COMMERCIAL = 3
```

用于nolog版本的输出级别，优先级最高。nolog版本阈值为COMMERCIAL。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-HiTraceOutputLevel-COMMERCIAL = 3--><!--Device-HiTraceOutputLevel-COMMERCIAL = 3-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

## MAX

```TypeScript
MAX = COMMERCIAL
```

输出级别范围限制，MAX = COMMERCIAL。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-HiTraceOutputLevel-MAX = COMMERCIAL--><!--Device-HiTraceOutputLevel-MAX = COMMERCIAL-End-->

**System capability:** SystemCapability.HiviewDFX.HiTrace

