# NetConnection

Represents the network connection handle.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-connection-export interface NetConnection--><!--Device-connection-export interface NetConnection-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## onNetBlockStatusChange

```TypeScript
onNetBlockStatusChange(callback: Callback<NetBlockStatusInfo>): void
```

Registers a listener for netBlockStatusChange events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-NetConnection-onNetBlockStatusChange(callback: Callback<NetBlockStatusInfo>): void--><!--Device-NetConnection-onNetBlockStatusChange(callback: Callback<NetBlockStatusInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetBlockStatusInfo](arkts-network-connection-netblockstatusinfo-i.md)&gt; | Yes | the callback used to return the result. |

## onNetLost

```TypeScript
onNetLost(callback: Callback<NetHandle>): void
```

Registers a listener for **netLost** events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NetConnection-onNetLost(callback: Callback<NetHandle>): void--><!--Device-NetConnection-onNetLost(callback: Callback<NetHandle>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetHandle&gt; | Yes | the callback used to return the result. |

## onNetUnavailable

```TypeScript
onNetUnavailable(callback: Callback<void>): void
```

Registers a listener for netUnavailable events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NetConnection-onNetUnavailable(callback: Callback<void>): void--><!--Device-NetConnection-onNetUnavailable(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback used to return the result. |

## on_netAvailable

```TypeScript
on(type: 'netAvailable', callback: Callback<NetHandle>): void
```

Registers a listener for netAvailable events.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NetConnection-on(type: 'netAvailable', callback: Callback<NetHandle>): void--><!--Device-NetConnection-on(type: 'netAvailable', callback: Callback<NetHandle>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'netAvailable' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetHandle&gt; | Yes | the callback used to return the result. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netAvailable events.
netCon.on('netAvailable', (data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to unsubscribe from netAvailable events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

## on_netBlockStatusChange

```TypeScript
on(type: 'netBlockStatusChange', callback: Callback<NetBlockStatusInfo>): void
```

Registers a listener for netBlockStatusChange events.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-NetConnection-on(type: 'netBlockStatusChange', callback: Callback<NetBlockStatusInfo>): void--><!--Device-NetConnection-on(type: 'netBlockStatusChange', callback: Callback<NetBlockStatusInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'netBlockStatusChange' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetBlockStatusInfo](arkts-network-connection-netblockstatusinfo-i.md)&gt; | Yes | the callback used to return the result. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netBlockStatusChange events.
netCon.on('netBlockStatusChange', (data: connection.NetBlockStatusInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to remove the listener for netBlockStatusChange events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

## on_netCapabilitiesChange

```TypeScript
on(type: 'netCapabilitiesChange', callback: Callback<NetCapabilityInfo>): void
```

Registers a listener for **netCapabilitiesChange** events.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NetConnection-on(type: 'netCapabilitiesChange', callback: Callback<NetCapabilityInfo>): void--><!--Device-NetConnection-on(type: 'netCapabilitiesChange', callback: Callback<NetCapabilityInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'netCapabilitiesChange' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetCapabilityInfo](arkts-network-connection-netcapabilityinfo-i.md)&gt; | Yes | the callback used to return the result. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netCapChange events.
netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Unsubscribe from netCapabilitiesChange events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

## on_netConnectionPropertiesChange

```TypeScript
on(type: 'netConnectionPropertiesChange', callback: Callback<NetConnectionPropertyInfo>): void
```

Registers a listener for netConnectionPropertiesChange events.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

<!--Device-NetConnection-on(type: 'netConnectionPropertiesChange', callback: Callback<NetConnectionPropertyInfo>): void--><!--Device-NetConnection-on(type: 'netConnectionPropertiesChange', callback: Callback<NetConnectionPropertyInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'netConnectionPropertiesChange' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetConnectionPropertyInfo](arkts-network-connection-netconnectionpropertyinfo-i.md)&gt; | Yes | the callback used to return the result. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netConnectionChange events.
netCon.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to remove the listener for netConnectionPropertiesChange events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

## on_netLost

```TypeScript
on(type: 'netLost', callback: Callback<NetHandle>): void
```

Registers a listener for **netLost** events.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NetConnection-on(type: 'netLost', callback: Callback<NetHandle>): void--><!--Device-NetConnection-on(type: 'netLost', callback: Callback<NetHandle>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'netLost' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetHandle&gt; | Yes | the callback used to return the result. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netLost events.
netCon.on('netLost', (data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to remove the listener for netLost events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

## on_netUnavailable

```TypeScript
on(type: 'netUnavailable', callback: Callback<void>): void
```

Registers a listener for netUnavailable events.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NetConnection-on(type: 'netUnavailable', callback: Callback<void>): void--><!--Device-NetConnection-on(type: 'netUnavailable', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'netUnavailable' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback used to return the result. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Create a NetConnection object.
let netCon: connection.NetConnection = connection.createNetConnection();

// Use the on API to enable listening for netUnavailable events.
netCon.on('netUnavailable', () => {
  console.info("Succeeded to get unavailable net event");
});

// Register a listener for network status change events. This API must be called after the on API.
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});

// Use the unregister API to remove the listener for netUnavailable events.
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

## register

```TypeScript
register(callback: AsyncCallback<void>): void
```

Receives status change notifications of a specified network.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NetConnection-register(callback: AsyncCallback<void>): void--><!--Device-NetConnection-register(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of register. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2101008](../errorcode-net-connection.md#2101008-callback-already-exists) | The callback already exists. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2101022](../errorcode-net-connection.md#2101022-number-of-requests-exceeding-the-maximum) | The number of requests exceeded the maximum allowed. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netCon: connection.NetConnection = connection.createNetConnection();
netCon.register((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

## unregister

```TypeScript
unregister(callback: AsyncCallback<void>): void
```

Cancels listening for network status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-NetConnection-unregister(callback: AsyncCallback<void>): void--><!--Device-NetConnection-unregister(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2101007](../errorcode-net-connection.md#2101007-callback-not-exist) | The callback does not exist. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netCon: connection.NetConnection = connection.createNetConnection();
netCon.unregister((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```

