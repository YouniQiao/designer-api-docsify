# Watcher

提供事件观察者的参数选项。用于配置和管理事件的观察者，实现对特定事件的监听和处理。

> **说明：**
> 
> 不建议在回调函数中执行[removeWatcher](arkts-performanceanalysis-hiappevent-removewatcher-f.md#removewatcher)的操作，watcher一旦被移除，则其原有的订阅回调功能也会随之失效，可能会造成某些事件发生后无订阅回调情况。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-interface Watcher--><!--Device-hiAppEvent-interface Watcher-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## onReceive

```TypeScript
onReceive?: (domain: string, appEventGroups: Array<AppEventGroup>) => void
```

订阅实时回调函数，与回调函数onTrigger同时存在时，只触发此回调，函数入参说明如下：

domain：回调事件的领域名称； 

appEventGroups：回调事件集合。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-onReceive?: (domain: string, appEventGroups: Array<AppEventGroup>) => void--><!--Device-Watcher-onReceive?: (domain: string, appEventGroups: Array<AppEventGroup>) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domain | string | Yes |  |
| appEventGroups | Array&lt;AppEventGroup&gt; | Yes |  |

## onTrigger

ArkTS-Dyn:
```TypeScript
onTrigger?: (curRow: number, curSize: number, holder: AppEventPackageHolder) => void
```

ArkTS-Sta:
```TypeScript
onTrigger?: (curRow: int, curSize: int, holder: AppEventPackageHolder) => void
```

订阅回调函数，需要与回调触发条件triggerCondition一同传入才会生效，函数入参说明如下：

curRow：在本次回调触发时的订阅事件总数量； 

curSize：在本次回调触发时的订阅事件总大小，单位为byte； 

holder：订阅数据持有者对象，可以通过其对订阅事件进行处理。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-onTrigger?: (curRow: int, curSize: int, holder: AppEventPackageHolder) => void--><!--Device-Watcher-onTrigger?: (curRow: int, curSize: int, holder: AppEventPackageHolder) => void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| curRow | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |
| curSize | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes |  |
| holder | [AppEventPackageHolder](arkts-performanceanalysis-hiappevent-appeventpackageholder-c.md) | Yes |  |

## appEventFilters

```TypeScript
appEventFilters?: AppEventFilter[]
```

订阅过滤条件，在需要对订阅事件进行过滤时传入。默认不过滤事件。

**Type:** [AppEventFilter](arkts-performanceanalysis-hiappevent-appeventfilter-i.md)[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-appEventFilters?: AppEventFilter[]--><!--Device-Watcher-appEventFilters?: AppEventFilter[]-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## name

```TypeScript
name: string
```

观察者名称，用于唯一标识观察者。首字符必须为字母字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过32个字符。如testName1、crash_Watcher等。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-name: string--><!--Device-Watcher-name: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## triggerCondition

```TypeScript
triggerCondition?: TriggerCondition
```

订阅回调触发条件，需要与回调函数onTrigger一同传入才会生效。默认不触发。

**Type:** [TriggerCondition](arkts-performanceanalysis-hiappevent-triggercondition-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Watcher-triggerCondition?: TriggerCondition--><!--Device-Watcher-triggerCondition?: TriggerCondition-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

