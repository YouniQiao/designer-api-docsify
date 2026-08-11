# ProcessManager

Provides APIs for throwing exceptions during the addition of a process.

Construct a **ProcessManager** object.

**Since:** 9

<!--Device-process-export class ProcessManager--><!--Device-process-export class ProcessManager-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## exit

```TypeScript
exit(code: number): void
```

Terminates this process.

Exercise caution when using this API. After this API is called, the application exits. If the input parameter is not 0, data loss or exceptions may occur.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-exit(code: number): void--><!--Device-ProcessManager-exit(code: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |

## Examples

```TypeScript
let pro = new process.ProcessManager();
pro.exit(0);
```

## getEnvironmentVar

```TypeScript
getEnvironmentVar(name: string): string
```

Obtains the value of an environment variable.

> **NOTE：**
> 
> Obtains the value of an environment variable. If the environment variable does not exist, **undefined** is
> returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-getEnvironmentVar(name: string): string--><!--Device-ProcessManager-getEnvironmentVar(name: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let pro = new process.ProcessManager();
let pres = pro.getEnvironmentVar("PATH");
```

## getSystemConfig

```TypeScript
getSystemConfig(name: number): number
```

Obtains the system configuration.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-getSystemConfig(name: number): number--><!--Device-ProcessManager-getSystemConfig(name: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro = new process.ProcessManager();
let _SC_ARG_MAX = 0;
let pres = pro.getSystemConfig(_SC_ARG_MAX);
```

## getThreadPriority

```TypeScript
getThreadPriority(v: number): number
```

Obtains the thread priority based on the specified TID.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-getThreadPriority(v: number): number--><!--Device-ProcessManager-getThreadPriority(v: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro = new process.ProcessManager();
let tid = process.tid;
let pres = pro.getThreadPriority(tid);
```

## getUidForName

```TypeScript
getUidForName(v: string): number
```

Obtains the UID of a user from the user database of the system based on the specified user name.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-getUidForName(v: string): number--><!--Device-ProcessManager-getUidForName(v: string): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let pro = new process.ProcessManager();
let pres = pro.getUidForName("tool");
```

## isAppUid

```TypeScript
isAppUid(v: number): boolean
```

Checks whether a UID belongs to this application.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-isAppUid(v: number): boolean--><!--Device-ProcessManager-isAppUid(v: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| v | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let pro = new process.ProcessManager();
// Use process.uid to obtain the UID.
let pres = process.uid;
let result = pro.isAppUid(pres);
console.info("result: " + result); // result: true
```

## kill

```TypeScript
kill(signal: number, pid: number): boolean
```

Sends a signal to the specified process to terminate it. Only the current process can be terminated.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-kill(signal: number, pid: number): boolean--><!--Device-ProcessManager-kill(signal: number, pid: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| signal | number | Yes |
| pid | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let pro = new process.ProcessManager();
let pres = process.pid;
let result = pro.kill(28, pres);
```
