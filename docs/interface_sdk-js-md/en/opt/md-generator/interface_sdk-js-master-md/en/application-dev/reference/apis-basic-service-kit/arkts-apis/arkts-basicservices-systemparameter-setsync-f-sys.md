# setSync (System API)

## Modules to Import

```TypeScript
import { systemParameter } from '@kit.BasicServicesKit';
```

## setSync

```TypeScript
function setSync(key: string, value: string): void
```

Sets a value for the specified key.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** setSync

<!--Device-systemParameter-function setSync(key: string, value: string): void--><!--Device-systemParameter-function setSync(key: string, value: string): void-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |

## Examples

```TypeScript
try {
    systemParameter.setSync("test.parameter.key", "default");
} catch(e) {
    console.error("set unexpected error: " + e);
}
```
