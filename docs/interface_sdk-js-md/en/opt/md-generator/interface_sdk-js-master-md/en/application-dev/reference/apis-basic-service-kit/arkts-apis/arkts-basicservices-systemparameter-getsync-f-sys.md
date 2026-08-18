# getSync (System API)

## Modules to Import

```TypeScript
```

## getSync

```TypeScript
function getSync(key: string, def?: string): string
```

Obtains a value of the specified key.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** getSync

<!--Device-systemParameter-function getSync(key: string, def?: string): string--><!--Device-systemParameter-function getSync(key: string, def?: string): string-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| def | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
try {
    let info: string = systemParameter.getSync("const.ohos.apiversion");
    console.info(JSON.stringify(info));
} catch(e) {
    console.error("getSync unexpected error: " + e);
}
```
