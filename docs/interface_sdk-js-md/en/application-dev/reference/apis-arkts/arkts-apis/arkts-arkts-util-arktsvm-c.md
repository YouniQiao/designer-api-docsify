# ArkTSVM

A class that provides VM maintenance and test capabilities for developers.

**Since:** 23

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## enableLocalHandleDetection

```TypeScript
static enableLocalHandleDetection(): void
```

Enable the local handle detection to avoid memory leakage in the event looper of Libuv or EventHandler.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## getAllVMHeapMemoryInfo

```TypeScript
static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>
```

Get all heap memory information from ArkTS-VMs and the shared heap.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HeapMemoryInfo](arkts-arkts-util-heapmemoryinfo-i.md)[]&gt; |

## offVMHeapMemoryPressure

```TypeScript
static offVMHeapMemoryPressure(): void
```

Unregister the callback that is triggered when the heap memory exceeds the critical warning threshold after a GC.@static

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## onVMHeapMemoryPressure

```TypeScript
static onVMHeapMemoryPressure(callback: Callback<string>, heapMemoryThreshold: HeapMemoryThreshold): boolean
```

Register a callback that is triggered if the heap memory exceeds the critical warning threshold after a GC. It must be called on the main thread and only one callback can be registered.NOTE: There is no guarantee that the callback will be triggered before OOM.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |
| heapMemoryThreshold | [HeapMemoryThreshold](arkts-arkts-util-heapmemorythreshold-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setMultithreadingDetectionEnabled

```TypeScript
static setMultithreadingDetectionEnabled(enabled: boolean, options?: MultithreadingDetectionOptions):void
```

Sets whether to enable multithreading detection. When **enabled** is set to **true**, the detection is turned on, and multithreading-related details will be included in the cppcrash files generated for multithreading issues. When **enabled** is set to **false**, the detection is turned off, and no such details will be present in the corresponding cppcrash files.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |
| options | [MultithreadingDetectionOptions](arkts-arkts-util-multithreadingdetectionoptions-i.md) | No |

## setTrackGlobalRef

```TypeScript
static setTrackGlobalRef(enable: boolean): void
```

Enable or disable tracking of the relationship between napi_ref and global handle. When enabled, heap snapshot will include native reference address information. When disabled (enable is false), the tracking will be stopped and heap snapshot will not display the relationship between native reference and global handle.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
