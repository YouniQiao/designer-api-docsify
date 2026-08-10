# getAllSkillInfos

## Modules to Import

```TypeScript
import { skillManager } from 'kits/@kit.AbilityKit';
```

## getAllSkillInfos

```TypeScript
function getAllSkillInfos(flags: int, userId?: int): Promise<Array<SkillInfo>>
```

获取设备上安装应用的所有技能信息。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getAllSkillInfos(flags: int, userId?: int): Promise<Array<SkillInfo>>--><!--Device-skillManager-function getAllSkillInfos(flags: int, userId?: int): Promise<Array<SkillInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| flags | int | Yes | { |
| userId | int | No | 指定查询的用户ID，可以通过getOsAccountLocalId获取。默认值：调用方所在用户。取值范围：大于等于0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;SkillInfo&gt;&gt; | Promise对象，返回所有应用的技能信息数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 17700004 | The specified user ID is not found. |

