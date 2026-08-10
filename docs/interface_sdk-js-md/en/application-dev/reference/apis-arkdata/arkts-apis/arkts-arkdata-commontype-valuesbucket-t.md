# ValuesBucket

```TypeScript
type ValuesBucket = Record<string, ValueType>
```

用于存储键值对的类型。该类型不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-commonType-type ValuesBucket = Record<string, ValueType>--><!--Device-commonType-type ValuesBucket = Record<string, ValueType>-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

**Property type:** Record<string, ValueType>

