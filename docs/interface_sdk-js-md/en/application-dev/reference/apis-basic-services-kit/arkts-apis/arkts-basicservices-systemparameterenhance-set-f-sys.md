# set (System API)

## Modules to Import

```TypeScript
import { systemParameterEnhance } from 'kits/@kit.BasicServicesKit';
```

## set

```TypeScript
function set(key: string, value: string, callback: AsyncCallback<void>): void
```

Sets a value of the specified key. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14700102](../errorcode-system-parameterV9.md#14700102-invalid-system-parameter-value) |
| [14700103](../errorcode-device-info.md#14700103-operation-permission-denied) |
| [14700104](../errorcode-system-parameterV9.md#14700104-internal-system-error-including-out-of-memory-and-deadlock) |


## set

```TypeScript
function set(key: string, value: string): Promise<void>
```

Sets a value of the specified key. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14700102](../errorcode-system-parameterV9.md#14700102-invalid-system-parameter-value) |
| [14700103](../errorcode-device-info.md#14700103-operation-permission-denied) |
| [14700104](../errorcode-system-parameterV9.md#14700104-internal-system-error-including-out-of-memory-and-deadlock) |
