# ConnectOptions

**ConnectOptions** can be used as an input parameter to receive status changes during the connection to a background service. For example, it is used as an input parameter of [connectServiceExtensionAbility](arkts-ability-uiabilitycontext-c.md#connectServiceExtensionAbility) to connect to a ServiceExtensionAbility.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface ConnectOptions--><!--Device-unnamed-export interface ConnectOptions-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onConnect

```TypeScript
onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void
```

Called when a connection is set up.

**Since:** 7

**Deprecated since:** -1

<!--Device-ConnectOptions-onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void--><!--Device-ConnectOptions-onConnect(elementName: ElementName, remote: rpc.IRemoteObject): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |
| [remote](../../apis-driver-development-kit/arkts-apis/arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md) | rpc.IRemoteObject | Yes |

## Examples

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

Called when a connection is interrupted.

**Since:** 7

**Deprecated since:** -1

<!--Device-ConnectOptions-onDisconnect(elementName: ElementName): void--><!--Device-ConnectOptions-onDisconnect(elementName: ElementName): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elementName | [ElementName](arkts-ability-elementname-i.md) | Yes |

## Examples

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

Called when a connection fails.

**Since:** 7

**Deprecated since:** -1

<!--Device-ConnectOptions-onFailed(code: number): void--><!--Device-ConnectOptions-onFailed(code: number): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | number | Yes |

## Examples

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

Callback invoked when a connection is set up.

**Type:** [OnConnectFn](arkts-ability-onconnectfn-t.md)

**Since:** 23

**Deprecated since:** -1

<!--Device-ConnectOptions-onConnect: OnConnectFn--><!--Device-ConnectOptions-onConnect: OnConnectFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onDisconnect

```TypeScript
onDisconnect: OnDisconnectFn
```

Callback invoked when a connection is interrupted.

**Type:** [OnDisconnectFn](arkts-ability-ondisconnectfn-t.md)

**Since:** 23

**Deprecated since:** -1

<!--Device-ConnectOptions-onDisconnect: OnDisconnectFn--><!--Device-ConnectOptions-onDisconnect: OnDisconnectFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onFailed

```TypeScript
onFailed: OnFailedFn
```

Callback invoked when a connection fails.

**Type:** [OnFailedFn](arkts-ability-onfailedfn-t.md)

**Since:** 23

**Deprecated since:** -1

<!--Device-ConnectOptions-onFailed: OnFailedFn--><!--Device-ConnectOptions-onFailed: OnFailedFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
