# evictFilePages

## Modules to Import

```TypeScript
```

## evictFilePages

```TypeScript
function evictFilePages(fileNames: Array<string>): Promise<void>
```

Sends a request to the system to release file page cache of specified files. The system determines whether to actually perform the release based on the current memory status, and success is not guaranteed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-appMemoryOptimizer-function evictFilePages(fileNames: Array<string>): Promise<void>--><!--Device-appMemoryOptimizer-function evictFilePages(fileNames: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fileNames | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 16000163 |
