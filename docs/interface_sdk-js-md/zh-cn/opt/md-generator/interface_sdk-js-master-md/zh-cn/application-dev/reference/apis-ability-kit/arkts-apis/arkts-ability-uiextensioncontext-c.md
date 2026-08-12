# UIExtensionContext

UIExtensionContext是[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#UIExtensionAbility)的上下文环境，继承自  
[ExtensionContext](./application/ExtensionContext:ExtensionContext)，提供UIExtensionAbility的相关配置信息以及操作UIAbility的方法，如启动UIAbility等。

**继承/实现关系：** UIExtensionContext extends [ExtensionContext](ExtensionContext)

**起始版本：** 10

<!--Device-unnamed-declare class UIExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class UIExtensionContext extends ExtensionContext-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

将当前UIExtensionAbility连接到一个ServiceExtensionAbility，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。ServiceExtensionAbility是一类特殊的[ExtensionAbility](../../../application-models/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-UIExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

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
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## connectUIServiceExtensionAbility

```TypeScript
connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>
```

连接到一个UIServiceExtensionAbility。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>--><!--Device-UIExtensionContext-connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>-End-->

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
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void
```

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用callback异步回调。ServiceExtensionAbility是一类特殊的[ExtensionAbility](../../../application-models/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| connection | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用Promise异步回调。ServiceExtensionAbility是一类特殊的[ExtensionAbility](../../../application-models/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## disconnectUIServiceExtensionAbility

```TypeScript
disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>
```

断开UIServiceExtensionAbility。使用Promise异步回调。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>--><!--Device-UIExtensionContext-disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [proxy](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-config-i.md) | [UIServiceProxy](arkts-ability-uiserviceproxy-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## openAtomicService

```TypeScript
openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>
```

打开一个独立窗口的原子化服务，并返回结果。使用Promise异步回调。分为以下几种情况：

- 正常情况下可通过调用  
[terminateSelfWithResult](./application/UIAbilityContext:UIAbilityContext.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback&lt;void&gt;))接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死原子化服务会返回异常信息给调用方，异常信息中resultCode为-1。  
- 如果不同应用多次调用该接口启动同一个原子化服务，当这个原子化服务调用  
[terminateSelfWithResult](./application/UIAbilityContext:UIAbilityContext.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback&lt;void&gt;))接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息，异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>-End-->

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
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000069](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000003-指定的id不存在) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## openLink

```TypeScript
openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>
```

通过App Linking或Deep Linking方式启动UIAbility。使用Promise异步回调。通过在link字段中传入标准格式的URL，基于隐式want匹配规则拉起目标UIAbility。目标方必须具备以下过滤器特征，才能处理App Linking链接：

- "actions"列表中包含"ohos.want.action.viewData"。  
- "entities"列表中包含"entity.system.browsable"。  
- "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。  
如果希望获取被拉起方终止后的结果，可以设置callback参数，此参数的使用可参照  
[startAbilityForResult](#startAbilityForResult)接口。传入的参数不合法时，如未设置必选参数或link字符串不是标准格式的URL，接口会直接抛出异常。参数校验通过，拉起目标方时出现的错误通过promise返回错误信息。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>--><!--Device-UIExtensionContext-openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>-End-->

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
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000069](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000136](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000136-不允许通过app-linking方式拉起应用自身uiability) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## reportDrawnCompleted

```TypeScript
reportDrawnCompleted(callback: AsyncCallback<void>): void
```

用于应用通知系统UIExtensionAbility对应的窗口内容已绘制完成。系统会根据开发者调用的时机进行资源分配优化等，以优化应用启动及显示时间。使用callback异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-reportDrawnCompleted(callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-reportDrawnCompleted(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## setColorMode

```TypeScript
setColorMode(colorMode: ConfigurationConstant.ColorMode): void
```

设置UIExtensionAbility的深浅色模式。调用该接口前需要保证该UIExtensionContext对应页面已完成加载。仅支持主线程调用。

> **说明：**
> 
> - 调用该接口后会创建新的资源管理器对象，如果此前有缓存资源管理器，需要进行更新。
> 
> - 深浅色模式生效的优先级：UIExtensionAbility的深浅色模式 > 应用的深浅色模式（
> [ApplicationContext.setColorMode](./application/ApplicationContext:ApplicationContext.setColorMode)）> 系统的深浅色模
> 式。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void--><!--Device-UIExtensionContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

启动一个UIAbility。使用callback异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-startAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000080](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000069](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000071](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000076](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startAbility

```TypeScript
startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

启动一个UIAbility。使用callback异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

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
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000080](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000069](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000071](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000076](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

启动一个UIAbility。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000080](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000069](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000071](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000076](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void
```

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用  
[terminateSelfWithResult](./application/UIAbilityContext:UIAbilityContext.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback&lt;void&gt;))接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死UIAbility会返回异常信息给调用方, 异常信息中resultCode为-1。  
- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用  
[terminateSelfWithResult](./application/UIAbilityContext:UIAbilityContext.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback&lt;void&gt;))接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000080](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000069](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000071](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000076](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void
```

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用  
[terminateSelfWithResult](./application/UIAbilityContext:UIAbilityContext.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback&lt;void&gt;))接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死UIAbility会返回异常信息给调用方，异常信息中resultCode为-1。  
- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用  
[terminateSelfWithResult](./application/UIAbilityContext:UIAbilityContext.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback&lt;void&gt;))接口使之终止时，只将正常结果返回给最后一个调用方，其它调用方返回异常信息, 异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void-End-->

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
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000080](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000069](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000071](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000076](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
```

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用  
[terminateSelfWithResult](./application/UIAbilityContext:UIAbilityContext.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback&lt;void&gt;))接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死UIAbility会返回异常信息给调用方, 异常信息中resultCode为-1。  
- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用  
[terminateSelfWithResult](./application/UIAbilityContext:UIAbilityContext.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback&lt;void&gt;))接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>-End-->

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
| [16000053](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000053-非顶层ability) |
| [16000055](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000055-免安装超时) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000080](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000080-不支持创建新实例) |
| [16000018](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000018-限制api-11以上版本三方应用跳转) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000069](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000069-严格模式下不允许该类型extension启动三方应用) |
| [16000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000006-不允许跨用户操作) |
| [16000070](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000070-严格模式下不允许该类型extension启动指定serviceextensionability) |
| [16000071](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000071-不支持应用分身模式) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000076](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000076-指定的appinstancekey不存在) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000077](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000077-应用的实例数量已达到上限) |
| [16000078](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000078-不支持应用多实例) |
| [16000079](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000079-不支持指定appinstancekey) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000072](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000072-不支持应用多开) |
| [16000009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000009-wukong模式不允许启动停止ability) |
| [16000073](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000073-传入的appcloneindex是一个无效值) |
| [16000010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000010-不允许带迁移flag) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## startUIServiceExtensionAbility

```TypeScript
startUIServiceExtensionAbility(want: Want): Promise<void>
```

启动一个UIServiceExtensionAbility。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-startUIServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIExtensionContext-startUIServiceExtensionAbility(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

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
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-内部错误) |
| [16000019](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000019-隐式启动未查找到匹配ability) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [16000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000004-可见性校验失败) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [16000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000005-指定的进程权限校验失败) |
| [16000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000001-指定的ability名称不存在) |
| [16000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000002-接口调用ability类型错误) |
| [16200001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16200001-通用组件客户端caller已回收) |
| [16000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000012-应用被管控) |
| [16000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000013-应用被edm管控) |
| [16000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000008-众测应用到期) |
| [16000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000011-上下文对象不存在) |

## terminateSelf

```TypeScript
terminateSelf(callback: AsyncCallback<void>): void
```

销毁UIExtensionAbility自身，同时关闭对应的窗口界面。使用callback异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-terminateSelf(callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-terminateSelf(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

销毁UIExtensionAbility自身，同时关闭对应的窗口界面。使用Promise异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-terminateSelf(): Promise<void>--><!--Device-UIExtensionContext-terminateSelf(): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## terminateSelfWithResult

```TypeScript
terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void
```

销毁UIExtensionAbility自身，同时关闭对应的窗口界面，并将结果返回给UIExtensionAbility的拉起方，拉起方通常为系统服务。使用callback异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## terminateSelfWithResult

```TypeScript
terminateSelfWithResult(parameter: AbilityResult): Promise<void>
```

销毁UIExtensionAbility自身，同时关闭对应的窗口界面，并将结果返回给UIExtensionAbility的拉起方，拉起方通常为系统服务。使用Promise异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult): Promise<void>--><!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
