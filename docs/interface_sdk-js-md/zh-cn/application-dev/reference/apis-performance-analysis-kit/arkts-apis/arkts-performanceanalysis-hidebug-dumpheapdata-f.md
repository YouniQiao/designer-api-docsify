# dumpHeapData

## 导入模块

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## dumpHeapData

```TypeScript
function dumpHeapData(filename: string): void
```


> **说明：**&gt;
> 从API version 8支持，从API version 9开始废弃，
> 虚拟机堆数据转储，生成`filename.heapsnapshot`文件。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md)

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filename | string | 是 |
