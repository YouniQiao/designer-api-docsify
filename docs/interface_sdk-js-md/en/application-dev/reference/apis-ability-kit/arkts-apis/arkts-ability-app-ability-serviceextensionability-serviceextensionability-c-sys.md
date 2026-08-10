# ServiceExtensionAbility (System API)

ServiceExtensionAbility模块提供后台服务相关扩展能力，提供后台服务创建、销毁、连接、断开等生命周期回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class ServiceExtensionAbility--><!--Device-unnamed-declare class ServiceExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { ServiceExtensionAbility } from 'kits/@kit.AbilityKit';
```

## onConfigurationUpdate

```TypeScript
onConfigurationUpdate(newConfig: Configuration): void
```

当Extension更新配置信息时调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onConfigurationUpdate(newConfig: Configuration): void--><!--Device-ServiceExtensionAbility-onConfigurationUpdate(newConfig: Configuration): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newConfig | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes | 表示需要更新的配置信息。 |

## Examples

```TypeScript
import { ServiceExtensionAbility, Configuration } from '@kit.AbilityKit';

class ServiceExt extends ServiceExtensionAbility {
  onConfigurationUpdate(newConfig: Configuration) {
    console.info(`onConfigurationUpdate, config: ${JSON.stringify(newConfig)}`);
  }
}
```

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>
```

Extension生命周期回调，如果是connectAbility拉起的服务，会在onCreate之后回调。返回一个RemoteObject对象，用于客户端和服务端进行通信。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>--><!--Device-ServiceExtensionAbility-onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**Return value:**

| Type | Description |
| --- | --- |
| rpc.RemoteObject | RemoteObject or Promise used to return a RemoteObject, which is used for communication between the client and server. |

## Examples

```TypeScript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

class StubTest extends rpc.RemoteObject{
  constructor(des: string) {
    super(des);
  }
  onConnect(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption) {
  }
}
class ServiceExt extends ServiceExtensionAbility {
  onConnect(want: Want) {
    console.info('onConnect , want: ${want.abilityName}');
    return new StubTest('test');
  }
}
```

If the returned RemoteObject depends on an asynchronous API, you can use the asynchronous lifecycle.

```TypeScript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

class StubTest extends rpc.RemoteObject{
  constructor(des: string) {
    super(des);
  }
  onConnect(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption) {
  }
}
async function getDescriptor() {
  // Call the asynchronous function.
  return "asyncTest"
}
class ServiceExt extends ServiceExtensionAbility {
  async onConnect(want: Want) {
    console.info(`onConnect , want: ${want.abilityName}`);
    let descriptor = await getDescriptor();
    return new StubTest(descriptor);
  }
}
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

Extension生命周期回调，在创建时回调，执行初始化业务逻辑操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onCreate(want: Want): void--><!--Device-ServiceExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

## Examples

```TypeScript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';

class ServiceExt extends ServiceExtensionAbility {
  onCreate(want: Want) {
    console.info(`onCreate, want: ${want.abilityName}`);
  }
}
```

## onDestroy

```TypeScript
onDestroy(): void
```

Extension生命周期回调，在销毁时回调，执行资源清理等操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onDestroy(): void--><!--Device-ServiceExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Examples

```TypeScript
import { ServiceExtensionAbility } from '@kit.AbilityKit';

class ServiceExt extends ServiceExtensionAbility {
  onDestroy() {
    console.info('onDestroy');
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(want: Want): void | Promise<void>
```

Extension的生命周期回调，客户端执行断开连接服务时回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onDisconnect(want: Want): void | Promise<void>--><!--Device-ServiceExtensionAbility-onDisconnect(want: Want): void | Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

## Examples

A synchronous callback example is as follows:

```TypeScript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';

class ServiceExt extends ServiceExtensionAbility {
  onDisconnect(want: Want) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
  }
}
```

A promise asynchronous callback example is as follows:

```TypeScript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';

class ServiceExt extends ServiceExtensionAbility {
  async onDisconnect(want: Want) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
    // Call the asynchronous function.
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(want: Want): Promise<void> | undefined
```

Extension的生命周期回调，客户端执行断开连接服务时回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onDisconnect(want: Want): Promise<void> | undefined--><!--Device-ServiceExtensionAbility-onDisconnect(want: Want): Promise<void> | undefined-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## onDump

```TypeScript
onDump(params: Array<string>): Array<string>
```

转储客户端信息时调用。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onDump(params: Array<string>): Array<string>--><!--Device-ServiceExtensionAbility-onDump(params: Array<string>): Array<string>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | Array&lt;string&gt; | Yes | 表示命令形式的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 表示转存客户端信息数组。 |

## Examples

```TypeScript
import { ServiceExtensionAbility } from '@kit.AbilityKit';

class ServiceExt extends ServiceExtensionAbility {
  onDump(params: Array<string>) {
    console.info(`dump, params: ${JSON.stringify(params)}`);
    return ['params'];
  }
}
```

## onReconnect

```TypeScript
onReconnect(want: Want): void
```

Extension的生命周期回调，当所有以前的客户端都断开连接之后，新客户端尝试连接到服务时调用。预留能力，当前暂未支持。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onReconnect(want: Want): void--><!--Device-ServiceExtensionAbility-onReconnect(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

## Examples

```TypeScript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';

class ServiceExt extends ServiceExtensionAbility {
  onReconnect(want: Want) {
    console.info('onReconnect, want: ${want.abilityName}');
  }
}
```

## onRequest

ArkTS-Dyn:
```TypeScript
onRequest(want: Want, startId: number): void
```

ArkTS-Sta:
```TypeScript
onRequest(want: Want, startId: int): void
```

Extension生命周期回调，如果是startAbility或者startServiceExtensionAbility拉起的服务，会在onCreate之后回调。每次拉起服务都会回调，startId会递增。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-onRequest(want: Want, startId: int): void--><!--Device-ServiceExtensionAbility-onRequest(want: Want, startId: int): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |
| startId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 返回拉起次数。首次拉起初始值返回1，多次之后自动递增。 |

## Examples

```TypeScript
import { ServiceExtensionAbility, Want } from '@kit.AbilityKit';

class ServiceExt extends ServiceExtensionAbility {
  onRequest(want: Want, startId: number) {
    console.info('onRequest, want: ${want.abilityName}');
  }
}
```

## context

```TypeScript
context: ServiceExtensionContext
```

ServiceExtension的上下文环境，继承自ExtensionContext。

**Type:** [ServiceExtensionContext](../../apis-default/arkts-apis/arkts-serviceextensioncontext-c-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ServiceExtensionAbility-context: ServiceExtensionContext--><!--Device-ServiceExtensionAbility-context: ServiceExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

