# getWant（系统接口）

## 导入模块

```TypeScript
import { wantAgent, WantAgent } from '@kit.AbilityKit';
```

## getWant

```TypeScript
function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void
```

获取WantAgent对象的want。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000007](../errorcode-ability.md#16000007-服务未响应) |
| [16000015](../errorcode-ability.md#16000015-服务超时) |
| [16000151](../errorcode-ability.md#16000151-无效wantagent对象) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { wantAgent, WantAgent as _WantAgent, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 用于存储创建的WantAgent实例
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
  wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// 创建WantAgent实例的回调函数
let getWantAgentCallback = (err: BusinessError, data: _WantAgent) => {
  if (err) {
    console.error(`getWantAgent failed, code: ${err.code}, message: ${err.message}`);
  } else {
    wantAgentData = data;
  }
  // 获取Want数据的回调函数
  let getWantCallback = (err: BusinessError, data: Want) => {
    if (err.code) {
      console.error(`Failed to getWant. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`getWant success, data: ${JSON.stringify(data)}.`);
    }
  }
  try {
    // 获取WantAgent对象的Want数据
    wantAgent.getWant(wantAgentData, getWantCallback);
  } catch(err) {
    let code = (err as BusinessError).code;
    let msg = (err as BusinessError).message;
    console.error(`getWant failed, code: ${code}, message: ${msg}.`);
  }
}

try {
  // 创建WantAgent实例
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch(err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`getWantAgent failed, code: ${code}, message: ${msg}.`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { wantAgent, WantAgent as _WantAgent, Want } from '@kit.AbilityKit';
import { BusinessError, RecordData } from '@kit.BasicServicesKit';

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
  wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError | null, data: _WantAgent | undefined) => {
    if (err) {
      console.error(`getWantAgent failed, code: ${err.code}, message: ${err.message}`);
      return;
    }

    if (!data) {
      console.error('getWantAgent failed: data is undefined');
      return;
    }

    console.info('getWantAgent success');

    wantAgent.getWant(data, (getWantErr: BusinessError | null, wantData: Want | undefined) => {
      if (getWantErr) {
        console.error(`getWant failed, code: ${getWantErr.code}, message: ${getWantErr.message}`);
      } else if (wantData) {
        console.info(`getWant success, data: ${JSON.stringify(wantData)}`);
      } else {
        console.error('getWant failed: wantData is undefined');
      }
    });
  });
} catch (err) {
  const error = err as BusinessError;
  console.error(`getWantAgent failed, code: ${error.code}, message: ${error.message}`);
}
```

ArkTS-Dyn示例：

```TypeScript
import { wantAgent, WantAgent as _WantAgent, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 用于存储创建的WantAgent实例
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
  wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

// 创建WantAgent实例的回调函数
let getWantAgentCallback = (err: BusinessError, data: _WantAgent) => {
  if (err) {
    console.error(`getWantAgent failed, code: ${err.code}, message: ${err.message}`);
  } else {
    wantAgentData = data;
  }
  try {
    // 获取WantAgent对象的Want数据
    wantAgent.getWant(wantAgentData).then((data)=>{
      console.info(`getWant success, data: ${JSON.stringify(data)}`);
    }).catch((err: BusinessError)=>{
      console.error(`getWant failed, code: ${err.code}, message: ${err.message}.`);
    });
  } catch(err){
    let code = (err as BusinessError).code;
    let msg = (err as BusinessError).message;
    console.error(`getWant failed, code: ${code}, message: ${msg}.`);
  }
}

try {
  // 创建WantAgent实例
  wantAgent.getWantAgent(wantAgentInfo, getWantAgentCallback);
} catch(err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`getWantAgent failed, code: ${code}, message: ${msg}.`);
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { wantAgent, WantAgent as _WantAgent, Want } from '@kit.AbilityKit';
import { BusinessError, RecordData } from '@kit.BasicServicesKit';

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
  wantAgent.getWantAgent(wantAgentInfo, (err: BusinessError | null, data: _WantAgent | undefined) => {
    if (err) {
      console.error(`getWantAgent failed, code: ${err.code}, message: ${err.message}`);
      return;
    }

    if (!data) {
      console.error('getWantAgent failed: data is undefined');
      return;
    }

    console.info('getWantAgent success');

    wantAgent.getWant(data).then((resData) => {
      console.info(`getWant success, data: ${JSON.stringify(resData)}`);
    }).catch((error) => {
      let err = error as BusinessError;
      console.error(`getWant failed, code: ${err.code}, message: ${err.message}.`);
    });
  });
} catch (err) {
  const error = err as BusinessError;
  console.error(`getWantAgent failed, code: ${error.code}, message: ${error.message}`);
}
```


## getWant

```TypeScript
function getWant(agent: WantAgent): Promise<Want>
```

获取WantAgent对象的want。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000007](../errorcode-ability.md#16000007-服务未响应) |
| [16000015](../errorcode-ability.md#16000015-服务超时) |
| [16000151](../errorcode-ability.md#16000151-无效wantagent对象) |

**示例**

参见 [getWant](#getwant)
