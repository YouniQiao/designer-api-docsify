# startEthEap

## Modules to Import

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## startEthEap

```TypeScript
function startEthEap(netId: number, profile: EthEapProfile): void
```

Starts EAP authentication on an Ethernet NIC.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netId | number | Yes |
| profile | [EthEapProfile](arkts-network-eap-etheapprofile-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [33200001](../errorcode-net-eap.md#33200001-invalid-netid) |
| [33200003](../errorcode-net-eap.md#33200003-invalid-eth-eap-configuration) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager-not-exist) |
| [33200010](../errorcode-net-eap.md#33200010-invalid-eap-status) |
| [33200099](../errorcode-net-eap.md#33200099-internal-program-error) |
