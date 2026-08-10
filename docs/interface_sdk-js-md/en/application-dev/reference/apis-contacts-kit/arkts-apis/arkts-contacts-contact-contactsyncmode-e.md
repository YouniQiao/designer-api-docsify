# ContactSyncMode

同步模式的类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-contact-enum ContactSyncMode--><!--Device-contact-enum ContactSyncMode-End-->

**System capability:** SystemCapability.Applications.ContactsData

## MODE_INCREMENTAL

```TypeScript
MODE_INCREMENTAL = 1
```

表示将在数据库中插入或更新云端和本地之间不同的联系人。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContactSyncMode-MODE_INCREMENTAL = 1--><!--Device-ContactSyncMode-MODE_INCREMENTAL = 1-End-->

**System capability:** SystemCapability.Applications.ContactsData

## MODE_CLOUD_BASED

```TypeScript
MODE_CLOUD_BASED = 2
```

表示所有本地联系人将被云联系人替换。

当使用云覆盖本地模式进行批量同步时，在第一次批量同步期间会删除所有本地联系人（第三方联系人除外）。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContactSyncMode-MODE_CLOUD_BASED = 2--><!--Device-ContactSyncMode-MODE_CLOUD_BASED = 2-End-->

**System capability:** SystemCapability.Applications.ContactsData

