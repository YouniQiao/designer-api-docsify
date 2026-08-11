# registerMissionListener（系统接口）

## registerMissionListener

```TypeScript
function registerMissionListener(listener: MissionListener): number
```

注册系统任务状态监听器。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** ohos.app.ability.missionManager/missionManager#on

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function registerMissionListener(listener: MissionListener): number--><!--Device-missionManager-function registerMissionListener(listener: MissionListener): number-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| listener | [MissionListener](arkts-ability-missionlistener-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
import missionManager from '@ohos.application.missionManager';

console.info('registerMissionListener');
// 注册系统任务状态监听器
let listenerId = missionManager.registerMissionListener({
  onMissionCreated: (mission) => {
    console.info('--------onMissionCreated-------');
  },
  onMissionDestroyed: (mission) => {
    console.info('--------onMissionDestroyed-------');
  },
  onMissionSnapshotChanged: (mission) => {
    console.info('--------onMissionSnapshotChanged-------');
  },
  onMissionMovedToFront: (mission) => {
    console.info('--------onMissionMovedToFront-------');
  },
  onMissionIconUpdated: (mission, icon) => {
    console.info('--------onMissionIconUpdated-------');
  },
  onMissionClosed: (mission) => {
    console.info('--------onMissionClosed-------');
  },
  onMissionLabelUpdated: (mission) => {
    console.info('--------onMissionLabelUpdated-------');
  }
});
```
