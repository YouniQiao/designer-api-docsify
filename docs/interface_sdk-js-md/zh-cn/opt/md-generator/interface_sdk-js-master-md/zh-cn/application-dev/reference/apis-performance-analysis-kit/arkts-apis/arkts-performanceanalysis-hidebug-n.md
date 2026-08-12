# hidebug

为应用提供多种调试、调优的方法，帮助开发者定位性能瓶颈、优化应用性能。主要功能包括：内存数据分析、CPU使用率监控、trace采集、profiler采集、VM堆快照转储。由于该模块的接口大多比较耗费性能，接口调用较为耗时，且基于HiDebug模块定义，该模块内的接口仅建议在应用调试、调优阶段使用。若需要在其他场景使用时，请认真评估所需调用的接口对应用性能的影响。

**起始版本：** 12

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
| [getNativeHeapSize](arkts-performanceanalysis-hidebug-getnativeheapsize-f.md#getnativeheapsize) |
| [getNativeHeapAllocatedSize](arkts-performanceanalysis-hidebug-getnativeheapallocatedsize-f.md#getnativeheapallocatedsize) |
| [getNativeHeapFreeSize](arkts-performanceanalysis-hidebug-getnativeheapfreesize-f.md#getnativeheapfreesize) |
| [getVss](arkts-performanceanalysis-hidebug-getvss-f.md#getvss) |
| [getPss](arkts-performanceanalysis-hidebug-getpss-f.md#getpss) |
| [getSharedDirty](arkts-performanceanalysis-hidebug-getshareddirty-f.md#getshareddirty) |
| [getPrivateDirty](arkts-performanceanalysis-hidebug-getprivatedirty-f.md#getprivatedirty) |
| [getCpuUsage](arkts-performanceanalysis-hidebug-getcpuusage-f.md#getcpuusage) |
| [startProfiling](arkts-performanceanalysis-hidebug-startprofiling-f.md#startprofiling) |
| [stopProfiling](arkts-performanceanalysis-hidebug-stopprofiling-f.md#stopprofiling) |
| [dumpHeapData](arkts-performanceanalysis-hidebug-dumpheapdata-f.md#dumpheapdata) |
| [startJsCpuProfiling](arkts-performanceanalysis-hidebug-startjscpuprofiling-f.md#startjscpuprofiling) |
| [stopJsCpuProfiling](arkts-performanceanalysis-hidebug-stopjscpuprofiling-f.md#stopjscpuprofiling) |
| [dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md#dumpjsheapdata) |
| [dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md#dumpjsheapdata-1) |
| [getServiceDump](arkts-performanceanalysis-hidebug-getservicedump-f.md#getservicedump) |
| [getSystemCpuUsage](arkts-performanceanalysis-hidebug-getsystemcpuusage-f.md#getsystemcpuusage) |
| [getAppThreadCpuUsage](arkts-performanceanalysis-hidebug-getappthreadcpuusage-f.md#getappthreadcpuusage) |
| [getSystemMemInfo](arkts-performanceanalysis-hidebug-getsystemmeminfo-f.md#getsystemmeminfo) |
| [getAppNativeMemInfo](arkts-performanceanalysis-hidebug-getappnativememinfo-f.md#getappnativememinfo) |
| [getAppMemoryLimit](arkts-performanceanalysis-hidebug-getappmemorylimit-f.md#getappmemorylimit) |
| [getAppVMMemoryInfo](arkts-performanceanalysis-hidebug-getappvmmemoryinfo-f.md#getappvmmemoryinfo) |
| [getAppVMObjectUsedSize](arkts-performanceanalysis-hidebug-getappvmobjectusedsize-f.md#getappvmobjectusedsize) |
| [getAppNativeMemInfoAsync](arkts-performanceanalysis-hidebug-getappnativememinfoasync-f.md#getappnativememinfoasync) |
| [getAppNativeMemInfoWithCache](arkts-performanceanalysis-hidebug-getappnativememinfowithcache-f.md#getappnativememinfowithcache) |
| [startAppTraceCapture](arkts-performanceanalysis-hidebug-startapptracecapture-f.md#startapptracecapture) |
| [stopAppTraceCapture](arkts-performanceanalysis-hidebug-stopapptracecapture-f.md#stopapptracecapture) |
| [getGwpAsanGrayscaleState](arkts-performanceanalysis-hidebug-getgwpasangrayscalestate-f.md#getgwpasangrayscalestate) |
| [requestTrace](arkts-performanceanalysis-hidebug-requesttrace-f.md#requesttrace) |
| [getVMRuntimeStats](arkts-performanceanalysis-hidebug-getvmruntimestats-f.md#getvmruntimestats) |
| [getVMRuntimeStat](arkts-performanceanalysis-hidebug-getvmruntimestat-f.md#getvmruntimestat) |
| [setAppResourceLimit](arkts-performanceanalysis-hidebug-setappresourcelimit-f.md#setappresourcelimit) |
| [isDebugState](arkts-performanceanalysis-hidebug-isdebugstate-f.md#isdebugstate) |
| [getGraphicsMemory](arkts-performanceanalysis-hidebug-getgraphicsmemory-f.md#getgraphicsmemory) |
| [getGraphicsMemorySync](arkts-performanceanalysis-hidebug-getgraphicsmemorysync-f.md#getgraphicsmemorysync) |
| [getGraphicsMemorySummary](arkts-performanceanalysis-hidebug-getgraphicsmemorysummary-f.md#getgraphicsmemorysummary) |
| [setJsRawHeapTrimLevel](arkts-performanceanalysis-hidebug-setjsrawheaptrimlevel-f.md#setjsrawheaptrimlevel) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md#dumpjsrawheapdata) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md#dumpjsrawheapdata-1) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md#dumpjsrawheapdata-2) |
| [enableGwpAsanGrayscale](arkts-performanceanalysis-hidebug-enablegwpasangrayscale-f.md#enablegwpasangrayscale) |
| [disableGwpAsanGrayscale](arkts-performanceanalysis-hidebug-disablegwpasangrayscale-f.md#disablegwpasangrayscale) |
| [getGwpAsanGrayscaleState](arkts-performanceanalysis-hidebug-getgwpasangrayscalestate-f.md#getgwpasangrayscalestate-1) |
| [setProcDumpInSharedOOM](arkts-performanceanalysis-hidebug-setprocdumpinsharedoom-f.md#setprocdumpinsharedoom) |
| [getRssInfo](arkts-performanceanalysis-hidebug-getrssinfo-f.md#getrssinfo) |
| [enableGwpAsanGrayscale](arkts-performanceanalysis-hidebug-enablegwpasangrayscale-f.md#enablegwpasangrayscale-1) |

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
