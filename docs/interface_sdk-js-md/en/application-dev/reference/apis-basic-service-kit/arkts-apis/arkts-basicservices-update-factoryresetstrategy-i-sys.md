# FactoryResetStrategy (System API)

恢复出厂设置策略，包含scope(重置范围)和strategy(重置策略描述)字段。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-update-export interface FactoryResetStrategy--><!--Device-update-export interface FactoryResetStrategy-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## scope

```TypeScript
scope: FactoryResetScope
```

重置范围。DATA仅清除用户数据分区，适用于仅清除数据的场景；DATA_AND_OS同时清除用户数据分区和操作系统分区，适用于同时清除系统和数据的场景。

**Type:** [FactoryResetScope](arkts-basicservices-update-factoryresetscope-e-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FactoryResetStrategy-scope: FactoryResetScope--><!--Device-FactoryResetStrategy-scope: FactoryResetScope-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## strategy

```TypeScript
strategy: string
```

重置策略，用于记录重置操作的具体策略信息。长度范围[0，64]，单位：字符，有效字符包括字母、数字、下划线、连字符和空格。超出范围或包含无效字符时抛出异常。为重置操作的自定义描述文本，如quick erase表示快速擦除、deep erase表示深度擦除等。

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FactoryResetStrategy-strategy: string--><!--Device-FactoryResetStrategy-strategy: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

