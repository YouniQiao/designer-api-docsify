# AppEventFilter

提供设置[Watcher](arkts-performanceanalysis-hiappevent-watcher-i.md)的订阅过滤条件的参数选项。用于在事件观察者中设置事件过滤条件，确保只有满足过滤条件的事件才会被监听处理。

> **说明：**
> 
> 不同类型应用上，系统事件的订阅规格不同，具体规格可参见[HiAppEvent约束与限制](../../../dfx/hiappevent-intro.md#约束与限制)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface AppEventFilter--><!--Device-hiAppEvent-interface AppEventFilter-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## domain

```TypeScript
domain: string
```

需要订阅的事件领域。可以是系统事件领域（hiAppEvent.domain.OS）或开发者在使用[Write](arkts-performanceanalysis-hiappevent-write-f.md#write)接口时传入的自定义事件信息（[AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md)）中的事件领域。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventFilter-domain: string--><!--Device-AppEventFilter-domain: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## eventTypes

```TypeScript
eventTypes?: EventType[]
```

需要订阅的事件类型集合。默认不进行过滤。

**Type:** [EventType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventFilter-eventTypes?: EventType[]--><!--Device-AppEventFilter-eventTypes?: EventType[]-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## names

```TypeScript
names?: string[]
```

需要订阅的事件名称集合。默认不进行过滤。

**Type:** string[]

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventFilter-names?: string[]--><!--Device-AppEventFilter-names?: string[]-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

