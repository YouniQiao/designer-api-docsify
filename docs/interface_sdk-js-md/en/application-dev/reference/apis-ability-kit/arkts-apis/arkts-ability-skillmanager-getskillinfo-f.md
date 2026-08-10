# getSkillInfo

## Modules to Import

```TypeScript
import { skillManager } from 'kits/@kit.AbilityKit';
```

## getSkillInfo

```TypeScript
function getSkillInfo(bundleName: string, moduleName: string, skillName: string,
    flags: int, userId?: int): Promise<SkillInfo>
```

获取指定应用中指定模块下指定名称的技能信息。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getSkillInfo(bundleName: string, moduleName: string, skillName: string,    flags: int, userId?: int): Promise<SkillInfo>--><!--Device-skillManager-function getSkillInfo(bundleName: string, moduleName: string, skillName: string,    flags: int, userId?: int): Promise<SkillInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 指定查询应用的包名。 |
| moduleName | string | Yes | 指定查询技能所属模块的名称。 |
| skillName | string | Yes | 指定查询技能的名称。 |
| flags | int | Yes | { |
| userId | int | No | 指定查询的用户ID，可以通过getOsAccountLocalId获取。默认值：调用方所在用户。取值范围：大于等于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SkillInfo&gt; | Promise对象，返回指定技能的SkillInfo。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700093 | The specified skillName is not found. |
| 201 | Permission denied. |
| 17700004 | The specified user ID is not found. |
| 17700002 | The specified module is not found. |
| 17700001 | The specified bundleName is not found. |

