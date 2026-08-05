# getSystemConfig

## getSystemConfig

```TypeScript
function getSystemConfig(name: number): number
```

Obtains the system configuration.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [process.ProcessManager.getSystemConfig](arkts-arkts-process-processmanager-c.md#getsystemconfig)

<!--Device-process-function getSystemConfig(name: number): number--><!--Device-process-function getSystemConfig(name: number): number-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | number | Yes | System configuration parameter name. |

**Return value:**

| Type | Description |
| --- | --- |
| number | System configuration obtained. |

**Example**

```TypeScript
let _SC_ARG_MAX = 0;
let pres = process.getSystemConfig(_SC_ARG_MAX);
```

