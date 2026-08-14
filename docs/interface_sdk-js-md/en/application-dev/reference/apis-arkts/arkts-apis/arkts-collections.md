# @arkts.collections

The collections module provides ArkTS containers for efficient data transfer in concurrency scenarios. The ArkTS containers provide similar functionalities as their JavaScript counterparts, except that their properties cannot be added or updated through `.` or `[]`. By default, ArkTS containers are passed by reference between concurrent instances. This means that multiple concurrent instances can simultaneously operate the same container instance. Pass-by-copy is also supported. In this mode, each concurrent instance holds an ArkTS container instance. ArkTS containers are not thread-safe. They adopt the fail-fast approach. An exception is thrown if multiple concurrent instances make structural changes to a container instance at the same time. Therefore, in multi-thread read/write scenarios, you must use the ArkTS asynchronous lock to ensure secure access to the ArkTS containers. Currently, the following ArkTS containers are provided: [Array](#@arkts.collections), [Map](#@arkts.collections), [Set](#@arkts.collections), TypedArray ([Int8Array](#@arkts.collections), [Uint8Array](#@arkts.collections), [Int16Array](#@arkts.collections), [Uint16Array](#@arkts.collections), [Int32Array](#@arkts.collections), [Uint32Array](#@arkts.collections), [Uint8ClampedArray](#@arkts.collections) and [Float32Array](#@arkts.collections)), [ArrayBuffer](#@arkts.collections), [BitVector](#@arkts.collections), and [ConcatArray](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace collections--><!--Device-unnamed-declare namespace collections-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from 'collections';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [Array](arkts-arkts-collections-array-c.md) | A linear data structure that is implemented on arrays and can be passed between ArkTS concurrent instances. Pass-by-reference is recommended for better transfer performance. > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > This section uses the following to identify the use of generics: - T: type, which can be any of the [sendable data types](../../../arkts-utils/arkts-sendable.md#sendable-data-types). **Decorator**: \@Sendable |
| [ArrayBuffer](arkts-arkts-collections-arraybuffer-c.md) | Underlying data structure of the ArkTS TypedArray ([Int8Array](#@arkts.collections), [Uint8Array](#@arkts.collections), [Int16Array](#@arkts.collections), [Uint16Array](#@arkts.collections), [Int32Array](#@arkts.collections), [Uint32Array](#@arkts.collections), [Uint8ClampedArray](#@arkts.collections), and [Float32Array](#@arkts.collections)). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [BitVector](arkts-arkts-collections-bitvector-c.md) | A linear data structure that is implemented on arrays. A bit vector stores bit values and provides bit-level storage and processing. > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [Float32Array](arkts-arkts-collections-float32array-c.md) | A linear data structure that is implemented on [ArkTS ArrayBuffer](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [Int16Array](arkts-arkts-collections-int16array-c.md) | A linear data structure that is implemented on [ArkTS ArrayBuffer](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [Int32Array](arkts-arkts-collections-int32array-c.md) | A linear data structure that is implemented on [ArkTS ArrayBuffer](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [Int8Array](arkts-arkts-collections-int8array-c.md) | A linear data structure that is implemented on [ArkTS ArrayBuffer](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [Map](arkts-arkts-collections-map-c.md) | A non-linear data structure. > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > This section uses the following to identify the use of generics: - K: key. - V: value. The K and V types must be any of the [sendable data types](../../../arkts-utils/arkts-sendable.md#sendable-data-types). **Decorator**: \@Sendable |
| [Set](arkts-arkts-collections-set-c.md) | A non-linear data structure. > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > This section uses the following to identify the use of generics: - T: type, which can be any of the [sendable data types](../../../arkts-utils/arkts-sendable.md#sendable-data-types). **Decorator**: \@Sendable |
| [Uint16Array](arkts-arkts-collections-uint16array-c.md) | A linear data structure that is implemented on [ArkTS ArrayBuffer](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [Uint32Array](arkts-arkts-collections-uint32array-c.md) | A linear data structure that is implemented on [ArkTS ArrayBuffer](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [Uint8Array](arkts-arkts-collections-uint8array-c.md) | A linear data structure that is implemented on [ArkTS ArrayBuffer](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) | A linear data structure that is implemented on [ArkTS ArrayBuffer](#@arkts.collections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > **Decorator**: \@Sendable |

### Interfaces

| Name | Description |
| --- | --- |
| [ConcatArray](arkts-arkts-collections-concatarray-i.md) | An array-like object that can be concatenated. This API extends **ISendable**. > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > This section uses the following to identify the use of generics: - T: type, which can be any of the [sendable data types](../../../arkts-utils/arkts-sendable.md#sendable-data-types). |

### Types

| Name | Description |
| --- | --- |
| [ArrayFromMapFn](arkts-arkts-collections-arrayfrommapfn-t.md) | Defines the ArkTS Array reduction function, which is used by the 'from' API of the Array class. |
| [ArrayPredicateFn](arkts-arkts-collections-arraypredicatefn-t.md) | Defines the ArkTS Array reduction function, which is used by the 'some' and 'every' APIs of the Array class to determine whether array elements meet certain test conditions. |
| [ArrayReduceCallback](arkts-arkts-collections-arrayreducecallback-t.md) | Defines the ArkTS Array reduction function, which is used by the 'reduceRight' API of the Array class. |
| [ISendable](arkts-arkts-collections-isendable-t.md) | 'ISendable' is the parent type of all sendable types except null and undefined. It does not have any necessary methods or properties. |
| [TypedArrayCompareFn](arkts-arkts-collections-typedarraycomparefn-t.md) | Describes the sort function of the ArkTS typed array. |
| [TypedArrayForEachCallback](arkts-arkts-collections-typedarrayforeachcallback-t.md) | Describes the traversal function of the ArkTS typed array. |
| [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md) | Describes the mapping function of the ArkTS typed array. |
| [TypedArrayMapCallback](arkts-arkts-collections-typedarraymapcallback-t.md) | Describes the conversion mapping function of the ArkTS typed array. |
| [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md) | Describes the assertion function of the ArkTS typed array. |
| [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md) | Describes the reduce function of the ArkTS typed array. |

