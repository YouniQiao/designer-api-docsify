# offMission（系统接口）

## offMission

```TypeScript
function offMission(listenerId: number, callback: AsyncCallback<void>): void
```

解注册任务状态监听器。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function offMission(listenerId: long, callback: AsyncCallback<void>): void--><!--Device-missionManager-function offMission(listenerId: long, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listenerId | number | 是 |
| callback | AsyncCallback & lt;void & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16300002](../errorcode-ability.md#16300002-指定的任务监听器不存在) |


## offMission

```TypeScript
function offMission(listenerId: number): Promise<void>
```

解注册任务状态监听。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function offMission(listenerId: long): Promise<void>--><!--Device-missionManager-function offMission(listenerId: long): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listenerId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16300002](../errorcode-ability.md#16300002-指定的任务监听器不存在) |
