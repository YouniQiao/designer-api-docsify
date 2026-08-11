# hidebug

Provide interfaces related to debugger access and obtaining CPU,memory and other virtual machine information during runtime for JS programs

**Since:** 12

<!--Device-unnamed-declare namespace hidebug--><!--Device-unnamed-declare namespace hidebug-End-->

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
| [getGwpAsanGrayscaleState](arkts-performanceanalysis-hidebug-getgwpasangrayscalestate-f.md#getgwpasangrayscalestate) |
| [setProcDumpInSharedOOM](arkts-performanceanalysis-hidebug-setprocdumpinsharedoom-f.md#setprocdumpinsharedoom) |
| [getRssInfo](arkts-performanceanalysis-hidebug-getrssinfo-f.md#getrssinfo) |

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
