# CpuUsageHighPolicy

提供CPU高负载事件配置策略的定义。

> **注意：**
> 
> 该接口被调用后，会将设置值持久化。后续重复调用该接口时，若不设置对应参数，则取上一次系统取用的值。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface CpuUsageHighPolicy--><!--Device-hiAppEvent-interface CpuUsageHighPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## backgroundLoadThreshold

```TypeScript
backgroundLoadThreshold?: int
```

应用后台CPU高负载异常阈值，阈值范围：[1, 100]，单位：%，默认值：10。若设置值在阈值范围外，系统将取用默认值10。

**说明：**建议取值小于10。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CpuUsageHighPolicy-backgroundLoadThreshold?: int--><!--Device-CpuUsageHighPolicy-backgroundLoadThreshold?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## foregroundLoadThreshold

```TypeScript
foregroundLoadThreshold?: int
```

应用前台CPU高负载异常阈值，阈值范围：[1, 100]，单位：%，默认值：30。若设置值在阈值范围外，系统将取用默认值30。

**说明：**建议取值小于30。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CpuUsageHighPolicy-foregroundLoadThreshold?: int--><!--Device-CpuUsageHighPolicy-foregroundLoadThreshold?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## perfLogCaptureCount

```TypeScript
perfLogCaptureCount?: int
```

采样栈每日采集次数。一旦系统检测到当前异常日志的采集次数超过设置值，系统仍会正常上报事件，但异常事件中的external_log字段，将不再附加日志文件路径信息。

Debug版本应用，阈值范围：[-1, 100]；

Release版本应用，阈值范围：[0, 20]。

单位：次，默认值：1。

若设置值在阈值范围外，系统将取用默认值1。

**说明：**

1. 值为-1，表示不限制采集日志次数。 2. 值为0，表示不采集日志。 3. 值大于0，表示每日采集次数上限。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CpuUsageHighPolicy-perfLogCaptureCount?: int--><!--Device-CpuUsageHighPolicy-perfLogCaptureCount?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## threadLoadInterval

```TypeScript
threadLoadInterval?: int
```

应用线程CPU高负载异常检测周期，阈值范围：[5, 3600]，单位：秒，默认值：60。

若设置值在阈值范围外，系统将取用默认值60。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CpuUsageHighPolicy-threadLoadInterval?: int--><!--Device-CpuUsageHighPolicy-threadLoadInterval?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## threadLoadThreshold

```TypeScript
threadLoadThreshold?: int
```

应用线程CPU高负载异常阈值，阈值范围：[15, 100]，单位：%，默认值：70。若设置值在阈值范围外，系统将取用默认值70。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-CpuUsageHighPolicy-threadLoadThreshold?: int--><!--Device-CpuUsageHighPolicy-threadLoadThreshold?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

