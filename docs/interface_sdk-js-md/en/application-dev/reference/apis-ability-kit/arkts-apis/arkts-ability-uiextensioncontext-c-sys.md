# UIExtensionContext

UIExtensionContext是[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)的上下文环境，继承自  
[ExtensionContext](arkts-ability-extensioncontext-c.md)，提供UIExtensionAbility的相关配置信息以及操作UIAbility的方法，如启动UIAbility等。

**Inheritance/Implementation:** UIExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class UIExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class UIExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbilityWithRootHostToken

ArkTS-Dyn:
```TypeScript
connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): number
```

ArkTS-Sta:
```TypeScript
connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): long
```

将当前UIExtensionAbility连接到一个  
[ServiceExtensionAbility](arkts-ability-app-ability-serviceextensionability-serviceextensionability-c-sys.md#onconnect)，通过返回的远程代理对象与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。与此同时，该方法会将UIExtensionAbility的原始宿主Ability的Token传递给被连接的ServiceExtensionAbility，ServiceExtensionAbility可以在  
[onCreate()](arkts-ability-app-ability-serviceextensionability-serviceextensionability-c-sys.md#oncreate)或  
[onConnect()](arkts-ability-app-ability-serviceextensionability-serviceextensionability-c-sys.md#onconnect)方法中，通过Want参数的  
[UI_EXTENSION_ROOT_TOKEN](arkts-ability-wantconstant-params-e.md)获取该Token。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): long--><!--Device-UIExtensionContext-connectServiceExtensionAbilityWithRootHostToken(want: Want, connect: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 连接ServiceExtensionAbility的Want信息，包括Ability名称、Bundle名称等。 |
| connect | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes | ConnectOptions类型的回调函数，返回服务连接成功、连接失败、断开的信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 返回连接标识ID，客户端可以通过 [disconnectServiceExtensionAbility](../../../reference/apis-ability-kit/js-apis-inner-application-uiExtensionContext.md#disconnectserviceextensionability) 传入该连接标识ID来断开连接。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |
| 201 | The application does not have permission to call the interface. Possible cause: target service extension ability is in cross-device and needed designated permission to be started, but call ability do not have this permission. |
| 202 | Not system application |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000070 | The extension cannot start the service. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## setHostPageOverlayForbidden

```TypeScript
setHostPageOverlayForbidden(isForbidden: boolean) : void
```

是否允许[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)拉起的页面被使用方的页面覆盖。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> 
> 该接口需要在窗口创建之前调用。建议在[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md)的
> [onCreate](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md#oncreate)生命周期内调用。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-setHostPageOverlayForbidden(isForbidden: boolean) : void--><!--Device-UIExtensionContext-setHostPageOverlayForbidden(isForbidden: boolean) : void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isForbidden | boolean | Yes | 是否允许[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md) 拉起的页面被使用方的页面覆盖。true表示不允许，false表示允许。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 202 | The application is not system-app, can not use system-api. |

## startAbilityForResultAsCaller

```TypeScript
startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>
```

使用设置的caller信息启动一个Ability，caller信息由want携带，在系统服务层识别，Ability可以在onCreate生命周期的want参数中获取到caller信息。使用该接口启动一个Ability时，want的caller信息不会被当前自身的应用信息覆盖，系统服务层可获取到初始caller的信息。使用Promise异步回调。

- 正常情况下可通过调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。  
- 异常情况下比如杀死Ability会返回异常信息给调用方，异常信息中resultCode为-1。  
- 如果被启动的Ability模式是单实例模式，不同应用多次调用该接口启动这个Ability，当这个Ability调用  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方，其它调用方返回异常信息，异常信息中resultCode为-1。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-startAbilityForResultAsCaller(want: Want, options?: StartOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动Ability的want信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | No | 启动Ability所携带的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Promise对象，返回Ability结果对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | Not System App. Interface caller is not a system app. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000073 | The app clone index is invalid. |

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want): Promise<void>
```

启动一个ServiceExtensionAbility。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIExtensionContext-startServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动ServiceExtensionAbility的Want信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 16000019 | No matching ability is found. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## startServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>
```

启动一个指定系统账号下的ServiceExtensionAbility。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> 
> 当accountId为当前用户时，无需进行权限校验。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>--><!--Device-UIExtensionContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动ServiceExtensionAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 16000019 | No matching ability is found. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## startUIAbilities

```TypeScript
startUIAbilities(wantList: Array<Want>): Promise<void>
```

同时启动多个UIAbility。使用Promise异步回调。开发者可以传入多个UIAbility对应的Want信息，这些UIAbility可以指向一个或多个应用。当所有的UIAbility都能启动成功时，系统会通过多个窗口同时展示这些UIAbility。根据窗口的处理，不同设备上可能会有不同的展示效果（包括窗口形态、数量和排版布局）。该接口仅在Phone和Tablet设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startUIAbilities(wantList: Array<Want>): Promise<void>--><!--Device-UIExtensionContext-startUIAbilities(wantList: Array<Want>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wantList | Array&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | Yes | 需要被同时拉起的多个UIAbility的启动参数列表，最多支持传入4个Want。启动参数Want不支持隐式启动、跨用户启动、分布式、免安装和按需加载，不指明分身的情况下默认 启动主应用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 16000080 | Creating a new instance is not supported. |
| 16000050 | Internal error. |
| 16000124 | Starting a remote UIAbility is not supported. |
| 201 | The application does not have permission to call the interface. |
| 16000125 | Starting a plugin UIAbility is not supported. |
| 202 | Not system application. |
| 16000126 | Starting DLP files is not supported. |
| 16000120 | A maximum of four UIAbility instances can be started simultaneously. The current parameter exceeds the maximum number or is less than 1. |
| 16000121 | The target component type is not a UIAbility. |
| 16000122 | The target component is blocked by the system module and does not support startup. |
| 16000123 | Implicit startup is not supported. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16200001 | The caller has been released. |
| 16000076 | The app instance key is invalid. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid. |
| 16000011 | The context does not exist. |

## startUIAbilitiesInSplitWindowMode

ArkTS-Dyn:
```TypeScript
startUIAbilitiesInSplitWindowMode(primaryWindowId: number, secondaryWant: Want): Promise<void>
```

ArkTS-Sta:
```TypeScript
startUIAbilitiesInSplitWindowMode(primaryWindowId: int, secondaryWant: Want): Promise<void>
```

当第一个UIAbility实例被创建后，启动第二个UIAbility，并以分屏模式进行显示。使用Promise异步回调。该接口仅在Phone设备中可正常调用，在其他设备中返回801错误码。

> **说明：**
> 
> 如果第一个UIAbility实例被销毁，那么第二个UIAbility将以全屏模式启动。
> 
> 第二个UIAbility仅支持[显示启动](../../../application-models/explicit-implicit-want-mappings.md#显式want匹配原理)。
> 
> 如果调用方位于后台，还需要具备ohos.permission.START_ABILITIES_FROM_BACKGROUND (该权限仅系统应用可申请)。
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.START_ABILITIES_FROM_BACKGROUND

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startUIAbilitiesInSplitWindowMode(primaryWindowId: int, secondaryWant: Want): Promise<void>--><!--Device-UIExtensionContext-startUIAbilitiesInSplitWindowMode(primaryWindowId: int, secondaryWant: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| primaryWindowId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 启动第一个UIAbility的主窗的窗口ID。窗口ID是 [WindowProperties](../../../reference/apis-arkui/arkts-apis-window-i.md#windowproperties)的属性，WindowProperties可通过 [getWindowProperties()](../../../reference/apis-arkui/arkts-apis-window-Window.md#getwindowproperties9)获取。 |
| secondaryWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动第二个UIAbility所需的Want信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 16000080 | Creating a new instance is not supported. |
| 16000050 | Failed to connect to the system service or system server handle failed. |
| 16000124 | Starting a remote UIAbility is not supported. |
| 201 | The application does not have permission to call the interface. |
| 16000125 | Starting a plugin UIAbility is not supported. |
| 202 | Not system application. |
| 16000126 | Starting DLP files is not supported. |
| 16000122 | The target component is blocked by the system module and does not support startup. |
| 16000123 | Implicit startup is not supported. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | Target UIAbility does not exist. |
| 16000076 | The app instance key is invalid. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid. |
| 16000011 | The context does not exist. |

