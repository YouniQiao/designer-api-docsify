# InputMethodExtensionContext

@ohos.InputMethodExtensionContext模块是InputMethodExtensionAbility的上下文环境，继承于ExtensionContext，为输入法扩展能力提供上下文级别的操作接口。 本模块是输入法ExtensionAbility的上下文类，继承自`ExtensionContext`，作为`InputMethodExtensionAbility`实例的`context`属性提供。它承载了输入法扩展应用在其生命周期内 可使用的上下文能力，包括销毁自身和拉起其他应用。 本模块提供两大核心能力：1）通过`destroy()`销毁输入法ExtensionAbility自身，实现输入法应用的生命周期终止；2）通过`startAbility()`拉起目标应用，使输入法应用能够启动其他Ability进行交互， 拓展输入法功能的灵活性和可扩展性。 当开发输入法ExtensionAbility并需要在其生命周期内执行上下文级操作时使用本模块。典型场景包括：输入法应用在`onDestroy`回调中主动销毁自身、输入法应用需要拉起设置页面或其他辅助应用等。   
> **说明：**
   
> 
   
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
   
> 本模块接口仅可在Stage模型下使用。
 模块内的核心API按功能分为两类： 
1. 生命周期管理：`destroy()`用于销毁输入法ExtensionAbility自身，终止输入法应用运行。 
2. Ability交互：`startAbility()`用于从输入法应用拉起目标Ability（如设置页面等），拓展输入法应用与其他应用的交互能力。 
 典型使用流程：在`InputMethodExtensionAbility`的`onCreate`回调中获取`this.context` → 在需要终止输入法时调用`context.destroy()` → 在需要拉起其他应用时调用 `context.startAbility(want)`。   
 | Class | 说明 | |---|---| | InputMethodExtensionContext | 输入法扩展上下文类，继承自`ExtensionContext`，为`InputMethodExtensionAbility`提供上下文操作能力。 关键方法包括：`destroy()`销毁输入法自身（支持callback和Promise两种异步方式）、`startAbility(want)`拉起目标应用（Promise方式，API 12+新增）。 | 本模块的`InputMethodExtensionContext`需通过`InputMethodExtensionAbility`子类实例获取，其API与InputMethodExtensionAbility生命周期回调组合使用。 

``` javascript
// 以下为阐述调用逻辑的伪代码

// 1. 定义InputMethodExtensionAbility子类
class InputMethodExtAbility extends InputMethodExtensionAbility {
 onCreate(want) {
 // 获取上下文对象
 let context = this.context; // InputMethodExtensionContext实例
 }

 onDestroy() {
 // 在生命周期回调中销毁自身
 this.context.destroy();
 }
}

// 2. 拉起目标应用（如输入法设置页面）
let targetWant = {
 bundleName: "com.example.settings",
 abilityName: "SettingsAbility"
};
this.context.startAbility(targetWant);
```

   
> **说明：**
   
> 
   
> `InputMethodExtensionContext`实例通过`InputMethodExtensionAbility`子类的`this.context`属性获取，不可直接创建。`destroy()`通常在
   
> `onDestroy`生命周期回调中调用，也可在其他时机主动调用以终止输入法ExtensionAbility。

**继承/实现关系：** InputMethodExtensionContext extends ExtensionContext

**起始版本：** 9

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { InputMethodExtensionContext } from 'kits/@kit.IMEKit';
```

## destroy

```TypeScript
destroy(callback: AsyncCallback<void>): void
```

销毁输入法应用。使用callback异步回调。   
- 含义/功能：销毁当前的InputMethodExtensionAbility，终止输入法应用的运行。调用后系统将触发`InputMethodExtensionAbility.onDestroy()`生命周期回调。   
- 使用场景：当输入法应用需要主动终止自身运行时使用。例如：输入法应用在处理完特定任务后主动退出、或在`onDestroy`回调中配合销毁以确保资源释放。   
- 使用后效果：调用成功后，当前的InputMethodExtensionAbility将被销毁，系统触发`onDestroy()`生命周期回调，输入法应用进程终止。调用后再进行其他上下文操作将不起效。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## destroy

```TypeScript
destroy(): Promise<void>
```

销毁输入法应用。使用Promise异步回调。   
- 含义/功能：销毁当前的InputMethodExtensionAbility，终止输入法应用的运行。调用后系统将触发`InputMethodExtensionAbility.onDestroy()`生命周期回调。   
- 使用场景：当输入法应用需要主动终止自身运行时使用。与callback形式功能相同，适合需要使用Promise链式调用的场景。   
- 使用后效果：调用成功后，当前的InputMethodExtensionAbility将被销毁，系统触发`onDestroy()`生命周期回调，输入法应用进程终止。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## startAbility

```TypeScript
startAbility(want: Want): Promise<void>
```

拉起目标应用。使用Promise异步回调。   
- 含义/功能：从输入法应用启动指定的Ability，使输入法应用能够与其他应用交互。通过Want参数指定目标应用的Ability名称和Bundle名称。   
- 使用场景：当输入法应用需要拉起其他应用时使用。例如：输入法应用拉起系统设置页面供用户配置输入法、拉起浏览器打开帮助文档等。   
- 使用后效果：调用成功后，目标Ability被启动并显示在前台。输入法应用自身不会受到影响，继续正常运行。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000019](../../apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000061](../../apis-ability-kit/errorcode-ability.md#16000061-不支持的操作) |
| [16000069](../../apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000070](../../apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16200001](../../apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
