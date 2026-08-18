# @arkts.collections

The collections module provides ArkTS containers for efficient data transfer in concurrency scenarios. The ArkTS containers provide similar functionalities as their JavaScript counterparts, except that their properties cannot be added or updated through `.` or `[]`. By default, ArkTS containers are passed by reference between concurrent instances. This means that multiple concurrent instances can simultaneously operate the same container instance. Pass-by-copy is also supported. In this mode, each concurrent instance holds an ArkTS container instance. ArkTS containers are not thread-safe. They adopt the fail-fast approach. An exception is thrown if multiple concurrent instances make structural changes to a container instance at the same time. Therefore, in multi-thread read/write scenarios, you must use the ArkTS asynchronous lock to ensure secure access to the ArkTS containers. Currently, the following ArkTS containers are provided: [Array](#arktscollections), [Map](#arktscollections), [Set](#arktscollections), TypedArray ([Int8Array](#arktscollections), [Uint8Array](#arktscollections), [Int16Array](#arktscollections), [Uint16Array](#arktscollections), [Int32Array](#arktscollections), [Uint32Array](#arktscollections), [Uint8ClampedArray](#arktscollections) and [Float32Array](#arktscollections)), [ArrayBuffer](#arktscollections), [BitVector](#arktscollections), and [ConcatArray](#arktscollections). > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets).

**Since:** 12

<!--Device-unnamed-declare namespace collections--><!--Device-unnamed-declare namespace collections-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Array](arkts-arkts-collections-array-c.md) |
| [ArrayBuffer](arkts-arkts-collections-arraybuffer-c.md) |
| [BitVector](arkts-arkts-collections-bitvector-c.md) |
| [Float32Array](arkts-arkts-collections-float32array-c.md) |
| [Int16Array](arkts-arkts-collections-int16array-c.md) |
| [Int32Array](arkts-arkts-collections-int32array-c.md) |
| [Int8Array](arkts-arkts-collections-int8array-c.md) |
| [Map](arkts-arkts-collections-map-c.md) |
| [Set](arkts-arkts-collections-set-c.md) |
| [Uint16Array](arkts-arkts-collections-uint16array-c.md) |
| [Uint32Array](arkts-arkts-collections-uint32array-c.md) |
| [Uint8Array](arkts-arkts-collections-uint8array-c.md) |
| [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConcatArray](arkts-arkts-collections-concatarray-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ArrayFromMapFn](arkts-arkts-collections-arrayfrommapfn-t.md) |
| [ArrayPredicateFn](arkts-arkts-collections-arraypredicatefn-t.md) |
| [ArrayReduceCallback](arkts-arkts-collections-arrayreducecallback-t.md) |
| [ISendable](arkts-arkts-collections-isendable-t.md) |
| [TypedArrayCompareFn](arkts-arkts-collections-typedarraycomparefn-t.md) |
| [TypedArrayForEachCallback](arkts-arkts-collections-typedarrayforeachcallback-t.md) |
| [TypedArrayFromMapFn](arkts-arkts-collections-typedarrayfrommapfn-t.md) |
| [TypedArrayMapCallback](arkts-arkts-collections-typedarraymapcallback-t.md) |
| [TypedArrayPredicateFn](arkts-arkts-collections-typedarraypredicatefn-t.md) |
| [TypedArrayReduceCallback](arkts-arkts-collections-typedarrayreducecallback-t.md) |
