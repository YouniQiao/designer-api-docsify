# replyCustomEapData

## Modules to Import

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## replyCustomEapData

```TypeScript
function replyCustomEapData(result: CustomResult, data: EapData): void
```

Notifies the system of the extensible authentication result.

> **NOTE：**&gt;
> - If this callback is used to process received EAP data packets, the customized portion added by the server must
> be removed from the EAP data transmitted to the system.&gt;
> - If this callback is used to process sent EAP data packets, the EAP data transmitted to the system is the EAP
> data with the customized portion added by the server.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | [CustomResult](arkts-network-eap-customresult-e.md) | Yes |
| data | [EapData](arkts-network-eap-eapdata-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [33200004](../errorcode-net-eap.md#33200004-invalid-eap-result-value) |
| [33200005](../errorcode-net-eap.md#33200005-invalid-data-length) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager-not-exist) |
| [33200099](../errorcode-net-eap.md#33200099-internal-program-error) |
