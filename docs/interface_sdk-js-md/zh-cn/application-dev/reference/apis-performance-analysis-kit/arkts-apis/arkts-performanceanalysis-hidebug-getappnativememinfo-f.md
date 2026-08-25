# getAppNativeMemInfo

## 导入模块

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getAppNativeMemInfo

```TypeScript
function getAppNativeMemInfo(): NativeMemInfo
```

获取应用进程内存信息。读取/proc/{pid}/smaps_rollup和/proc/{pid}/statm节点的数据。

> **注意**：&gt;
> 由于读取/proc/{pid}/smaps_rollup耗时较长，推荐使用异步接口
> [hidebug.getAppNativeMemInfoAsync](arkts-performanceanalysis-hidebug-getappnativememinfoasync-f.md)，以避免应用丢帧或卡顿。&gt;
> 推荐使用[hidebug.getRssInfo](arkts-performanceanalysis-hidebug-getrssinfo-f.md)接口获取应用的rss使用信息

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| [NativeMemInfo](arkts-performanceanalysis-hidebug-nativememinfo-i.md) |
