# hidebug_type.h

## Overview

Defines the code of the HiDebug module.

**Library**: libohhidebug.so

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Since**: 12

**Related module**: [HiDebug](capi-hidebug.md)

## Summary

### Struct

| Name | typedef keyword | Description |
| -- | -- | -- |
| [HiDebug_ThreadCpuUsage](capi-hidebug-hidebug-threadcpuusage.md) | HiDebug_ThreadCpuUsage | Defines the struct for the CPU usage of all threads of an application. |
| [HiDebug_SystemMemInfo](capi-hidebug-hidebug-systemmeminfo.md) | HiDebug_SystemMemInfo | Defines a struct for the system memory information. |
| [HiDebug_NativeMemInfo](capi-hidebug-hidebug-nativememinfo.md) | HiDebug_NativeMemInfo | Defines the struct for the local memory information of the application process. |
| [HiDebug_MemoryLimit](capi-hidebug-hidebug-memorylimit.md) | HiDebug_MemoryLimit | Defines the struct for the memory limit of the application process. |
| [OH_HiDebug_RequestTraceConfig](capi-hidebug-oh-hidebug-requesttraceconfig.md) | OH_HiDebug_RequestTraceConfig | Defines trace request configuration. |
| [HiDebug_MallocDispatch](capi-hidebug-hidebug-mallocdispatch.md) | HiDebug_MallocDispatch | Defines the struct types of the replaceable/restorable **HiDebug_MallocDispatch** table of the applicationprocess. |
| [HiDebug_JsStackFrame](capi-hidebug-hidebug-jsstackframe.md) | HiDebug_JsStackFrame | Defines a struct for the JS stack frame content. |
| [HiDebug_NativeStackFrame](capi-hidebug-hidebug-nativestackframe.md) | HiDebug_NativeStackFrame | Defines the native stack frame content. |
| [HiDebug_StackFrame](capi-hidebug-hidebug-stackframe.md) | HiDebug_StackFrame | Defines the stack frame content. |
| [HiDebug_GraphicsMemorySummary](capi-hidebug-hidebug-graphicsmemorysummary.md) | HiDebug_GraphicsMemorySummary | Defines a struct for the application graphics memory usage details. |
| [HiDebug_ProcessSamplerConfig](capi-hidebug-hidebug-processsamplerconfig.md) | HiDebug_ProcessSamplerConfig | Defines a struct for sampling configuration. |
| [OH_HiDebug_ResProfilerConfig](capi-hidebug-oh-hidebug-resprofilerconfig.md) | OH_HiDebug_ResProfilerConfig | Defines a struct for the resource profiler configuration. |
| [OH_HiDebug_ProfilingResult](capi-hidebug-oh-hidebug-profilingresult.md) | OH_HiDebug_ProfilingResult | Encapsulates result of a single profiling request operation.It represents data delivered via OH_HiDebug_ProfilingCallback. |
| [HiDebug_Backtrace_Object__*](capi-hidebug-hidebug-backtrace-object--8h.md) | HiDebug_Backtrace_Object | Defines an object used for stack backtracing and stack parsing. |
| [HiDebug_ThreadCpuUsage*](capi-hidebug-hidebug-threadcpuusage8h.md) | HiDebug_ThreadCpuUsagePtr | Defines pointer of HiDebug_ThreadCpuUsage. |

### Enum

