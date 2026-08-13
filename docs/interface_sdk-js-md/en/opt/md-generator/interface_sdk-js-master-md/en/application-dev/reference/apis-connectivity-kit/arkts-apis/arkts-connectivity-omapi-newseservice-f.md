# newSEService

## Modules to Import

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
```

## newSEService

```TypeScript
function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService
```

Establish a new connection that can be used to connect to all the SEs available in the system. The connection process can be quite long, so it happens in an asynchronous way. It is usable only if the specified callback is called or if isConnected() returns true.

**Since:** 10

**Deprecated since:** 12

**Substitutes:** [createService](arkts-connectivity-omapi-createservice-f.md#createService)

<!--Device-omapi-function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService--><!--Device-omapi-function newSEService(type: 'serviceState', callback: Callback<ServiceState>): SEService-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'serviceState' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ServiceState](arkts-connectivity-omapi-servicestate-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SEService](arkts-connectivity-omapi-seservice-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## Examples

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
