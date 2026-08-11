# getSkillInfosForSelf

## Modules to Import

```TypeScript
import { skillManager } from 'kits/@kit.AbilityKit';
```

## getSkillInfosForSelf

```TypeScript
function getSkillInfosForSelf(flags: number): Promise<Array<SkillInfo>>
```

Obtains all SkillInfo objects of the calling application.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getSkillInfosForSelf(flags: int): Promise<Array<SkillInfo>>--><!--Device-skillManager-function getSkillInfosForSelf(flags: int): Promise<Array<SkillInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;SkillInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [17700101](../errorcode-bundle.md#17700101-bundle-manager-service-abnormal) |
