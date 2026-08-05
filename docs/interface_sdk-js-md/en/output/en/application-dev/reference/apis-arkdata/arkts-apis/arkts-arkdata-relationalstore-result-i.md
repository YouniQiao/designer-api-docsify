# Result

Records the number of affected data rows and the result set.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-relationalStore-interface Result--><!--Device-relationalStore-interface Result-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## changed

```TypeScript
readonly changed: long
```

Number of affected rows.

**Type:** long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Result-readonly changed: long--><!--Device-Result-readonly changed: long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## resultSet

```TypeScript
readonly resultSet: LiteResultSet
```

Result set of the affected data. Defaults to 1,024 rows of data, with a maximum supported limit of 32,766 rows supported; excess rows will be discarded.

**Type:** LiteResultSet

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Result-readonly resultSet: LiteResultSet--><!--Device-Result-readonly resultSet: LiteResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

