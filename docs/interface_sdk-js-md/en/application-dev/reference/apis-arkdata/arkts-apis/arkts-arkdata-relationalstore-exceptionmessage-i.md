# ExceptionMessage

Represents an exception message about the SQL statement executed by the database.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-relationalStore-interface ExceptionMessage--><!--Device-relationalStore-interface ExceptionMessage-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'relationalStore';
```

## code

```TypeScript
code: int
```

Error code returned by the executed SQL statement. For details about the values and meanings, see [SQLite Error Codes](https://www.sqlite.org/rescode.html).

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ExceptionMessage-code: int--><!--Device-ExceptionMessage-code: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## message

```TypeScript
message: string
```

Exception message returned by the executed SQL statement.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ExceptionMessage-message: string--><!--Device-ExceptionMessage-message: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## sql

```TypeScript
sql: string
```

SQL statement that reports the error.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ExceptionMessage-sql: string--><!--Device-ExceptionMessage-sql: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

