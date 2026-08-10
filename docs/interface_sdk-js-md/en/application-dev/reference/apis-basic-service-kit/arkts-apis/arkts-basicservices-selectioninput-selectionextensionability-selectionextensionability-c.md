# SelectionExtensionAbility

本模块提供划词扩展能力，支持开发者通过继承SelectionExtensionAbility实现自定义的划词扩展服务，适用于在用户通过鼠标、触控板选中文本后提供搜索、翻译等扩展交互的场景。开发者需在工程配置中声明该ExtensionAbility。具体的配置请参见  
[实现一个划词扩展能力](../../../basic-services/selectionInput/selection-services-application-guide.md)。本模块提供的具体能力包括：

- 生命周期管理：通过[onConnect](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md#onconnect)和  
[onDisconnect](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md#ondisconnect)回调处理连接与断开逻辑。  
- 提供context属性：开发者可通过context调用  
[startAbility](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md#startability)拉起同应用内的目标Ability，或将context作为[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)的入参创建划词面板。

> **说明：**
> 
> - 本模块仅支持PC/2in1设备。开发者可通过canIUse('SystemCapability.SelectionInput.Selection')判断当前设备是否支持该能力。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-unnamed-declare class SelectionExtensionAbility--><!--Device-unnamed-declare class SelectionExtensionAbility-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { SelectionExtensionAbility } from 'kits/@kit.BasicServicesKit';
```

## onConnect

```TypeScript
onConnect(want: Want): rpc.RemoteObject
```

当客户端连接到SelectionExtensionAbility时，系统会触发该回调，开发者可在该回调中返回RPC通信对象，用于客户端与服务端建立IPC通信连接。开发者需返回一个继承了rpc.RemoteObject的通信桩对象，系统将该桩对象传递给客户端，客户端通过该桩对象与SelectionExtensionAbility进行IPC通信。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionExtensionAbility-onConnect(want: Want): rpc.RemoteObject--><!--Device-SelectionExtensionAbility-onConnect(want: Want): rpc.RemoteObject-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 连接SelectionExtensionAbility时系统传入的Want对象，包含当前Ability的名称、Bundle名称等描述信息，用于在onConnect回调中获取 Ability连接配置，以便据此执行相应的初始化逻辑。 |

**Return value:**

| Type | Description |
| --- | --- |
| rpc.RemoteObject | RemoteObject通信桩对象，开发者需实现该对象的远程消息处理方法（如onRemoteMessageRequest），系统将此对象传递给客户端用于IPC通信。 |

## Examples

```TypeScript
import { SelectionExtensionAbility } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[SelectionExtensionAbility]';

// Define the RPC stub class for IPC between the client and server.
class StubTest extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(
    code: number,
    data: rpc.MessageSequence,
    reply: rpc.MessageSequence,
    options: rpc.MessageOption
  ): boolean | Promise<boolean> {
    return true;
  }
}

class ServiceExtAbility extends SelectionExtensionAbility {
  // Implement the onConnect lifecycle callback to return the RPC object when the client connects to the SelectionExtensionAbility.
  onConnect(want: Want): rpc.RemoteObject {
    hilog.info(0x0000, TAG, `onConnect, want: ${want.abilityName}`);
    // Return the RPC stub object for establishing IPC between the client and server.
    return new StubTest('test');
  }
}
```

## onDisconnect

```TypeScript
onDisconnect(): void
```

当客户端断开与SelectionExtensionAbility的连接（例如用户关闭划词开关或切换划词应用）时，系统会触发该回调。开发者可在该回调中执行与onConnect对应的清理操作，如调用  
[destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroypanel)销毁已创建的面板、调用  
[off('selectionCompleted')](@ohos.selectionInput.selectionManager:selectionManager.off(type: 'selectionCompleted', callback?: Callback&lt;SelectionInfo&gt;))取消订阅的划词完成事件等。

仅当SelectionExtensionAbility正常断开连接时会触发该回调，异常断开场景（例如低内存终止进程）不会触发该回调。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionExtensionAbility-onDisconnect(): void--><!--Device-SelectionExtensionAbility-onDisconnect(): void-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## Examples

```TypeScript
import { SelectionExtensionAbility } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[SelectionExtensionAbility]';

class ServiceExtAbility extends SelectionExtensionAbility {
  // Implement the onDisconnect lifecycle callback to perform cleanup operations when the client disconnects from the SelectionExtensionAbility.
  onDisconnect(): void {
    hilog.info(0x0000, TAG, `onDisconnect`);
  }
}
```

## context

```TypeScript
context: SelectionExtensionContext
```

SelectionExtensionAbility的上下文环境，继承自[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)。开发者可通过context调用  
[startAbility](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md#startability)拉起同应用内的目标Ability，或将context作为[createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel)的入参创建划词面板。

**Type:** [SelectionExtensionContext](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SelectionExtensionAbility-context: SelectionExtensionContext--><!--Device-SelectionExtensionAbility-context: SelectionExtensionContext-End-->

**System capability:** SystemCapability.SelectionInput.Selection

