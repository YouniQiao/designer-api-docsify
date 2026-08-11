# SelectionExtensionContext

SelectionExtensionContext是  
[SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md)的上下文，继承自  
[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)。

每个SelectionExtensionAbility组件实例化时，系统都会自动创建对应的SelectionExtensionContext。开发者可以通过SelectionExtensionContext调用  
[startAbility](arkts-basicservices-selectioninput-selectionextensioncontext-selectionextensioncontext-c.md#startability)接口拉起同应用内其他Ability。适用于在划词扩展场景中需要跳转至应用内其他Ability的情况，帮助用户在划词操作后快速获取与划词内容关联的功能或信息。

> **说明：**
> 
> - 本模块仅支持PC/2in1设备。开发者可通过canIUse('SystemCapability.SelectionInput.Selection')判断当前设备是否支持该功能。

**继承/实现关系：** SelectionExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**起始版本：** 24

<!--Device-unnamed-declare class SelectionExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class SelectionExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

拉起同应用内的目标Ability，适用于在划词扩展场景中需要跳转至应用内其他Ability的情况。系统根据Want对象中指定的bundleName和abilityName匹配并调度启动目标Ability。使用Promise异步回调。关于Ability启动机制，请参见[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SelectionExtensionContext-startAbility(want: Want): Promise<void>--><!--Device-SelectionExtensionContext-startAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000019](../../apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000083](../../apis-ability-kit/errorcode-ability.md#16000083-不允许该类型extensionability启动指定ability) |
| [16000061](../../apis-ability-kit/errorcode-ability.md#16000061-不支持的操作) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000069](../../apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000070](../../apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## 示例

```TypeScript
import { SelectionExtensionAbility, BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class SelectionAbilityStub extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }
  onRemoteMessageRequest(
    code: number,
    data: rpc.MessageSequence,
    reply: rpc.MessageSequence,
    options: rpc.MessageOption
  ): boolean | Promise<boolean> {
    console.info(`onRemoteMessageRequest code: ${code}`);
    return true;
  }
}

class SelectionExtAbility extends SelectionExtensionAbility {
  onConnect(want: Want): rpc.RemoteObject {
    try {
      // 构造Want对象，指定要拉起的目标Ability信息
      let wantAbility: Want = {
        bundleName: 'com.selection.selectionapplication',
        abilityName: 'EntryAbility',
      };
      // 拉起目标Ability，this.context由SelectionExtensionAbility实例自动提供，无需额外获取
      this.context.startAbility(wantAbility).then(() => {
        console.info(`startAbility success`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to startAbility. Error code: ${err.code}, error message: ${err.message}`);
      });
    } catch (err) {
      console.error(`Failed to startAbility. Error code: ${err.code}, error message: ${err.message}`);
    }
    return new SelectionAbilityStub('remote');
  }
}
```
