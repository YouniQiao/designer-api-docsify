# UIExtensionContext

UIExtensionContext是[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability)的上下文环境，继承自 [ExtensionContext](arkts-ability-extensioncontext-c.md#extensioncontext)，提供UIExtensionAbility的相关配置信息以及操作UIAbility的方法，如 启动UIAbility等。

**继承/实现关系：** UIExtensionContext extends ExtensionContext

**起始版本：** 23

<!--Device-unnamed-declare class UIExtensionContext--><!--Device-unnamed-declare class UIExtensionContext-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbilityWithRootHostToken

```TypeScript
connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): number
```

将当前UIExtensionAbility连接到一个 [ServiceExtensionAbility](arkts-ability-app-ability-serviceextensionability-serviceextensionability-c-sys.md#onconnect)，通过返回的远 程代理对象与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。与此同时，该方法会将UIExtensionAbility的原始宿主Ability的Token传 递给被连接的ServiceExtensionAbility，ServiceExtensionAbility可以在 [onCreate()](arkts-ability-app-ability-serviceextensionability-serviceextensionability-c-sys.md#oncreate)或 [onConnect()](arkts-ability-app-ability-serviceextensionability-serviceextensionability-c-sys.md#onconnect)方法中，通过Want参数的 [UI_EXTENSION_ROOT_TOKEN](arkts-ability-wantconstant-params-e.md#params)获取该Token。 > **说明：** > > 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): long--><!--Device-UIExtensionContext-connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): long-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| connect | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000070](../errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setHostPageOverlayForbidden

```TypeScript
setHostPageOverlayForbidden(isForbidden: boolean) : void
```

是否允许[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability)拉起的页面被使用方的页面覆盖。 > **说明：** > > 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。 > > 该接口需要在窗口创建之前调用。建议在[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#uiextensionability)的 > [onCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#oncreate)生命周期内调用。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-setHostPageOverlayForbidden(isForbidden: boolean) : void--><!--Device-UIExtensionContext-setHostPageOverlayForbidden(isForbidden: boolean) : void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isForbidden | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## startAbilityForResultAsCaller

```TypeScript
startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>
```

使用设置的caller信息启动一个Ability，caller信息由want携带，在系统服务层识别，Ability可以在onCreate生命周期的want参数中获取到caller信息。使用该接口启动一个Ability时，want的 caller信息不会被当前自身的应用信息覆盖，系统服务层可获取到初始caller的信息。使用Promise异步回调。 - 正常情况下可通过调用 [terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止并且返回结果给调用方。 - 异常情况下比如杀死Ability会返回异常信息给调用方，异常信息中resultCode为-1。 - 如果被启动的Ability模式是单实例模式，不同应用多次调用该接口启动这个Ability，当这个Ability调用 [terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) 接口使之终止时，只将正常结果返回给最后一个调用方，其它调用方返回异常信息，异常信息中resultCode为-1。 > **说明：** > > 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000069](../errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000070](../errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000071](../errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000077](../errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000072](../errorcode-ability.md#16000072-不支持应用多开) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want): Promise<void>
```

启动一个ServiceExtensionAbility。使用Promise异步回调。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startServiceExtensionAbilityWithAccount

```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: number): Promise<void>
```

启动一个指定系统账号下的ServiceExtensionAbility。使用Promise异步回调。 > **说明：** > > 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。 > > 当accountId为当前用户时，无需进行权限校验。

**起始版本：** 23

**需要权限：** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>--><!--Device-UIExtensionContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startUIAbilities

```TypeScript
startUIAbilities(wantList: Array<Want>): Promise<void>
```

同时启动多个UIAbility。使用Promise异步回调。 开发者可以传入多个UIAbility对应的Want信息，这些UIAbility可以指向一个或多个应用。当所有的UIAbility都能启动成功时，系统会通过多个窗口同时展示这些UIAbility。根据窗口的处理，不同设备上可能会有不 同的展示效果（包括窗口形态、数量和排版布局）。 该接口仅在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。 > **说明：** > > 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startUIAbilities(wantList: Array<Want>): Promise<void>--><!--Device-UIExtensionContext-startUIAbilities(wantList: Array<Want>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| wantList | Array&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000124](../errorcode-ability.md#16000124-不支持启动分布式uiability) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000125](../errorcode-ability.md#16000125-不支持启动插件uiability) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000126](../errorcode-ability.md#16000126-不支持启动dlp文件) |
| [16000120](../errorcode-ability.md#16000120-wantlist内的元素个数超出4个或小于1个) |
| [16000121](../errorcode-ability.md#16000121-待启动的目标组件类型不是uiability) |
| [16000122](../errorcode-ability.md#16000122-待启动的目标组件被系统管控模块拦截) |
| [16000123](../errorcode-ability.md#16000123-不支持隐式启动) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startUIAbilitiesInSplitWindowMode

```TypeScript
startUIAbilitiesInSplitWindowMode(primaryWindowId: number, secondaryWant: Want): Promise<void>
```

当第一个UIAbility实例被创建后，启动第二个UIAbility，并以分屏模式进行显示。使用Promise异步回调。 该接口仅在Phone设备中可正常调用，在其他设备中返回801错误码。 > **说明：** > > 如果第一个UIAbility实例被销毁，那么第二个UIAbility将以全屏模式启动。 > > 第二个UIAbility仅支持[显示启动](../../../application-models/explicit-implicit-want-mappings.md#显式want匹配原理)。 > > 如果调用方位于后台，还需要具备ohos.permission.START_ABILITIES_FROM_BACKGROUND (该权限仅系统应用可申请)。 > > 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 23

**需要权限：** ohos.permission.START_ABILITIES_FROM_BACKGROUND

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startUIAbilitiesInSplitWindowMode(primaryWindowId: int, secondaryWant: Want): Promise<void>--><!--Device-UIExtensionContext-startUIAbilitiesInSplitWindowMode(primaryWindowId: int, secondaryWant: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| primaryWindowId | number | 是 |
| secondaryWant | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000124](../errorcode-ability.md#16000124-不支持启动分布式uiability) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000125](../errorcode-ability.md#16000125-不支持启动插件uiability) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000126](../errorcode-ability.md#16000126-不支持启动dlp文件) |
| [16000122](../errorcode-ability.md#16000122-待启动的目标组件被系统管控模块拦截) |
| [16000123](../errorcode-ability.md#16000123-不支持隐式启动) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
