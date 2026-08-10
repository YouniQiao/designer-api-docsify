# UIAbilityContext

UIAbilityContext是需要保存状态的[UIAbility](arkts-app-ability-uiability.md)所对应的context，继承自[Context](arkts-ability-context-t.md)，提供UIAbility的相关配置信息以及操作UIAbility和ServiceExtensionAbility的方法，如启动UIAbility，停止当前UIAbilityContext所属的UIAbility，启动、停止、连接、断开连接ServiceExtensionAbility等。

**Inheritance/Implementation:** UIAbilityContext extends [Context](arkts-ability-context-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class UIAbilityContext extends Context--><!--Device-unnamed-declare class UIAbilityContext extends Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
connectServiceExtensionAbilityWithAccount(want: Want, accountId: number, options: ConnectOptions): number
```

ArkTS-Sta:
```TypeScript
connectServiceExtensionAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long
```

将当前UIAbility连接到一个指定account的ServiceExtensionAbility。仅支持在主线程调用。该接口在Phone、Tablet中可正常调用，在其他设备类型中返回16000006错误码。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-connectServiceExtensionAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long--><!--Device-UIAbilityContext-connectServiceExtensionAbilityWithAccount(want: Want, accountId: int, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| options | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes | 与ServiceExtensionAbility建立连接后回调函数的实例。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 返回Ability连接的结果code。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI.<br>**Applicable version:** 10 and later |
| 16000055 | Installation-free timed out.<br>**Applicable version:** 10 and later |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed.<br>**Applicable version:** 10 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 10 and later |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000008 | The crowdtesting application expires.<br>**Applicable version:** 10 and later |
| 16000011 | The context does not exist. |

## requestModalUIExtension

```TypeScript
requestModalUIExtension(pickerWant: Want, callback: AsyncCallback<void>): void
```

请求在指定的前台应用上拉起对应类型的UIExtensionAbility。使用callback异步回调。仅支持在主线程调用。其中，前台应用通过want.parameters中bundleName来指定，如果未指定前台应用、bundleName指定的应用未在前台或指定的前台应用的bundleName不正确，则在系统界面上直接拉起UIExtensionAbility；被拉起的UIExtensionAbility通过want中bundleName、abilityName、moduleName字段共同确定，同时需要通过want.parameters中的ability.want.params.uiExtensionType字段配置UIExtensionAbility的类型。在前台应用上拉起UIExtensionAbility之前，必须确保该应用已完成页面初始化，否则将导致拉起失败、并出现"uiContent is nullptr"的报错信息。应用可通过监听页面加载状态来判断拉起UIExtensionAbility的时机，页面初始化成功后会出现关键日志信息"UIContentImpl: focus again"。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-requestModalUIExtension(pickerWant: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-requestModalUIExtension(pickerWant: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pickerWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 拉起UIExtension的Want信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当拉起UIExtension成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 11 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist.<br>**Applicable version:** 11 and later |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 11 and later |
| 16000050 | Internal error. |
| 16200001 | The caller has been released.<br>**Applicable version:** 11 and later |
| 201 | The application does not have permission to call the interface.<br>**Applicable version:** 11 and later |
| 202 | The application is not system-app, can not use system-api. |

## requestModalUIExtension

```TypeScript
requestModalUIExtension(pickerWant: Want): Promise<void>
```

请求在指定的前台应用上拉起对应类型的UIExtensionAbility。使用Promise异步回调。仅支持在主线程调用。其中，前台应用通过want.parameters中bundleName来指定，如果未指定前台应用、bundleName指定的应用未在前台或指定的前台应用的bundleName不正确，则在系统界面上直接拉起UIExtensionAbility；被拉起的UIExtensionAbility通过want中bundleName、abilityName、moduleName字段共同确定，同时需要通过want.parameters中的ability.want.params.uiExtensionType字段配置UIExtensionAbility的类型。在前台应用上拉起UIExtensionAbility之前，必须确保该应用已完成页面初始化，否则将导致拉起失败、并出现"uiContent is nullptr"的报错信息。应用可通过监听页面加载状态来判断拉起UIExtensionAbility的时机，页面初始化成功后会出现关键日志信息"UIContentImpl: focus again"。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-requestModalUIExtension(pickerWant: Want): Promise<void>--><!--Device-UIAbilityContext-requestModalUIExtension(pickerWant: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pickerWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 拉起UIExtension的Want信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 11 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist.<br>**Applicable version:** 11 and later |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 11 and later |
| 16000050 | Internal error. |
| 16200001 | The caller has been released.<br>**Applicable version:** 11 and later |
| 201 | The application does not have permission to call the interface.<br>**Applicable version:** 11 and later |
| 202 | The application is not system-app, can not use system-api. |

## requestModalUIExtensionWithAccount

ArkTS-Dyn:
```TypeScript
requestModalUIExtensionWithAccount(pickerWant: Want, accountId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
requestModalUIExtensionWithAccount(pickerWant: Want, accountId: int): Promise<void>
```

请求指定的前台应用启动对应类型的UIExtensionAbility。指定用户。该接口使用promise返回结果。它只能在主线程上调用。  
> **说明：**
> >
> 关于stage模型中组件的启动规则，请参见
> 【组件启动规则（阶段模型）】(../../../application-models/component-startup-rules.md)。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-requestModalUIExtensionWithAccount(pickerWant: Want, accountId: int): Promise<void>--><!--Device-UIAbilityContext-requestModalUIExtensionWithAccount(pickerWant: Want, accountId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pickerWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 需要用于启动UIExtensionAbility的信息 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要请求的帐户 &lt;br&gt;取值范围为全体整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 不会返回任何值的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. Possible causes: 1.Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. 4.The logical screen corresponding to the specified accountId is not in the foreground. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |

## setMissionIcon

```TypeScript
setMissionIcon(icon: image.PixelMap, callback: AsyncCallback<void>): void
```

设置当前UIAbility在任务中显示的图标，图标大小最大为600M。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-setMissionIcon(icon: image.PixelMap, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-setMissionIcon(icon: image.PixelMap, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | image.PixelMap | Yes | 在最近的任务中显示的UIAbility图标。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当设置当前UIAbility在任务中显示的图标成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |
| 202 | The application is not system-app, can not use system-api.<br>**Applicable version:** 10 and later |
| 16000011 | The context does not exist. |

## setMissionIcon

```TypeScript
setMissionIcon(icon: image.PixelMap): Promise<void>
```

设置当前UIAbility在任务中显示的图标, 图标大小最大为600M。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-setMissionIcon(icon: image.PixelMap): Promise<void>--><!--Device-UIAbilityContext-setMissionIcon(icon: image.PixelMap): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | image.PixelMap | Yes | 在最近的任务中显示的UIAbility图标。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |
| 202 | The application is not system-app, can not use system-api.<br>**Applicable version:** 10 and later |
| 16000011 | The context does not exist. |

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, callback: AsyncCallback<void>): void
```

使用设置的caller信息启动一个UIAbility，caller信息由want携带，在系统服务层识别，UIAbility可以在onCreate生命周期的want参数中获取到caller信息。使用该接口启动一个UIAbility时，want的caller信息不会被当前自身的应用信息覆盖，系统服务层可获取到初始caller的信息。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
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

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

使用设置的caller信息启动一个UIAbility，caller信息由want携带，在系统服务层识别，UIAbility可以在onCreate生命周期的want参数中获取到caller信息。使用该接口启动一个UIAbility时，want的caller信息不会被当前自身的应用信息覆盖，系统服务层可获取到初始caller的信息。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | Yes | 启动UIAbility所携带的参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
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

## startAbilityAsCaller

```TypeScript
startAbilityAsCaller(want: Want, options?: StartOptions): Promise<void>
```

使用设置的caller信息启动一个UIAbility，caller信息由want携带，在系统服务层识别，UIAbility可以在onCreate生命周期的want参数中获取到caller信息。使用该接口启动一个UIAbility时，want的caller信息不会被当前自身的应用信息覆盖，系统服务层可获取到初始caller的信息。使用Promise异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIAbilityContext-startAbilityAsCaller(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | No | 启动UIAbility所携带的参数。 |

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
| 202 | The application is not system-app, can not use system-api. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
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

## startAbilityByCallWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityByCallWithAccount(want: Want, accountId: number): Promise<Caller>
```

ArkTS-Sta:
```TypeScript
startAbilityByCallWithAccount(want: Want, accountId: int): Promise<Caller>
```

根据accountId对指定的UIAbility进行call调用，并且可以使用返回的Caller通信接口与被调用方进行通信。仅支持在主线程调用。使用Promise异步回调。该接口不支持拉起启动模式为[specified模式](../../../application-models/uiability-launch-type.md#specified启动模式)的UIAbility。使用规则：

- 跨用户场景下，Call调用目标UIAbility时，调用方应用需同时申请`ohos.permission.ABILITY_BACKGROUND_COMMUNICATION`与`  
ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS`权限。  
- 调用方应用位于后台时，使用该接口启动UIAbility需申请`ohos.permission.START_ABILITIES_FROM_BACKGROUND`权限。  
- 跨应用场景下，目标UIAbility的exported属性若配置为false，调用方应用需申请`ohos.permission.START_INVISIBLE_ABILITY`权限。  
- 同设备与跨设备场景下，该接口的使用规则存在差异，详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ABILITY_BACKGROUND_COMMUNICATION and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityByCallWithAccount(want: Want, accountId: int): Promise<Caller>--><!--Device-UIAbilityContext-startAbilityByCallWithAccount(want: Want, accountId: int): Promise<Caller>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 传入需要启动的UIAbility的信息，包含abilityName、moduleName、bundleName、deviceId(可选)、parameters(可选)，其中deviceId缺省或 为空表示启动本地UIAbility，parameters缺省或为空表示后台启动UIAbility。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，-1表示当前活动用户，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Caller](arkts-ability-app-ability-uiability-caller-i.md)&gt; | Promise对象，返回要通讯的caller对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
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
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000011 | The context does not exist. |

## startAbilityForResultWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityForResultWithAccount(want: Want, accountId: number, callback: AsyncCallback<AbilityResult>): void
```

ArkTS-Sta:
```TypeScript
startAbilityForResultWithAccount(want: Want, accountId: int, callback: AsyncCallback<AbilityResult>): void
```

启动一个UIAbility并在该UIAbility销毁时返回执行结果。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityForResultWithAccount(want: Want, accountId: int, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIAbilityContext-startAbilityForResultWithAccount(want: Want, accountId: int, callback: AsyncCallback<AbilityResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Yes | 回调函数，当接口调用成功，err中code为0，data为被拉起的UIAbility销毁时的结果码和数据；否则err会返回对应的错误码和错 误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startAbilityForResultWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityForResultWithAccount(
    want: Want,
    accountId: number,
    options: StartOptions,
    callback: AsyncCallback<void>
  ): void
```

ArkTS-Sta:
```TypeScript
startAbilityForResultWithAccount(
    want: Want,
    accountId: int,
    options: StartOptions,
    callback: AsyncCallback<void>
  ): void
```

启动一个UIAbility并在该UIAbility销毁时返回执行结果。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityForResultWithAccount(    want: Want,    accountId: int,    options: StartOptions,    callback: AsyncCallback<void>  ): void--><!--Device-UIAbilityContext-startAbilityForResultWithAccount(    want: Want,    accountId: int,    options: StartOptions,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | Yes | 启动UIAbility所携带的参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 9 and later |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden.<br>**Applicable version:** 9 and later |
| 16000011 | The context does not exist. |

## startAbilityForResultWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityForResultWithAccount(want: Want, accountId: number, options?: StartOptions): Promise<AbilityResult>
```

ArkTS-Sta:
```TypeScript
startAbilityForResultWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<AbilityResult>
```

启动一个UIAbility并在该UIAbility销毁时返回执行结果。使用Promise异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityForResultWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIAbilityContext-startAbilityForResultWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | No | 启动UIAbility所携带的参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Promise对象，包含AbilityResult参数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
startAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void
```

根据want和accountId启动UIAbility。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
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

## startAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityWithAccount(want: Want, accountId: number, options: StartOptions, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
startAbilityWithAccount(want: Want, accountId: int, options: StartOptions, callback: AsyncCallback<void>): void
```

根据want、accountId及startOptions启动UIAbility。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | Yes | 启动UIAbility所携带的参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 9 and later |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden.<br>**Applicable version:** 9 and later |
| 16000011 | The context does not exist. |

## startAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startAbilityWithAccount(want: Want, accountId: number, options?: StartOptions): Promise<void>
```

ArkTS-Sta:
```TypeScript
startAbilityWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<void>
```

根据want、accountId和startOptions启动UIAbility。使用Promise异步回调。仅支持在主线程调用。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<void>--><!--Device-UIAbilityContext-startAbilityWithAccount(want: Want, accountId: int, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动UIAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | No | 启动UIAbility所携带的参数。 |

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
| 202 | The application is not system-app, can not use system-api. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
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

## startRecentAbility

```TypeScript
startRecentAbility(want: Want, callback: AsyncCallback<void>): void
```

启动一个指定的UIAbility，如果这个UIAbility有多个实例，将拉起最近启动的那个实例。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> - 跨设备场景下，调用方与目标方必须为同一应用，且该应用需要具备ohos.permission.DISTRIBUTED_DATASYNC权限，才能启动成功。
> 
> - 跨应用场景下，目标UIAbility的visible属性若配置为false，调用方应用需申请ohos.permission.START_INVISIBLE_ABILITY权限。
> 
> - 如果指定的UIAbility有多个实例，调用方应用需申请ohos.permission.START_RECENT_ABILITY权限（该权限仅系统应用可申请），才能拉起最近启动的那个实例。
> 
> - 如果调用方位于后台，还需要具备ohos.permission.START_ABILITIES_FROM_BACKGROUND（该权限仅系统应用可申请）。
> 更多的组件启动规则详见[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startRecentAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startRecentAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 需要启动UIAbility的Want信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface.<br>**Applicable version:** 10 and later |
| 202 | The application is not system-app, can not use system-api.<br>**Applicable version:** 14 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startRecentAbility

```TypeScript
startRecentAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

启动一个指定的UIAbility。如果这个UIAbility有多个实例，将拉起最近启动的那个实例。当开发者需要携带启动参数时可以选择此API。使用callback异步回调。仅支持在主线程调用。

> **说明：**
> 
> - 跨设备场景下，调用方与目标方必须为同一应用，且该应用需要具备ohos.permission.DISTRIBUTED_DATASYNC权限，才能启动成功。
> 
> - 跨应用场景下，目标UIAbility的visible属性若配置为false，调用方应用需申请ohos.permission.START_INVISIBLE_ABILITY权限。
> 
> - 如果指定的UIAbility有多个实例，调用方应用需申请ohos.permission.START_RECENT_ABILITY权限（该权限仅系统应用可申请），才能拉起最近启动的那个实例。
> 
> - 如果调用方位于后台，还需要具备ohos.permission.START_ABILITIES_FROM_BACKGROUND（该权限仅系统应用可申请）。
> 更多的组件启动规则详见[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startRecentAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startRecentAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 需要启动UIAbility的Want信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | Yes | 启动UIAbility所携带的参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface.<br>**Applicable version:** 10 and later |
| 202 | The application is not system-app, can not use system-api.<br>**Applicable version:** 14 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type.<br>**Applicable version:** 9 and later |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden.<br>**Applicable version:** 9 and later |
| 16000011 | The context does not exist. |

## startRecentAbility

```TypeScript
startRecentAbility(want: Want, options?: StartOptions): Promise<void>
```

启动一个指定的UIAbility。如果这个UIAbility有多个实例，将拉起最近启动的那个实例。使用Promise异步回调。仅支持在主线程调用。

> **说明：**
> 
> - 跨设备场景下，调用方与目标方必须为同一应用，且该应用需要具备ohos.permission.DISTRIBUTED_DATASYNC权限，才能启动成功。
> 
> - 跨应用场景下，目标UIAbility的visible属性若配置为false，调用方应用需申请ohos.permission.START_INVISIBLE_ABILITY权限。
> 
> - 如果指定的UIAbility有多个实例，调用方应用需申请ohos.permission.START_RECENT_ABILITY权限（该权限仅系统应用可申请），才能拉起最近启动的那个实例。
> 
> - 如果调用方位于后台，还需要具备ohos.permission.START_ABILITIES_FROM_BACKGROUND（该权限仅系统应用可申请）。
> 更多的组件启动规则详见[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startRecentAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIAbilityContext-startRecentAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 需要启动UIAbility的Want信息。 |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c-sys.md) | No | 启动UIAbility所携带的参数。 |

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
| 201 | The application does not have permission to call the interface.<br>**Applicable version:** 10 and later |
| 202 | The application is not system-app, can not use system-api.<br>**Applicable version:** 14 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000080 | Creating a new instance is not supported.<br>**Applicable version:** 14 and later |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000071 | App clone is not supported.<br>**Applicable version:** 14 and later |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000076 | The app instance key is invalid.<br>**Applicable version:** 14 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000077 | The number of app instances reaches the limit.<br>**Applicable version:** 14 and later |
| 16000078 | The multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000079 | The APP_INSTANCE_KEY cannot be specified.<br>**Applicable version:** 14 and later |
| 16000008 | The crowdtesting application expires. |
| 16000072 | App clone or multi-instance is not supported.<br>**Applicable version:** 14 and later |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000073 | The app clone index is invalid.<br>**Applicable version:** 12 and later |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void
```

启动一个新的ServiceExtensionAbility。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动ServiceExtensionAbility的Want信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## startServiceExtensionAbility

```TypeScript
startServiceExtensionAbility(want: Want): Promise<void>
```

启动一个新的ServiceExtensionAbility。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIAbilityContext-startServiceExtensionAbility(want: Want): Promise<void>-End-->

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
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## startServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
startServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void
```

启动一个新的ServiceExtensionAbility。使用callback异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动ServiceExtensionAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
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

启动一个新的ServiceExtensionAbility。使用Promise异步回调。

> **说明：**
> 
> 组件启动规则详见：[组件启动规则（Stage模型）](../../../application-models/component-startup-rules.md)。
> > 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>--><!--Device-UIAbilityContext-startServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 启动ServiceExtensionAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 16000019 | No matching ability is found.<br>**Applicable version:** 12 and later |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |

## stopServiceExtensionAbility

```TypeScript
stopServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void
```

停止指定的ServiceExtensionAbility后台服务。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-stopServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-stopServiceExtensionAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 停止ServiceExtensionAbility的Want信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当停止ServiceExtensionAbility的接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000050 | Internal error. |
| 201 | The application does not have permission to call the interface.<br>**Applicable version:** 10 and later |
| 202 | The application is not system-app, can not use system-api. |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16200001 | The caller has been released. |
| 16000012 | The application is controlled.<br>**Applicable version:** 10 and later |
| 16000013 | The application is controlled by EDM.<br>**Applicable version:** 10 and later |
| 16000011 | The context does not exist. |

## stopServiceExtensionAbility

```TypeScript
stopServiceExtensionAbility(want: Want): Promise<void>
```

停止同一应用程序内的服务。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-stopServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIAbilityContext-stopServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 停止ServiceExtensionAbility的Want信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |
| 201 | The application does not have permission to call the interface.<br>**Applicable version:** 10 and later |
| 202 | The application is not system-app, can not use system-api. |
| 16000011 | The context does not exist. |

## stopServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
stopServiceExtensionAbilityWithAccount(want: Want, accountId: number, callback: AsyncCallback<void>): void
```

ArkTS-Sta:
```TypeScript
stopServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void
```

停止同一应用程序内指定账户的服务。使用callback异步回调。

> **说明：**
> 
> 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-stopServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void--><!--Device-UIAbilityContext-stopServiceExtensionAbilityWithAccount(want: Want, accountId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 停止ServiceExtensionAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，当停止ServiceExtensionAbility的接口调用成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000011 | The context does not exist. |

## stopServiceExtensionAbilityWithAccount

ArkTS-Dyn:
```TypeScript
stopServiceExtensionAbilityWithAccount(want: Want, accountId: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
stopServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>
```

停止同一应用程序内指定账户的服务。使用Promise异步回调。

> **说明：**
> 
> 当accountId为当前用户时，无需进行权限校验。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIAbilityContext-stopServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>--><!--Device-UIAbilityContext-stopServiceExtensionAbilityWithAccount(want: Want, accountId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | 停止ServiceExtensionAbility的Want信息。 |
| accountId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 系统账号的账号ID，可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid) 接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000004 | Cannot start an invisible component.<br>**Applicable version:** 10 and later |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |
| 201 | The application does not have permission to call the interface. |
| 202 | The application is not system-app, can not use system-api. |
| 16000011 | The context does not exist. |

