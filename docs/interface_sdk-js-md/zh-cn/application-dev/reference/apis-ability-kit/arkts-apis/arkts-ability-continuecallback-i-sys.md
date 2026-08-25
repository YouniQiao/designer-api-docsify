# ContinueCallback（系统接口）

ContinueCallback registered for notify continue result.@interface ContinueCallback

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

## onContinueDone

```TypeScript
onContinueDone: OnContinueDoneCallback
```

Called by system when continue mission done.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**示例**

ArkTS-Dyn示例:

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 调用continueMission方法，发起任务迁移
distributedMissionManager.continueMission(
  {
    srcDeviceId: '123', // 源设备ID，需通过deviceManager等接口获取
    dstDeviceId: '456', // 目标设备ID，需通过deviceManager等接口获取
    missionId: 123, // 任务ID，需通过distributedMissionManager获取或从其他接口返回
    wantParam: {
      'key': 'value' // 迁移数据
    }
  },
  {
    // 迁移完成回调函数，接收迁移结果
    onContinueDone(result: number) {
      console.info(`onContinueDone, result: ${JSON.stringify(result)}`);
    }
  }, (error: BusinessError) => {
  // 错误处理回调函数
  // 判断是否有错误及错误码
  if (error && error.code) {
    console.error(`continueMission failed, error.code: ${error.code}, error.message: ${error.message}`);
  }
  console.info(`continueMission finished`);
});
```

ArkTS-Sta示例：

```TypeScript
import distributedMissionManager from '@ohos.distributedMissionManager';
import { BusinessError } from '@ohos.base';

// 迁移完成回调函数，接收迁移结果
function onContinueDone(result: int) {
  console.info(`onContinueDone, result: ${JSON.stringify(result)}`);
}
let options:distributedMissionManager.ContinueCallback={
  onContinueDone: onContinueDone
}
let continueDeviceInfo:distributedMissionManager.ContinueDeviceInfo={
  srcDeviceId: '123', // 源设备ID，需通过deviceManager等接口获取
  dstDeviceId: '456', // 目标设备ID，需通过deviceManager等接口获取
  missionId: 123, // 任务ID，需通过distributedMissionManager获取或从其他接口返回
  wantParam: {
    'key': 'value' // 迁移数据
  }
}
// 调用continueMission方法，发起任务迁移
distributedMissionManager.continueMission(
  continueDeviceInfo,
  options,
  (error: BusinessError|null,data:string[]|undefined) => {
  // 错误处理回调函数
  // 判断是否有错误及错误码
  if (error && error.code) {
    console.error(`continueMission failed, error.code: ${error.code}, error.message: ${error.message}`);
  }
  console.info(`continueMission finished`);
});
```
