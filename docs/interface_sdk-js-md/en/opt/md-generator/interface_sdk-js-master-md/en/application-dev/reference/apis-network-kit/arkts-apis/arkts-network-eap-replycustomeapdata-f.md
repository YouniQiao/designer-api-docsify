# replyCustomEapData

## Modules to Import

```TypeScript
import { eap } from '@kit.NetworkKit';
```

## replyCustomEapData

```TypeScript
function replyCustomEapData(result: CustomResult, data: EapData): void
```

send Customized eap packets to system

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function replyCustomEapData(result: CustomResult, data: EapData): void--><!--Device-eap-function replyCustomEapData(result: CustomResult, data: EapData): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | [CustomResult](arkts-network-eap-customresult-e.md) | Yes |
| data | [EapData](arkts-network-eap-eapdata-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [33200009](../errorcode-net-eap.md#33200009-netmanager-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [33200099](../errorcode-net-eap.md#33200099-internal-program-error) |
| [33200004](../errorcode-net-eap.md#33200004-invalid-eap-result-value) |
| [33200005](../errorcode-net-eap.md#33200005-invalid-data-length) |
