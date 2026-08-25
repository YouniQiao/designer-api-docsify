# getSignatureInfo

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getSignatureInfo

```TypeScript
function getSignatureInfo(uid: number): SignatureInfo
```

Obtains the [signature information](arkts-ability-bundleinfo-signatureinfo-i.md) of an application based on the given UID.

**Since:** 18

**Required permissions:** ohos.permission.GET_SIGNATURE_INFO

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
