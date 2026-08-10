# SetStorageOptions

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-unnamed-export interface SetStorageOptions--><!--Device-unnamed-export interface SetStorageOptions-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-SetStorageOptions-complete?: () => void--><!--Device-SetStorageOptions-complete?: () => void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数，data为错误信息，code为错误码。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-SetStorageOptions-fail?: (data: string, code: number) => void--><!--Device-SetStorageOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: () => void
```

接口调用成功的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-SetStorageOptions-success?: () => void--><!--Device-SetStorageOptions-success?: () => void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

## key

```TypeScript
key: string
```

要修改的存储值的索引。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-SetStorageOptions-key: string--><!--Device-SetStorageOptions-key: string-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

## value

```TypeScript
value: string
```

新值。长度需小于128字节。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-SetStorageOptions-value: string--><!--Device-SetStorageOptions-value: string-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

