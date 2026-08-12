# on

## Modules to Import

```TypeScript
import { omapi } from '@kit.ConnectivityKit';
```

## on('stateChanged')

```TypeScript
function on(type: 'stateChanged', callback: Callback<ServiceState>): void
```

Register the service state changed event.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-omapi-function on(type: 'stateChanged', callback: Callback<ServiceState>): void--><!--Device-omapi-function on(type: 'stateChanged', callback: Callback<ServiceState>): void-End-->

**System capability:** SystemCapability.Communication.SecureElement

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChanged' | Yes | The type to register. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ServiceState](arkts-connectivity-omapi-servicestate-e.md)&gt; | Yes | The callback used to listen for the state change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

