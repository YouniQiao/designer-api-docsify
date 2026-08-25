# setIfaceConfig (System API)

## Modules to Import

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## setIfaceConfig

```TypeScript
function setIfaceConfig(iface: string, ic: InterfaceConfiguration, callback: AsyncCallback<void>): void
```

Sets the network interface configuration information. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iface | string | Yes |
| ic | [InterfaceConfiguration](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| 2201004 |
| [2201005](../errorcode-net-ethernet.md#2201005-device-information-not-exist) |
| [2201006](../errorcode-net-ethernet.md#2201006-device-not-connected) |
| [2201007](../errorcode-net-ethernet.md#2201007-failed-to-write-the-user-configuration) |


## setIfaceConfig

```TypeScript
function setIfaceConfig(iface: string, ic: InterfaceConfiguration): Promise<void>
```

Sets the network interface configuration information. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iface | string | Yes |
| ic | [InterfaceConfiguration](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| 2201004 |
| [2201005](../errorcode-net-ethernet.md#2201005-device-information-not-exist) |
| [2201006](../errorcode-net-ethernet.md#2201006-device-not-connected) |
| [2201007](../errorcode-net-ethernet.md#2201007-failed-to-write-the-user-configuration) |
