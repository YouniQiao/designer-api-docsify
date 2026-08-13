# getSync (System API)

## Modules to Import

```TypeScript
import { systemParameterEnhance } from '@kit.BasicServicesKit';
```

## getSync

```TypeScript
function getSync(key: string, def?: string): string
```

Obtains a value of the specified key. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-systemParameterEnhance-function getSync(key: string, def?: string): string--><!--Device-systemParameterEnhance-function getSync(key: string, def?: string): string-End-->

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

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14700101](../../apis-basic-services-kit/errorcode-system-parameterV9.md#14700101-failure-to-query-the-system-parameter) |
| [14700103](../../apis-basic-services-kit/errorcode-device-info.md#14700103-operation-permission-denied) |
| [14700104](../../apis-basic-services-kit/errorcode-system-parameterV9.md#14700104-internal-system-error-including-out-of-memory-and-deadlock) |

## Examples

```TypeScript
try {
    let info: string = systemParameterEnhance.getSync("const.ohos.apiversion");
    console.info(JSON.stringify(info));
} catch(e) {
    console.error("getSync unexpected error: " + e);
}
```
