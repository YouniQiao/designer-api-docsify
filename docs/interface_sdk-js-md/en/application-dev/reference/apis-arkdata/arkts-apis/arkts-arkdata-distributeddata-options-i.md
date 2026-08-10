# Options

用于提供创建数据库的配置信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Options

<!--Device-distributedData-interface Options--><!--Device-distributedData-interface Options-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## autoSync

```TypeScript
autoSync?: boolean
```

设置数据库文件是否自动同步。默认为false，即手动同步。

ohos.permission.DISTRIBUTED_DATASYNC

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Options#autoSync

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-Options-autoSync?: boolean--><!--Device-Options-autoSync?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## backup

```TypeScript
backup?: boolean
```

设置数据库文件是否备份，默认为true，即备份。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Options#backup

<!--Device-Options-backup?: boolean--><!--Device-Options-backup?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## createIfMissing

```TypeScript
createIfMissing?: boolean
```

当数据库文件不存在时是否创建数据库，默认为true，即创建。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Options#createIfMissing

<!--Device-Options-createIfMissing?: boolean--><!--Device-Options-createIfMissing?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## encrypt

```TypeScript
encrypt?: boolean
```

设置数据库文件是否加密，默认为false，即不加密。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Options#encrypt

<!--Device-Options-encrypt?: boolean--><!--Device-Options-encrypt?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## kvStoreType

```TypeScript
kvStoreType?: KVStoreType
```

设置要创建的数据库类型，默认为DEVICE_COLLABORATION，即多设备协同数据库。

**Type:** [KVStoreType](arkts-arkdata-distributeddata-kvstoretype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Options#kvStoreType

<!--Device-Options-kvStoreType?: KVStoreType--><!--Device-Options-kvStoreType?: KVStoreType-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## schema

```TypeScript
schema?: Schema
```

设置定义存储在数据库中的值，默认为undefined，即不使用schema。

**Type:** [Schema](arkts-arkdata-distributedkvstore-schema-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Options#schema

<!--Device-Options-schema?: Schema--><!--Device-Options-schema?: Schema-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## securityLevel

```TypeScript
securityLevel?: SecurityLevel
```

设置数据库安全级别(S1-S4)。

**Type:** [SecurityLevel](arkts-arkdata-distributedkvstore-securitylevel-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.data.distributedKVStore.Options#securityLevel

<!--Device-Options-securityLevel?: SecurityLevel--><!--Device-Options-securityLevel?: SecurityLevel-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

