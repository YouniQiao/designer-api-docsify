# ExceptionMessage

Represents an exception message about the SQL statement executed by the database.

**Since:** 23

<!--Device-relationalStore-interface ExceptionMessage--><!--Device-relationalStore-interface ExceptionMessage-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
```

## code

```TypeScript
code: number
```

Error code returned by the executed SQL statement. For details about the values and meanings, see [SQLite Error Codes](https://www.sqlite.org/rescode.html).

**Type:** number

**Since:** 23

<!--Device-ExceptionMessage-code: int--><!--Device-ExceptionMessage-code: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## message

```TypeScript
message: string
```

Exception message returned by the executed SQL statement.

**Type:** string

**Since:** 23

<!--Device-ExceptionMessage-message: string--><!--Device-ExceptionMessage-message: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## sql

```TypeScript
sql: string
```

SQL statement that reports the error.

**Type:** string

**Since:** 23

<!--Device-ExceptionMessage-sql: string--><!--Device-ExceptionMessage-sql: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core
