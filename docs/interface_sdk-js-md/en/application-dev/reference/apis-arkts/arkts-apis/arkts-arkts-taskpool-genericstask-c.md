# GenericsTask

Implements a generic task. **GenericsTask** inherits from [Task](arkts-arkts-taskpool-task-c.md). During the creation of a generic task, the passed-in parameter types and return value types of concurrent functions are verified in the compilation phase. Other behaviors are the same as those during the creation of a task.

**Inheritance/Implementation:** GenericsTask extends [Task](arkts-arkts-taskpool-task-c.md)

**Since:** 13

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { taskpool } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(func: (...args: A) => R | Promise<R>, ...args: A)
```

A constructor used to create a **GenericsTask** object.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |

## constructor

```TypeScript
constructor(name: string, func: (...args: A) => R | Promise<R>, ...args: A)
```

A constructor used to create a **GenericsTask** instance, with the task name specified.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| func | (...args: A) = & gt; R \ | Promise & lt;R & gt; | Yes |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | A | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200014](../errorcode-utils.md#10200014-non-concurrent-function-error) |
