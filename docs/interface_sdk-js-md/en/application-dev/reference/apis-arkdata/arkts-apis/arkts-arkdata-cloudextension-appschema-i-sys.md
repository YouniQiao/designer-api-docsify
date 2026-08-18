# AppSchema (System API)

Represents the application database schema.

**Since:** 23

<!--Device-cloudExtension-export interface AppSchema--><!--Device-cloudExtension-export interface AppSchema-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from '@kit.ArkData';
```

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 23

<!--Device-AppSchema-bundleName: string--><!--Device-AppSchema-bundleName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## databases

```TypeScript
databases: Array<Database>
```

Database information of the application.

**Type:** Array&lt;[Database](arkts-arkdata-cloudextension-database-i-sys.md)&gt;

**Since:** 23

<!--Device-AppSchema-databases: Array<Database>--><!--Device-AppSchema-databases: Array<Database>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## version

```TypeScript
version: int
```

Version of the database schema.

**Type:** int

**Since:** 23

<!--Device-AppSchema-version: int--><!--Device-AppSchema-version: int-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

