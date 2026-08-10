# ExtensionValue (System API)

当前数据记录的扩展信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface ExtensionValue--><!--Device-cloudExtension-export interface ExtensionValue-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## createTime

```TypeScript
readonly createTime: long
```

创建行数据的时间（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ExtensionValue-readonly createTime: long--><!--Device-ExtensionValue-readonly createTime: long-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## id

```TypeScript
readonly id: string
```

执行插入操作时系统自动生成的ID。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ExtensionValue-readonly id: string--><!--Device-ExtensionValue-readonly id: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## modifyTime

```TypeScript
readonly modifyTime: long
```

修改行数据的时间（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ExtensionValue-readonly modifyTime: long--><!--Device-ExtensionValue-readonly modifyTime: long-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## operation

```TypeScript
readonly operation: Flag
```

对行数据所做的操作。

**Type:** [Flag](arkts-arkdata-cloudextension-flag-e-sys.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ExtensionValue-readonly operation: Flag--><!--Device-ExtensionValue-readonly operation: Flag-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

