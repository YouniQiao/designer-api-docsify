# CloudType（系统接口）

```TypeScript
type CloudType = null | number | number | string | boolean | Uint8Array | CloudAsset | CloudAssets
```

表示云数据字段可使用的类型。各接口参数的实际类型视其功能而定。

**起始版本：** 11

<!--Device-cloudExtension-type CloudType = null | long | double | string | boolean | Uint8Array | CloudAsset | CloudAssets--><!--Device-cloudExtension-type CloudType = null | long | double | string | boolean | Uint8Array | CloudAsset | CloudAssets-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

| 类型 |
| --- |
| null |
| long |
| double |
| string |
| boolean |
| Uint8Array |
| [CloudAsset](arkts-arkdata-cloudextension-cloudasset-i-sys.md) |
| [CloudAssets](arkts-arkdata-cloudextension-cloudassets-t-sys.md) |
