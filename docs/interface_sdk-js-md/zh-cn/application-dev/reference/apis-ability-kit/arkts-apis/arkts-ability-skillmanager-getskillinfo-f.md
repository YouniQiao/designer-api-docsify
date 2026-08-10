# getSkillInfo

## 导入模块

```TypeScript
import { skillManager } from 'kits/@kit.AbilityKit';
```

## getSkillInfo

```TypeScript
function getSkillInfo(bundleName: string, moduleName: string, skillName: string,
    flags: int, userId?: int): Promise<SkillInfo>
```

获取指定应用中指定模块下指定名称的技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**需要权限：** ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-skillManager-function getSkillInfo(bundleName: string, moduleName: string, skillName: string,    flags: int, userId?: int): Promise<SkillInfo>--><!--Device-skillManager-function getSkillInfo(bundleName: string, moduleName: string, skillName: string,    flags: int, userId?: int): Promise<SkillInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 指定查询应用的包名。 |
| moduleName | string | 是 | 指定查询技能所属模块的名称。 |
| skillName | string | 是 | 指定查询技能的名称。 |
| flags | int | 是 | { |
| userId | int | 否 | 指定查询的用户ID，可以通过getOsAccountLocalId获取。默认值：调用方所在用户。取值范围：大于等于0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;SkillInfo&gt; | Promise对象，返回指定技能的SkillInfo。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 17700093 | The specified skillName is not found. |
| 201 | Permission denied. |
| 17700004 | The specified user ID is not found. |
| 17700002 | The specified module is not found. |
| 17700001 | The specified bundleName is not found. |

