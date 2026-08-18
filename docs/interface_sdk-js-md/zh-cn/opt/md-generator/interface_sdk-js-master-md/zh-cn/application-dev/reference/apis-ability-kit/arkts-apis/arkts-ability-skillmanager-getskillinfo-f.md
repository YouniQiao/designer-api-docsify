# getSkillInfo

## 导入模块

```TypeScript
```

## getSkillInfo

```TypeScript
function getSkillInfo(bundleName: string, moduleName: string, skillName: string,
    flags: number, userId?: number): Promise<SkillInfo>
```

获取指定应用中指定模块下指定名称的技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-skillManager-function getSkillInfo(bundleName: string, moduleName: string, skillName: string,    flags: int, userId?: int): Promise<SkillInfo>--><!--Device-skillManager-function getSkillInfo(bundleName: string, moduleName: string, skillName: string,    flags: int, userId?: int): Promise<SkillInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| moduleName | string | 是 |
| [skillName](arkts-ability-skillinfo-i.md) | string | 是 |
| flags | number | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;SkillInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17700093](../errorcode-bundle.md#17700093-指定的skillname不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
