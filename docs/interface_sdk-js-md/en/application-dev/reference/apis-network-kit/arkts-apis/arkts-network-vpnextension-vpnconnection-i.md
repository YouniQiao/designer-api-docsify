# VpnConnection

Defines a VPN connection object. Before calling **VpnConnection** APIs, you need to create a VPN connection object by calling **vpnExt.createVpnConnection**.

**Since:** 11

**System capability:** SystemCapability.Communication.NetManager.Vpn

## Modules to Import

```TypeScript
import { vpnExtension } from 'kits/@kit.NetworkKit';
```

## create

```TypeScript
create(config: VpnConfig): Promise<number>
```

Creates a VPN based on the specified configuration. This API uses a promise to return the result.

> **NOTE：**&gt;
> You are advised to call [destroy()](#destroy) or
> [destroy(vpnId: string)](#destroy) to destroy the VPN and clear
> resources when the VPN is not needed.

**Since:** 11

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [VpnConfig](arkts-network-vpnextension-vpnconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2203001](../errorcode-net-vpn.md#2203001-failed-to-create-a-vpn) |
| [2203002](../errorcode-net-vpn.md#2203002-vpn-already-exists) |

## destroy

```TypeScript
destroy(): Promise<void>
```

Destroys a VPN. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |

## destroy

```TypeScript
destroy(vpnId: string): Promise<void>
```

Destroys a VPN based on the specified VPN ID. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| vpnId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19900001](../errorcode-net-vpn.md#19900001-invalid-parameter) |
| [19900002](../errorcode-net-vpn.md#19900002-system-internal-error) |

## generateVpnId

```TypeScript
generateVpnId(): Promise<string>
```

Generates a unique VPN ID. This API uses a promise to return the result.To use the multi-VPN capability of the system, you need to call this API to generate a VPN ID and configure it in **VpnConfig**.

> **NOTE：**&gt;
> Currently, the multi-VPN capability of the system supports only IPv4.

**Since:** 20

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19900001](../errorcode-net-vpn.md#19900001-invalid-parameter) |
| [19900002](../errorcode-net-vpn.md#19900002-system-internal-error) |

## protect

```TypeScript
protect(socketFd: number): Promise<void>
```

Protects sockets against a VPN connection. The data sent through sockets is directly transmitted over the physical network and therefore the traffic does not traverse through the VPN. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| socketFd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |
| [2203004](../errorcode-net-vpn.md#2203004-invalid-descriptor) |

## protectProcessNet

```TypeScript
protectProcessNet(): Promise<void>
```

Protects application processes against a VPN connection. The data sent through the protected processes is transmitted over the physical network without traversing the VPN. This API uses a promise to return the result.

**Since:** 22

**System capability:** SystemCapability.Communication.NetManager.Vpn

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
