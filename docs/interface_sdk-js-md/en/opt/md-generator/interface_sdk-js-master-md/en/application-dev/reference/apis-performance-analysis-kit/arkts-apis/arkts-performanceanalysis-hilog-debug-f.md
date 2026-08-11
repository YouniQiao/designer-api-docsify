# debug

## Modules to Import

```TypeScript
import { hilog } from 'kits/@kit.PerformanceAnalysisKit';
```

## debug

```TypeScript
function debug(domain: number, tag: string, format: string, ...args: any[]): void
```

Prints DEBUG logs.

DEBUG logs are not recorded in official versions by default. They are available in debug versions or in official versions with the debug function enabled.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hilog-function debug(domain: number, tag: string, format: string, ...args: any[]): void--><!--Device-hilog-function debug(domain: number, tag: string, format: string, ...args: any[]): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| domain | number | Yes |
| tag | string | Yes |
| format | string | Yes |
| args | any[] | Yes |

## Examples

This example is used to output a DEBUG log with the format string being "%{public}s World %{private}d". The variable  is a plaintext string, and the variable  is a private integer.

```TypeScript
hilog.debug(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

If "hello" is filled in %{public}s and 3 in %{private}d, the output log is as follows:

```TypeScript
08-05 12:21:47.579  2695-2703  A00001/testTag  com.example.hilogDemo  D     hello World <private>
```