| Name | typedef keyword | Description |
| -- | -- | -- |
| [HiDebug_TraceFlag](#hidebug_traceflag) | HiDebug_TraceFlag | Enumerates the thread types for trace collection. |
| [HiDebug_StackFrameType](#hidebug_stackframetype) | HiDebug_StackFrameType | Enumerates the stack frame types. |
| [HiDebug_CrashObjType](#hidebug_crashobjtype) | HiDebug_CrashObjType | Enumerates the data types of debugging information. |
| [OH_HiDebug_ResourceType](#oh_hidebug_resourcetype) | OH_HiDebug_ResourceType | Defines an enum for the resource profiler types. |
| [OH_HiDebug_MemListenerType](#oh_hidebug_memlistenertype) | OH_HiDebug_MemListenerType | Defines an enum for memory listener callbacks. |

### Macro

| Name | Description |
| -- | -- |
| HIDEBUG_TRACE_TAG_FFRT (1ULL << 13) | FFRT tasks.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_COMMON_LIBRARY (1ULL << 16) | Common library subsystem tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_HDF (1ULL << 18) | HDF subsystem tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_NET (1ULL << 23) | Net tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_NWEB (1ULL << 24) | NWeb tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_AUDIO (1ULL << 27) | Distributed audio tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_FILE_MANAGEMENT (1ULL << 29) | File management tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_OHOS (1ULL << 30) | OHOS generic tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_ABILITY_MANAGER (1ULL << 31) | Ability Manager tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_CAMERA (1ULL << 32) | Camera module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_MEDIA (1ULL << 33) | Media module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_IMAGE (1ULL << 34) | Image module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_AUDIO (1ULL << 35) | Audio module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_DATA (1ULL << 36) | Distributed data manager module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_GRAPHICS (1ULL << 38) | Graphics module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_ARKUI (1ULL << 39) | ARKUI development framework tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_NOTIFICATION (1ULL << 40) | Notification module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_MISC (1ULL << 41) | MISC module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_MULTIMODAL_INPUT (1ULL << 42) | Multimodal input module tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_RPC (1ULL << 46) | RPC tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_ARK (1ULL << 47) | ARK tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_WINDOW_MANAGER (1ULL << 48) | Window manager tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_SCREEN (1ULL << 50) | Distributed screen tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_CAMERA (1ULL << 51) | Distributed camera tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_FRAMEWORK (1ULL << 52) | Distributed hardware framework tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_GLOBAL_RESOURCE_MANAGER (1ULL << 53) | Global resource manager tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_HARDWARE_DEVICE_MANAGER (1ULL << 54) | Distributed hardware device manager tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_SAMGR (1ULL << 55) | SA tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_POWER_MANAGER (1ULL << 56) | Power manager tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_SCHEDULER (1ULL << 57) | Distributed scheduler tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_DISTRIBUTED_INPUT (1ULL << 59) | Distributed input tag.<br>**Since**: 12 |
| HIDEBUG_TRACE_TAG_BLUETOOTH (1ULL << 60) | bluetooth tag.<br>**Since**: 12 |

### Function

| Name | typedef keyword | Description |
| -- | -- | -- |
| [typedef void (\*OH_HiDebug_RequestTraceCallback)(HiDebug_ErrorCode errorCode, const char* filePath)](#oh_hidebug_requesttracecallback) | OH_HiDebug_RequestTraceCallback | Defines callback type for trace request. |
| [typedef void (\*OH_HiDebug_ProfilingCallback)(OH_HiDebug_ProfilingResult* result)](#oh_hidebug_profilingcallback) | OH_HiDebug_ProfilingCallback | Callback signature for the resource profiling result. |

## Enum type description

### HiDebug_TraceFlag

```c
enum HiDebug_TraceFlag
```

**Description**

Enumerates the thread types for trace collection.

**Since**: 12

| Enum item | Description |
| -- | -- |
| HIDEBUG_TRACE_FLAG_MAIN_THREAD = 1 | Only the main thread of the current application. |
| HIDEBUG_TRACE_FLAG_ALL_THREADS = 2 | All threads of the application. |

### HiDebug_StackFrameType

```c
enum HiDebug_StackFrameType
```

**Description**

Enumerates the stack frame types.

**Since**: 20

| Enum item | Description |
| -- | -- |
| HIDEBUG_STACK_FRAME_TYPE_JS = 1 | JS stack frame. |
| HIDEBUG_STACK_FRAME_TYPE_NATIVE = 2 | Native stack frame. |

### HiDebug_CrashObjType

```c
enum HiDebug_CrashObjType
```

**Description**

Enumerates the data types of debugging information.

**Since**: 23

| Enum item | Description |
| -- | -- |
| HIDEBUG_CRASHOBJ_STRING = 0 | String. |
| HIDEBUG_CRASHOBJ_MEMORY_64B = 1 | 64-byte memory block. |
| HIDEBUG_CRASHOBJ_MEMORY_256B = 2 | 256-byte memory block. |
| HIDEBUG_CRASHOBJ_MEMORY_1024B = 3 | 1024-byte memory block. |
| HIDEBUG_CRASHOBJ_MEMORY_2048B = 4 | 2048-byte memory block. |
| HIDEBUG_CRASHOBJ_MEMORY_4096B = 5 | 4096-byte memory block. |

### OH_HiDebug_ResourceType

```c
enum OH_HiDebug_ResourceType
```

**Description**

Defines an enum for the resource profiler types.

**Since**: 24

| Enum item | Description |
| -- | -- |
| OH_RES_TYPE_FD |  |
| OH_RES_TYPE_THREAD |  |
| OH_RES_TYPE_NATIVE |  |
| OH_RES_TYPE_GPU |  |
| OH_RES_TYPE_GLOBAL_HANDLE |  |

### OH_HiDebug_MemListenerType

```c
enum OH_HiDebug_MemListenerType
```

**Description**

Defines an enum for memory listener callbacks.

**Since**: 26.0.0

| Enum item | Description |
| -- | -- |
| OH_HIDEBUG_DO_NOTHING = 0 |  |
| OH_HIDEBUG_RUNNING_GC = 1 |  |
| OH_HIDEBUG_DUMP_SNAPSHOT = 2 |  |


## Function description

### OH_HiDebug_RequestTraceCallback()

```c
typedef void (*OH_HiDebug_RequestTraceCallback)(HiDebug_ErrorCode errorCode, const char* filePath)
```

**Description**

Defines callback type for trace request.

**Since**: 24

**Parameters**:

| Parameter | Description |
| -- | -- |
| (HiDebug_ErrorCode errorCode | Result code, see {@link HiDebug_ErrorCode}. |
| const char\* filePath | Path of the generated trace file, may be NULL on failure. |

### OH_HiDebug_ProfilingCallback()

```c
typedef void (*OH_HiDebug_ProfilingCallback)(OH_HiDebug_ProfilingResult* result)
```

**Description**

Callback signature for the resource profiling result.

**Since**: 24

**Parameters**:

| Parameter | Description |
| -- | -- |
| (OH_HiDebug_ProfilingResult\* result | Pointer to the OH_HiDebug_ProfilingResult structure. |


