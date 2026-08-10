# ResourceOverlimitPolicy

提供资源泄漏事件配置策略的定义。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-hiAppEvent-interface ResourceOverlimitPolicy--><!--Device-hiAppEvent-interface ResourceOverlimitPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## jsHeapLogtype

```TypeScript
jsHeapLogtype?: string
```

设置传递堆快照规格。

"event"：应用发生OOM时，不传递堆快照。

"event_rawheap"：应用发生OOM时，系统生成并传递堆快照。

**说明：**

- 当前仅接收以上二值，如果传入其他内容，方法将调用失败，不会产生任何效果。  
- 参数值为"event_rawheap"，无法确保成功生成堆快照文件。原因是生成堆快照时，应用可能因性能问题触发冻屏而提前退出。  
- 应用每次使能行为只在应用当前生命周期生效，在同一生命周期内，以最后一次成功调用的使能状态为准。应用重启后，需要重新设置使能状态。

**起始版本**：26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务中使用。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ResourceOverlimitPolicy-jsHeapLogtype?: string--><!--Device-ResourceOverlimitPolicy-jsHeapLogtype?: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## pageSwitchLogEnable

```TypeScript
pageSwitchLogEnable?: boolean
```

是否使能资源泄漏事件的页面切换日志。

true：使能资源泄漏事件的页面切换日志。

false：不使能资源泄漏事件的页面切换日志。

默认值：false。

**说明：**应用每次使能行为只在应用当前生命周期生效，在同一生命周期内，以最后一次成功调用的使能状态为准。应用重启后，需要重新设置使能状态。

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ResourceOverlimitPolicy-pageSwitchLogEnable?: boolean--><!--Device-ResourceOverlimitPolicy-pageSwitchLogEnable?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## useRefinedLogFileName

```TypeScript
useRefinedLogFileName?: boolean
```

是否使能事件日志文件名精细化开关。

true：使能事件日志文件名精细化开关。

false：不使能事件日志文件名精细化开关。

默认值：false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ResourceOverlimitPolicy-useRefinedLogFileName?: boolean--><!--Device-ResourceOverlimitPolicy-useRefinedLogFileName?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

