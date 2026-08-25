# getAllDisplays

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAllDisplays

```TypeScript
function getAllDisplays(callback: AsyncCallback<Array<Display>>): void
```

Obtains all Display objects. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Display](arkts-arkui-display-display-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |


## getAllDisplays

```TypeScript
function getAllDisplays(): Promise<Array<Display>>
```

Obtains all Display objects. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Display](arkts-arkui-display-display-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
