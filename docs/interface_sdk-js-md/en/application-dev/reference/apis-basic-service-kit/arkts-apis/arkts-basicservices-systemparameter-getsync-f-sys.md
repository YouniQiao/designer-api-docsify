# getSync (System API)

## Modules to Import

```TypeScript
import { systemParameter } from 'kits/@kit.BasicServicesKit';
```

## getSync

```TypeScript
function getSync(key: string, def?: string): string
```

Obtains a value of the specified key.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.systemParameterEnhance.getSync

<!--Device-systemParameter-function getSync(key: string, def?: string): string--><!--Device-systemParameter-function getSync(key: string, def?: string): string-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be queried. |
| def | string | No | Default value of the system parameter.&lt;br&gt; It works only when the system parameter does not exist.&lt;br&gt;The value can be **undefined** or any custom value. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Value of the system parameter. &lt;br&gt; If the specified key exists, the set value is returned. &lt;br&gt; If the specified key does not exist and **def** is set to a valid value, the set value is returned. If the specified key does not exist and **def** is set to an invalid value (such as **undefined**) or is not set, an empty string is returned. |

