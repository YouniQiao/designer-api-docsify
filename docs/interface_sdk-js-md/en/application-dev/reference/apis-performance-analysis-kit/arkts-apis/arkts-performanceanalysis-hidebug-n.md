# hidebug

HiDebug provides multiple methods for debugging and profiling applications. With these methods, you can obtain memory, CPU, GPU, and GC data, collect process trace and profiler data, and dump VM heap snapshots. Since most APIs of this module are both performance-consuming and time-consuming, and are defined based on the HiDebug module, you are advised to use these APIs only during the application debugging and profiling phases. If the APIs are required in other scenarios, evaluate the impact of the APIs on application performance.@namespace hidebug

**Since:** 8

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## Summary

### Namespaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [tags](arkts-performanceanalysis-hidebug-tags-n.md) |

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getNativeHeapSize](arkts-performanceanalysis-hidebug-getnativeheapsize-f.md) |
| [getNativeHeapAllocatedSize](arkts-performanceanalysis-hidebug-getnativeheapallocatedsize-f.md) |
| [getNativeHeapFreeSize](arkts-performanceanalysis-hidebug-getnativeheapfreesize-f.md) |
| [getVss](arkts-performanceanalysis-hidebug-getvss-f.md) |
| [getPss](arkts-performanceanalysis-hidebug-getpss-f.md) |
| [getSharedDirty](arkts-performanceanalysis-hidebug-getshareddirty-f.md) |
| [getPrivateDirty](arkts-performanceanalysis-hidebug-getprivatedirty-f.md) |
| [getCpuUsage](arkts-performanceanalysis-hidebug-getcpuusage-f.md) |
| [startProfiling](arkts-performanceanalysis-hidebug-startprofiling-f.md) |
| [stopProfiling](arkts-performanceanalysis-hidebug-stopprofiling-f.md) |
| [dumpHeapData](arkts-performanceanalysis-hidebug-dumpheapdata-f.md) |
| [startJsCpuProfiling](arkts-performanceanalysis-hidebug-startjscpuprofiling-f.md) |
| [stopJsCpuProfiling](arkts-performanceanalysis-hidebug-stopjscpuprofiling-f.md) |
| [dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md) |
| [dumpJsHeapData](arkts-performanceanalysis-hidebug-dumpjsheapdata-f.md) |
| [getServiceDump](arkts-performanceanalysis-hidebug-getservicedump-f.md) |
| [getSystemCpuUsage](arkts-performanceanalysis-hidebug-getsystemcpuusage-f.md) |
| [getAppThreadCpuUsage](arkts-performanceanalysis-hidebug-getappthreadcpuusage-f.md) |
| [getSystemMemInfo](arkts-performanceanalysis-hidebug-getsystemmeminfo-f.md) |
| [getAppNativeMemInfo](arkts-performanceanalysis-hidebug-getappnativememinfo-f.md) |
| [getAppMemoryLimit](arkts-performanceanalysis-hidebug-getappmemorylimit-f.md) |
| [getAppVMMemoryInfo](arkts-performanceanalysis-hidebug-getappvmmemoryinfo-f.md) |
| [getAppVMObjectUsedSize](arkts-performanceanalysis-hidebug-getappvmobjectusedsize-f.md) |
| [getAppNativeMemInfoAsync](arkts-performanceanalysis-hidebug-getappnativememinfoasync-f.md) |
| [getAppNativeMemInfoWithCache](arkts-performanceanalysis-hidebug-getappnativememinfowithcache-f.md) |
| [startAppTraceCapture](arkts-performanceanalysis-hidebug-startapptracecapture-f.md) |
| [stopAppTraceCapture](arkts-performanceanalysis-hidebug-stopapptracecapture-f.md) |
| [requestTrace](arkts-performanceanalysis-hidebug-requesttrace-f.md) |
| [getVMRuntimeStats](arkts-performanceanalysis-hidebug-getvmruntimestats-f.md) |
| [getVMRuntimeStat](arkts-performanceanalysis-hidebug-getvmruntimestat-f.md) |
| [setAppResourceLimit](arkts-performanceanalysis-hidebug-setappresourcelimit-f.md) |
| [isDebugState](arkts-performanceanalysis-hidebug-isdebugstate-f.md) |
| [getGraphicsMemory](arkts-performanceanalysis-hidebug-getgraphicsmemory-f.md) |
| [getGraphicsMemorySync](arkts-performanceanalysis-hidebug-getgraphicsmemorysync-f.md) |
| [getGraphicsMemorySummary](arkts-performanceanalysis-hidebug-getgraphicsmemorysummary-f.md) |
| [setJsRawHeapTrimLevel](arkts-performanceanalysis-hidebug-setjsrawheaptrimlevel-f.md) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md) |
| [dumpJsRawHeapData](arkts-performanceanalysis-hidebug-dumpjsrawheapdata-f.md) |
| [enableGwpAsanGrayscale](arkts-performanceanalysis-hidebug-enablegwpasangrayscale-f.md) |
| [disableGwpAsanGrayscale](arkts-performanceanalysis-hidebug-disablegwpasangrayscale-f.md) |
| [getGwpAsanGrayscaleState](arkts-performanceanalysis-hidebug-getgwpasangrayscalestate-f.md) |
| [setProcDumpInSharedOOM](arkts-performanceanalysis-hidebug-setprocdumpinsharedoom-f.md) |
| [getRssInfo](arkts-performanceanalysis-hidebug-getrssinfo-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TraceFlag](arkts-performanceanalysis-hidebug-traceflag-e.md) |
| [JsRawHeapTrimLevel](arkts-performanceanalysis-hidebug-jsrawheaptrimlevel-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [GcStats](arkts-performanceanalysis-hidebug-gcstats-t.md) |
