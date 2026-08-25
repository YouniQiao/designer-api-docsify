# moveMissionToFront（系统接口）

## 导入模块

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## moveMissionToFront

```TypeScript
function moveMissionToFront(missionId: number, callback: AsyncCallback<void>): void
```

把指定任务ID的任务切到前台。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |
| callback | AsyncCallback & lt;void & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |


## moveMissionToFront

```TypeScript
function moveMissionToFront(missionId: number, options: StartOptions, callback: AsyncCallback<void>): void
```

把指定任务ID的任务切到前台，同时指定任务切换到前台时的启动参数，例如窗口模式、设备ID等。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 是 |
| callback | AsyncCallback & lt;void & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |


## moveMissionToFront

```TypeScript
function moveMissionToFront(missionId: number, options?: StartOptions): Promise<void>
```

把指定任务ID的任务切到前台，同时指定任务切换到前台时的启动参数，例如窗口模式、设备ID等。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| missionId | number | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

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
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
