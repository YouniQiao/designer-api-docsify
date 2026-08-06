# getEnvironmentVar

## getEnvironmentVar

```TypeScript
function getEnvironmentVar(name: string): string
```

Obtains the value of an environment variable.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.getEnvironmentVar](arkts-arkts-process-processmanager-c.md#getenvironmentvar)

<!--Device-process-function getEnvironmentVar(name: string): string--><!--Device-process-function getEnvironmentVar(name: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Environment variable name. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Value of the environment variable. |

**Example**

```TypeScript
let pres = process.getEnvironmentVar("PATH");
```

