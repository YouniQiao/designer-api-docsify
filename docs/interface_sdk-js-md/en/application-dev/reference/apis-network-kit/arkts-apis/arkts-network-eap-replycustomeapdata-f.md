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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function replyCustomEapData(result: CustomResult, data: EapData): void--><!--Device-eap-function replyCustomEapData(result: CustomResult, data: EapData): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [CustomResult](arkts-network-eap-customresult-e.md) | Yes | Indicates the result of custom authentication. |
| data | [EapData](arkts-network-eap-eapdata-i.md) | Yes | Indicates eap packet data after customization. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [33200009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200009-netmanager-not-exist) | netmanager stop |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [33200099](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200099-internal-program-error) | internal error |
| [33200004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200004-invalid-eap-result-value) | Invalid result |
| [33200005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-eap.md#33200005-invalid-data-length) | Invalid size of eap data |

