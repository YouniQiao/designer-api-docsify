# acquireShareData（系统接口）

## 导入模块

```TypeScript
```

## acquireShareData

```TypeScript
function acquireShareData(missionId: number, callback: AsyncCallback<Record<string, Object>>): void
```

系统弹框通过该接口发起原子化服务分享，触发目标UIAbility的 [onShare](arkts-ability-app-ability-uiability-uiability-c.md#onshare)回调并返回分享数据。使用 callback异步回调。

**起始版本：** 10

<!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, Object>>): void--><!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, Object>>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Record&lt;string, Object&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## acquireShareData

```TypeScript
function acquireShareData(missionId: number, callback: AsyncCallback<Record<string, RecordData>>): void
```

系统弹框通过该接口发起原子化服务分享，调用到目标UIAbility的onShare，返回分享数据。使用callback异步回调。

**起始版本：** 23

<!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, RecordData>>): void--><!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, RecordData>>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Record&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## acquireShareData

```TypeScript
function acquireShareData(missionId: number): Promise<Record<string, Object>>
```

系统弹框通过该接口发起原子化服务分享，触发目标UIAbility的 [onShare](arkts-ability-app-ability-uiability-uiability-c.md#onshare)回调并返回分享数据。使用 Promise异步回调。

**起始版本：** 10

<!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, Object>>--><!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, Object>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;{ [key: string]: Object |
| Promise & lt;Record & lt;string, Object & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## acquireShareData

```TypeScript
function acquireShareData(missionId: number): Promise<Record<string, RecordData>>
```

系统弹框通过该接口发起原子化服务分享，调用到目标UIAbility的onShare，返回分享数据。使用Promise异步回调。

**起始版本：** 23

<!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, RecordData>>--><!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, RecordData>>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Record&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
