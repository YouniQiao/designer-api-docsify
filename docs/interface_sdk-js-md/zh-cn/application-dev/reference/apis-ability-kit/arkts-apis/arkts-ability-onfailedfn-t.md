# OnFailedFn

```TypeScript
type OnFailedFn = (code: int) => void
```

与指定的后台服务建立连接失败时，会触发该回调，返回连接失败的错误码。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | int | 是 |

**示例**

ArkTS-Sta示例：

```TypeScript
'use static'
import { UIAbility, common, Want, AbilityConstant } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import rpc from '@ohos.rpc';

let connectWant: Want = {
  bundleName: 'com.example.myapp',
  abilityName: 'MyAbility'
};

let connectOptions: common.ConnectOptions = {
  onConnect: (elementName: bundleManager.ElementName, remote: rpc.IRemoteObject): void => {
    console.info(`onConnect elementName: ${JSON.stringify(elementName)}`);
  },
  onDisconnect: (elementName: bundleManager.ElementName): void => {
    console.info(`onDisconnect elementName: ${JSON.stringify(elementName)}`);
  },
  onFailed: (code: int): void => {
    console.error(`onFailed code: ${code}`);
  }
};

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let connection = this.context.connectServiceExtensionAbility(connectWant, connectOptions);
  }
}
```
