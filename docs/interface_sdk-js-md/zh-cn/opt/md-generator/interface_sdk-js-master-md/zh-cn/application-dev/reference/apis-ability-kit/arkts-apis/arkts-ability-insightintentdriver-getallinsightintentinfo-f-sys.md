# getAllInsightIntentInfo（系统接口）

## getAllInsightIntentInfo

```TypeScript
function getAllInsightIntentInfo(intentFlags: number): Promise<Array<InsightIntentInfo>>
```

查询当前设备上的所有意图信息。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-insightIntentDriver-function getAllInsightIntentInfo(intentFlags: int): Promise<Array<InsightIntentInfo>>--><!--Device-insightIntentDriver-function getAllInsightIntentInfo(intentFlags: int): Promise<Array<InsightIntentInfo>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [intentFlags](arkts-ability-insightintentdriver-insightintentinfofilter-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[InsightIntentInfo](arkts-ability-insightintentdriver-insightintentinfo-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
