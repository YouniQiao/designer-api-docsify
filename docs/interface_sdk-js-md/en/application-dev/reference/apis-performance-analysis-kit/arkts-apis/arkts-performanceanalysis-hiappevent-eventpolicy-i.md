# EventPolicy

提供系统事件配置策略的定义，用于使用[configEventPolicy](arkts-performanceanalysis-hiappevent-configeventpolicy-f.md#configeventpolicy)设置事件配置策略。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface EventPolicy--><!--Device-hiAppEvent-interface EventPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addressSanitizerPolicy

```TypeScript
addressSanitizerPolicy?: AddressSanitizerPolicy
```

地址越界事件配置策略。

**Type:** [AddressSanitizerPolicy](arkts-performanceanalysis-hiappevent-addresssanitizerpolicy-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-EventPolicy-addressSanitizerPolicy?: AddressSanitizerPolicy--><!--Device-EventPolicy-addressSanitizerPolicy?: AddressSanitizerPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## appCrashPolicy

```TypeScript
appCrashPolicy?: AppCrashPolicy
```

崩溃事件配置策略。

**Type:** [AppCrashPolicy](arkts-performanceanalysis-hiappevent-appcrashpolicy-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-EventPolicy-appCrashPolicy?: AppCrashPolicy--><!--Device-EventPolicy-appCrashPolicy?: AppCrashPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## appFreezePolicy

```TypeScript
appFreezePolicy?: AppFreezePolicy
```

应用冻屏事件配置策略。

**Type:** [AppFreezePolicy](arkts-performanceanalysis-hiappevent-appfreezepolicy-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-EventPolicy-appFreezePolicy?: AppFreezePolicy--><!--Device-EventPolicy-appFreezePolicy?: AppFreezePolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## cpuUsageHighPolicy

```TypeScript
cpuUsageHighPolicy?: CpuUsageHighPolicy
```

CPU高负载事件配置策略。

**Type:** [CpuUsageHighPolicy](arkts-performanceanalysis-hiappevent-cpuusagehighpolicy-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-EventPolicy-cpuUsageHighPolicy?: CpuUsageHighPolicy--><!--Device-EventPolicy-cpuUsageHighPolicy?: CpuUsageHighPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## mainThreadJankPolicy

```TypeScript
mainThreadJankPolicy?: MainThreadJankPolicy
```

主线程超时事件配置策略。

**Type:** [MainThreadJankPolicy](arkts-performanceanalysis-hiappevent-mainthreadjankpolicy-i.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-EventPolicy-mainThreadJankPolicy?: MainThreadJankPolicy--><!--Device-EventPolicy-mainThreadJankPolicy?: MainThreadJankPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## resourceOverlimitPolicy

```TypeScript
resourceOverlimitPolicy?: ResourceOverlimitPolicy
```

资源泄漏事件配置策略。

**Type:** [ResourceOverlimitPolicy](arkts-performanceanalysis-hiappevent-resourceoverlimitpolicy-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-EventPolicy-resourceOverlimitPolicy?: ResourceOverlimitPolicy--><!--Device-EventPolicy-resourceOverlimitPolicy?: ResourceOverlimitPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

