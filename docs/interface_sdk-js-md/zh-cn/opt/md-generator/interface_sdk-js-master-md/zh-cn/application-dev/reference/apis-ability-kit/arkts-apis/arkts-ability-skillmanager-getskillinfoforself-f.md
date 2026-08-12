# getSkillInfoForSelf

## getSkillInfoForSelf

```TypeScript
function getSkillInfoForSelf(moduleName: string, skillName: string, flags: number): Promise<SkillInfo>
```

获取本应用中指定模块下指定名称的技能信息。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-skillManager-function getSkillInfoForSelf(moduleName: string, skillName: string, flags: int): Promise<SkillInfo>--><!--Device-skillManager-function getSkillInfoForSelf(moduleName: string, skillName: string, flags: int): Promise<SkillInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| [skillName](arkts-ability-skillinfo-i.md) | string | 是 |
| flags | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;SkillInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [17700093](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700093-指定的skillname不存在) |
| [17700002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700002-指定的modulename不存在) |
