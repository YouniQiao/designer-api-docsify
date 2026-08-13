# getSkillInfos

## getSkillInfos

```TypeScript
function getSkillInfos(bundleName: string, flags: number, userId?: number): Promise<Array<SkillInfo>>
```

获取指定应用的所有技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_SKILL_PRIVILEGE or ohos.permission.MANAGE_SKILL

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-skillManager-function getSkillInfos(bundleName: string, flags: int, userId?: int): Promise<Array<SkillInfo>>--><!--Device-skillManager-function getSkillInfos(bundleName: string, flags: int, userId?: int): Promise<Array<SkillInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| flags | number | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;SkillInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700004](../errorcode-bundle.md#17700004-指定的用户不存在) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |
