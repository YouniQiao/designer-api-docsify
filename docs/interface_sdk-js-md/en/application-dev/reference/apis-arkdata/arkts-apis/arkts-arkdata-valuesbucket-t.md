# ValuesBucket

```TypeScript
export type ValuesBucket = Record<string, ValueType | Uint8Array | null>
```

用于存储键值对的类型。该类型不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ValuesBucket = Record<string, ValueType | Uint8Array | null>--><!--Device-unnamed-export type ValuesBucket = Record<string, ValueType | Uint8Array | null>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Core

**Property type:** Record<string, ValueType | Uint8Array | null>

