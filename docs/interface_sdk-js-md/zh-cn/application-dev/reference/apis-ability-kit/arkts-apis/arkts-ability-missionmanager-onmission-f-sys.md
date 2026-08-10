# onMission（系统接口）

## 导入模块

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## onMission

```TypeScript
function onMission(listener: MissionListener): long
```

注册系统任务状态监听器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function onMission(listener: MissionListener): long--><!--Device-missionManager-function onMission(listener: MissionListener): long-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [MissionListener](arkts-ability-missionmanager-missionlistener-t-sys.md) | 是 | 系统任务监听器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 监听器的index值，由系统创建，在注册系统任务状态监听时分配，和监听器一一对应 。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

