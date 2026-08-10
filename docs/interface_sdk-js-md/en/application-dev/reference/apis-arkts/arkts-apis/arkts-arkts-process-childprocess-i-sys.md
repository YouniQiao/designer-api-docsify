# ChildProcess (System API)

childprocess 对象可用于创建新的进程。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-process-export interface ChildProcess--><!--Device-process-export interface ChildProcess-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## close

```TypeScript
close(): void
```

关闭目标进程。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-close(): void--><!--Device-ChildProcess-close(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## getErrorOutput

```TypeScript
getErrorOutput(): Promise<Uint8Array>
```

返回子进程的标准错误输出，以 Uint8Array 形式返回直到 EOF。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-getErrorOutput(): Promise<Uint8Array>--><!--Device-ChildProcess-getErrorOutput(): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | 返回子进程的标准错误输出。 |

## getOutput

```TypeScript
getOutput(): Promise<Uint8Array>
```

返回子进程的标准输出，以 Uint8Array 形式返回直到 EOF。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-getOutput(): Promise<Uint8Array>--><!--Device-ChildProcess-getOutput(): Promise<Uint8Array>-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Uint8Array&gt; | 返回子进程的标准输出。 |

## kill

```TypeScript
kill(signal: number | string): void
```

向进程发送信号。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-kill(signal: number | string): void--><!--Device-ChildProcess-kill(signal: number | string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| signal | number \| string | Yes | number 或 string，表示发送的信号。 |

## wait

```TypeScript
wait(): Promise<number>
```

返回 number 表示目标进程的退出码。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-wait(): Promise<number>--><!--Device-ChildProcess-wait(): Promise<number>-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | 返回目标进程的退出码。 |

## exitCode

```TypeScript
readonly exitCode: number
```

返回 exitCode 表示当前子进程的退出码。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-readonly exitCode: number--><!--Device-ChildProcess-readonly exitCode: number-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## killed

```TypeScript
readonly killed: boolean
```

返回 boolean 表示当前进程信号是否发送成功。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-readonly killed: boolean--><!--Device-ChildProcess-readonly killed: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## pid

```TypeScript
readonly pid: number
```

返回 pid 表示当前进程的 pid。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-readonly pid: number--><!--Device-ChildProcess-readonly pid: number-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## ppid

```TypeScript
readonly ppid: number
```

返回 ppid 表示当前子进程的 pid。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-ChildProcess-readonly ppid: number--><!--Device-ChildProcess-readonly ppid: number-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

