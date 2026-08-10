# TriggerCondition

提供设置[Watcher](arkts-performanceanalysis-hiappevent-watcher-i.md)的onTrigger回调触发条件的参数选项。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface TriggerCondition--><!--Device-hiAppEvent-interface TriggerCondition-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## row

```TypeScript
row?: int
```

满足触发回调的事件总数量，正整数。默认值0，不触发回调。传入负值时，会被置为默认值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TriggerCondition-row?: int--><!--Device-TriggerCondition-row?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## size

```TypeScript
size?: int
```

满足触发回调的事件总大小，正整数，单位为byte。默认值0，不触发回调。传入负值时，会被置为默认值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TriggerCondition-size?: int--><!--Device-TriggerCondition-size?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## timeOut

```TypeScript
timeOut?: int
```

满足触发回调的超时时长，正整数，单位为s，值为timeOut * 30。默认值0，不触发回调。传入负值时，会被置为默认值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TriggerCondition-timeOut?: int--><!--Device-TriggerCondition-timeOut?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

