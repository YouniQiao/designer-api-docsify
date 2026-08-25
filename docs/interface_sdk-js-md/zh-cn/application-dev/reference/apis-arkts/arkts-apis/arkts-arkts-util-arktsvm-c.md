# ArkTSVM

为开发者提供虚拟机维测能力的类。

**起始版本：** 23

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## enableLocalHandleDetection

```TypeScript
static enableLocalHandleDetection(): void
```

开启 local handle 检测，以避免在 Libuv 或 EventHandler 的事件循环（event looper）中出现内存泄漏。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## getAllVMHeapMemoryInfo

```TypeScript
static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>
```

从 ArkTS-VM 和共享堆中获取所有堆内存信息。

> **说明：**&gt;
> 此接口在执行时会暂停所有VM线程运行以获取内存信息。由于需要等待所有VM线程暂停，高负载场景下调用此接口的耗时可能较高。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Promise&lt;[HeapMemoryInfo](arkts-arkts-util-heapmemoryinfo-i.md)[]&gt; |

## offVMHeapMemoryPressure

```TypeScript
static offVMHeapMemoryPressure(): void
```

取消注册在 GC 后堆内存超过临界预警阈值时触发的回调。@static

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## onVMHeapMemoryPressure

```TypeScript
static onVMHeapMemoryPressure(callback: Callback<string>, heapMemoryThreshold: HeapMemoryThreshold): boolean
```

注册一个回调函数，在 GC（垃圾回收）后堆内存超过临界预警阈值时触发。 必须在主线程上调用，且仅能注册一个回调。NOTE: 无法保证在 OOM（内存溢出）前一定会触发该回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 |
| heapMemoryThreshold | [HeapMemoryThreshold](arkts-arkts-util-heapmemorythreshold-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setMultithreadingDetectionEnabled

```TypeScript
static setMultithreadingDetectionEnabled(enabled: boolean, options?: MultithreadingDetectionOptions):void
```

设置是否开启多线程安全检测。当 **enabled** 设置为 **true** 时开启检测，多线程问题的 cppcrash 文件中将包含多线程相关的 详细信息。当 **enabled** 设置为 **false** 时关闭检测，相应的 cppcrash 文件中将不包含此类详细信息。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |
| options | [MultithreadingDetectionOptions](arkts-arkts-util-multithreadingdetectionoptions-i.md) | 否 |

## setTrackGlobalRef

```TypeScript
static setTrackGlobalRef(enable: boolean): void
```

开启或关闭 napi_ref 与全局 handle 之间关联关系的追踪。开启后，堆快照将包含 native 引用地址信息。关闭后（enable 为 false），将停止追踪，堆快照中不再显示 native 引用与全局 handle 之间的关联关系。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |
