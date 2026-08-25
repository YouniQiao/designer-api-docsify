# getSystemMemInfo

## 导入模块

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## getSystemMemInfo

```TypeScript
function getSystemMemInfo(): SystemMemInfo
```

获取系统内存信息。读取/proc/meminfo节点的数据。

**起始版本：** 12

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**返回值：**

| 类型 |
| --- |
| [SystemMemInfo](arkts-performanceanalysis-hidebug-systemmeminfo-i.md) |
