# CloudType (System API)

```TypeScript
type CloudType = null | long | double | string | boolean | Uint8Array | CloudAsset | CloudAssets
```

表示云数据字段可使用的类型。各接口参数的实际类型视其功能而定。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-type CloudType = null | long | double | string | boolean | Uint8Array | CloudAsset | CloudAssets--><!--Device-cloudExtension-type CloudType = null | long | double | string | boolean | Uint8Array | CloudAsset | CloudAssets-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

| Type | Description |
| --- | --- |
| null | 表示值的类型为空。 |
| long | 表示值的类型为数字类型。 |
| double | 表示值的类型为数字类型。 |
| string | 表示值的类型为字符串类型。 |
| boolean | 表示值的类型为布尔类型。 |
| Uint8Array | 表示值的类型为Uint8Array类型。 |
| CloudAsset | 表示值的类型为云资产类型。 |
| CloudAssets | 表示值的类型为云资产数组类型。 |

