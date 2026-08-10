# getSkillInfoForSelf

## Modules to Import

```TypeScript
import { skillManager } from 'kits/@kit.AbilityKit';
```

## getSkillInfoForSelf

```TypeScript
function getSkillInfoForSelf(moduleName: string, skillName: string, flags: int): Promise<SkillInfo>
```

获取本应用中指定模块下指定名称的技能信息。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getSkillInfoForSelf(moduleName: string, skillName: string, flags: int): Promise<SkillInfo>--><!--Device-skillManager-function getSkillInfoForSelf(moduleName: string, skillName: string, flags: int): Promise<SkillInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 指定查询技能所属模块的名称。 |
| skillName | string | Yes | 指定查询技能的名称。 |
| flags | int | Yes | { |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SkillInfo&gt; | Promise对象，返回指定技能的SkillInfo。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700093 | The specified skillName is not found. |
| 17700002 | The specified module is not found. |

