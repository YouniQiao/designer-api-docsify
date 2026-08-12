# initialize

## Modules to Import

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
```

## initialize

```TypeScript
function initialize(): void
```

Initializes the connected NFC tag.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-connectedTag-function initialize(): void--><!--Device-connectedTag-function initialize(): void-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [3200101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-connectivity-kit/errorcode-nfc.md#3200101-abnormal-active-nfc-tag-status) | Connected NFC tag running state is abnormal in service. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

