# AddressSanitizerPolicy

提供地址越界事件配置策略的定义。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-hiAppEvent-interface AddressSanitizerPolicy--><!--Device-hiAppEvent-interface AddressSanitizerPolicy-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## pageSwitchLogEnable

```TypeScript
pageSwitchLogEnable?: boolean
```

是否使能地址越界事件的页面切换日志。

true：使能地址越界事件的页面切换日志。

false：不使能地址越界事件的页面切换日志。

默认值：false。

**说明：**应用每次使能行为只在应用当前生命周期生效，在同一生命周期内，以最后一次成功调用的使能状态为准。应用重启后，需要重新设置使能状态。

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AddressSanitizerPolicy-pageSwitchLogEnable?: boolean--><!--Device-AddressSanitizerPolicy-pageSwitchLogEnable?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

