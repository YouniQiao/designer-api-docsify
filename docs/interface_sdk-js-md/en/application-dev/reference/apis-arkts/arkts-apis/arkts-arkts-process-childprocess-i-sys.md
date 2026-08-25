# ChildProcess (System API)

The childprocess object can be used to create a new process.

**Since:** 7

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

Close the target process

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## getErrorOutput

```TypeScript
getErrorOutput(): Promise<Uint8Array>
```

Return it as 'Uint8Array of the stderr until EOF

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

## getOutput

```TypeScript
getOutput(): Promise<Uint8Array>
```

Return it as 'Uint8Array' of the stdout until EOF

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Uint8Array & gt; |

## kill

```TypeScript
kill(signal: number | string): void
```

Send a signal to process

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [signal](arkts-arkts-locks-asynclockoptions-c.md) | number \| string | Yes |

## wait

```TypeScript
wait(): Promise<number>
```

Return 'number' is the target process exit code

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## exitCode

```TypeScript
readonly exitCode: number
```

Return exitCode is the exit code of the current child process

**Type:** number

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## killed

```TypeScript
readonly killed: boolean
```

Return boolean is whether the current process signal is sent successfully

**Type:** boolean

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## pid

```TypeScript
readonly pid: number
```

Return pid is the pid of the current process

**Type:** number

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

## ppid

```TypeScript
readonly ppid: number
```

Return ppid is the pid of the current child process

**Type:** number

**Since:** 7

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.
