# addWatcher

## 导入模块

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addWatcher

```TypeScript
function addWatcher(watcher: Watcher): AppEventPackageHolder
```

添加事件观察者。可通过事件观察者的回调函数监听事件。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watcher | [Watcher](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-watcher-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [AppEventPackageHolder](arkts-performanceanalysis-hiappevent-appeventpackageholder-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11102001](../errorcode-hiappevent.md#11102001-非法的观察者名称) |
| [11102002](../errorcode-hiappevent.md#11102002-非法的过滤事件领域) |
| [11102003](../errorcode-hiappevent.md#11102003-非法的条数值) |
| [11102004](../errorcode-hiappevent.md#11102004-非法的大小值) |
| [11102005](../errorcode-hiappevent.md#11102005-非法的超时值) |
