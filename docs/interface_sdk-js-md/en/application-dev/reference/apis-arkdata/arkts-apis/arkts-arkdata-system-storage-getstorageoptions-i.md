# GetStorageOptions

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-unnamed-export interface GetStorageOptions--><!--Device-unnamed-export interface GetStorageOptions-End-->

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

<!--Device-GetStorageOptions-complete?: () => void--><!--Device-GetStorageOptions-complete?: () => void-End-->

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

<!--Device-GetStorageOptions-fail?: (data: string, code: number) => void--><!--Device-GetStorageOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: (data: any) => void
```

接口调用成功的回调函数，data为返回key对应的value。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetStorageOptions-success?: (data: any) => void--><!--Device-GetStorageOptions-success?: (data: any) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | any | Yes |  |

## default

```TypeScript
default?: string
```

key不存在则返回的默认值。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetStorageOptions-default?: string--><!--Device-GetStorageOptions-default?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

## key

```TypeScript
key: string
```

内容索引。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-GetStorageOptions-key: string--><!--Device-GetStorageOptions-key: string-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

