# ApplicationContext

ApplicationContext inherits from [Context](arkts-ability-context-t.md) and provides application-level management capabilities, such as application lifecycle listening, process management, and application environment setting.

> **NOTE：**
> 
> The APIs of this module can be used only in the stage model.

**Inheritance/Implementation:** ApplicationContext extends [Context](arkts-ability-context-t.md)

**Since:** 9

<!--Device-unnamed-declare class ApplicationContext extends Context--><!--Device-unnamed-declare class ApplicationContext extends Context-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## clearUpApplicationData

```TypeScript
clearUpApplicationData(): Promise<void>
```

Clears up all data in the application file path and revokes the permissions that the application has requested from users. This API uses a promise to return the result. It can be called only on the main thread.

> **NOTE：**
> 
> For details about the application file path, see
> [Application File Directory and Application File Path](../../../file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path)
> . The figure shows only the application file paths in the EL1 and EL2 directories. For the application file paths
> in other directories, refer to EL1.
> 
> This API stops the application process. After the application process is stopped, all subsequent callbacks will
> not be triggered.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-clearUpApplicationData(): Promise<void>--><!--Device-ApplicationContext-clearUpApplicationData(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## clearUpApplicationData

```TypeScript
clearUpApplicationData(callback: AsyncCallback<void>): void
```

Clears up all data in the application file path and revokes the permissions that the application has requested from users. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

> **NOTE：**
> 
> For details about the application file path, see
> [Application File Directory and Application File Path](../../../file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path)
> . The figure shows only the application file paths in the EL1 and EL2 directories. For the application file paths
> in other directories, refer to EL1.
> 
> This API stops the application process. After the application process is stopped, all subsequent callbacks will
> not be triggered.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-clearUpApplicationData(callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-clearUpApplicationData(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## disableDelayedProcessExit

```TypeScript
disableDelayedProcessExit(): Promise<void>
```

Disables delayed process exit for the current process.

&lt;p&gt;&lt;b&gt;NOTE&lt;/b&gt;:&lt;br&gt;This API can be called only by the main thread.&lt;br&gt;Calling this API cancels the effect of {@link enableDelayedProcessExit}.&lt;/p&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-disableDelayedProcessExit(): Promise<void>--><!--Device-ApplicationContext-disableDelayedProcessExit(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 16000150 |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## enableDelayedProcessExit

```TypeScript
enableDelayedProcessExit(): Promise<void>
```

Enable delayed exit for the current process.&lt;p&gt;**NOTE：**:&lt;br&gt;It can be called only by the main thread.&lt;br&gt;Under normal circumstances, the process exits after the last UIAbility within the application process has exited. After calling this interface, the process will delay its exit for 10 seconds after the last UIAbility exits. If a new Ability is started within the 10 seconds in the current process, the process no longer exits.&lt;/p&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-enableDelayedProcessExit(): Promise<void>--><!--Device-ApplicationContext-enableDelayedProcessExit(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 16000150 |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## getAllRunningInstanceKeys

```TypeScript
getAllRunningInstanceKeys(): Promise<Array<string>>
```

Obtains the unique instance IDs of all multi-instances of this application. This API uses a promise to return the result. It can be called only on the main thread.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getAllRunningInstanceKeys(): Promise<Array<string>>--><!--Device-ApplicationContext-getAllRunningInstanceKeys(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## getAllWindowStages

```TypeScript
getAllWindowStages(): Promise<Array<window.WindowStage>>
```

Obtains all WindowStage objects in the current application process. This API uses a promise to return the result.It can be called only on the main thread.

This API is used to manage multiple windows in an application that contains several UIAbility components, for example, managing the states of different WindowStage objects, or synchronizing state or data between multiple windows within the same application.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationContext-getAllWindowStages(): Promise<Array<window.WindowStage>>--><!--Device-ApplicationContext-getAllWindowStages(): Promise<Array<window.WindowStage>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;window.WindowStage&gt;&gt; |

## getCurrentAppCloneIndex

```TypeScript
getCurrentAppCloneIndex(): number
```

Obtains the index of the current application clone.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ApplicationContext-getCurrentAppCloneIndex(): int--><!--Device-ApplicationContext-getCurrentAppCloneIndex(): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## getCurrentInstanceKey

```TypeScript
getCurrentInstanceKey(): string
```

Obtains the unique instance ID of this application. This API can be called only on the main thread.

This API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000078is returned.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getCurrentInstanceKey(): string--><!--Device-ApplicationContext-getCurrentInstanceKey(): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## getRunningProcessInformation

```TypeScript
getRunningProcessInformation(): Promise<Array<ProcessInformation>>
```

Obtains the information about running processes. This API uses a promise to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-getRunningProcessInformation(): Promise<Array<ProcessInformation>>--><!--Device-ApplicationContext-getRunningProcessInformation(): Promise<Array<ProcessInformation>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ProcessInformation](arkts-ability-processinformation-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## getRunningProcessInformation

```TypeScript
getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void
```

Obtains the information about running processes. This API uses an asynchronous callback to return the result.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void--><!--Device-ApplicationContext-getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ProcessInformation](arkts-ability-processinformation-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## getUIAbilityByInstanceId

```TypeScript
getUIAbilityByInstanceId(instanceId: string): UIAbility
```

Get the UIAbility instance by the instance Id.

&lt;p&gt;**NOTE：**:&lt;br&gt;It can be called only by the main thread.&lt;/p&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getUIAbilityByInstanceId(instanceId: string): UIAbility--><!--Device-ApplicationContext-getUIAbilityByInstanceId(instanceId: string): UIAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| instanceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## killAllProcesses

```TypeScript
killAllProcesses(): Promise<void>
```

Kills all processes of this application. The application will not execute the normal lifecycle when exiting. This API uses a promise to return the result. It can be called only on the main thread.

> **NOTE：**
> 
> This API is used to forcibly exit an application in abnormal scenarios. To exit an application properly, call
> [terminateSelf()](arkts-ability-uiabilitycontext-c.md#terminateself).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-killAllProcesses(): Promise<void>--><!--Device-ApplicationContext-killAllProcesses(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## killAllProcesses

```TypeScript
killAllProcesses(clearPageStack: boolean): Promise<void>
```

Kills all processes of this application. The application will not execute the normal lifecycle when exiting. This API uses a promise to return the result. It can be called only on the main thread.

> **NOTE：**
> 
> This API is used to forcibly exit an application in abnormal scenarios. To exit an application properly, call
> [terminateSelf()](arkts-ability-uiabilitycontext-c.md#terminateself).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ApplicationContext-killAllProcesses(clearPageStack: boolean): Promise<void>--><!--Device-ApplicationContext-killAllProcesses(clearPageStack: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clearPageStack | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## killAllProcesses

```TypeScript
killAllProcesses(callback: AsyncCallback<void>): void
```

Kills all processes of this application. The application will not execute the normal lifecycle when exiting. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

> **NOTE：**
> 
> This API is used to forcibly exit an application in abnormal scenarios. To exit an application properly, call
> [terminateSelf()](arkts-ability-uiabilitycontext-c.md#terminateself).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-killAllProcesses(callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-killAllProcesses(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## off('abilityLifecycle')

```TypeScript
off(type: 'abilityLifecycle', callbackId: number, callback: AsyncCallback<void>): void
```

Unregisters a listener for the lifecycle of a UIAbility within the application. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-off(type: 'abilityLifecycle', callbackId: number, callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-off(type: 'abilityLifecycle', callbackId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'abilityLifecycle' | Yes |
| callbackId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## off('abilityLifecycle')

```TypeScript
off(type: 'abilityLifecycle', callbackId: number): Promise<void>
```

Unregisters a listener for the lifecycle of a UIAbility within the application. This API uses a promise to return the result. It can be called only on the main thread.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-off(type: 'abilityLifecycle', callbackId: number): Promise<void>--><!--Device-ApplicationContext-off(type: 'abilityLifecycle', callbackId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'abilityLifecycle' | Yes |
| callbackId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## off('environment')

```TypeScript
off(type: 'environment', callbackId: number, callback: AsyncCallback<void>): void
```

Unregisters the listener for system environment changes. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-off(type: 'environment', callbackId: number, callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-off(type: 'environment', callbackId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'environment' | Yes |
| callbackId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## off('environment')

```TypeScript
off(type: 'environment', callbackId: number): Promise<void>
```

Unregisters the listener for system environment changes. This API uses a promise to return the result. It can be called only on the main thread.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-off(type: 'environment', callbackId: number): Promise<void>--><!--Device-ApplicationContext-off(type: 'environment', callbackId: number): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'environment' | Yes |
| callbackId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## off('applicationStateChange')

```TypeScript
off(type: 'applicationStateChange', callback?: ApplicationStateChangeCallback): void
```

Unregisters the listener for application process state changes. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-off(type: 'applicationStateChange', callback?: ApplicationStateChangeCallback): void--><!--Device-ApplicationContext-off(type: 'applicationStateChange', callback?: ApplicationStateChangeCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'applicationStateChange' | Yes |
| callback | [ApplicationStateChangeCallback](arkts-ability-app-ability-applicationstatechangecallback-applicationstatechangecallback-c.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## offSystemConfigurationUpdated

```TypeScript
offSystemConfigurationUpdated(callback?: systemConfiguration.UpdatedCallback): void
```

unregisters a listener for system configuration updated.

&lt;p&gt;**NOTE：**:&lt;br&gt;It can be called only by the main thread.&lt;/p&gt;

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ApplicationContext-offSystemConfigurationUpdated(callback?: systemConfiguration.UpdatedCallback): void--><!--Device-ApplicationContext-offSystemConfigurationUpdated(callback?: systemConfiguration.UpdatedCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | systemConfiguration.UpdatedCallback | No |

## on('abilityLifecycle')

```TypeScript
on(type: 'abilityLifecycle', callback: AbilityLifecycleCallback): number
```

Registers a listener for the lifecycle of a UIAbility within the application. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-on(type: 'abilityLifecycle', callback: AbilityLifecycleCallback): number--><!--Device-ApplicationContext-on(type: 'abilityLifecycle', callback: AbilityLifecycleCallback): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'abilityLifecycle' | Yes |
| callback | [AbilityLifecycleCallback](arkts-ability-app-ability-abilitylifecyclecallback-abilitylifecyclecallback-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## on('environment')

```TypeScript
on(type: 'environment', callback: EnvironmentCallback): number
```

Registers a listener for system environment changes. This API uses an asynchronous callback to return the result.It can be called only on the main thread.

> **NOTE：**
> 
> - You can also use [onConfigurationUpdate](arkts-ability-app-ability-ability-ability-c.md#onconfigurationupdate) to
> listen for system environment changes. Unlike
> [onConfigurationUpdate](arkts-ability-app-ability-ability-ability-c.md#onconfigurationupdate) of **Ability**, this
> API offers greater flexibility. It can be used both within application components and pages. However, the
> environment variables that can be subscribed to are different from those of
> [onConfigurationUpdate](arkts-ability-app-ability-ability-ability-c.md#onconfigurationupdate). For example, this
> API cannot be used to subscribe to direction, screen density, and display ID changes. For details, see the
> description of each environment variable in
> [Configuration](arkts-ability-app-ability-configuration-configuration-i.md).
> 
> - There are certain restrictions when this API is triggered. For example, if you set the application language by
> calling [setLanguage](arkts-ability-applicationcontext-c.md#setlanguage), the system does not trigger the
> callback for the current API even if the system language changes. For details, see
> [When to Use](../../../application-models/subscribe-system-environment-variable-changes.md#when-to-use).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-on(type: 'environment', callback: EnvironmentCallback): number--><!--Device-ApplicationContext-on(type: 'environment', callback: EnvironmentCallback): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'environment' | Yes |
| callback | [EnvironmentCallback](arkts-ability-app-ability-environmentcallback-environmentcallback-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## on('applicationStateChange')

```TypeScript
on(type: 'applicationStateChange', callback: ApplicationStateChangeCallback): void
```

Registers a listener for application process state changes. This API uses an asynchronous callback to return the result. It can be called only on the main thread.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-on(type: 'applicationStateChange', callback: ApplicationStateChangeCallback): void--><!--Device-ApplicationContext-on(type: 'applicationStateChange', callback: ApplicationStateChangeCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'applicationStateChange' | Yes |
| callback | [ApplicationStateChangeCallback](arkts-ability-app-ability-applicationstatechangecallback-applicationstatechangecallback-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## onSystemConfigurationUpdated

```TypeScript
onSystemConfigurationUpdated(callback: systemConfiguration.UpdatedCallback): void
```

Registers a listener for system configuration updated.

&lt;p&gt;**NOTE：**:&lt;br&gt;It can be called only by the main thread.&lt;/p&gt;

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ApplicationContext-onSystemConfigurationUpdated(callback: systemConfiguration.UpdatedCallback): void--><!--Device-ApplicationContext-onSystemConfigurationUpdated(callback: systemConfiguration.UpdatedCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | systemConfiguration.UpdatedCallback | Yes |

## restartApp

```TypeScript
restartApp(want: Want): void
```

Restarts the application and starts the specified UIAbility. This API can be called only by the main thread, and the application to restart must be active.

> **NOTE：**
> 
> When this API is called to restart the application, the **onDestroy** lifecycle callback of the ability in the
> application is not triggered.
> 
> If an atomic service calls this API,
> [restartSelfAtomicService()](arkts-ability-abilitymanager-restartselfatomicservice-f.md#restartselfatomicservice)
> , or [UIAbilityContext.restartApp()](arkts-ability-uiabilitycontext-c.md#restartapp) within 3 seconds after a
> successful call to this API, the system returns error code 16000064.
> 
> If an application calls this API or
> [UIAbilityContext.restartApp()](arkts-ability-uiabilitycontext-c.md#restartapp) within 3 seconds after a
> successful call to this API, the system returns error code 16000064.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ApplicationContext-restartApp(want: Want): void--><!--Device-ApplicationContext-restartApp(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000064](../errorcode-ability.md#16000064-frequent-application-restart) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000063](../errorcode-ability.md#16000063-invalid-ability-during-application-restart) |

## setColorMode

```TypeScript
setColorMode(colorMode: ConfigurationConstant.ColorMode): void
```

Sets the dark/light color mode for the application. This API can be called only on the main thread.

> **NOTE：**
> 
> Before calling this API, ensure that the window has been created and the page corresponding to the UIAbility has
> been loaded (using the
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9) API in the
> [onWindowStageCreate()](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate) lifecycle).

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void--><!--Device-ApplicationContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## setFont

```TypeScript
setFont(font: string): void
```

Sets the font for this application. This API can be called only on the main thread.

> **NOTE：**
> 
> Before calling this API, ensure that the window has been created and the page corresponding to the UIAbility has
> been loaded (using the
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9) API in the
> [onWindowStageCreate()](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate) lifecycle).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-setFont(font: string): void--><!--Device-ApplicationContext-setFont(font: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| font | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## setFontSizeScale

```TypeScript
setFontSizeScale(fontSizeScale: number): void
```

Sets the scale ratio for the font size of this application. This API can be called only on the main thread.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-ApplicationContext-setFontSizeScale(fontSizeScale: double): void--><!--Device-ApplicationContext-setFontSizeScale(fontSizeScale: double): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fontSizeScale | number | Yes |

## setLanguage

```TypeScript
setLanguage(language: string): void
```

Sets the language for the application. This API can be called only on the main thread.

> **NOTE：**
> 
> Before calling this API, ensure that the window has been created and the page corresponding to the UIAbility has
> been loaded (using the
> [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9) API in the
> [onWindowStageCreate()](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate) lifecycle).

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-setLanguage(language: string): void--><!--Device-ApplicationContext-setLanguage(language: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| language | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## setSupportedProcessCache

```TypeScript
setSupportedProcessCache(isSupported : boolean): void
```

Sets whether the current application's process supports resource caching, so that the cached process resources can be reused when the application is started again. This API can be called only on the main thread.

This setting applies only to the current process instance and does not affect others. If the application process instance is terminated, the previously set state will not be preserved and must be reset.

This API can be properly called only on phones and 2-in-1 devices. If it is called on other device types, error code 801 is returned.

> **NOTE：**
> 
> - This API only sets the application to be ready for quick startup after caching. It does not mean that quick
> startup will be triggered. Other conditions must be considered to determine whether to trigger quick startup.
> 
> - To ensure that this API is effective before the process exits, it should be called as soon as possible. You are
> advised to call this API within the **onCreate()** callback of the
> [AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md).
> 
> - If this API is called multiple times within the same process, the outcome of the final call is used. In cases
> where there are multiple AbilityStage instances, to achieve the desired result, this API must be called and
> configured with the same value in each AbilityStage.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-setSupportedProcessCache(isSupported : boolean): void--><!--Device-ApplicationContext-setSupportedProcessCache(isSupported : boolean): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isSupported | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## startSelfUIAbility

```TypeScript
startSelfUIAbility(want: Want): Promise<void>
```

Starts a UIAbility of the current application during the delayed-exit window.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-startSelfUIAbility(want: Want): Promise<void>--><!--Device-ApplicationContext-startSelfUIAbility(want: Want): Promise<void>-End-->

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
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| 16000161 |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000130](../errorcode-ability.md#16000130-uiability-does-not-belong-to-the-caller) |
| 16000162 |
| [16000124](../errorcode-ability.md#16000124-starting-a-distributed-uiability-is-not-supported) |
| [16000125](../errorcode-ability.md#16000125-starting-a-plugin-is-not-supported) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000122](../errorcode-ability.md#16000122-target-component-is-intercepted-by-the-system-control-module) |
| [16000123](../errorcode-ability.md#16000123-implicit-startup-is-not-supported) |
