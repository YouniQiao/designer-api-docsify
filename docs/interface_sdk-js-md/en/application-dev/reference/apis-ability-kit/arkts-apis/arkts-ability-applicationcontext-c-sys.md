# ApplicationContext

ApplicationContext inherits from Context and provides application-level management capabilities, such as application lifecycle listening, process management, and application environment setting. > **NOTE：**> > The APIs of this module can be used only in the stage model.

**Inheritance/Implementation:** ApplicationContext extends Context

**Since:** 23

<!--Device-unnamed-declare class ApplicationContext--><!--Device-unnamed-declare class ApplicationContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## getProcessRunningInformation

```TypeScript
getProcessRunningInformation(): Promise<Array<ProcessInformation>>
```

Obtains information about the running processes. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [getRunningProcessInformation](arkts-ability-applicationcontext-c.md#getrunningprocessinformation)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getProcessRunningInformation(): Promise<Array<ProcessInformation>>--><!--Device-ApplicationContext-getProcessRunningInformation(): Promise<Array<ProcessInformation>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[ProcessInformation](arkts-ability-processinformation-i.md)&gt;&gt; | Promise used to return the API call result and the process running information. You can perform error handling or custom processing in this callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

## getProcessRunningInformation

```TypeScript
getProcessRunningInformation(callback: AsyncCallback<Array<ProcessInformation>>): void
```

Obtains information about the running processes. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [getRunningProcessInformation](arkts-ability-applicationcontext-c.md#getrunningprocessinformation)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getProcessRunningInformation(callback: AsyncCallback<Array<ProcessInformation>>): void--><!--Device-ApplicationContext-getProcessRunningInformation(callback: AsyncCallback<Array<ProcessInformation>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ProcessInformation](arkts-ability-processinformation-i.md)&gt;&gt; | Yes | Callback used to return the information about the running processes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

## preloadUIExtensionAbility

```TypeScript
preloadUIExtensionAbility(want: Want): Promise<void>
```

Preloads a UIExtensionAbility instance. This API uses a promise to return the result. The preloaded UIExtensionAbility instance is sent to the **onCreate** lifecycle of the UIExtensionAbility and waits to be loaded by the current application. A UIExtensionAbility instance can be preloaded for multiple times. Each time a preloaded UIExtensionAbility instance is loaded, the next preloaded UIExtensionAbility instance is sent to the **onCreate** lifecycle of the UIExtensionAbility. | Name| Type| Mandatory| Description| | -------- | -------- | -------- | -------- | | want | [Want](arkts-ability-app-ability-want-want-c.md#want) | Yes| Want information of the UIExtensionAbility.|

**Since:** 23

**Required permissions:** ohos.permission.PRELOAD_UI_EXTENSION_ABILITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-preloadUIExtensionAbility(want: Want): Promise<void>--><!--Device-ApplicationContext-preloadUIExtensionAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Want information of the UIExtensionAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | The application does not have permission to call the interface. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    let want: Want = {
      bundleName: 'com.ohos.uiextensionprovider',
      abilityName: 'UIExtensionProvider',
      moduleName: 'entry',
      parameters: {
        // The value must be the same as the value of type in the module.json5 file of the UIExtensionAbility.
        'ability.want.params.uiExtensionType': 'sys/commonUI'
      }
    };
    try {
      let applicationContext = this.context.getApplicationContext();
      applicationContext.preloadUIExtensionAbility(want)
        .then(() => {
          // Carry out normal service processing.
          console.info('preloadUIExtensionAbility succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error('preloadUIExtensionAbility failed');
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`preloadUIExtensionAbility failed. code: ${code}, msg: ${message}`);
    }
  }
}
```

## registerAbilityLifecycleCallback

```TypeScript
registerAbilityLifecycleCallback(abilityLifecycleCallback: AbilityLifecycleCallback): number
```

Registers a listener to monitor the ability lifecycle of the application. This API uses an asynchronous callback to return the result. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [on](arkts-ability-applicationcontext-c.md#onabilitylifecycle)(type: 'abilityLifecycle', callback: AbilityLifecycleCallback)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-registerAbilityLifecycleCallback(abilityLifecycleCallback: AbilityLifecycleCallback): number--><!--Device-ApplicationContext-registerAbilityLifecycleCallback(abilityLifecycleCallback: AbilityLifecycleCallback): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| abilityLifecycleCallback | [AbilityLifecycleCallback](arkts-ability-app-ability-abilitylifecyclecallback-abilitylifecyclecallback-c.md) | Yes | Callback used to return the ID of the registered listener. |

**Return value:**

| Type | Description |
| --- | --- |
| number | ID of the callback registered. This ID is used to unregister the corresponding callback in [ApplicationContext.unregisterAbilityLifecycleCallback]{ |

## registerEnvironmentCallback

```TypeScript
registerEnvironmentCallback(environmentCallback: EnvironmentCallback): number
```

Register environment callback.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [on](arkts-ability-applicationcontext-c.md#onabilitylifecycle)(type: 'environment', callback: EnvironmentCallback)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-registerEnvironmentCallback(environmentCallback: EnvironmentCallback): number--><!--Device-ApplicationContext-registerEnvironmentCallback(environmentCallback: EnvironmentCallback): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| environmentCallback | [EnvironmentCallback](../../apis-na/arkts-apis/arkts-na-app-ability-environmentcallback-environmentcallback-i.md) | Yes | Callback used to return the ID of the registered listener. |

**Return value:**

| Type | Description |
| --- | --- |
| number | ID of the callback registered. This ID is used to unregister the corresponding callback in [ApplicationContext.unregisterEnvironmentCallback]{ |

## unregisterAbilityLifecycleCallback

```TypeScript
unregisterAbilityLifecycleCallback(callbackId: number, callback: AsyncCallback<void>): void
```

Unregisters the listener that monitors the ability lifecycle of the application. This API uses an asynchronous callback to return the result. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [off](arkts-ability-applicationcontext-c.md#offabilitylifecycle)(type: 'abilityLifecycle', callbackId: number, callback: AsyncCallback&lt;void&gt;)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-unregisterAbilityLifecycleCallback(callbackId: number, callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-unregisterAbilityLifecycleCallback(callbackId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackId | number | Yes | ID returned when the [ApplicationContext.registerAbilityLifecycleCallback](#registerabilitylifecyclecallback) |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the ID of the registered listener. |

## unregisterAbilityLifecycleCallback

```TypeScript
unregisterAbilityLifecycleCallback(callbackId: number): Promise<void>
```

Unregisters a listener for the lifecycle of a UIAbility within the application. This API uses a promise to return the result. It can be called only on the main thread. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 9

**Deprecated since:** 10

**Substitutes:** off(type: 'abilityLifecycle', callbackId: number): Promise&lt;void&gt;;

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-unregisterAbilityLifecycleCallback(callbackId: number): Promise<void>--><!--Device-ApplicationContext-unregisterAbilityLifecycleCallback(callbackId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackId | number | Yes | ID returned when the [ApplicationContext.registerAbilityLifecycleCallback](#registerabilitylifecyclecallback) |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

## unregisterEnvironmentCallback

```TypeScript
unregisterEnvironmentCallback(callbackId: number, envcallback: AsyncCallback<void>): void
```

Unregisters the listener for system environment changes. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [off](arkts-ability-applicationcontext-c.md#offabilitylifecycle)(type: 'environment', callbackId: number, callback: AsyncCallback&lt;void&gt;)

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-unregisterEnvironmentCallback(callbackId: number, envcallback: AsyncCallback<void>): void--><!--Device-ApplicationContext-unregisterEnvironmentCallback(callbackId: number, envcallback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackId | number | Yes | ID returned when the [ApplicationContext.registerEnvironmentCallback](#registerenvironmentcallback) |
| envcallback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the ID of the registered listener. |

## unregisterEnvironmentCallback

```TypeScript
unregisterEnvironmentCallback(callbackId: number): Promise<void>
```

Unregisters the listener for system environment changes. This API uses a promise to return the result. It can be called only on the main thread.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** off(type: 'environment', callbackId: number): Promise&lt;void&gt;;

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-unregisterEnvironmentCallback(callbackId: number): Promise<void>--><!--Device-ApplicationContext-unregisterEnvironmentCallback(callbackId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackId | number | Yes | ID returned when the [ApplicationContext.registerEnvironmentCallback](#registerenvironmentcallback) |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

