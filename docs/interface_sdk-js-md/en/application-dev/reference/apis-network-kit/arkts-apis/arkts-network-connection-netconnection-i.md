# NetConnection

Represents the network connection object type.

> **NOTE：**&gt;
> (1) When the network transitions from unavailable to available, the **netAvailable**, **netCapabilitiesChange**,
> and **netConnectionPropertiesChange** events are triggered.&gt;
> (2) If the network transitions from available to unavailable after a **netAvailable** event is received, a
> **netLost** event is triggered.&gt;
> (3) If no **netAvailable** event is received, a **netUnavailable** event is directly triggered.&gt;
> (4) When the network transitions from Wi-Fi to cellular, a **netLost** event is first triggered to indicate that
> the Wi-Fi network is lost and then a **netAvailable** event is triggered to indicate that the cellular network is
> available.

**Since:** 8

**System capability:** SystemCapability.Communication.NetManager.Core

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## on('netAvailable')

```TypeScript
on(type: 'netAvailable', callback: Callback<NetHandle>): void
```

Registers a listener for **netAvailable** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netAvailable' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetHandle&gt; | Yes |

## on('netBlockStatusChange')

```TypeScript
on(type: 'netBlockStatusChange', callback: Callback<NetBlockStatusInfo>): void
```

Registers a listener for **netBlockStatusChange** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Since:** 8

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netBlockStatusChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetBlockStatusInfo](arkts-network-connection-netblockstatusinfo-i.md)&gt; | Yes |

## on('netCapabilitiesChange')

```TypeScript
on(type: 'netCapabilitiesChange', callback: Callback<NetCapabilityInfo>): void
```

Registers a listener for **netCapabilitiesChange** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netCapabilitiesChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetCapabilityInfo](arkts-network-connection-netcapabilityinfo-i.md)&gt; | Yes |

## on('netConnectionPropertiesChange')

```TypeScript
on(type: 'netConnectionPropertiesChange', callback: Callback<NetConnectionPropertyInfo>): void
```

Registers a listener for **netConnectionPropertiesChange** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Since:** 8

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netConnectionPropertiesChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetConnectionPropertyInfo](arkts-network-connection-netconnectionpropertyinfo-i.md)&gt; | Yes |

## on('netLost')

```TypeScript
on(type: 'netLost', callback: Callback<NetHandle>): void
```

Registers a listener for **netLost** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netLost' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetHandle&gt; | Yes |

## on('netUnavailable')

```TypeScript
on(type: 'netUnavailable', callback: Callback<void>): void
```

Registers a listener for **netUnavailable** events. Before you call this API, make sure that you have called **register** to add a listener for network status changes. When the listener is no longer needed, call **unregister** to remove it.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netUnavailable' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## register

```TypeScript
register(callback: AsyncCallback<void>): void
```

Registers a listener for network status changes. To listen for a specific type of events, call **on** to enable listening and then call **register** to register an event listener.

> **NOTE：**&gt;
> After using the **register** API, you need to call **unregister** to deregister the listener.
> **Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 8

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2101008](../errorcode-net-connection.md#2101008-callback-already-exists) |
| [2101022](../errorcode-net-connection.md#2101022-number-of-requests-exceeding-the-maximum) |

## unregister

```TypeScript
unregister(callback: AsyncCallback<void>): void
```

Unregisters the listener for network status changes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2101007](../errorcode-net-connection.md#2101007-callback-not-exist) |
