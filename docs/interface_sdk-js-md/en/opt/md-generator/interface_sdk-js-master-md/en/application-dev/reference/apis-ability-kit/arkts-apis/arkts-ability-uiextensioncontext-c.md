# UIExtensionContext

UIExtensionContext provides the context environment for  
[UIExtensionAbility](arkts-ability-app-ability-uiextensionability-uiextensionability-c.md). It inherits from  
[ExtensionContext](arkts-ability-extensioncontext-c.md) and provides UIExtensionAbility-related configuration and APIs for operating the UIExtensionAbility. For example, you can use the APIs to start a UIExtensionAbility.

**Inheritance/Implementation:** UIExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**Since:** 10

<!--Device-unnamed-declare class UIExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class UIExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

Connects this UIExtensionAbility to a ServiceExtensionAbility. It enables communication with the ServiceExtensionAbility via a proxy, allowing access to the capabilities exposed by the ServiceExtensionAbility.ServiceExtensionAbility is a special type of  
[ExtensionAbility](../../../application-models/extensionability-overview.md) provided by the system. It is designed to offer background services for specific scenarios and is not customizable by developers. It can be connected to by other components and handles requests in the background based on the caller information.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-UIExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## connectUIServiceExtensionAbility

```TypeScript
connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>
```

