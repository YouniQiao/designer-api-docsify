# hidebug

为应用提供多种调试、调优的方法，帮助开发者定位性能瓶颈、优化应用性能。主要功能包括：内存数据分析、CPU使用率监控、trace采集、profiler采集、VM堆快照转储。由于该模块的接口大多比较耗费性能，接口调用较为耗时，且基于HiDebug模块定义，该模块内的接口仅建议在应用调试、调优阶段使用。若需要在其他场景使用时，请认真评估所需调用的接口对应用性能的影响。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace hidebug--><!--Device-unnamed-declare namespace hidebug-End-->

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## 汇总

### 命名空间

| 名称 |
| --- |
| [tags](arkts-performanceanalysis-hidebug-tags-n.md) |

### 函数

| 名称 |
| --- |
| [getNativeHeapSize](arkts-performanceanalysis-hidebug-getnativeheapsize-f.md#getNativeHeapSize) |
| [getNativeHeapAllocatedSize](arkts-performanceanalysis-hidebug-getnativeheapallocatedsize-f.md#getNativeHeapAllocatedSize) |
| [getNativeHeapFreeSize](arkts-performanceanalysis-hidebug-getnativeheapfreesize-f.md#getNativeHeapFreeSize) |
| [getVss](arkts-performanceanalysis-hidebug-getvss-f.md#getVss) |
| [getPss](arkts-performanceanalysis-hidebug-getpss-f.md#getPss) |
| [getSharedDirty](arkts-performanceanalysis-hidebug-getshareddirty-f.md#getSharedDirty) |
| [getPrivateDirty](arkts-performanceanalysis-hidebug-getprivatedirty-f.md#getPrivateDirty) |
| [getCpuUsage](arkts-performanceanalysis-hidebug-getcpuusage-f.md#getCpuUsage) |
| [startProfiling](arkts-performanceanalysis-hidebug-startprofiling-f.md#startProfiling) |
| [stopProfiling](arkts-performanceanalysis-hidebug-stopprofiling-f.md#stopProfiling) |
| [dumpHeapData](arkts-performanceanalysis-hidebug-dumpheapdata-f.md#dumpHeapData) |
| [startJsCpuProfiling](arkts-performanceanalysis-hidebug-startjscpuprofiling-f.md#startJsCpuProfiling) |
| [stopJsCpuProfiling](arkts-performanceanalysis-hidebug-stopjscpuprofiling-f.md#stopJsCpuProfiling) |
| [dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md#dumpJsHeapData) |
| [dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md#dumpJsHeapData) |
| [getServiceDump](arkts-performanceanalysis-hidebug-getservicedump-f.md#getServiceDump) |
| [getSystemCpuUsage](arkts-performanceanalysis-hidebug-getsystemcpuusage-f.md#getSystemCpuUsage) |
| [getAppThreadCpuUsage](arkts-performanceanalysis-hidebug-getappthreadcpuusage-f.md#getAppThreadCpuUsage) |
| [getSystemMemInfo](arkts-performanceanalysis-hidebug-getsystemmeminfo-f.md#getSystemMemInfo) |
| [getAppNativeMemInfo](arkts-performanceanalysis-hidebug-getappnativememinfo-f.md#getAppNativeMemInfo) |
| [getAppMemoryLimit](arkts-performanceanalysis-hidebug-getappmemorylimit-f.md#getAppMemoryLimit) |
| [getAppVMMemoryInfo](arkts-performanceanalysis-hidebug-getappvmmemoryinfo-f.md#getAppVMMemoryInfo) |
| [getAppVMObjectUsedSize](arkts-performanceanalysis-hidebug-getappvmobjectusedsize-f.md#getAppVMObjectUsedSize) |
| [getAppNativeMemInfoAsync](arkts-performanceanalysis-hidebug-getappnativememinfoasync-f.md#getAppNativeMemInfoAsync) |
| [getAppNativeMemInfoWithCache](arkts-performanceanalysis-hidebug-getappnativememinfowithcache-f.md#getAppNativeMemInfoWithCache) |
| [startAppTraceCapture](arkts-performanceanalysis-hidebug-startapptracecapture-f.md#startAppTraceCapture) |
| [stopAppTraceCapture](arkts-performanceanalysis-hidebug-stopapptracecapture-f.md#stopAppTraceCapture) |
| [getGwpAsanGrayscaleState](arkts-performanceanalysis-hidebug-getgwpasangrayscalestate-f.md#getGwpAsanGrayscaleState) |
| [requestTrace](arkts-performanceanalysis-hidebug-requesttrace-f.md#requestTrace) |
| [getVMRuntimeStats](arkts-performanceanalysis-hidebug-getvmruntimestats-f.md#getVMRuntimeStats) |
| [getVMRuntimeStat](arkts-performanceanalysis-hidebug-getvmruntimestat-f.md#getVMRuntimeStat) |
| [setAppResourceLimit](arkts-performanceanalysis-hidebug-setappresourcelimit-f.md#setAppResourceLimit) |
| [isDebugState](arkts-performanceanalysis-hidebug-isdebugstate-f.md#isDebugState) |
| [getGraphicsMemory](arkts-performanceanalysis-hidebug-getgraphicsmemory-f.md#getGraphicsMemory) |
| [getGraphicsMemorySync](arkts-performanceanalysis-hidebug-getgraphicsmemorysync-f.md#getGraphicsMemorySync) |
| [getGraphicsMemorySummary](arkts-performanceanalysis-hidebug-getgraphicsmemorysummary-f.md#getGraphicsMemorySummary) |
| [setJsRawHeapTrimLevel](arkts-performanceanalysis-hidebug-setjsrawheaptrimlevel-f.md#setJsRawHeapTrimLevel) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md#dumpJsRawHeapData) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md#dumpJsRawHeapData) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md#dumpJsRawHeapData) |
| [enableGwpAsanGrayscale](arkts-performanceanalysis-hidebug-enablegwpasangrayscale-f.md#enableGwpAsanGrayscale) |
| [disableGwpAsanGrayscale](arkts-performanceanalysis-hidebug-disablegwpasangrayscale-f.md#disableGwpAsanGrayscale) |
| [getGwpAsanGrayscaleState](arkts-performanceanalysis-hidebug-getgwpasangrayscalestate-f.md#getGwpAsanGrayscaleState) |
| [setProcDumpInSharedOOM](arkts-performanceanalysis-hidebug-setprocdumpinsharedoom-f.md#setProcDumpInSharedOOM) |
| [getRssInfo](arkts-performanceanalysis-hidebug-getrssinfo-f.md#getRssInfo) |
| [enableGwpAsanGrayscale](arkts-performanceanalysis-hidebug-enablegwpasangrayscale-f.md#enableGwpAsanGrayscale) |

### 接口

| 名称 |
| --- |
| [ThreadCpuUsage](arkts-performanceanalysis-hidebug-threadcpuusage-i.md) |
| [SystemMemInfo](arkts-performanceanalysis-hidebug-systemmeminfo-i.md) |
| [NativeMemInfo](arkts-performanceanalysis-hidebug-nativememinfo-i.md) |
| [MemoryLimit](arkts-performanceanalysis-hidebug-memorylimit-i.md) |
| [VMMemoryInfo](arkts-performanceanalysis-hidebug-vmmemoryinfo-i.md) |
| [RequestTraceConfig](arkts-performanceanalysis-hidebug-requesttraceconfig-i.md) |
| [GraphicsMemorySummary](arkts-performanceanalysis-hidebug-graphicsmemorysummary-i.md) |
| [GwpAsanOptions](arkts-performanceanalysis-hidebug-gwpasanoptions-i.md) |
| [RssInfo](arkts-performanceanalysis-hidebug-rssinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [TraceFlag](arkts-performanceanalysis-hidebug-traceflag-e.md) |
| [JsRawHeapTrimLevel](arkts-performanceanalysis-hidebug-jsrawheaptrimlevel-e.md) |

### 类型

| 名称 |
| --- |
| [GcStats](arkts-performanceanalysis-hidebug-gcstats-t.md) |
