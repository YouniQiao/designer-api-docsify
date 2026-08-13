# onMission（系统接口）

## onMission

```TypeScript
function onMission(listener: MissionListener): number
```

注册系统任务状态监听器。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function onMission(listener: MissionListener): long--><!--Device-missionManager-function onMission(listener: MissionListener): long-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listener | [MissionListener](arkts-ability-missionmanager-missionlistener-t-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