Connects to a UIServiceExtensionAbility. This API uses a promise to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>--><!--Device-UIExtensionContext-connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [UIServiceExtensionConnectCallback](arkts-ability-uiserviceextensionconnectcallback-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UIServiceProxy](arkts-ability-uiserviceproxy-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void
```

Disconnects from a ServiceExtensionAbility. Once the connection is terminated, set the remote object, which is returned when the connection is established, to null. This API uses an asynchronous callback to return the result.ServiceExtensionAbility is a special type of  
[ExtensionAbility](../../../application-models/extensionability-overview.md) provided by the system. It is designed to offer background services for specific scenarios and is not customizable by developers. It can be connected to by other components and handles requests in the background based on the caller information.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connection | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

Disconnects from a ServiceExtensionAbility. Once the connection is terminated, set the remote object, which is returned when the connection is established, to null. This API uses a promise to return the result.ServiceExtensionAbility is a special type of  
[ExtensionAbility](../../../application-models/extensionability-overview.md) provided by the system. It is designed to offer background services for specific scenarios and is not customizable by developers. It can be connected to by other components and handles requests in the background based on the caller information.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-UIExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connection | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## disconnectUIServiceExtensionAbility

```TypeScript
disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>
```

Disconnects from a UIServiceExtensionAbility. This API uses a promise to return the result.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>--><!--Device-UIExtensionContext-disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| proxy | [UIServiceProxy](arkts-ability-uiserviceproxy-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## openAtomicService

```TypeScript
openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>
```

Opens an atomic service in an independent window and returns the result. This API uses a promise to return the result.The following situations may be possible for a started atomic service:

- Normally, you can call  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the atomic service. The result is returned to the caller.  
- If an exception occurs, for example, the atomic service is killed, an error message, in which **resultCode** is  
**-1**, is returned to the caller.  
- If different applications call this API to start an atomic service and then call  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the atomic service, the normal result is returned to the last caller, and an exception message, in which **resultCode** is **-1**, is returned to others.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appId | string | Yes |
| options | [AtomicServiceOptions](arkts-ability-app-ability-atomicserviceoptions-atomicserviceoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## openLink

```TypeScript
openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>
```

Starts a UIAbility by using App Linking or Deep Linking. This API uses a promise to return the result.A URL in the standard format is passed in to the **link** field to start the target UIAbility based on the implicit  Want matching rules. The target UIAbility must have the following filter characteristics to process links of App Linking:

- The **actions** field must contain **ohos.want.action.viewData**.  
- The **entities** field must contain **entity.system.browsable**.  
- The **uris** field must contain elements whose **scheme** is **https** and **domainVerify** is **true**.  
If you want to obtain the result after the started UIAbility is terminated, set the **callback** parameter. For details about how to use this parameter, see  
[startAbilityForResult](arkts-ability-uiextensioncontext-c.md#startabilityforresult).If an input parameter is invalid, for example, a mandatory parameter is not set or the URL set in **link** is not in the standard format, an exception is thrown. If the parameter verification is successful but an error occurs when starting the target UIAbility, the error information is returned through promise.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>--><!--Device-UIExtensionContext-openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| link | string | Yes |
| options | [OpenLinkOptions](arkts-ability-app-ability-openlinkoptions-openlinkoptions-i.md) | No |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000136](../errorcode-ability.md#16000136-prohibited-from-launching-the-applications-own-uiability-via-app-linking) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## reportDrawnCompleted

```TypeScript
reportDrawnCompleted(callback: AsyncCallback<void>): void
```

Called when the window content associated with the UIExtensionAbility finishes drawing. The system uses the information to optimize resource allocation, thereby enhancing the efficiency of application startup and display.This API uses an asynchronous callback to return the result.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-reportDrawnCompleted(callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-reportDrawnCompleted(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## setColorMode

```TypeScript
setColorMode(colorMode: ConfigurationConstant.ColorMode): void
```

Sets the dark/light color mode for this UIExtensionAbility. Before calling this API, ensure that the page corresponding to the UIExtensionContext has been loaded. This API can be called only by the main thread.

> **NOTE：**
> 
> - After this API is called, a new resource manager object is created. If a resource manager was previously cached
> , it should be updated accordingly.
> 
> - The priority of the dark/light color mode is as follows: UIExtensionAbility dark/light color mode > Application
> dark/light color mode (set via
> [ApplicationContext.setColorMode](arkts-ability-applicationcontext-c.md#setcolormode)) > System
> dark/light color mode.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void--><!--Device-UIExtensionContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbility

```TypeScript
startAbility(want: Want, callback: AsyncCallback<void>): void
```

Starts a UIAbility. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbility(want: Want, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-startAbility(want: Want, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000018](../errorcode-ability.md#16000018-restricting-redirection-to-thirdparty-applications-of-api-version-11-or-later) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbility

```TypeScript
startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
```

Starts a UIAbility. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000018](../errorcode-ability.md#16000018-restricting-redirection-to-thirdparty-applications-of-api-version-11-or-later) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

Starts a UIAbility. This API uses a promise to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-UIExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000018](../errorcode-ability.md#16000018-restricting-redirection-to-thirdparty-applications-of-api-version-11-or-later) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void
```

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses an asynchronous callback to return the result. The following situations may be possible for a started UIAbility:

- Normally, you can call  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the UIAbility. The result is returned to the caller.  
- If an exception occurs, for example, the UIAbility is killed, an error message, in which **resultCode** is **-1**  
, is returned to the initiator UIAbility.  
- If different applications call this API to start a UIAbility that uses the singleton mode and then call  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the UIAbility, the normal result is returned to the last caller, and an exception message, in which  
**resultCode** is **-1**, is returned to others.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000018](../errorcode-ability.md#16000018-restricting-redirection-to-thirdparty-applications-of-api-version-11-or-later) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void
```

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses an asynchronous callback to return the result. The following situations may be possible for a started UIAbility:

- Normally, you can call  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the UIAbility. The result is returned to the caller.  
- If an exception occurs, for example, the UIAbility is killed, an error message, in which **resultCode** is **-1**  
, is returned to the initiator UIAbility.  
- If different applications call this API to start a UIAbility that uses the singleton mode and then call  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the UIAbility, the normal result is returned to the last caller, and an exception message, in which  
**resultCode** is **-1**, is returned to others.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000018](../errorcode-ability.md#16000018-restricting-redirection-to-thirdparty-applications-of-api-version-11-or-later) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
```

Starts a UIAbility and returns the exit result of the launched UIAbility via a callback. This API uses a promise to  return the result. The following situations may be possible for a started UIAbility:

- Normally, you can call  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the UIAbility. The result is returned to the caller.  
- If an exception occurs, for example, the UIAbility is killed, an error message, in which **resultCode** is **-1**  
, is returned to the initiator UIAbility.  
- If different applications call this API to start a UIAbility that uses the singleton mode and then call  
[terminateSelfWithResult](arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) to terminate the UIAbility, the normal result is returned to the last caller, and an exception message, in which  
**resultCode** is **-1**, is returned to others.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>--><!--Device-UIExtensionContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityResult](arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000018](../errorcode-ability.md#16000018-restricting-redirection-to-thirdparty-applications-of-api-version-11-or-later) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000069](../errorcode-ability.md#16000069-extensionability-fails-to-start-a-thirdparty-application-in-strict-mode) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startUIServiceExtensionAbility

```TypeScript
startUIServiceExtensionAbility(want: Want): Promise<void>
```

Starts a UIServiceExtensionAbility. This API uses a promise to return the result.

> **NOTE：**
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-startUIServiceExtensionAbility(want: Want): Promise<void>--><!--Device-UIExtensionContext-startUIServiceExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## terminateSelf

```TypeScript
terminateSelf(callback: AsyncCallback<void>): void
```

Destroys this UIExtensionAbility and closes the corresponding window. This API uses an asynchronous callback to return the result.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-terminateSelf(callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-terminateSelf(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

Destroys this UIExtensionAbility and closes the corresponding window. This API uses a promise to return the result.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-terminateSelf(): Promise<void>--><!--Device-UIExtensionContext-terminateSelf(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## terminateSelfWithResult

```TypeScript
terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void
```

Destroys this UIExtensionAbility, closes the corresponding window, and returns the result to the caller of the UIExtensionAbility (usually a system service). This API uses an asynchronous callback to return the result.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void--><!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## terminateSelfWithResult

```TypeScript
terminateSelfWithResult(parameter: AbilityResult): Promise<void>
```

Destroys this UIExtensionAbility, closes the corresponding window, and returns the result to the caller of the UIExtensionAbility (usually a system service). This API uses a promise to return the result.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult): Promise<void>--><!--Device-UIExtensionContext-terminateSelfWithResult(parameter: AbilityResult): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parameter | [AbilityResult](arkts-ability-abilityresult-abilityresult-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
