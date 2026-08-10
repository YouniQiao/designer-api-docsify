# ReturningConfig

指定returning相关接口操作后需要返回的字段名列表和结果集中允许包含的最大记录数。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-relationalStore-interface ReturningConfig--><!--Device-relationalStore-interface ReturningConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## columns

```TypeScript
columns: Array<string>
```

指定结果集中返回的字段，支持传入1到4个字段。注意：不能传入带有空格、逗号以及星号的字段名。

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReturningConfig-columns: Array<string>--><!--Device-ReturningConfig-columns: Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## maxReturningCount

```TypeScript
maxReturningCount?: int
```

指定结果集返回的最大行数量，默认为1024条，最大支持32766条。注意：当实际修改行数超过maxReturningCount设置的值时，系统会丢弃超出部分的数据。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReturningConfig-maxReturningCount?: int--><!--Device-ReturningConfig-maxReturningCount?: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

