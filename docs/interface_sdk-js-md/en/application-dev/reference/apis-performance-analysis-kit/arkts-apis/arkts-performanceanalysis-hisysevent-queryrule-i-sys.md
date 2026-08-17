# QueryRule (System API)

Defines event query rules.

**Since:** 23

<!--Device-hiSysEvent-interface QueryRule--><!--Device-hiSysEvent-interface QueryRule-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { hiSysEvent } from 'hiSysEvent';
```

## condition

```TypeScript
condition?: string | null | undefined
```

Additional event conditions. The value of this parameter is in the format of **{"version":"V1","condition":{"and":[{"param":"*Parameter*","op":"*Operator*","value":"*Comparison value*"}]}}**. Parameter: key value of the specified event parameter. Supported operators: **=**, **!=**, **&lt;**, **<=**, **>** and **&gt;=**. Multiple conditions can be configured in the **"and"** array, and the intersection of the query results is used.

**Type:** string \| null \| undefined

**Since:** 23

<!--Device-QueryRule-condition?: string | null | undefined--><!--Device-QueryRule-condition?: string | null | undefined-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## domain

```TypeScript
domain: string
```

Event domain.

**Type:** string

**Since:** 23

<!--Device-QueryRule-domain: string--><!--Device-QueryRule-domain: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

## names

```TypeScript
names: string[]
```

Array of event names. A **QueryRule** object contains multiple system event names.

**Type:** string[]

**Since:** 23

<!--Device-QueryRule-names: string[]--><!--Device-QueryRule-names: string[]-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

