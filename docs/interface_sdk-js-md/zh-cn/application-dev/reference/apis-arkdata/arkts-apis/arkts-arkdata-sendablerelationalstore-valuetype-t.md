# ValueType

```TypeScript
type ValueType = null | number | string | boolean | collections.Uint8Array | Asset | Assets |
    collections.Float32Array | bigint
```

用于表示允许的数据字段类型，接口参数具体类型根据其功能而定。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 |
| --- |
| null |
| number |
| string |
| boolean |
| collections.Uint8Array |
| [Asset](arkts-arkdata-commontype-asset-i.md) |
| [Assets](arkts-arkdata-sendablerelationalstore-assets-t.md) |
| collections.Float32Array |
| bigint |
