# Options (System API)

```TypeScript
interface Options
```

Provides KV store configuration.

**Since:** 9

<!--Device-distributedKVStore-interface Options--><!--Device-distributedKVStore-interface Options-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## dumpStackOnFileDeletion

```TypeScript
dumpStackOnFileDeletion?: boolean
```

Indicates whether to enable the dump-stack on file deletion function for KV storage. This function is used to locate the problem that database files are deleted unexpectedly.

**true**: The stack dump function is enabled when a file is deleted. After the KV storage is enabled, the operation stack is deleted when the file system output invokes the file interface to directly delete database files(**db**, **wal**, and **shm**).

**false** (default): Disable dump-stack when deleting files.

This parameter takes effect only for the **db**, **wal**, and **shm** files of the active/standby database.

This parameter depends on the dump-stack capability of the device file system. If the file system does not support this capability, this parameter does not take effect, and the KV storage function is not affected.

This parameter is not persisted to the metadata database and must be enabled each time the KV is stored. Common operations such as deleting, restoring, and rebuilding KV storage do not trigger call stack output.

Default value: false.

**Type:** boolean

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-Options-dumpStackOnFileDeletion?: boolean--><!--Device-Options-dumpStackOnFileDeletion?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.
