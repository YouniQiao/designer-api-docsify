# getSkillInfo

## Modules to Import

```TypeScript
import { skillManager } from '@kit.AbilityKit';
```

## getSkillInfo

```TypeScript
function getSkillInfo(bundleName: string, moduleName: string, skillName: string,
    flags: number, userId?: number): Promise<SkillInfo>
```

Obtains SkillInfo of a specified application based on bundleName, moduleName and skillName. To query information for other local accounts, the permission ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS must additionally be granted.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getSkillInfo(bundleName: string, moduleName: string, skillName: string,    flags: int, userId?: int): Promise<SkillInfo>--><!--Device-skillManager-function getSkillInfo(bundleName: string, moduleName: string, skillName: string,    flags: int, userId?: int): Promise<SkillInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |
| [skillName](arkts-ability-skillinfo-i.md) | string | Yes |
| flags | number | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SkillInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 17700093 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
