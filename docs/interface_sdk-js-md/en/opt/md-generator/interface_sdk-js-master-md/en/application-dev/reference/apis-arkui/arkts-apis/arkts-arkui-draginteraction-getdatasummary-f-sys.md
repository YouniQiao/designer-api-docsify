# getDataSummary (System API)

## Modules to Import

```TypeScript
```

## getDataSummary

```TypeScript
function getDataSummary(): Array<Summary>
```

Obtains the data summary of all dragged objects.

**Since:** 23

<!--Device-dragInteraction-function getDataSummary(): Array<Summary>--><!--Device-dragInteraction-function getDataSummary(): Array<Summary>-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Summary & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
let summary: Array<dragInteraction.Summary> = dragInteraction.getDataSummary();
console.info(`Drag interaction summary: ${summary}`);
```
