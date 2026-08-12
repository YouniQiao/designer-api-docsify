# Storage

**Since:** 3

**Deprecated since:** 6

<!--Device-unnamed-export default class Storage--><!--Device-unnamed-export default class Storage-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

## clear

```TypeScript
static clear(options?: ClearStorageOptions): void
```

Clears the stored content.

**Since:** 3

**Deprecated since:** 6

**Substitutes:** [clear](ohos.preferences.preferences.clear)

**Model restriction:** This API can be used only in the FA model.

<!--Device-Storage-static clear(options?: ClearStorageOptions): void--><!--Device-Storage-static clear(options?: ClearStorageOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ClearStorageOptions](arkts-arkdata-system-storage-clearstorageoptions-i.md) | No |

## delete

```TypeScript
static delete(options: DeleteStorageOptions): void
```

Deletes the stored content.

**Since:** 3

**Deprecated since:** 6

**Substitutes:** [delete](ohos.preferences.preferences.delete)

**Model restriction:** This API can be used only in the FA model.

<!--Device-Storage-static delete(options: DeleteStorageOptions): void--><!--Device-Storage-static delete(options: DeleteStorageOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DeleteStorageOptions](arkts-arkdata-system-storage-deletestorageoptions-i.md) | Yes |

## get

```TypeScript
static get(options: GetStorageOptions): void
```

Reads the stored content.

**Since:** 3

**Deprecated since:** 6

**Substitutes:** [get](ohos.preferences.preferences.get)

**Model restriction:** This API can be used only in the FA model.

<!--Device-Storage-static get(options: GetStorageOptions): void--><!--Device-Storage-static get(options: GetStorageOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GetStorageOptions](arkts-arkdata-system-storage-getstorageoptions-i.md) | Yes |

## set

```TypeScript
static set(options: SetStorageOptions): void
```

Modifies the stored content.

**Since:** 3

**Deprecated since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Storage-static set(options: SetStorageOptions): void--><!--Device-Storage-static set(options: SetStorageOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SetStorageOptions](arkts-arkdata-system-storage-setstorageoptions-i.md) | Yes |
