# InputMethodExtensionContext

**@ohos.InputMethodExtensionContext**模块是InputMethodExtensionAbility的上下文环境，继承于ExtensionContext，为输入法扩展能力提供上下文级别的操作接口。 本模块是输入法ExtensionAbility的上下文类，继承自`ExtensionContext`，作为`InputMethodExtensionAbility`实例的`context`属性提供。它承载了输入法扩展应用在其生命周期内 可使用的上下文能力，包括销毁自身和拉起其他应用。 本模块提供两大核心能力：1）通过`destroy()`销毁输入法ExtensionAbility自身，实现输入法应用的生命周期终止；2）通过`startAbility()`拉起目标应用，使输入法应用能够启动其他Ability进行交互， 拓展输入法功能的灵活性和可扩展性。 当开发输入法ExtensionAbility并需要在其生命周期内执行上下文级操作时使用本模块。典型场景包括：输入法应用在`onDestroy`回调中主动销毁自身、输入法应用需要拉起设置页面或其他辅助应用等。 模块内的核心API按功能分为两类： 1. **生命周期管理**：`destroy()`用于销毁输入法ExtensionAbility自身，终止输入法应用运行。 2. **Ability交互**：`startAbility()`用于从输入法应用拉起目标Ability（如设置页面等），拓展输入法应用与其他应用的交互能力。 典型使用流程：在`InputMethodExtensionAbility`的`onCreate`回调中获取`this.context` → 在需要终止输入法时调用`context.destroy()` → 在需要拉起其他应用时调用 `context.startAbility(want)`。

**继承/实现关系：** InputMethodExtensionContext extends ExtensionContext

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare class InputMethodExtensionContext--><!--Device-unnamed-declare class InputMethodExtensionContext-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## connectAbility

```TypeScript
connectAbility(want: Want, options: ConnectOptions): number
```

将当前Ability连接到ServiceExtensionAbility。

**起始版本：** 9

**废弃版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-connectAbility(want: Want, options: ConnectOptions): number--><!--Device-InputMethodExtensionContext-connectAbility(want: Want, options: ConnectOptions): number-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## connectAbilityWithAccount

```TypeScript
connectAbilityWithAccount(want: Want, accountId: number): number
```

以指定账户连接ServiceExtensionAbility。

**起始版本：** 9

**废弃版本：** 10

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-connectAbilityWithAccount(want: Want, accountId: number): number--><!--Device-InputMethodExtensionContext-connectAbilityWithAccount(want: Want, accountId: number): number-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

将当前Ability连接到ServiceExtensionAbility。

**起始版本：** 9

**废弃版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): number--><!--Device-InputMethodExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): number-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectAbility

```TypeScript
disconnectAbility(connection: number, callback: AsyncCallback<void>): void
```

断开与ServiceExtensionAbility的连接。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-disconnectAbility(connection: number, callback: AsyncCallback<void>): void--><!--Device-InputMethodExtensionContext-disconnectAbility(connection: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectAbility

```TypeScript
disconnectAbility(connection: number): Promise<void>
```

断开与ServiceExtensionAbility的连接。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-disconnectAbility(connection: number): Promise<void>--><!--Device-InputMethodExtensionContext-disconnectAbility(connection: number): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void
```

断开与ServiceExtensionAbility的连接。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void--><!--Device-InputMethodExtensionContext-disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

断开与ServiceExtensionAbility的连接。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-disconnectServiceExtensionAbility(connection: number): Promise<void>--><!--Device-InputMethodExtensionContext-disconnectServiceExtensionAbility(connection: number): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityWithAccount

```TypeScript
startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void
```

以指定账户拉起目标应用。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void--><!--Device-InputMethodExtensionContext-startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityWithAccount

```TypeScript
startAbilityWithAccount(want: Want, accountId: number): Promise<void>
```

以指定账户拉起目标应用。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 10

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-startAbilityWithAccount(want: Want, accountId: number): Promise<void>--><!--Device-InputMethodExtensionContext-startAbilityWithAccount(want: Want, accountId: number): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../../apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## terminateSelf

```TypeScript
terminateSelf(callback: AsyncCallback<void>): void
```

销毁输入法ExtensionAbility。使用callback异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [destroy](arkts-ime-inputmethodextensioncontext-c.md#destroy)(callback: AsyncCallback&lt;void&gt;)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-terminateSelf(callback: AsyncCallback<void>): void--><!--Device-InputMethodExtensionContext-terminateSelf(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

销毁输入法ExtensionAbility。使用Promise异步回调。

**起始版本：** 9

**废弃版本：** 10

**替代接口：** [destroy](arkts-ime-inputmethodextensioncontext-c.md#destroy)()

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InputMethodExtensionContext-terminateSelf(): Promise<void>--><!--Device-InputMethodExtensionContext-terminateSelf(): Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
