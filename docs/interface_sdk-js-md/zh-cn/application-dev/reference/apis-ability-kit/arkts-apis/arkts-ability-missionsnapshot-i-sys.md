# MissionSnapshot（系统接口）

一个任务的任务快照对象，可以通过 [missionManager.getMissionSnapShot](arkts-ability-missionmanager-getmissionsnapshot-f-sys.md) 获取。

**起始版本：** 23

<!--Device-unnamed-export interface MissionSnapshot--><!--Device-unnamed-export interface MissionSnapshot-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

## ability

```TypeScript
ability: ElementName
```

表示该任务的组件信息。

**类型：** [ElementName](arkts-ability-elementname-i.md)

**起始版本：** 23

<!--Device-MissionSnapshot-ability: ElementName--><!--Device-MissionSnapshot-ability: ElementName-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

## snapshot

```TypeScript
snapshot: image.PixelMap
```

表示任务快照。

**类型：** image.PixelMap

**起始版本：** 23

<!--Device-MissionSnapshot-snapshot: image.PixelMap--><!--Device-MissionSnapshot-snapshot: image.PixelMap-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**示例**

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 获取任务快照信息
  missionManager.getMissionInfo('', 1, (error, data) => {
    if (error) {
      // 处理业务逻辑错误
      console.error(`getMissionInfo failed, error.code: ${error.code}, error.message: ${error.message}`);
      return;
    }
    if (!data) {
      console.error('getMissionInfo failed: data is undefined');
      return;
    }

    console.info(`getMissionInfo missionId is: ${data.missionId}`);
    console.info(`getMissionInfo runningState is: ${data.runningState}`);
    console.info(`getMissionInfo lockedState is: ${data.lockedState}`);
    console.info(`getMissionInfo timestamp is: ${data.timestamp}`);
    console.info(`getMissionInfo want is: ${data.want}`);
    console.info(`getMissionInfo label is: ${data.label}`);
    console.info(`getMissionInfo iconPath is: ${data.iconPath}`);
    console.info(`getMissionInfo continuable is: ${data.continuable}`);
    console.info(`getMissionInfo unclearable is: ${data.unclearable}`);

    missionManager.getMissionSnapShot('', data.missionId).then(snapshot => {
      // 执行正常业务
      console.info(`bundleName = ${snapshot.ability.bundleName}`);
    });
  });
} catch (paramError) {
  console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
}
```

