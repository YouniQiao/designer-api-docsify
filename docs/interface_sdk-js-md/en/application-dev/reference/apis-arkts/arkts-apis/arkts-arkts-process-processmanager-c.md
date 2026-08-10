# ProcessManager

提供进程管理相关接口，包括进程 UID 判断、用户信息查询、线程优先级获取、环境变量获取、进程退出和信号发送等功能。

通过 `new process.ProcessManager()` 构造 ProcessManager 对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

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

终止程序。

请谨慎使用此接口，此接口调用后应用会退出，如果输入参数非0，可能会导致数据丢失或出现未定义的运行异常。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-exit(code: number): void--><!--Device-ProcessManager-exit(code: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | 进程的退出码。 |

## Examples

```TypeScript
let pro = new process.ProcessManager();
pro.exit(0);
```

## getEnvironmentVar

```TypeScript
getEnvironmentVar(name: string): string
```

获取环境变量对应的值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-getEnvironmentVar(name: string): string--><!--Device-ProcessManager-getEnvironmentVar(name: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 环境变量名。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回指定环境变量名对应的值。如果环境变量不存在，返回undefined。 |

## Examples

```TypeScript
let pro = new process.ProcessManager();
let pres = pro.getEnvironmentVar("PATH");
```

## getSystemConfig

```TypeScript
getSystemConfig(name: number): number
```

获取系统配置信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-getSystemConfig(name: number): number--><!--Device-ProcessManager-getSystemConfig(name: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | number | Yes | 指定系统配置参数名。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回系统配置信息。如果配置不存在，返回 -1。 |

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

根据指定的 tid 获取线程优先级。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-getThreadPriority(v: number): number--><!--Device-ProcessManager-getThreadPriority(v: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | number | Yes | 指定的线程 tid。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回线程的优先级。优先级顺序取决于当前操作系统。 |

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

根据指定的用户名，从系统的用户数据库中获取该用户 uid。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-getUidForName(v: string): number--><!--Device-ProcessManager-getUidForName(v: string): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | string | Yes | 用户名。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 获取用户 uid，如果用户不存在则返回 -1。 |

## Examples

```TypeScript
let pro = new process.ProcessManager();
let pres = pro.getUidForName("tool");
```

## isAppUid

```TypeScript
isAppUid(v: number): boolean
```

判断 uid 是否属于当前应用程序。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-isAppUid(v: number): boolean--><!--Device-ProcessManager-isAppUid(v: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| v | number | Yes | 应用程序的 uid。可通过 process.uid 获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回判断结果。如果是应用程序的 uid 则返回 true； 否则返回 false。 |

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

发送信号到指定的进程，结束指定进程（仅支持结束本进程）。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ProcessManager-kill(signal: number, pid: number): boolean--><!--Device-ProcessManager-kill(signal: number, pid: number): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| signal | number | Yes | 发送特定的信号给目标进程。取值范围：1 <= signal <= 64。 |
| pid | number | Yes | 进程的 id。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 信号是否发送成功。如果信号发送成功则返回 true； 否则返回 false。 |

## Examples

```TypeScript
let pro = new process.ProcessManager();
let pres = process.pid;
let result = pro.kill(28, pres);
```

