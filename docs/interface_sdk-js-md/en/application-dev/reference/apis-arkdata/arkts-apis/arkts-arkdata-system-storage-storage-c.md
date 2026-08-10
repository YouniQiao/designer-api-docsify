# Storage

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-unnamed-export default class Storage--><!--Device-unnamed-export default class Storage-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

## clear

```TypeScript
static clear(options?: ClearStorageOptions): void
```

清空缓存中存储的键值对。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Substitutes:** ohos.preferences.preferences.clear

**Model restriction:** This API can be used only in the FA model.

<!--Device-Storage-static clear(options?: ClearStorageOptions): void--><!--Device-Storage-static clear(options?: ClearStorageOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ClearStorageOptions](arkts-arkdata-system-storage-clearstorageoptions-i.md) | No | Indicates the target options. |

## delete

```TypeScript
static delete(options: DeleteStorageOptions): void
```

删除缓存中索引对应的键值对。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Substitutes:** ohos.preferences.preferences.delete

**Model restriction:** This API can be used only in the FA model.

<!--Device-Storage-static delete(options: DeleteStorageOptions): void--><!--Device-Storage-static delete(options: DeleteStorageOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DeleteStorageOptions](arkts-arkdata-system-storage-deletestorageoptions-i.md) | Yes | Indicates the target options. |

## get

```TypeScript
static get(options: GetStorageOptions): void
```

通过索引读取缓存中存储的值。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Substitutes:** ohos.preferences.preferences.get

**Model restriction:** This API can be used only in the FA model.

<!--Device-Storage-static get(options: GetStorageOptions): void--><!--Device-Storage-static get(options: GetStorageOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetStorageOptions](arkts-arkdata-system-storage-getstorageoptions-i.md) | Yes | Indicates the target options. |

## set

```TypeScript
static set(options: SetStorageOptions): void
```

修改缓存中索引对应的值。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Storage-static set(options: SetStorageOptions): void--><!--Device-Storage-static set(options: SetStorageOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SetStorageOptions](arkts-arkdata-system-storage-setstorageoptions-i.md) | Yes | Indicates the target options. |

