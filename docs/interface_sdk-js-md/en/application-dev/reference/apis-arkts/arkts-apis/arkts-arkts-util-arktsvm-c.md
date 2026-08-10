# ArkTSVM

为开发者提供虚拟机维测能力的类。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-util-class ArkTSVM--><!--Device-util-class ArkTSVM-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## enableLocalHandleDetection

```TypeScript
static enableLocalHandleDetection(): void
```

开启 local handle 检测，以避免在 Libuv 或 EventHandler 的事件循环（event looper）中出现内存泄漏。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArkTSVM-static enableLocalHandleDetection(): void--><!--Device-ArkTSVM-static enableLocalHandleDetection(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## getAllVMHeapMemoryInfo

```TypeScript
static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>
```

从 ArkTS-VM 和共享堆中获取所有堆内存信息。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArkTSVM-static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>--><!--Device-ArkTSVM-static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HeapMemoryInfo[]&gt; | 返回一个 promise，包含 ArkTS-VM 的 local 堆和共享堆中的所有堆内存信息。 |

## offVMHeapMemoryPressure

```TypeScript
static offVMHeapMemoryPressure(): void
```

取消注册在 GC 后堆内存超过临界预警阈值时触发的回调。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArkTSVM-static offVMHeapMemoryPressure(): void--><!--Device-ArkTSVM-static offVMHeapMemoryPressure(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## onVMHeapMemoryPressure

```TypeScript
static onVMHeapMemoryPressure(callback: Callback<string>, heapMemoryThreshold: HeapMemoryThreshold): boolean
```

注册一个回调函数，在 GC（垃圾回收）后堆内存超过临界预警阈值时触发。必须在主线程上调用，且仅能注册一个回调。

NOTE:无法保证在 OOM（内存溢出）前一定会触发该回调。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArkTSVM-static onVMHeapMemoryPressure(callback: Callback<string>, heapMemoryThreshold: HeapMemoryThreshold): boolean--><!--Device-ArkTSVM-static onVMHeapMemoryPressure(callback: Callback<string>, heapMemoryThreshold: HeapMemoryThreshold): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | 在 GC 后内存达到阈值时触发的回调。字符串参数表示内存压力事件的类型： "LocalHeapMemPressure"、"SharedHeapMemPressure" 或 "ProcessHeapMemPressure"。 |
| heapMemoryThreshold | [HeapMemoryThreshold](arkts-arkts-util-heapmemorythreshold-i.md) | Yes | 表示 GC 后触发回调的堆内存百分比阈值。取值范围为 [70, 95]。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 注册成功返回 { |

## setMultithreadingDetectionEnabled

```TypeScript
static setMultithreadingDetectionEnabled(enabled: boolean, options?: MultithreadingDetectionOptions):void
```

设置是否开启多线程检测。当 **enabled** 设置为 **true** 时开启检测，多线程问题的 cppcrash 文件中将包含多线程相关的详细信息。当 **enabled** 设置为 **false** 时关闭检测，相应的 cppcrash 文件中将不包含此类详细信息。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArkTSVM-static setMultithreadingDetectionEnabled(enabled: boolean, options?: MultithreadingDetectionOptions):void--><!--Device-ArkTSVM-static setMultithreadingDetectionEnabled(enabled: boolean, options?: MultithreadingDetectionOptions):void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 控制是否开启多线程检测。**true** 表示开启检测，**false** 表示关闭检测。 |
| options | [MultithreadingDetectionOptions](arkts-arkts-util-multithreadingdetectionoptions-i.md) | No | 可选的配置项。<br>**Since:** 26.0.0 |

## setTrackGlobalRef

```TypeScript
static setTrackGlobalRef(enable: boolean): void
```

开启或关闭 napi_ref 与全局 handle 之间关联关系的追踪。开启后，堆快照将包含 native 引用地址信息。关闭后（enable 为false），将停止追踪，堆快照中不再显示 native 引用与全局 handle 之间的关联关系。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArkTSVM-static setTrackGlobalRef(enable: boolean): void--><!--Device-ArkTSVM-static setTrackGlobalRef(enable: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 布尔标志位，指示是开启还是关闭追踪。**true** 表示开启追踪，**false** 表示关闭追踪。 |

