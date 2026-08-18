# getLogFile

## Modules to Import

```TypeScript
```

## getLogFile

```TypeScript
function getLogFile(latestSeconds: number): Array<string>
```

Returns the list of hilog log file paths in the sandbox for the specified recent time period.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-hilog-function getLogFile(latestSeconds: int): Array<string>--><!--Device-hilog-function getLogFile(latestSeconds: int): Array<string>-End-->

**System capability:** SystemCapability.HiviewDFX.HiLog

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| latestSeconds | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Examples**

Obtain the files that have been modified within 5 minutes.

```TypeScript
hilog.setOutputType(hilog.OutputType.SHARE_SANDBOX_WITH_CONSOLE);
hilog.info(0x0001, "testTag", 'sandbox log to share sandbox with console');
hilog.flush();
let logs = hilog.getLogFile(300);
hilog.info(0x0001, "testTag", 'sandbox log files:%{public}s', logs.toString());
```

Sandbox log output.

```TypeScript
05-15 16:57:04.238 40518 40518 I A00001/testTag: sandbox log files:hiapplog.40518.001.20260515-165602.log
```
