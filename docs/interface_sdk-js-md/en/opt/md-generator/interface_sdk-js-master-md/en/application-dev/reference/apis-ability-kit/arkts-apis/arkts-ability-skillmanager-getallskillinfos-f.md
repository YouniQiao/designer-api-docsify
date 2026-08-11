# getAllSkillInfos

## Modules to Import

```TypeScript
import { skillManager } from 'kits/@kit.AbilityKit';
```

## getAllSkillInfos

```TypeScript
function getAllSkillInfos(flags: number, userId?: number): Promise<Array<SkillInfo>>
```

Obtains all SkillInfo objects installed on the device.To query information for other local accounts, the permission ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS must additionally be granted.

**Since:** 26.0.0

**Required permissions:** ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getAllSkillInfos(flags: int, userId?: int): Promise<Array<SkillInfo>>--><!--Device-skillManager-function getAllSkillInfos(flags: int, userId?: int): Promise<Array<SkillInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flags | number | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;SkillInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
