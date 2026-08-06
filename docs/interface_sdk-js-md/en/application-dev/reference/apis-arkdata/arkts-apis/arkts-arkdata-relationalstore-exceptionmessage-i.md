# ExceptionMessage

Represents an exception message about the SQL statement executed by the database.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface ExceptionMessage--><!--Device-relationalStore-interface ExceptionMessage-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## code

```TypeScript
code: int
```

Error code returned by the executed SQL statement. For details about the values and meanings, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ExceptionMessage-code: int--><!--Device-ExceptionMessage-code: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## message

```TypeScript
message: string
```

Exception message returned by the executed SQL statement.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ExceptionMessage-message: string--><!--Device-ExceptionMessage-message: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## sql

```TypeScript
sql: string
```

SQL statement that reports the error.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ExceptionMessage-sql: string--><!--Device-ExceptionMessage-sql: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

