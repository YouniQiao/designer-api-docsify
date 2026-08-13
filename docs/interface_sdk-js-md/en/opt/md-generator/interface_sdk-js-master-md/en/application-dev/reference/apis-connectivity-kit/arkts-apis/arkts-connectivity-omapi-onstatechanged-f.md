# on_stateChanged

## Modules to Import

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
```

## on_stateChanged

```TypeScript
function on(type: 'stateChanged', callback: Callback<ServiceState>): void
```

Register the service state changed event.

**Since:** 18

**Deprecated since:** -1

<!--Device-omapi-function on(type: 'stateChanged', callback: Callback<ServiceState>): void--><!--Device-omapi-function on(type: 'stateChanged', callback: Callback<ServiceState>): void-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChanged' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ServiceState](arkts-connectivity-omapi-servicestate-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
