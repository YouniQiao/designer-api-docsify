# getSignatureInfo

## Modules to Import

```TypeScript
```

## getSignatureInfo

```TypeScript
function getSignatureInfo(uid: number): SignatureInfo
```

Obtains the [signature information](arkts-ability-bundleinfo-signatureinfo-i.md#signatureinfo) of an application based on the given UID.

**Since:** 23

**Required permissions:** ohos.permission.GET_SIGNATURE_INFO

<!--Device-bundleManager-function getSignatureInfo(uid: int): SignatureInfo--><!--Device-bundleManager-function getSignatureInfo(uid: int): SignatureInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SignatureInfo](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-signatureinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17700021](../errorcode-bundle.md#17700021-invalid-uid) |

**Examples**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let uid = 20010005; // Replace uid with the UID of the corresponding application.
try {
  let data = bundleManager.getSignatureInfo(uid);
  hilog.info(0x0000, 'testTag', 'getSignatureInfo successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSignatureInfo failed. Cause: %{public}s', message);
}
```
