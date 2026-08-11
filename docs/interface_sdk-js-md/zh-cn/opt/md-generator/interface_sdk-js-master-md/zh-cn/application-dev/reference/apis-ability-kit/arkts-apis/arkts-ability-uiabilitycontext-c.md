# UIAbilityContext

UIAbilityContext是需要保存状态的[UIAbility](arkts-app-ability-uiability.md)所对应的context，继承自[Context](arkts-ability-context-t.md)，提供UIAbility的相关配置信息以及操作UIAbility和ServiceExtensionAbility的方法，如启动UIAbility，停止当前UIAbilityContext所属的UIAbility，启动、停止、连接、断开连接ServiceExtensionAbility等。

**继承/实现关系：** UIAbilityContext extends [Context](arkts-ability-context-t.md)

**起始版本：** 9

<!--Device-unnamed-declare class UIAbilityContext extends Context--><!--Device-unnamed-declare class UIAbilityContext extends Context-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## backToCallerAbilityWithResult

```TypeScript
backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise<void>
```

当通过  
[startAbilityForResult](arkts-ability-uiabilitycontext-c.md#startabilityforresult)或[openLink](arkts-ability-uiabilitycontext-c.md#openlink)拉起目标方UIAbility，且需要目标方返回结果时，目标方可以通过该接口将结果返回并拉起调用方。与  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)不同的是，本接口在返回时不会销毁当前UIAbility。使用Promise异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise<void>--><!--Device-UIAbilityContext-backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| abilityResult | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |
| requestCode | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000074](../errorcode-ability.md#16000074-返回结果时requestcode对应的调用方不存在) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000075](../errorcode-ability.md#16000075-不支持返回结果时拉起调用方) |

## connectAppServiceExtensionAbility

```TypeScript
connectAppServiceExtensionAbility(want: Want, callback: ConnectOptions): number
```

将当前UIAbility连接到  
[AppServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md)。通过返回的proxy与AppServiceExtensionAbility进行通信，以使用AppServiceExtensionAbility对外提供的能力。仅支持在主线程调用。该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> 如果
> [AppServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md)
> 实例未启动，该接口的调用方必须为AppServiceExtensionAbility所属应用或者在AppServiceExtensionAbility支持的应用清单（即
> [extensionAbilities标签](../../../quick-start/module-configuration-file.md#extensionabilities标签)的
> appIdentifierAllowList属性）中的应用。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-connectAppServiceExtensionAbility(want: Want, callback: ConnectOptions): long--><!--Device-UIAbilityContext-connectAppServiceExtensionAbility(want: Want, callback: ConnectOptions): long-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000201](../errorcode-ability.md#16000201-目标服务还未启动) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

将当前UIAbility连接到一个[ServiceExtensionAbility](../../../application-models/extensionability-overview.md)，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-UIAbilityContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## connectUIServiceExtensionAbility

```TypeScript
connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>
```

连接一个UIServiceExtensionAbility。使用Promise异步回调。该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>--><!--Device-UIAbilityContext-connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [UIServiceExtensionConnectCallback](arkts-ability-uiserviceextensionconnectcallback-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UIServiceProxy](arkts-ability-uiserviceproxy-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectAppServiceExtensionAbility

```TypeScript
disconnectAppServiceExtensionAbility(connection: number): Promise<void>
```

断开与  
[AppServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md)的连接。仅支持在主线程调用。使用Promise异步回调。断开连接之后，为了防止使用可能失效的remote对象进行通信，建议将连接成功时返回的remote对象设置为null。该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-disconnectAppServiceExtensionAbility(connection: long): Promise<void>--><!--Device-UIAbilityContext-disconnectAppServiceExtensionAbility(connection: long): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void
```

断开与[ServiceExtensionAbility](../../../application-models/extensionability-overview.md)的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用callback异步回调。仅支持在主线程调用。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

断开与[ServiceExtensionAbility](../../../application-models/extensionability-overview.md)的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用Promise异步回调。仅支持在主线程调用。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-UIAbilityContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectUIServiceExtensionAbility

```TypeScript
disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>
```

断开与UIServiceExtensionAbility的连接。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>--><!--Device-UIAbilityContext-disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| proxy | [UIServiceProxy](arkts-ability-uiserviceproxy-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## hideAbility

```TypeScript
hideAbility(): Promise<void>
```

隐藏当前UIAbility。使用Promise异步回调。仅支持在主线程调用。调用此接口前要求确保应用已添加至状态栏。该接口仅在PC/2in1设备中、或处于[自由多窗模式](../../../windowmanager/window-terminology.md#自由多窗模式)的Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-hideAbility(): Promise<void>--><!--Device-UIAbilityContext-hideAbility(): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000067](../errorcode-ability.md#16000067-ability启动参数校验失败) |

## isTerminating

```TypeScript
isTerminating(): boolean
```

查询UIAbility是否处于消亡中状态。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-isTerminating(): boolean--><!--Device-UIAbilityContext-isTerminating(): boolean-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## moveAbilityToBackground

```TypeScript
moveAbilityToBackground(): Promise<void>
```

将处于前台的UIAbility移动到后台。使用Promise异步回调。仅支持在主线程调用。&lt;br/&gt;&lt;!--RP1--&gt;&lt;!--RP1End--&gt;从API version 12开始，该接口仅在Phone、Wearable和TV设备中可正常调用，在其他设备上返回16000061错误码。从API version 13开始，该接口仅在Phone、Tablet、Wearable和TV设备中可正常调用，在其他设备上返回16000061错误码。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-moveAbilityToBackground(): Promise<void>--><!--Device-UIAbilityContext-moveAbilityToBackground(): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000065](../errorcode-ability.md#16000065-接口只支持ability在前台时调用) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000066](../errorcode-ability.md#16000066--wukong模式不允许移动ability到前台后台) |
| [16000061](../errorcode-ability.md#16000061-不支持的操作) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## openAtomicService

```TypeScript
openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>
```

启动一个独立窗口的原子化服务。使用Promise异步回调。仅支持在主线程调用。原子化服务被启动后，有如下情况：

- 正常情况下原子化服务可以通过  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口销毁自身，并且返回结果给调用方。  
- 异常情况下比如杀死原子化服务会返回异常结果给调用方，异常结果的resultCode为-1。  
- 如果不同应用多次调用该接口启动同一个原子化服务，当这个原子化服务调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方, 其它调用方返回异常结果，异常结果中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>--><!--Device-UIAbilityContext-openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appId | string | 是 |
| options | [AtomicServiceOptions](arkts-ability-app-ability-atomicserviceoptions-atomicserviceoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000003](../errorcode-ability.md#16000003-指定的id不存在) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## openLink

```TypeScript
openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>
```

通过&lt;!--RP2--&gt;[App Linking](../../../application-models/app-linking-startup.md)&lt;!--RP2End--&gt;或  
[Deep Linking](../../../application-models/deep-linking-startup.md)方式启动UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。仅支持在主线程调用。通过在link字段中传入标准格式的URL，基于隐式want匹配规则拉起目标UIAbility。目标方必须同时具备以下过滤器特征，才能处理App Linking链接：

- "actions"列表中包含"ohos.want.action.viewData"。  
- "entities"列表中包含"entity.system.browsable"。  
- "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。  
如果希望获取被拉起方终止后的结果，可以设置callback参数，此参数的使用可参照  
[startAbilityForResult](arkts-ability-uiabilitycontext-c.md#startabilityforresult)接口。传入的参数不合法时，如未设置必选参数或link字符串不是标准格式的URL，接口会直接抛出异常。参数校验通过，拉起目标方时出现的错误通过promise返回错误信息。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>--><!--Device-UIAbilityContext-openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| link | string | 是 |
| options | [OpenLinkOptions](arkts-ability-app-ability-openlinkoptions-openlinkoptions-i.md) | 否 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000136](../errorcode-ability.md#16000136-不允许通过app-linking方式拉起应用自身uiability) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## reportDrawnCompleted

```TypeScript
reportDrawnCompleted(callback: AsyncCallback<void>): void
```

用于通知系统UIAbility对应的窗口内容已经绘制完成。使用callback异步回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-reportDrawnCompleted(callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-reportDrawnCompleted(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## requestDialogService

```TypeScript
requestDialogService(want: Want, result: AsyncCallback<dialogRequest.RequestResult>): void
```

启动一个支持模态弹框的ServiceExtensionAbility。ServiceExtensionAbility被启动后，应用弹出模态弹框，通过调用  
[setRequestResult](arkts-ability-dialogrequest-requestcallback-i.md#setrequestresult)接口返回结果给调用者。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-requestDialogService(want: Want, result: AsyncCallback<dialogRequest.RequestResult>): void--><!--Device-UIAbilityContext-requestDialogService(want: Want, result: AsyncCallback<dialogRequest.RequestResult>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| result | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;dialogRequest.RequestResult&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## requestDialogService

```TypeScript
requestDialogService(want: Want): Promise<dialogRequest.RequestResult>
```

启动一个支持模态弹框的ServiceExtensionAbility。ServiceExtensionAbility被启动后，应用弹出模态弹框，通过调用  
[setRequestResult](arkts-ability-dialogrequest-requestcallback-i.md#setrequestresult)接口返回结果给调用者。使用Promise异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-requestDialogService(want: Want): Promise<dialogRequest.RequestResult>--><!--Device-UIAbilityContext-requestDialogService(want: Want): Promise<dialogRequest.RequestResult>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;dialogRequest.RequestResult&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## restartApp

```TypeScript
restartApp(want: Want): Promise<void>
```

处于获焦状态的UIAbility可以通过该接口，重启当前UIAbility所在的进程，并拉起应用内的指定UIAbility。仅支持主线程调用。使用Promise异步回调。如果指定UIAbility就是当前UIAbility，则会刷新窗口至初始状态；如果是其他UIAbility，则会跳转并打开新的UIAbility窗口。该接口仅在Phone设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> 通过该接口重启进程时，不会触发进程中Ability的onDestroy生命周期回调。
> 
> 在原子化服务调用本接口成功后的3秒内，再次调用本接口、
> [restartSelfAtomicService()](arkts-ability-abilitymanager-restartselfatomicservice-f.md#restartselfatomicservice)或
> [ApplicationContext.restartApp()](arkts-ability-applicationcontext-c.md#restartapp)接口中的任一接口，系统将
> 返回错误码16000064。
> 
> 在应用调用本接口成功后的3秒内，若再次调用本接口或
> [ApplicationContext.restartApp()](arkts-ability-applicationcontext-c.md#restartapp)接口中的任一接口，系统将
> 返回错误码16000064。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-restartApp(want: Want): Promise<void>--><!--Device-UIAbilityContext-restartApp(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000064](../errorcode-ability.md#16000064-重启应用频繁) |
| [16000065](../errorcode-ability.md#16000065-接口只支持ability在前台时调用) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000063](../errorcode-ability.md#16000063-重启应用指定组件无效) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## restoreWindowStage

```TypeScript
restoreWindowStage(localStorage: LocalStorage): void
```

恢复UIAbility中的WindowStage数据。仅支持在主线程调用。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-restoreWindowStage(localStorage: LocalStorage): void--><!--Device-UIAbilityContext-restoreWindowStage(localStorage: LocalStorage): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| localStorage | [LocalStorage](../../apis-arkui/arkts-apis/arkts-arkui-localstorage-c.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setAbilityInstanceInfo

```TypeScript
setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>
```

设置当前UIAbility实例的图标和标签信息。图标与标签信息可在任务中心和快捷栏的界面中显示。使用Promise异步回调。该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 15

**需要权限：** ohos.permission.SET_ABILITY_INSTANCE_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>--><!--Device-UIAbilityContext-setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| label | string | 是 |
| icon | image.PixelMap | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setColorMode

```TypeScript
setColorMode(colorMode: ConfigurationConstant.ColorMode): void
```

设置UIAbility的深浅色模式。调用该接口前需要保证该UIAbility对应页面已完成加载。仅支持主线程调用。

> **说明：**
> 
> - 调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在
> [onWindowStageCreate()](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate)生命周期中通过
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9)方法加载页面之后调用。
> 
> - 调用该接口后会创建新的资源管理器对象，如果此前有缓存资源管理器，需要进行更新。
> 
> - 深浅色模式生效的优先级：UIAbility的深浅色模式 > 应用的深浅色模式（
> [ApplicationContext.setColorMode](arkts-ability-applicationcontext-c.md#setcolormode)）> 系统的深浅色模
> 式。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void--><!--Device-UIAbilityContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setMissionContinueState

```TypeScript
setMissionContinueState(state: AbilityConstant.ContinueState, callback: AsyncCallback<void>): void
```

设置UIAbility任务的流转状态。使用callback异步回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-setMissionContinueState(state: AbilityConstant.ContinueState, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-setMissionContinueState(state: AbilityConstant.ContinueState, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | AbilityConstant.ContinueState | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setMissionContinueState

```TypeScript
setMissionContinueState(state: AbilityConstant.ContinueState): Promise<void>
```

设置UIAbility任务的流转状态。使用Promise异步回调。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-setMissionContinueState(state: AbilityConstant.ContinueState): Promise<void>--><!--Device-UIAbilityContext-setMissionContinueState(state: AbilityConstant.ContinueState): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | AbilityConstant.ContinueState | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setMissionLabel

```TypeScript
setMissionLabel(label: string, callback: AsyncCallback<void>): void
```

设置UIAbility在多任务界面中显示的名称。使用callback异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-setMissionLabel(label: string, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-setMissionLabel(label: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| label | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setMissionLabel

```TypeScript
setMissionLabel(label: string): Promise<void>
```

设置UIAbility在多任务界面中显示的名称。使用Promise异步回调。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-setMissionLabel(label: string): Promise<void>--><!--Device-UIAbilityContext-setMissionLabel(label: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| label | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## setMissionWindowIcon

```TypeScript
setMissionWindowIcon(windowIcon: image.PixelMap): Promise<void>
```

设置当前UIAbility在应用窗口、任务中心应用卡片、快捷栏窗口快照的图标。使用Promise异步回调。该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> setMissionWindowIcon&lt;!--Del--&gt;、
> [setMissionIcon](arkts-ability-uiabilitycontext-c-sys.md#setmissionicon)
> &lt;!--DelEnd--&gt;和
> [setAbilityInstanceInfo](arkts-ability-uiabilitycontext-c.md#setabilityinstanceinfo)之间不存在调用优先级关系。
> 当多个接口被依次调用时，后一次调用的接口所设置的图标信息将覆盖之前调用接口所设置的内容，最终生效的图标以最后一次调用的接口为准。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-setMissionWindowIcon(windowIcon: image.PixelMap): Promise<void>--><!--Device-UIAbilityContext-setMissionWindowIcon(windowIcon: image.PixelMap): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowIcon | image.PixelMap | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000135](../errorcode-ability.md#16000135-uiability的主窗不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## setOnNewWantSkipScenarios

```TypeScript
setOnNewWantSkipScenarios(scenarios: number): Promise<void>
```

在特定场景下拉起UIAbility时，如果不需要触发[onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onnewwant)生命周期回调，可以通过该接口设置。仅支持在主线程调用。使用Promise异步回调。

> **说明：**
> 
> 该接口通常用于[onCreate](arkts-ability-app-ability-uiability-uiability-c.md#oncreate)生命周期回调中。入参取值建议包含所有的
> [Scenarios](arkts-ability-contextconstant-scenarios-e.md)枚举值。详见下方示例代码。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-setOnNewWantSkipScenarios(scenarios: int): Promise<void>--><!--Device-UIAbilityContext-setOnNewWantSkipScenarios(scenarios: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scenarios | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-内部错误) |

## setRestoreEnabled

```TypeScript
setRestoreEnabled(enabled: boolean): void
```

设置UIAbility是否启用备份恢复。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-setRestoreEnabled(enabled: boolean): void--><!--Device-UIAbilityContext-setRestoreEnabled(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## showAbility

```TypeScript
showAbility(): Promise<void>
```

显示当前UIAbility。使用Promise异步回调。仅支持在主线程调用。调用此接口前要求确保应用已添加至状态栏。该接口仅在PC/2in1设备中、或处于[自由多窗模式](../../../windowmanager/window-terminology.md#自由多窗模式)的Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-showAbility(): Promise<void>--><!--Device-UIAbilityContext-showAbility(): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000067](../errorcode-ability.md#16000067-ability启动参数校验失败) |

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000071](../errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startAbility

```TypeScript
startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16300003](../errorcode-ability.md#16300003-目标应用程序不是自身应用程序) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000068](../errorcode-ability.md#16000068-ability已经在运行中) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000071](../errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000067](../errorcode-ability.md#16000067-ability启动参数校验失败) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

启动一个UIAbility。使用Promise异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIAbilityContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16300003](../errorcode-ability.md#16300003-目标应用程序不是自身应用程序) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000068](../errorcode-ability.md#16000068-ability已经在运行中) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000071](../errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000067](../errorcode-ability.md#16000067-ability启动参数校验失败) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityByCall

```TypeScript
startAbilityByCall(want: Want): Promise<Caller>
```

该接口用于获取[Caller](arkts-ability-app-ability-uiability-caller-i.md)通信对象，以便于与  
[Callee](arkts-ability-app-ability-uiability-callee-i.md)进行通信。如果指定UIAbility未启动，则会将UIAbility启动至前台或后台。使用Promise异步回调。仅支持在主线程调用。该接口不支持拉起启动模式为[specified模式](../../../application-models/uiability-launch-type.md#specified启动模式)的UIAbility。

> **说明：**
> 
> - 跨设备场景下，调用方与目标方必须为同一应用。
> 
> - 同设备场景下，要求调用方与目标方为不同应用，且调用方具备ohos.permission.ABILITY_BACKGROUND_COMMUNICATION权限（该权限仅系统应用可申请）。
> 
> - 此外如果应用需要在后台调用该接口，需要具备ohos.permission.START_ABILITIES_FROM_BACKGROUND（该权限仅系统应用可申请）。更多的组件启动规则详见
> [组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > **说明：**
> 
> - API version 10及之前版本，需申请ohos.permission.ABILITY_BACKGROUND_COMMUNICATION（该权限仅系统应用可用）。
> 
> - API version 11开始，仅需申请ohos.permission.DISTRIBUTED_DATASYNC（该权限仅当执行应用间建链操作时由软总线实施权限校验，在应用拉起阶段不做校验）。

**起始版本：** 9

**需要权限：** 
- API版本11+：ohos.permission.DISTRIBUTED_DATASYNC
- API版本9 - 10：ohos.permission.ABILITY_BACKGROUND_COMMUNICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-startAbilityByCall(want: Want): Promise<Caller>--><!--Device-UIAbilityContext-startAbilityByCall(want: Want): Promise<Caller>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Caller](arkts-ability-app-ability-uiability-caller-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000018](../errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000071](../errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../errorcode-ability.md#16000072-不支持应用多开) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityByType

```TypeScript
startAbilityByType(type: string, wantParam: Record<string, Object>,
    abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void
```

通过type隐式启动[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)。使用callback异步回调。仅支持在主线程调用，仅支持处于前台的应用调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startAbilityByType(type: string, wantParam: Record<string, Object>,    abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityByType(type: string, wantParam: Record<string, Object>,    abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| wantParam | Record&lt;string, Object&gt; | 是 |
| abilityStartCallback | [AbilityStartCallback](arkts-ability-abilitystartcallback-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## startAbilityByType

```TypeScript
startAbilityByType(type: string, wantParam: Record<string, Object>,
    abilityStartCallback: AbilityStartCallback): Promise<void>
```

通过type隐式启动[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)。使用Promise异步回调。仅支持在主线程调用，仅支持处于前台的应用调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startAbilityByType(type: string, wantParam: Record<string, Object>,    abilityStartCallback: AbilityStartCallback): Promise<void>--><!--Device-UIAbilityContext-startAbilityByType(type: string, wantParam: Record<string, Object>,    abilityStartCallback: AbilityStartCallback): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |
| wantParam | Record&lt;string, Object&gt; | 是 |
| abilityStartCallback | [AbilityStartCallback](arkts-ability-abilitystartcallback-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void
```

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。仅支持在主线程调用。UIAbility被启动后，有如下情况：

- 正常情况下可以通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口销毁自身，并将结果返回给调用方。  
- 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。  
- 如果被启动的UIAbility是[单实例模式](../../../application-models/uiability-launch-type.md#singleton启动模式)，且这个UIAbility被不同应用多次调  
用该接口启动，当这个UIAbility调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIAbilityContext-startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000071](../errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void
```

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。仅支持在主线程调用。UIAbility被启动后，有如下情况：

- 正常情况下可以通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口销毁自身，并将结果返回给调用方。  
- 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。  
- 如果被启动的UIAbility是[单实例模式](../../../application-models/uiability-launch-type.md#singleton启动模式)，且这个UIAbility被不同应用多次调  
用该接口启动，当这个UIAbility调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIAbilityContext-startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000071](../errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
```

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。仅支持在主线程调用。UIAbility被启动后，有如下情况：

- 正常情况下可以通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口销毁自身，并将结果返回给调用方。  
- 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。  
- 如果被启动的UIAbility是[单实例模式](../../../application-models/uiability-launch-type.md#singleton启动模式)，且这个UIAbility被不同应用多次调  
用该接口启动，当这个UIAbility调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIAbilityContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

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
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../errorcode-ability.md#16000055-免安装超时) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000080](../errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000071](../errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000076](../errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startAppServiceExtensionAbility

```TypeScript
startAppServiceExtensionAbility(want: Want): Promise<void>
```

启动  
[AppServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md)实例。使用Promise异步回调。该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> 该接口的调用方必须为
> [AppServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md)
> 所属应用或者在AppServiceExtensionAbility支持的应用清单（即
> [extensionAbilities标签](../../../quick-start/module-configuration-file.md#extensionabilities标签)的
> appIdentifierAllowList属性）中的应用。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-startAppServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIAbilityContext-startAppServiceExtensionAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000200](../errorcode-ability.md#16000200-不允许该调用方启动应用后台服务) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## startSelfUIAbilityInCurrentProcess

```TypeScript
startSelfUIAbilityInCurrentProcess(want: Want, specifiedFlag: string, options?: StartOptions): Promise<void>
```

在当前进程中启动应用程序自己的UIAbility。从API version 23开始，该接口仅在PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。从API version 22开始，该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> - 只能冷启动目标UIAbility，如果目标UIAbility实例已经启动过，则启动失败。
> 
> - 通过该接口启动的UIAbility实例，将运行在调用方所在的进程中。其他关于目标UIAbility的进程相关的策略（例如在
> [module.json5配置文件](../../../quick-start/module-configuration-file.md)中通过isolationProcess或isolationMode字段来指定进程），均
> 不会生效。

> **说明：**
> >
> -目标UIAability只能是冷启动的。如果目标UIAability的实例已经
> 启动，启动失败。
> >
> -通过此API启动的UIAbility实例与调用方在同一进程中运行。其他流程相关
> 目标UIAability的策略（例如通过**隔离进程**或**隔离模式**指定的策略）
> [module.json5](../../../quick-start/module-configuration-file.md)文件中的字段不生效。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-startSelfUIAbilityInCurrentProcess(want: Want, specifiedFlag: string, options?: StartOptions): Promise<void>--><!--Device-UIAbilityContext-startSelfUIAbilityInCurrentProcess(want: Want, specifiedFlag: string, options?: StartOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| specifiedFlag | string | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000053](../errorcode-ability.md#16000053-非顶层ability) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000130](../errorcode-ability.md#16000130-uiability不属于调用方) |
| [16000131](../errorcode-ability.md#16000131-uiability已启动) |
| [16000124](../errorcode-ability.md#16000124-不支持启动分布式uiability) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000122](../errorcode-ability.md#16000122-待启动的目标组件被系统管控模块拦截) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |
| [16000123](../errorcode-ability.md#16000123-不支持隐式启动) |

## startUIServiceExtensionAbility

```TypeScript
startUIServiceExtensionAbility(want: Want): Promise<void>
```

启动一个UIServiceExtensionAbility。使用Promise异步回调。该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-startUIServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIAbilityContext-startUIServiceExtensionAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000019](../errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../errorcode-ability.md#16000012-应用被管控) |
| [16000013](../errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## stopAppServiceExtensionAbility

```TypeScript
stopAppServiceExtensionAbility(want: Want): Promise<void>
```

停止  
[AppServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md)实例。使用Promise异步回调。该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> 该接口的调用方必须为
> [AppServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md)
> 所属应用或者在AppServiceExtensionAbility支持的应用清单（即
> [extensionAbilities标签](../../../quick-start/module-configuration-file.md#extensionabilities标签)的
> appIdentifierAllowList属性）中的应用。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIAbilityContext-stopAppServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIAbilityContext-stopAppServiceExtensionAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000200](../errorcode-ability.md#16000200-不允许该调用方启动应用后台服务) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## terminateSelf

```TypeScript
terminateSelf(callback: AsyncCallback<void>): void
```

销毁UIAbility自身。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置
> [removeMissionAfterTerminate](../../../quick-start/module-configuration-file.md#abilities标签)为true。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-terminateSelf(callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-terminateSelf(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

销毁UIAbility自身。使用Promise异步回调。仅支持在主线程调用。

> **说明：**
> 
> 调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置
> [removeMissionAfterTerminate](../../../quick-start/module-configuration-file.md#abilities标签)为true。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-terminateSelf(): Promise<void>--><!--Device-UIAbilityContext-terminateSelf(): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## terminateSelfWithResult

```TypeScript
terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void
```

销毁UIAbility自身。使用callback异步回调。仅支持在主线程调用。仅当UIAbility通过  
[startAbilityForResult](arkts-ability-uiabilitycontext-c.md#startabilityforresult)接口拉起时，调用terminateSelfWithResult接口销毁UIAbility，才会返回结果给调用方。

> **说明：**
> 
> 调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置
> [removeMissionAfterTerminate](../../../quick-start/module-configuration-file.md#abilities标签)为true。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## terminateSelfWithResult

```TypeScript
terminateSelfWithResult(parameter: AbilityResult): Promise<void>
```

销毁UIAbility自身。使用Promise异步回调。仅支持在主线程调用。仅当UIAbility通过  
[startAbilityForResult](arkts-ability-uiabilitycontext-c.md#startabilityforresult)接口拉起时，调用terminateSelfWithResult接口销毁UIAbility，才会返回结果给调用方。

> **说明：**
> 
> 调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置
> [removeMissionAfterTerminate](../../../quick-start/module-configuration-file.md#abilities标签)为true。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-terminateSelfWithResult(parameter: AbilityResult): Promise<void>--><!--Device-UIAbilityContext-terminateSelfWithResult(parameter: AbilityResult): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [16000005](../errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000001](../errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000009](../errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000011](../errorcode-ability.md#16000011-上下文对象不存在) |

## abilityInfo

```TypeScript
abilityInfo: AbilityInfo
```

UIAbility的相关信息。

**类型：** [AbilityInfo](arkts-ability-abilityinfo-i.md)

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-abilityInfo: AbilityInfo--><!--Device-UIAbilityContext-abilityInfo: AbilityInfo-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## config

```TypeScript
config: Configuration
```

应用运行时的环境变量，如语言、颜色模式等。

**类型：** [Configuration](arkts-ability-app-ability-configuration-configuration-i.md)

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-config: Configuration--><!--Device-UIAbilityContext-config: Configuration-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## currentHapModuleInfo

```TypeScript
currentHapModuleInfo: HapModuleInfo
```

当前UIAbility所属HAP的信息。

**类型：** [HapModuleInfo](arkts-ability-hapmoduleinfo-i.md)

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-currentHapModuleInfo: HapModuleInfo--><!--Device-UIAbilityContext-currentHapModuleInfo: HapModuleInfo-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## windowStage

```TypeScript
windowStage: window.WindowStage
```

当前WindowStage对象。仅支持在主线程调用。

**类型：** window.WindowStage

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-UIAbilityContext-windowStage: window.WindowStage--><!--Device-UIAbilityContext-windowStage: window.WindowStage-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core
