# ConnectOptions

在连接指定的后台服务时作为入参，用于接收连接过程中的状态变化，如作为 [connectServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#connectserviceextensionability) 的入参，连接指定的ServiceExtensionAbility。

**起始版本：** 23

<!--Device-unnamed-export interface ConnectOptions--><!--Device-unnamed-export interface ConnectOptions-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onConnect

```TypeScript
onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void
```

建立连接时的回调函数。

**起始版本：** 7

<!--Device-ConnectOptions-onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void--><!--Device-ConnectOptions-onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |
| [remote](../../apis-driver-development-kit/arkts-apis/arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md) | rpc.IRemoteObject | 是 |

**示例**

```TypeScript
import { UIAbility, common, Want, AbilityConstant } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectWant: Want = {
  bundleName: 'com.example.myapp',
  abilityName: 'MyAbility'
};

let connectOptions: common.ConnectOptions = {
  onConnect(elementName: bundleManager.ElementName, remote: rpc.IRemoteObject) {
    console.info(`onConnect elementName: ${elementName}`);
  },
  onDisconnect(elementName: bundleManager.ElementName) {
    console.info(`onDisconnect elementName: ${elementName}`);
  },
  onFailed(code: number) {
    console.error(`onFailed code: ${code}`);
  }
};

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let connection: number = this.context.connectServiceExtensionAbility(connectWant, connectOptions);
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(elementName: ElementName): void
```

断开连接时的回调函数。

**起始版本：** 7

<!--Device-ConnectOptions-onDisconnect(elementName: ElementName): void--><!--Device-ConnectOptions-onDisconnect(elementName: ElementName): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | 是 |

**示例**

```TypeScript
import { UIAbility, common, Want, AbilityConstant } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectWant: Want = {
  bundleName: 'com.example.myapp',
  abilityName: 'MyAbility'
};

let connectOptions: common.ConnectOptions = {
  onConnect(elementName: bundleManager.ElementName, remote: rpc.IRemoteObject) {
    console.info(`onConnect elementName: ${elementName}`);
  },
  onDisconnect(elementName: bundleManager.ElementName) {
    console.info(`onDisconnect elementName: ${elementName}`);
  },
  onFailed(code: number) {
    console.error(`onFailed code: ${code}`);
  }
};

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let connection: number = this.context.connectServiceExtensionAbility(connectWant, connectOptions);
  }
}
```

## onFailed

```TypeScript
onFailed(code: number): void
```

连接失败时的回调函数。

**起始版本：** 7

<!--Device-ConnectOptions-onFailed(code: number): void--><!--Device-ConnectOptions-onFailed(code: number): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

**示例**

```TypeScript
import { UIAbility, common, Want, AbilityConstant } from '@kit.AbilityKit';
import { bundleManager } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectWant: Want = {
  bundleName: 'com.example.myapp',
  abilityName: 'MyAbility'
};

let connectOptions: common.ConnectOptions = {
  onConnect(elementName: bundleManager.ElementName, remote: rpc.IRemoteObject) {
    console.info(`onConnect elementName: ${elementName}`);
  },
  onDisconnect(elementName: bundleManager.ElementName) {
    console.info(`onDisconnect elementName: ${elementName}`);
  },
  onFailed(code: number) {
    console.error(`onFailed code: ${code}`);
  }
};

class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let connection: number = this.context.connectServiceExtensionAbility(connectWant, connectOptions);
  }
}
```

## onConnect

```TypeScript
onConnect: OnConnectFn
```

与指定的后台服务成功建立连接时，会触发该回调。

**类型：** [OnConnectFn](arkts-ability-onconnectfn-t.md)

**起始版本：** 23

<!--Device-ConnectOptions-onConnect: OnConnectFn--><!--Device-ConnectOptions-onConnect: OnConnectFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onDisconnect

```TypeScript
onDisconnect: OnDisconnectFn
```

与指定的后台服务成功断开连接时，会触发该回调。

**类型：** [OnDisconnectFn](arkts-ability-ondisconnectfn-t.md)

**起始版本：** 23

<!--Device-ConnectOptions-onDisconnect: OnDisconnectFn--><!--Device-ConnectOptions-onDisconnect: OnDisconnectFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onFailed

```TypeScript
onFailed: OnFailedFn
```

与指定的后台服务建立连接失败时，会触发该回调。

**类型：** [OnFailedFn](arkts-ability-onfailedfn-t.md)

**起始版本：** 23

<!--Device-ConnectOptions-onFailed: OnFailedFn--><!--Device-ConnectOptions-onFailed: OnFailedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
