# UIExtensionContext

UIExtensionContext是[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)的上下文环境，继承自  
[ExtensionContext](arkts-ability-extensioncontext-c.md)，提供UIExtensionAbility的相关配置信息以及操作UIAbility的方法，如启动UIAbility等。

**Inheritance/Implementation:** UIExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class UIExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class UIExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

ArkTS-Sta:
```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): long
```

将当前UIExtensionAbility连接到一个ServiceExtensionAbility，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。ServiceExtensionAbility是一类特殊的[ExtensionAbility](../../../application-models/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-UIExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 连接ServiceExtensionAbility的Want信息，包括Ability名称，Bundle名称等。 |
| options | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes | ConnectOptions类型的回调函数，返回服务连接成功、连接失败、断开的信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 返回连接id，客户端可以通过 [disconnectServiceExtensionAbility]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000070 | The extension cannot start the service. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## connectUIServiceExtensionAbility

```TypeScript
connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>
```

连接到一个UIServiceExtensionAbility。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>--><!--Device-UIExtensionContext-connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 用于连接的Want信息。 |
| callback | [UIServiceExtensionConnectCallback](arkts-ability-uiserviceextensionconnectcallback-i.md) | Yes | 连接UIServiceExtensionAbility回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[UIServiceProxy](arkts-ability-uiserviceproxy-i.md)&gt; | Promise对象，连接UIServiceExtensionAbility成功时，返回 [UIServiceProxy]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 16000005 | The specified process does not have the permission. |
| 16000055 | Installation-free timed out. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## disconnectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void
```

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用callback异步回调。ServiceExtensionAbility是一类特殊的[ExtensionAbility](../../../application-models/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 连接的ServiceExtensionAbility的标识Id，即connectServiceExtensionAbility返回的connectionId。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当断开与ServiceExtensionAbility的连接成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |
| 16000011 | The context does not exist. |

## disconnectServiceExtensionAbility

ArkTS-Dyn:
```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
disconnectServiceExtensionAbility(connection: long): Promise<void>
```

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用Promise异步回调。ServiceExtensionAbility是一类特殊的[ExtensionAbility](../../../application-models/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 连接的ServiceExtensionAbility的标识Id，即 [connectServiceExtensionAbility](arkts-ability-uiextensioncontext-c.md#connectserviceextensionability)返回的connectionId。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |
| 16000011 | The context does not exist. |

## disconnectUIServiceExtensionAbility

```TypeScript
disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>
```

断开UIServiceExtensionAbility。使用Promise异步回调。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>--><!--Device-UIExtensionContext-disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| proxy | [UIServiceProxy](arkts-ability-uiserviceproxy-i.md) | Yes | [connectUIServiceExtensionAbility](arkts-ability-uiextensioncontext-c.md#connectuiserviceextensionability)返回的Proxy。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000050 | Internal error. |
| 16000011 | The context does not exist. |

## openAtomicService

```TypeScript
openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>
```

打开一个独立窗口的原子化服务，并返回结果。使用Promise异步回调。分为以下几种情况：

- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死原子化服务会返回异常信息给调用方，异常信息中resultCode为-1。  
- 如果不同应用多次调用该接口启动同一个原子化服务，当这个原子化服务调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息，异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | 应用的唯一标识，由云端统一分配。 |
| options | [AtomicServiceOptions](arkts-ability-app-ability-atomicserviceoptions-atomicserviceoptions-c.md) | No | 启动原子化服务所携带的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Promise对象。返回给拉起方的信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000069 | The extension cannot start the third party application. |
| 16000002 | Incorrect ability type. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |
| 16000003 | The specified ID does not exist. |
| 16000012 | The application is controlled. |
| 16000011 | The context does not exist. |

## openLink

```TypeScript
openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>
```

通过App Linking或Deep Linking方式启动UIAbility。使用Promise异步回调。通过在link字段中传入标准格式的URL，基于隐式want匹配规则拉起目标UIAbility。目标方必须具备以下过滤器特征，才能处理App Linking链接：

- "actions"列表中包含"ohos.want.action.viewData"。  
- "entities"列表中包含"entity.system.browsable"。  
- "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。  
如果希望获取被拉起方终止后的结果，可以设置callback参数，此参数的使用可参照  
[startAbilityForResult](arkts-ability-uiextensioncontext-c.md#startabilityforresult)接口。传入的参数不合法时，如未设置必选参数或link字符串不是标准格式的URL，接口会直接抛出异常。参数校验通过，拉起目标方时出现的错误通过promise返回错误信息。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>--><!--Device-UIExtensionContext-openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| link | string | Yes | 指示要打开的标准格式URL。 |
| options | [OpenLinkOptions](arkts-ability-app-ability-openlinkoptions-openlinkoptions-i.md) | No | 打开URL的选项参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | No | 回调函数，包含返回给拉起方的信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000019 | No matching ability is found. |
| 201 | The application does not have permission to call the interface. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000069 | The extension cannot start the third party application. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000136 | The UIAbility is prohibited from launching itself via App Linking.<br>**Applicable version:** 23 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## reportDrawnCompleted

```TypeScript
reportDrawnCompleted(callback: AsyncCallback<void>): void
```

用于应用通知系统UIExtensionAbility对应的窗口内容已绘制完成。系统会根据开发者调用的时机进行资源分配优化等，以优化应用启动及显示时间。使用callback异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-reportDrawnCompleted(callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-reportDrawnCompleted(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当打点成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 16000011 | The context does not exist. |

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
> [ApplicationContext.setColorMode](arkts-ability-applicationcontext-c.md#setcolormode)）> 系统的深浅色模
> 式。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void--><!--Device-UIExtensionContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | Yes | 设置颜色模式，包括：&lt;br&gt; - COLOR_MODE_DARK：深色模式 &lt;br&gt; - COLOR_MODE_LIGHT：浅色模 式 &lt;br&gt; - COLOR_MODE_NOT_SET：不设置（跟随系统或应用） |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000011 | The context does not exist. |

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

启动一个UIAbility。使用callback异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-startAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当启动UIAbility成功时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11.<br>**Applicable version:** 12 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000069 | The extension cannot start the third party application.<br>**Applicable version:** 12 and later |
| 16000006 | Cross-user operations are not allowed. |
| 16000070 | The extension cannot start the service.<br>**Applicable version:** 12 and later |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM. |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startAbility

```TypeScript
startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

启动一个UIAbility。使用callback异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | Yes | 启动UIAbility所携带的额外参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当启动UIAbility成功时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11.<br>**Applicable version:** 12 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000069 | The extension cannot start the third party application.<br>**Applicable version:** 12 and later |
| 16000006 | Cross-user operations are not allowed. |
| 16000070 | The extension cannot start the service.<br>**Applicable version:** 12 and later |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM. |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000011 | The context does not exist. |

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

启动一个UIAbility。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No | 启动UIAbility所携带的额外参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11.<br>**Applicable version:** 12 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000069 | The extension cannot start the third party application.<br>**Applicable version:** 12 and later |
| 16000006 | Cross-user operations are not allowed. |
| 16000070 | The extension cannot start the service.<br>**Applicable version:** 12 and later |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM. |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void
```

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死UIAbility会返回异常信息给调用方, 异常信息中resultCode为-1。  
- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Yes | 回调函数，包含返回给拉起方的信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11.<br>**Applicable version:** 12 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000069 | The extension cannot start the third party application.<br>**Applicable version:** 12 and later |
| 16000006 | Cross-user operations are not allowed. |
| 16000070 | The extension cannot start the service.<br>**Applicable version:** 12 and later |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM. |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void
```

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死UIAbility会返回异常信息给调用方，异常信息中resultCode为-1。  
- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方，其它调用方返回异常信息, 异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | Yes | 启动UIAbility所携带的额外参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Yes | 回调函数，包含返回给拉起方的信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11.<br>**Applicable version:** 12 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000069 | The extension cannot start the third party application.<br>**Applicable version:** 12 and later |
| 16000006 | Cross-user operations are not allowed. |
| 16000070 | The extension cannot start the service.<br>**Applicable version:** 12 and later |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM. |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000011 | The context does not exist. |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
```

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。UIAbility被启动后，有如下情况:

- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死UIAbility会返回异常信息给调用方, 异常信息中resultCode为-1。  
- 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No | 启动UIAbility所携带的额外参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Promise对象，返回被拉起的UIAbility退出时的返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11.<br>**Applicable version:** 12 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000069 | The extension cannot start the third party application.<br>**Applicable version:** 12 and later |
| 16000006 | Cross-user operations are not allowed. |
| 16000070 | The extension cannot start the service.<br>**Applicable version:** 12 and later |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM. |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startUIServiceExtensionAbility

```TypeScript
startUIServiceExtensionAbility(want: Want): Promise<void>
```

启动一个UIServiceExtensionAbility。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startUIServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIExtensionContext-startUIServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIServiceExtensionAbility的Want。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Internal error. |
| 16000019 | No matching ability is found. |
| 201 | The application does not have permission to call the interface. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000005 | The specified process does not have the permission. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## terminateSelf

```TypeScript
terminateSelf(callback: AsyncCallback<void>): void
```

销毁UIExtensionAbility自身，同时关闭对应的窗口界面。使用callback异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-terminateSelf(callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-terminateSelf(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。UIExtensionAbility停止成功时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

销毁UIExtensionAbility自身，同时关闭对应的窗口界面。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-terminateSelf(): Promise<void>--><!--Device-UIExtensionContext-terminateSelf(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

## terminateSelfWithResult

```TypeScript
terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void
```

销毁UIExtensionAbility自身，同时关闭对应的窗口界面，并将结果返回给UIExtensionAbility的拉起方，拉起方通常为系统服务。使用callback异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes | 返回给UIExtensionAbility拉起方的信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。UIExtensionAbility停止成功时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

## terminateSelfWithResult

```TypeScript
terminateSelfWithResult(parameter: AbilityResult): Promise<void>
```

销毁UIExtensionAbility自身，同时关闭对应的窗口界面，并将结果返回给UIExtensionAbility的拉起方，拉起方通常为系统服务。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult): Promise<void>--><!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes | 返回给UIExtensionAbility拉起方的信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

