# Options（系统接口）

```TypeScript
interface Options
```

用于提供创建数据库的配置信息。

**起始版本：** 9

<!--Device-distributedKVStore-interface Options--><!--Device-distributedKVStore-interface Options-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## dumpStackOnFileDeletion

```TypeScript
dumpStackOnFileDeletion?: boolean
```

KV存储是否开启dump-stack on文件删除开关，用于定位问题数据库文件被意外删除。

**true**：启用文件删除时转储堆栈功能。打开KV存储后，文件系统输出调用通过文件接口直接删除数据库文件（**db**、**wal**、**shm**）时删除操作堆栈。

**false**（默认）：删除文件时禁用dump-stack。

该参数只对主备数据库的**db**、**wal**、**shm**文件生效。

该参数依赖于设备文件系统的dump-stack能力。如果文件系统没有支持该能力，则该参数不生效，不影响打开KV存储。

此参数不持久化到元数据库，每次KV存储时都需要配置已打开。KV存储的删除、恢复、重建等常规操作，不触发调用栈输出。

默认值：false。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Options-dumpStackOnFileDeletion?: boolean--><!--Device-Options-dumpStackOnFileDeletion?: boolean-End-->

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**系统接口：** 此接口为系统接口。
