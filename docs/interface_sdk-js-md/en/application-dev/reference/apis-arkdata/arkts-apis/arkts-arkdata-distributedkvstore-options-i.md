# Options

用于提供创建数据库的配置信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-interface Options--><!--Device-distributedKVStore-interface Options-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## autoSync

```TypeScript
autoSync?: boolean
```

设置数据库是否支持跨设备自动同步。默认为false，即只支持手动同步。配置为true，即只支持在跨设备Call调用实现的多端协同中生效，其他场景无法生效。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-autoSync?: boolean--><!--Device-Options-autoSync?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## backup

```TypeScript
backup?: boolean
```

设置数据库文件是否备份，true为备份，false为不备份，默认为true。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-backup?: boolean--><!--Device-Options-backup?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## createIfMissing

```TypeScript
createIfMissing?: boolean
```

当数据库文件不存在时是否创建数据库，true为创建，false为不创建，默认为true。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-createIfMissing?: boolean--><!--Device-Options-createIfMissing?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## encrypt

```TypeScript
encrypt?: boolean
```

设置数据库文件是否加密，true为加密，false为不加密，默认为false。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-encrypt?: boolean--><!--Device-Options-encrypt?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## kvStoreType

```TypeScript
kvStoreType?: KVStoreType
```

设置要创建的数据库类型，默认为DEVICE_COLLABORATION，即多设备协同数据库。

**Type:** [KVStoreType](arkts-arkdata-distributeddata-kvstoretype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-kvStoreType?: KVStoreType--><!--Device-Options-kvStoreType?: KVStoreType-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## rootDir

```TypeScript
rootDir?: string
```

设置数据库文件存储路径，不设置即为默认路径（context.databaseDir）。不能设置空字符串，创建数据库和删除数据库时目录必须有访问权限且存在，关闭数据库不校验此参数。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-rootDir?: string--><!--Device-Options-rootDir?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## schema

```TypeScript
schema?: Schema
```

设置定义存储在数据库中的值，默认为undefined，即不使用Schema。

**Type:** [Schema](arkts-arkdata-distributedkvstore-schema-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-schema?: Schema--><!--Device-Options-schema?: Schema-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## securityLevel

```TypeScript
securityLevel: SecurityLevel
```

设置数据库安全级别。

**Type:** [SecurityLevel](arkts-arkdata-distributedkvstore-securitylevel-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-securityLevel: SecurityLevel--><!--Device-Options-securityLevel: SecurityLevel-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

