# newSEService

## Modules to Import

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
```

## newSEService('serviceState')

```TypeScript
function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService
```

Creates an **SEService** instance for connecting to all available SEs in the system. The connection is time- consuming. Therefore, this API supports only the asynchronous mode. This API uses an asynchronous callback to return the result.The returned **SEService** instance is available only when **true** is returned by the specified callback or [isConnected](arkts-connectivity-omapi-seservice-i.md#isconnected).

> **NOTE：**&gt;
> This API is supported since API version 10 and deprecated since API version 12. Use
> [createService](arkts-connectivity-omapi-createservice-f.md) instead.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Deprecated since:** 12

**Substitutes:** [createService](arkts-connectivity-omapi-createservice-f.md)

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'serviceState' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ServiceState](arkts-connectivity-omapi-servicestate-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SEService](arkts-connectivity-omapi-seservice-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

**Examples**

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let seService : omapi.SEService;

function secureElementDemo() {
    // Obtain the service.
    try {
        seService = omapi.newSEService("serviceState", (state) => {
        hilog.info(0x0000, 'testTag', 'se service state = %{public}s', JSON.stringify(state));
        });
    } catch (error) {
        hilog.error(0x0000, 'testTag', 'newSEService error %{public}s', JSON.stringify(error));
    }
    if (seService == undefined || !seService.isConnected()) {
        hilog.error(0x0000, 'testTag', 'secure element service disconnected.');
        return;
    }
}
```
