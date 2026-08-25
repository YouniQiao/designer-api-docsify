# AppEventPackageHolder

订阅数据持有者类，用于对事件信息进行处理。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

## 导入模块

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## constructor

```TypeScript
constructor(watcherName: string)
```

类构造函数，用于创建订阅数据持有者实例。先通过[addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)添加事件观察者，再通过观察者名称关联到应用内已添加的观察者对象。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watcherName | string | 是 |

**示例**

```TypeScript
// 添加数据观察者“Watcher1”，订阅监听系统事件
hiAppEvent.addWatcher({
  name: "Watcher1",
  appEventFilters: [
    {
      domain: hiAppEvent.domain.OS,
    }
  ],
});

// 创建订阅数据持有者实例，holder1持有的数据为上述addWatcher中添加的观察者“Watcher1”监听到的事件
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

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11104001](../errorcode-hiappevent.md#11104001-非法的事件包大小值) |

**示例**

```TypeScript
// 创建订阅数据持有者实例，holder3持有的数据为已通过addWatcher添加的观察者“Watcher1”监听到的事件
let holder3: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// 设置每次取出的事件包的数据条数为1000条
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11104001](../errorcode-hiappevent.md#11104001-非法的事件包大小值) |

**示例**

```TypeScript
// 创建订阅数据持有者实例，holder2持有的数据为已通过addWatcher添加的观察者“Watcher1”监听到的事件
let holder2: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// 设置每次取出事件包的数据大小阈值为1000byte
holder2.setSize(1000);
```

## takeNext

```TypeScript
takeNext(): AppEventPackage
```

获取订阅事件。系统根据setSize设置的数据大小阈值或setRow设置的条数来取出订阅事件数据，默认取1条订阅事件。当订阅事件数据全部被取出时返回null。当setRow和setSize同时调用时仅setRow生效。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**返回值：**

| 类型 |
| --- |
| [AppEventPackage](arkts-performanceanalysis-hiappevent-appeventpackage-i.md) |

**示例**

```TypeScript
// 创建订阅数据持有者实例，holder4持有的数据为已通过addWatcher添加的观察者“Watcher1”监听到的事件
let holder4: hiAppEvent.AppEventPackageHolder = new hiAppEvent.AppEventPackageHolder("Watcher1");
// 获取订阅事件
let eventPkg: hiAppEvent.AppEventPackage | null = holder4.takeNext();
```

## takeNext

```TypeScript
takeNext(): AppEventPackage | null
```

获取订阅事件。<br>系统根据 **setSize** 设置的数据大小阈值或 **setRow** 设置的条数来取出订阅事件数据，默认取1条订阅事件。 当订阅事件数据全部被取出时返回null。<br>当 **setRow** 和 **setSize** 同时调用时仅 **setRow** 生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**返回值：**

| 类型 |
| --- |
| [AppEventPackage](arkts-performanceanalysis-hiappevent-appeventpackage-i.md) \| null |

**示例**

参见 [takeNext](#takenext)
