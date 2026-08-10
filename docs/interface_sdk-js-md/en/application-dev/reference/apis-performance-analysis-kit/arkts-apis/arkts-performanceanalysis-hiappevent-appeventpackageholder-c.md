# AppEventPackageHolder

订阅数据持有者类，用于对事件信息进行处理。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiAppEvent-class AppEventPackageHolder--><!--Device-hiAppEvent-class AppEventPackageHolder-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## constructor

```TypeScript
constructor(watcherName: string)
```

类构造函数，用于创建订阅数据持有者实例。先通过[addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addwatcher)添加事件观察者，再通过观察者名称关联到应用内已添加的观察者对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-constructor(watcherName: string)--><!--Device-AppEventPackageHolder-constructor(watcherName: string)-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| watcherName | string | Yes | 已通过[addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md#addwatcher)添加的事件观察者名称。若未通过addWatcher添加，则默认无数据。 |

## Examples

```TypeScript
// Add the Watcher1 to subscribe to system events.
hiAppEvent.addWatcher({
  name: "Watcher1",
  appEventFilters: [
    {
      domain: hiAppEvent.domain.OS,
    }
  ],
});

// Create an AppEventPackageHolder instance. holder1 holds the event data subscribed by Watcher1 added through addWatcher.
let holder1: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
```

## setRow

ArkTS-Dyn:
```TypeScript
setRow(size: number): void
```

ArkTS-Sta:
```TypeScript
setRow(size: int): void
```

设置每次取出的事件包的数据条数，优先级高于setSize，和setSize同时调用时仅setRow生效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AppEventPackageHolder-setRow(size: int): void--><!--Device-AppEventPackageHolder-setRow(size: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 事件条数，单位为条。取值范围(0, 2^31-1]，超出范围会抛异常。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 11104001 | Invalid size value. Possibly caused by the size value is less than or equal to zero. |

## Examples

```TypeScript
// Create an AppEventPackageHolder instance. holder3 holds the event data subscribed by Watcher1 added through addWatcher.
let holder3: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// Set the number of data records for obtaining the event package each time to 1000.
holder3.setRow(1000);
```

## setSize

ArkTS-Dyn:
```TypeScript
setSize(size: number): void
```

ArkTS-Sta:
```TypeScript
setSize(size: int): void
```

设置每次取出的事件包的数据大小阈值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-setSize(size: int): void--><!--Device-AppEventPackageHolder-setSize(size: int): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 数据大小阈值，单位为byte。取值范围[0, 2^31-1]，超出范围会抛异常。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 11104001 | Invalid size value. Possibly caused by the size value is less than or equal to zero. |

## Examples

```TypeScript
// Create an AppEventPackageHolder instance. holder2 holds the event data subscribed by Watcher1 added through addWatcher.
let holder2: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// Set the data size threshold for obtaining the event package each time to 1000 bytes.
holder2.setSize(1000);
```

## takeNext

```TypeScript
takeNext(): AppEventPackage
```

获取订阅事件。

系统根据setSize设置的数据大小阈值或setRow设置的条数来取出订阅事件数据，默认取1条订阅事件。当订阅事件数据全部被取出时返回null。

当setRow和setSize同时调用时仅setRow生效。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AppEventPackageHolder-takeNext(): AppEventPackage--><!--Device-AppEventPackageHolder-takeNext(): AppEventPackage-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| Type | Description |
| --- | --- |
| [AppEventPackage](arkts-performanceanalysis-hiappevent-appeventpackage-i.md) | 取出的事件包对象，订阅事件数据被全部取出后会返回null。 |

## Examples

```TypeScript
// Create an AppEventPackageHolder instance. holder4 holds the event data subscribed by Watcher1 added through addWatcher.
let holder4: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// Obtain the subscribed event.
let eventPkg: hiAppEvent.AppEventPackage | null = holder4.takeNext();
```

## takeNext

```TypeScript
takeNext(): AppEventPackage | null
```

获取订阅事件。

&lt;br&gt;系统根据 **setSize** 设置的数据大小阈值或  
**setRow** 设置的条数来取出订阅事件数据，默认取1条订阅事件。 当订阅事件数据全部被取出时返回null。

&lt;br&gt;当 **setRow** 和 **setSize** 同时调用时仅 **setRow** 生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AppEventPackageHolder-takeNext(): AppEventPackage | null--><!--Device-AppEventPackageHolder-takeNext(): AppEventPackage | null-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Return value:**

| Type | Description |
| --- | --- |
| [AppEventPackage](arkts-performanceanalysis-hiappevent-appeventpackage-i.md) | 取出的事件包对象，订阅事件数据被全部取出后 会返回null。 |

