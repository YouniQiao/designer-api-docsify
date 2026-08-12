# getSkillInfoForSelf

## Modules to Import

```TypeScript
import { skillManager } from '@kit.AbilityKit';
```

## getSkillInfoForSelf

```TypeScript
function getSkillInfoForSelf(moduleName: string, skillName: string, flags: number): Promise<SkillInfo>
```

Obtains SkillInfo of the calling application based on moduleName and skillName.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getSkillInfoForSelf(moduleName: string, skillName: string, flags: int): Promise<SkillInfo>--><!--Device-skillManager-function getSkillInfoForSelf(moduleName: string, skillName: string, flags: int): Promise<SkillInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| moduleName | string | Yes |
| [skillName](arkts-ability-skillinfo-i.md) | string | Yes |
| flags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SkillInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 17700093 |
| [17700002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700002-module-name-does-not-exist) |
