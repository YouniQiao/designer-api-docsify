# ApplicationContext

ApplicationContext inherits from [Context](arkts-ability-context-t.md) and provides application-level management capabilities, such as application lifecycle listening, process management, and application environment setting.

> **NOTE：**
> 
> The APIs of this module can be used only in the stage model.

**Inheritance/Implementation:** ApplicationContext extends [Context](arkts-ability-context-t.md)

**Since:** 9

<!--Device-unnamed-declare class ApplicationContext extends Context--><!--Device-unnamed-declare class ApplicationContext extends Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## getProcessRunningInformation

```TypeScript
getProcessRunningInformation(): Promise<Array<ProcessInformation>>
```

Obtains information about the running processes.This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [ApplicationContext#getRunningProcessInformation](arkts-ability-applicationcontext-c.md#getrunningprocessinformation)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getProcessRunningInformation(): Promise<Array<ProcessInformation>>--><!--Device-ApplicationContext-getProcessRunningInformation(): Promise<Array<ProcessInformation>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ProcessInformation](arkts-ability-processinformation-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## getProcessRunningInformation

```TypeScript
getProcessRunningInformation(callback: AsyncCallback<Array<ProcessInformation>>): void
```

Obtains information about the running processes.This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [ApplicationContext#getRunningProcessInformation](arkts-ability-applicationcontext-c.md#getrunningprocessinformation)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getProcessRunningInformation(callback: AsyncCallback<Array<ProcessInformation>>): void--><!--Device-ApplicationContext-getProcessRunningInformation(callback: AsyncCallback<Array<ProcessInformation>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ProcessInformation](arkts-ability-processinformation-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## preloadUIExtensionAbility

```TypeScript
preloadUIExtensionAbility(want: Want): Promise<void>
```

Preloads a UIExtensionAbility instance. This API uses a promise to return the result.

The preloaded UIExtensionAbility instance is sent to the **onCreate** lifecycle of the UIExtensionAbility and waits to be loaded by the current application.

A UIExtensionAbility instance can be preloaded for multiple times. Each time a preloaded UIExtensionAbility instance is loaded, the next preloaded UIExtensionAbility instance is sent to the **onCreate** lifecycle of the UIExtensionAbility.

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory| Description|
| -------- | -------- | -------- | -------- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes|

**Since:** 12

**Required permissions:** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-preloadUIExtensionAbility(want: Want): Promise<void>--><!--Device-ApplicationContext-preloadUIExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

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
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## registerAbilityLifecycleCallback

```TypeScript
registerAbilityLifecycleCallback(abilityLifecycleCallback: AbilityLifecycleCallback): number
```

Registers a listener to monitor the ability lifecycle of the application.This API uses an asynchronous callback to return the result.

&lt;p&gt;**NOTE：**:&lt;br&gt;It can be called only by the main thread.&lt;/p&gt;

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ApplicationContext#on(type:

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-registerAbilityLifecycleCallback(abilityLifecycleCallback: AbilityLifecycleCallback): number--><!--Device-ApplicationContext-registerAbilityLifecycleCallback(abilityLifecycleCallback: AbilityLifecycleCallback): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| abilityLifecycleCallback | [AbilityLifecycleCallback](arkts-ability-app-ability-abilitylifecyclecallback-abilitylifecyclecallback-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## registerEnvironmentCallback

```TypeScript
registerEnvironmentCallback(environmentCallback: EnvironmentCallback): number
```

Register environment callback.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ApplicationContext#on(type:

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-registerEnvironmentCallback(environmentCallback: EnvironmentCallback): number--><!--Device-ApplicationContext-registerEnvironmentCallback(environmentCallback: EnvironmentCallback): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| environmentCallback | [EnvironmentCallback](arkts-ability-app-ability-environmentcallback-environmentcallback-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## unregisterAbilityLifecycleCallback

```TypeScript
unregisterAbilityLifecycleCallback(callbackId: number, callback: AsyncCallback<void>): void
```

Unregisters the listener that monitors the ability lifecycle of the application.This API uses an asynchronous callback to return the result.

&lt;p&gt;**NOTE：**:&lt;br&gt;It can be called only by the main thread.&lt;/p&gt;

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ApplicationContext#off(type:

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-unregisterAbilityLifecycleCallback(callbackId: number, callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-unregisterAbilityLifecycleCallback(callbackId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## unregisterAbilityLifecycleCallback

```TypeScript
unregisterAbilityLifecycleCallback(callbackId: number): Promise<void>
```

Unregisters a listener for the lifecycle of a UIAbility within the application. This API uses a promise to return the result. It can be called only on the main thread.

&lt;p&gt;**NOTE：**:&lt;br&gt;It can be called only by the main thread.&lt;/p&gt;

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ApplicationContext#off(type:

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-unregisterAbilityLifecycleCallback(callbackId: number): Promise<void>--><!--Device-ApplicationContext-unregisterAbilityLifecycleCallback(callbackId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## unregisterEnvironmentCallback

```TypeScript
unregisterEnvironmentCallback(callbackId: number, envcallback: AsyncCallback<void>): void
```

Unregisters the listener for system environment changes. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ApplicationContext#off(type:

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-unregisterEnvironmentCallback(callbackId: number, envcallback: AsyncCallback<void>): void--><!--Device-ApplicationContext-unregisterEnvironmentCallback(callbackId: number, envcallback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackId | number | Yes |
| envcallback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## unregisterEnvironmentCallback

```TypeScript
unregisterEnvironmentCallback(callbackId: number): Promise<void>
```

Unregisters the listener for system environment changes. This API uses a promise to return the result. It can be called only on the main thread.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** ApplicationContext#off(type:

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-unregisterEnvironmentCallback(callbackId: number): Promise<void>--><!--Device-ApplicationContext-unregisterEnvironmentCallback(callbackId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
