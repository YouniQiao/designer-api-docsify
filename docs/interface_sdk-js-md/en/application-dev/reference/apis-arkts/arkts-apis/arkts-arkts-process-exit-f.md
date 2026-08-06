# exit

## exit

```TypeScript
function exit(code: number): void
```

Terminates this process.

Exercise caution when using this API. After this API is called, the application exits. If the input parameter is not 0, data loss or exceptions may occur.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.exit](arkts-arkts-process-processmanager-c.md#exit)

<!--Device-process-function exit(code: number): void--><!--Device-process-function exit(code: number): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | number | Yes | Exit code of the process. |

**Example**

```TypeScript
process.exit(0);
```

