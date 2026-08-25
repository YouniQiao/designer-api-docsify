# setWantAgentMultithreading（系统接口）

## 导入模块

```TypeScript
import { wantAgent, WantAgent } from '@kit.AbilityKit';
```

## setWantAgentMultithreading

```TypeScript
function setWantAgentMultithreading(isMultithreadingSupported: boolean) : void
```

开启或者关闭WantAgent多线程传递功能。

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isMultithreadingSupported | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { wantAgent, WantAgent as _WantAgent, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义wantAgent对象
let wantAgentData: _WantAgent;
// 定义WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters:
      {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [false, true, false],
        mykey5: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey6: true,
      }
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// 定义getWantAgent回调
let getWantAgentCallback = (err: BusinessError, data: _WantAgent) => {
  if (err) {
    console.error(`Failed to call getWantAgentCallback. Code is ${err.code}. Message is ${err.message}.`);
  } else {
    wantAgentData = data;
  }

  try {
    // 开启WantAgent多线程传递功能
    wantAgent.setWantAgentMultithreading(true);
  } catch (err) {
    let code = (err as BusinessError).code;
    let msg = (err as BusinessError).message;
    console.error(`Failed to set wantAgentMultithreading. Code: ${code}, message: ${msg}`);
  }
}

try {
  // 创建WantAgent实例
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`Failed to get wantAgent. Code: ${code}, message: ${msg}`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { wantAgent, WantAgent as _WantAgent, Want } from '@kit.AbilityKit';
import { BusinessError, RecordData } from '@kit.BasicServicesKit';

// 定义wantAgent对象
let wantAgentData: _WantAgent;
// WantAgentInfo对象
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: 'deviceId',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      action: 'action1',
      entities: ['entity1'],
      type: 'MIMETYPE',
      uri: 'key={true,true,false}',
      parameters: {
        'mykey0': 2222,
        'mykey1': [1, 2, 3],
        'mykey2': '[1, 2, 3]',
        'mykey3': 'ssssssssssssssssssssssssss',
        'mykey4': [false, true, false],
        'mykey5': ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        'mykey6': true,
      } as Record<string, RecordData>
    } as Want
  ],
  actionType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
};

try {
  wantAgent.getWantAgent(wantAgentInfo).then(data => {
    wantAgentData = data;
    try {
      wantAgent.setWantAgentMultithreading(true);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Failed to set wantAgentMultithreading. Code is ${err.code}. Message is ${err.message}.`);
    }
  }).catch((err) => {

  });
} catch (error) {
  let err = error as BusinessError;
  console.error(`Failed to get wantAgent. Code is ${err.code}. Message is ${err.message}.`);
}
```
