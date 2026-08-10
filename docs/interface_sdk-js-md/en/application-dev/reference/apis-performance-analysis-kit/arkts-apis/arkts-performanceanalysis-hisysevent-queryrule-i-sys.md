# QueryRule (System API)

系统事件查询规则对象接口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-hiSysEvent-interface QueryRule--><!--Device-hiSysEvent-interface QueryRule-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## condition

```TypeScript
condition?: string
```

事件的额外参数条件，格式：{"version":"V1","condition":{"and":[{"param":"参数","op":"操作符","value":"比较值"}]}}。

参数：指定事件参数的键值。

操作符支持：=、!=、&lt;、<=、>和&gt;&lt;=、&gt;和>=。

支持在“and”数组中配置多个条件，查询结果取交集。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-QueryRule-condition?: string--><!--Device-QueryRule-condition?: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## domain

```TypeScript
domain: string
```

查询包含的事件领域。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-QueryRule-domain: string--><!--Device-QueryRule-domain: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## names

```TypeScript
names: string[]
```

查询所包含的多个事件名称，每个查询规则对象包含多个系统事件名称。

**Type:** string[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-QueryRule-names: string[]--><!--Device-QueryRule-names: string[]-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

