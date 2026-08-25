# collections(Defines the collections for ArkTS)

本模块提供的ArkTS容器集，可以用于并发场景下的高性能数据传递。功能与JavaScript内建的对应容器类似，但ArkTS容器实例无法通过`"."`或者`"[]"`添加或更新属性。 ArkTS容器在多个并发实例间传递时，其默认行为是引用传递，支持多个并发实例可以同时操作同一个容器实例。另外，也支持拷贝传递，即每个并发实例持有一个ArkTS容器实例。 ArkTS容器并不是线程安全的，内部使用了fail-fast（快速失败）机制：当检测多个并发实例同时对容器进行结构性改变时，会触发异常。因此，在多线程读写容器时，容器使用方需要使用ArkTS提供的异步锁机制保证ArkTS容器的安全访问。 当前ArkTS容器集主要包含以下几种容器：[Array](arkts-arkts-collections-array-c.md), [Map](arkts-arkts-collections-map-c.md), [Set](arkts-arkts-collections-set-c.md), TypedArray ([Int8Array](arkts-arkts-collections-int8array-c.md), [Uint8Array](arkts-arkts-collections-uint8array-c.md), [Int16Array](arkts-arkts-collections-int16array-c.md), [Uint16Array](arkts-arkts-collections-uint16array-c.md), [Int32Array](arkts-arkts-collections-int32array-c.md), [Uint32Array](arkts-arkts-collections-uint32array-c.md), [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) and [Float32Array](arkts-arkts-collections-float32array-c.md)), [ArrayBuffer](arkts-arkts-collections-arraybuffer-c.md), [BitVector](arkts-arkts-collections-bitvector-c.md), and [ConcatArray](arkts-arkts-collections-concatarray-i.md).

> **说明：**&gt;
> - 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

**起始版本：** 12

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { collections } from 'kits/@kit.ArkTS';
```

## 汇总

### 类

| 名称 |
| --- |
| [Array(Defines the collections for ArkTS)](arkts-arkts-collections-array-c.md) |
| [Map(Defines the collections for ArkTS)](arkts-arkts-collections-map-c.md) |
| [Set(Defines the collections for ArkTS)](arkts-arkts-collections-set-c.md) |
| [ArrayBuffer(Defines the collections for ArkTS)](arkts-arkts-collections-arraybuffer-c.md) |
| [Int8Array(Defines the collections for ArkTS)](arkts-arkts-collections-int8array-c.md) |
| [Uint8ClampedArray(Defines the collections for ArkTS)](arkts-arkts-collections-uint8clampedarray-c.md) |
| [Uint8Array(Defines the collections for ArkTS)](arkts-arkts-collections-uint8array-c.md) |
| [Int16Array(Defines the collections for ArkTS)](arkts-arkts-collections-int16array-c.md) |
| [Uint16Array(Defines the collections for ArkTS)](arkts-arkts-collections-uint16array-c.md) |
| [Int32Array(Defines the collections for ArkTS)](arkts-arkts-collections-int32array-c.md) |
| [Uint32Array(Defines the collections for ArkTS)](arkts-arkts-collections-uint32array-c.md) |
| [Float32Array(Defines the collections for ArkTS)](arkts-arkts-collections-float32array-c.md) |
| [BitVector(Defines the collections for ArkTS)](arkts-arkts-collections-bitvector-c.md) |

### 接口

| 名称 |
| --- |
| [ConcatArray(Defines the collections for ArkTS)](arkts-arkts-collections-concatarray-i.md) |

### 类型

| 名称 |
| --- |
| [TypedArrayFromMapFn(Defines the collections for ArkTS)](arkts-arkts-collections-typedarrayfrommapfn-t.md) |
| [TypedArrayPredicateFn(Defines the collections for ArkTS)](arkts-arkts-collections-typedarraypredicatefn-t.md) |
| [TypedArrayForEachCallback(Defines the collections for ArkTS)](arkts-arkts-collections-typedarrayforeachcallback-t.md) |
| [TypedArrayMapCallback(Defines the collections for ArkTS)](arkts-arkts-collections-typedarraymapcallback-t.md) |
| [TypedArrayReduceCallback(Defines the collections for ArkTS)](arkts-arkts-collections-typedarrayreducecallback-t.md) |
| [TypedArrayCompareFn(Defines the collections for ArkTS)](arkts-arkts-collections-typedarraycomparefn-t.md) |
| [ArrayFromMapFn(Defines the collections for ArkTS)](arkts-arkts-collections-arrayfrommapfn-t.md) |
| [ArrayPredicateFn(Defines the collections for ArkTS)](arkts-arkts-collections-arraypredicatefn-t.md) |
| [ArrayElementPredicateFn(Defines the collections for ArkTS)](arkts-arkts-collections-arrayelementpredicatefn-t.md) |
| [ArrayReduceCallback(Defines the collections for ArkTS)](arkts-arkts-collections-arrayreducecallback-t.md) |
| [ISendable(Defines the collections for ArkTS)](arkts-arkts-collections-isendable-t.md) |
