# resolveLocalService

## Modules to Import

```TypeScript
import { mdns } from 'kits/@kit.NetworkKit';
```

## resolveLocalService

```TypeScript
function resolveLocalService(context: Context, serviceInfo: LocalServiceInfo,
                               callback: AsyncCallback<LocalServiceInfo>): void
```

Resolves an MDNS service. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.MDNS

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| [serviceInfo](arkts-network-mdns-discoveryeventinfo-i.md) | [LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2204003](../errorcode-net-mdns.md#2204003-repeated-registration) |
| [2204006](../errorcode-net-mdns.md#2204006-service-resolution-timeout) |
| [2204010](../errorcode-net-mdns.md#2204010-message-sending-failure) |


## resolveLocalService

```TypeScript
function resolveLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>
```

Resolves an MDNS service. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.MDNS

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| [serviceInfo](arkts-network-mdns-discoveryeventinfo-i.md) | [LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[LocalServiceInfo](arkts-network-mdns-localserviceinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2204003](../errorcode-net-mdns.md#2204003-repeated-registration) |
| [2204006](../errorcode-net-mdns.md#2204006-service-resolution-timeout) |
| [2204010](../errorcode-net-mdns.md#2204010-message-sending-failure) |
