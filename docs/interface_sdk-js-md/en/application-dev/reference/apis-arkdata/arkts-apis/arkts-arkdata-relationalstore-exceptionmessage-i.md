# ExceptionMessage

描述数据库执行的SQL语句的错误信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface ExceptionMessage--><!--Device-relationalStore-interface ExceptionMessage-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## code

```TypeScript
code: int
```

表示执行SQL返回的错误码，对应的取值和含义请见[SQLite错误码](https://www.sqlite.org/rescode.html)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ExceptionMessage-code: int--><!--Device-ExceptionMessage-code: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## message

```TypeScript
message: string
```

表示执行SQL返回的错误信息，长度不超过1024字节。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ExceptionMessage-message: string--><!--Device-ExceptionMessage-message: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## sql

```TypeScript
sql: string
```

表示报错执行的SQL语句，长度不超过1024字节。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ExceptionMessage-sql: string--><!--Device-ExceptionMessage-sql: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

