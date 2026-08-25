# UIAbility

Application component that has the UI. It provides lifecycle callbacks such as component creation, destruction, and foreground/background switching, and supports background communication.

**Inheritance/Implementation:** UIAbility extends [Ability](arkts-ability-app-ability-ability-ability-c.md)

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { UIAbility, Callee, CalleeCallback, Caller, OnReleaseCallback, OnRemoteStateChangeCallback } from 'kits/@kit.AbilityKit';
```

## onBackground

```TypeScript
onBackground(): void
```

Called when the application transitions from the foreground to the background. You can release resources when the UI is no longer visible, for example, stopping location services, within this callback.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onBackPressed

```TypeScript
onBackPressed(): boolean
```

Called when an operation of going back to the previous page is triggered on this UIAbility. The return value determines whether to destroy the UIAbility instance.  
- When the target SDK version is earlier than 12, the default return value is **false**, indicating that the  
UIAbility will be destroyed.  
- When the target SDK version is 12 or later, the default return value is **true**, indicating that the UIAbility  
will be moved to the background and will not be destroyed.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## onCollaborate

```TypeScript
onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult
```

Callback invoked to return the collaboration result in multi-device collaboration scenarios.

> **NOTE：**&gt;
> - This callback does not support ability launch in
> [specified mode](../../../application-models/uiability-launch-type.md#specified).&gt;
> - When you use methods such as
> [startAbility](arkts-ability-uiabilitycontext-c.md#startability)
> to start an application, you must include **FLAG_ABILITY_ON_COLLABORATE** in
> [Flags](arkts-ability-wantconstant-flags-e.md) in the Want object.&gt;
> - During a
> [cold start](../../../application-models/uiability-intra-device-interaction.md#cold-starting-uiability), this
> callback must be invoked before [onForeground](#onforeground) or after
> [onBackground](#onbackground). During a
> [hot start](../../../application-models/uiability-intra-device-interaction.md#hot-starting-uiability), this
> callback must be invoked before [onNewWant](#onnewwant).

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wantParam | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| AbilityConstant.CollaborateResult |

## onContinue

```TypeScript
onContinue(wantParam: Record<string, Object>):
    AbilityConstant.OnContinueResult | Promise<AbilityConstant.OnContinueResult>
