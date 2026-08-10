# DriverExtensionAbility

DriverExtensionAbility模块提供驱动相关扩展能力，提供驱动创建、销毁、连接、断开等生命周期回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class DriverExtensionAbility--><!--Device-unnamed-declare class DriverExtensionAbility-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

## Modules to Import

```TypeScript
import { DriverExtensionContext } from 'kits/@kit.DriverDevelopmentKit';
```

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>
```

Extension生命周期回调，会在[onCreate](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-abilitystage-abilitystage-c.md/arkts-ability-app-ability-abilitystage-abilitystage-c.md#oncreate)之后回调。返回一个  
[RemoteObject](../../apis-ipc-kit/arkts-apis/arkts-ipc-rpc-remoteobject-c.md/arkts-ipc-rpc-remoteobject-c.md)对象，用于客户端和服务端进行通信。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DriverExtensionAbility-onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>--><!--Device-DriverExtensionAbility-onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**Return value:**

| Type | Description |
| --- | --- |
| rpc.RemoteObject | 一个RemoteObject对象，用于客户端和服务端进行通信；或一个Promise对象，返回用于通信的 RemoteObject对象。 |

## Examples

```TypeScript
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class StubTest extends rpc.RemoteObject{
    constructor(des : string) {
        super(des);
    }
    onRemoteMessageRequest(code : number, data : rpc.MessageSequence, reply : rpc.MessageSequence, option : rpc.MessageOption) {
      // This interface must be overridden.
      return true;
    }
}
class DriverExt extends DriverExtensionAbility {
  onConnect(want : Want) {
    console.info(`onConnect , want: ${want.abilityName}`);
    return new StubTest('test');
  }
}
```

If the returned [RemoteObject](../apis-ipc-kit/js-apis-rpc.md#remoteobject) object depends on an asynchronous API, you can use the asynchronous lifecycle.

```TypeScript
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class StubTest extends rpc.RemoteObject{
    constructor(des : string) {
        super(des);
    }
    onRemoteMessageRequest(code : number, data : rpc.MessageSequence, reply : rpc.MessageSequence, option : rpc.MessageOption) {
      // This interface must be overridden.
      return true;
    }
}
async function getDescriptor() {
    // Call the asynchronous function.
    return "asyncTest";
}
class DriverExt extends DriverExtensionAbility {
  async onConnect(want : Want) {
    console.info(`onConnect , want: ${want.abilityName}`);
    let descriptor = await getDescriptor();
    return new StubTest(descriptor);
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(want: Want): void | Promise<void>
```

Extension的生命周期回调，客户端执行断开连接服务时回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DriverExtensionAbility-onDisconnect(want: Want): void | Promise<void>--><!--Device-DriverExtensionAbility-onDisconnect(want: Want): void | Promise<void>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

## Examples

```TypeScript
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  onDisconnect(want : Want) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
  }
}
```

After the onDisconnect lifecycle callback is executed, the application may exit. As a result, the asynchronous function in onDisconnect may fail to be executed correctly, for example, asynchronously writing data to the database. The asynchronous lifecycle can be used to ensure that the subsequent lifecycle continues after the asynchronous onDisconnect is complete.

```TypeScript
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  async onDisconnect(want : Want) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
    // Call the asynchronous function.
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(want: Want): undefined | Promise<void>
```

Extension的生命周期回调，客户端执行断开连接服务时回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DriverExtensionAbility-onDisconnect(want: Want): undefined | Promise<void>--><!--Device-DriverExtensionAbility-onDisconnect(want: Want): undefined | Promise<void>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Indicates disconnection information about the driver extension. |

**Return value:**

| Type | Description |
| --- | --- |
| undefined | 返回值为空；或一个Promise对象，无返回结果。 |

## onDump

```TypeScript
onDump(params: Array<string>): Array<string>
```

转储客户端信息时调用，建议不要转储敏感信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DriverExtensionAbility-onDump(params: Array<string>): Array<string>--><!--Device-DriverExtensionAbility-onDump(params: Array<string>): Array<string>-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | Array&lt;string&gt; | Yes | 表示命令形式的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 一个string类型的数组，用于转存客户端信息。 |

## Examples

```TypeScript
class DriverExt extends DriverExtensionAbility {
    onDump(params : Array<string>) {
        console.info(`dump, params: ${JSON.stringify(params)}`);
        return ['params'];
    }
}
```

## onInit

```TypeScript
onInit(want: Want): void
```

Extension生命周期回调，在创建时回调，执行初始化业务逻辑操作。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DriverExtensionAbility-onInit(want: Want): void--><!--Device-DriverExtensionAbility-onInit(want: Want): void-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

## Examples

```TypeScript
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  onInit(want : Want) {
    console.info(`onInit, want: ${want.abilityName}`);
  }
}
```

## onRelease

```TypeScript
onRelease(): void
```

Extension生命周期回调，在销毁时回调，执行资源清理等操作。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DriverExtensionAbility-onRelease(): void--><!--Device-DriverExtensionAbility-onRelease(): void-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

## Examples

```TypeScript
class DriverExt extends DriverExtensionAbility {
  onRelease() {
    console.info('onRelease');
  }
}
```

## context

```TypeScript
context: DriverExtensionContext
```

DriverExtension的上下文环境，继承自ExtensionContext。

**Type:** [DriverExtensionContext](arkts-driverdevelopment-driverextensioncontext-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DriverExtensionAbility-context: DriverExtensionContext--><!--Device-DriverExtensionAbility-context: DriverExtensionContext-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

