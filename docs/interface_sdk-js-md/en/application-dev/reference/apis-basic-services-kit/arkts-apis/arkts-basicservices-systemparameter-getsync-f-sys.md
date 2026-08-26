# getSync (System API)

## Modules to Import

```TypeScript
import systemParameter from '@kit.BasicServicesKit';
```

## getSync

```TypeScript
function getSync(key: string, def?: string): string
```

Obtains a value of the specified key.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** getSync

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Key to be queried. |
| def | string | No | Default value of the system parameter.It works only when the system parameter does not exist.The value can be **undefined** or any custom value. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Value of the system parameter. |

**Examples**

```TypeScript
try {
    let info: string = systemParameter.getSync("const.ohos.apiversion");
    console.info(JSON.stringify(info));
} catch(e) {
    console.error("getSync unexpected error: " + e);
}
```
