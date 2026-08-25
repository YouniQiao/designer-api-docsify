# moveMissionsToForeground（系统接口）

## 导入模块

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## moveMissionsToForeground

```TypeScript
function moveMissionsToForeground(missionIds: Array<number>, callback: AsyncCallback<void>): void
```

将指定任务批量切到前台。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionIds | Array & lt;number & gt; | 是 |
| callback | AsyncCallback & lt;void & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |


## moveMissionsToForeground

```TypeScript
function moveMissionsToForeground(missionIds: Array<number>, topMission: number, callback: AsyncCallback<void>): void
```

将指定任务批量切换到前台，并将任务ID等于topMission的任务移动到最顶层。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionIds | Array & lt;number & gt; | 是 |
| topMission | number | 是 |
| callback | AsyncCallback & lt;void & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |


## moveMissionsToForeground

```TypeScript
function moveMissionsToForeground(missionIds: Array<number>, topMission?: number): Promise<void>
```

将指定任务批量切到前台，并将任务ID等于topMission的任务移动到最顶层。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionIds | Array & lt;number & gt; | 是 |
| topMission | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