```

Called when a UIAbility is to be migrated across devices. You can save service data to be migrated.

> **NOTE：**&gt;
> For versions prior to API version 18, only synchronous calls are supported. Starting from API version 18,
> asynchronous calls are also supported.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wantParam | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| AbilityConstant.OnContinueResult |
| AbilityConstant.OnContinueResult \| Promise & lt;AbilityConstant.OnContinueResult & gt; |

## onCreate

```TypeScript
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
```

Called when a UIAbility instance is created. You can execute initialization logic (such as defining variables and loading resources) in this callback. This callback is invoked during a [cold start](../../../application-models/uiability-intra-device-interaction.md#cold-starting-uiability) of the UIAbility.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| launchParam | AbilityConstant.LaunchParam | Yes |

## onDestroy

```TypeScript
onDestroy(): void | Promise<void>
```

Called when the UIAbility is destroyed (for example, when the UIAbility is terminated using the [terminateSelf](arkts-ability-uiabilitycontext-c.md#terminateself) API). You can clear resources and save data during this lifecycle.This API returns the result synchronously or uses a promise to return the result.

> **NOTE：**&gt;
> - Once the **onDestroy** lifecycle callback completes, the application may exit. This can interrupt any pending
> asynchronous operations (such as asynchronously writing data to a database), preventing them from finishing
> successfully. In this case, you are advised to use a promise to return the result.&gt;
> - The callback is invoked only when the UIAbility exits gracefully. It is not invoked in cases of abnormal exits
> (for example, process termination due to low memory conditions).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onDidBackground

```TypeScript
onDidBackground(): void
```

Called after the application has transitioned to the background. It is called after [onBackground](#onbackground). It can be used to release resources after the application has entered the background, for example, stopping audio playback.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onDidForeground

```TypeScript
onDidForeground(): void
```

Called after the application has transitioned to the foreground. It is called after [onForeground](#onforeground). It can be used to capture the moment when the application fully transitions to the foreground. When paired with [onWillForeground](#onwillforeground), it can also measure the duration from the application's initial foreground entry to its full transition into the foreground state.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onDump

```TypeScript
onDump(params: Array<string>): Array<string>
```

Called when UIAbility data is dumped by running the dump command during application debugging. You can return non- sensitive information to be dumped by the UIAbility in this callback.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

## onForeground

```TypeScript
onForeground(): void
```

Called when the application is initially launched into the foreground or transitions from the background to the foreground. You can request necessary system resources, for example, requesting location services when the application transitions to the foreground, within this callback.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onNewWant

```TypeScript
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void
```

Called when a started UIAbility instance is brought up again. If there are specific scenarios where you do not want this lifecycle callback to be triggered, you can use [setOnNewWantSkipScenarios](arkts-ability-uiabilitycontext-c.md#setonnewwantskipscenarios) to set those [scenarios](arkts-ability-contextconstant-scenarios-e.md).This API returns the result synchronously and does not support asynchronous callback.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| launchParam | AbilityConstant.LaunchParam | Yes |

## onPrepareToTerminate

```TypeScript
onPrepareToTerminate(): boolean
```

Triggered by the system just before the UIAbility is about to close (for example, when the user clicks the close button in the top-right corner of the application window or exits from the dock or system tray), allowing for additional operations to be performed before the UIAbility is officially shut down. You can return **true** to block the current closure attempt and then manually call [terminateSelf](arkts-ability-uiabilitycontext-c.md#terminateself) at an appropriate time to close it. For example, you might ask the user to confirm whether they want to close the UIAbility and then proceed with the closure manually. This API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on other devices.

> **NOTE：**&gt;
> - Starting from API version 15, this callback is not executed when
> [UIAbility.onPrepareToTerminateAsync](#onpreparetoterminateasync) is implemented. When
> [AbilityStage.onPrepareTerminationAsync](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onprepareterminationasync)
> or [AbilityStage.onPrepareTermination](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onpreparetermination) is
> implemented, this callback is not executed if the user right-clicks the dock bar or system tray to close the
> UIAbility.&gt;
> - Additionally, if the application or a third-party framework registers a listener for
> window.WindowStage.on
> , this callback function is not executed.

**Since:** 10

**Required permissions:** ohos.permission.PREPARE_APP_TERMINATE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## onPrepareToTerminateAsync

```TypeScript
onPrepareToTerminateAsync(): Promise<boolean>
```

Triggered by the system just before the UIAbility is close (for example, when the user clicks the close button in the top-right corner of the application window or exits from the dock or system tray), allowing for additional operations to be performed before the UIAbility is officially shut down.You can return **true** to block the current closure attempt and then manually call [terminateSelf](arkts-ability-uiabilitycontext-c.md#terminateself) at an appropriate time to close it. For example, you might ask the user to confirm whether they want to close the UIAbility and then proceed with the closure manually. Starting from API version 15, this API executes the callback normally only on 2-in-1 devices. It does not execute the callback on other devices. Starting from API version 19, this API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on other devices.

> **NOTE：**&gt;
> - When
> [AbilityStage.onPrepareTerminationAsync](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onprepareterminationasync)
> or [AbilityStage.onPrepareTermination](arkts-ability-app-ability-abilitystage-abilitystage-c.md#onpreparetermination) is
> implemented, this callback is not executed if the user right-clicks the dock bar or system tray to close the
> UIAbility.&gt;
> - Additionally, if the application or a third-party framework registers a listener for
> [window.WindowStage.on('windowStageClose')](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#onwindowstageclose)
> , this callback function is not executed.&gt;
> - If an asynchronous callback crashes, it will be handled as a timeout. If the UIAbility does not respond within
> 10 seconds, it will be terminated forcibly.

**Since:** 15

**Required permissions:** ohos.permission.PREPARE_APP_TERMINATE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## onSaveState

```TypeScript
onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>): AbilityConstant.OnSaveResult
```

This API must be used with [appRecovery](arkts-app-ability-apprecovery.md). When the application has enabled the fault recovery feature (with the **saveOccasion** parameter in [enableAppRecovery](arkts-ability-apprecovery-enableapprecovery-f.md) set to **SAVE_WHEN_ERROR**), this callback is invoked to save the UIAbility data in the case of an application fault.

> **NOTE：**&gt;
> Starting from API version 20, this callback is not executed when
> [onSaveStateAsync](#onsavestateasync)
> is implemented.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | AbilityConstant.StateType | Yes |
| wantParam | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| AbilityConstant.OnSaveResult |

## onSaveStateAsync

```TypeScript
onSaveStateAsync(stateType: AbilityConstant.StateType, wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult>
```

This API must be used with [appRecovery](arkts-app-ability-apprecovery.md). When the application has enabled the fault recovery feature (with the **saveOccasion** parameter in [enableAppRecovery](arkts-ability-apprecovery-enableapprecovery-f.md) set to **SAVE_WHEN_ERROR**), this callback is invoked to save the UIAbility data in the case of an application fault. This API uses a promise to return the result.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [stateType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) | AbilityConstant.StateType | Yes |
| wantParam | Record & lt;string, Object & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;AbilityConstant.OnSaveResult & gt; |

## onShare

```TypeScript
onShare(wantParam: Record<string, Object>): void
```

Called when an atomic service is shared across devices. You can set the title, abstract, and URL of the atomic service to be shared in this callback.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wantParam | Record & lt;string, Object & gt; | Yes |

## onWillBackground

```TypeScript
onWillBackground(): void
```

Called just when the application transitions to the background. It is called before [onBackground](#onbackground). It can be used to log various types of data, such as faults, statistics, security information, and user behavior that occur during application running.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWillForeground

```TypeScript
onWillForeground(): void
```

Called just before the application transitions to the foreground. It is called before [onForeground](#onforeground). It can be used to capture the moment when the application starts to transition to the foreground. When paired with [onDidForeground](#ondidforeground), it can also measure the duration from the application's initial foreground entry to its full transition into the foreground state.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageCreate

```TypeScript
onWindowStageCreate(windowStage: window.WindowStage): void
```

Called when a [WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-n.md) instance is created. You can load a page through the WindowStage instance in this callback.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowStage | window.WindowStage | Yes |

## onWindowStageDestroy

```TypeScript
onWindowStageDestroy(): void
```

Called when the WindowStage instance has been destroyed. It informs applications that the WindowStage instance is no longer available for use.The callback is invoked only when the UIAbility exits gracefully. It is not invoked in cases of abnormal exits (for example, process termination due to low memory conditions).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageRestore

```TypeScript
onWindowStageRestore(windowStage: window.WindowStage): void
```

Called when the page stack is restored for the target UIAbility during cross-device migration.

> **NOTE：**&gt;
> When an application is launched as a result of a migration, the **onWindowStageRestore()** lifecycle callback
> function, rather than **onWindowStageCreate()**, is triggered following [onCreate()](#oncreate) or
> [onNewWant()](#onnewwant). This sequence occurs for both
> [cold start](../../../application-models/uiability-intra-device-interaction.md#cold-starting-uiability) and
> [hot start](../../../application-models/uiability-intra-device-interaction.md#hot-starting-uiability).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowStage | window.WindowStage | Yes |

## onWindowStageWillDestroy

```TypeScript
onWindowStageWillDestroy(windowStage: window.WindowStage): void
```

Called when the WindowStage instance is about to be destroyed. You can cancel the listening of WindowStage events in this lifecycle.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowStage | window.WindowStage | Yes |

## callee

```TypeScript
callee: Callee
```

Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee), which is capable of receiving data sent from the Caller object.

**Type:** [Callee](arkts-ability-app-ability-uiability-callee-i.md)

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## context

```TypeScript
context: UIAbilityContext
```

Context of the UIAbility.

**Type:** [UIAbilityContext](arkts-ability-uiabilitycontext-c.md)

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## isDestroyed

```TypeScript
isDestroyed: boolean
```

Indicates whether the UIAbility has been destroyed. The default value is **false**.After the [onDestroy](#ondestroy) callback is executed, this property is set to **true**.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## lastRequestWant

```TypeScript
lastRequestWant: Want
```

Want in the most recent request to launch the UIAbility.  
- On the first launch of a UIAbility, it is the Want parameter received in [onCreate](#oncreate).  
- On subsequent launches, it is the most recent Want received in [onNewWant](#onnewwant).

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## launchWant

```TypeScript
launchWant: Want
```

Want in the request used to [cold start](../../../application-models/uiability-intra-device-interaction.md#cold-starting-uiability) the UIAbility. The value is the Want received in [onCreate](#oncreate).

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## specifiedId

```TypeScript
specifiedId?: string
```

Custom UIAbility ID. This parameter is available only when the UIAbility launch mode is set to [specified](../../../application-models/uiability-launch-type.md#specified).

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore
