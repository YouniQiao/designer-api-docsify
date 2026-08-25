# getInsightIntentInfoByFilter（系统接口）

## 导入模块

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## getInsightIntentInfoByFilter

```TypeScript
function getInsightIntentInfoByFilter(filter: InsightIntentInfoFilter): Promise<Array<InsightIntentInfo>>
```

Obtains the intent information on the current device based on the given intent filter. This API uses a promise to return the result.If the user ID of the calling application is different from the user ID of the intent, the

**起始版本：** 23

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [InsightIntentInfoFilter](arkts-ability-insightintentdriver-insightintentinfofilter-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
