# ApplicationContext

ApplicationContext inherits from Context and provides application-level management capabilities, such as application lifecycle listening, process management, and application environment setting. > **NOTE：**> > The APIs of this module can be used only in the stage model.

**Inheritance/Implementation:** ApplicationContext extends Context

**Since:** 23

<!--Device-unnamed-declare class ApplicationContext--><!--Device-unnamed-declare class ApplicationContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## clearUpApplicationData

```TypeScript
clearUpApplicationData(): Promise<void>
```

Clears up all data in the application file path and revokes the permissions that the application has requested from users. This API uses a promise to return the result. It can be called only on the main thread. > **NOTE：**> > For details about the application file path, see > [Application File Directory and Application File Path](../../../file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path) > . The figure shows only the application file paths in the EL1 and EL2 directories. For the application file paths > in other directories, refer to EL1. > > This API stops the application process. After the application process is stopped, all subsequent callbacks will > not be triggered.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-clearUpApplicationData(): Promise<void>--><!--Device-ApplicationContext-clearUpApplicationData(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.clearUpApplicationData();
  }
}
```

## clearUpApplicationData

```TypeScript
clearUpApplicationData(callback: AsyncCallback<void>): void
```

Clears up all data in the application file path and revokes the permissions that the application has requested from users. This API uses an asynchronous callback to return the result. It can be called only on the main thread. > **NOTE：**> > For details about the application file path, see > [Application File Directory and Application File Path](../../../file-management/app-sandbox-directory.md#application-file-directory-and-application-file-path) > . The figure shows only the application file paths in the EL1 and EL2 directories. For the application file paths > in other directories, refer to EL1. > > This API stops the application process. After the application process is stopped, all subsequent callbacks will > not be triggered.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-clearUpApplicationData(callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-clearUpApplicationData(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the application data is cleared up, &lt;code&gt;error&lt;/code&gt; is &lt;code&gt;undefined&lt;/code&gt;; otherwise, &lt;code&gt;error&lt;/code&gt; is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.clearUpApplicationData(error => {
      if (error) {
        console.error(`clearUpApplicationData fail, error: ${JSON.stringify(error)}`);
      }
    });
  }
}
```

## disableDelayedProcessExit

```TypeScript
disableDelayedProcessExit(): Promise<void>
```

Disables delayed process exit for the current process. &lt;p&gt;&lt;b&gt;NOTE&lt;/b&gt;: <br>This API can be called only by the main thread. <br>Calling this API cancels the effect of [enableDelayedProcessExit](#enabledelayedprocessexit).&lt;/p&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-disableDelayedProcessExit(): Promise<void>--><!--Device-ApplicationContext-disableDelayedProcessExit(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 16000150 | The current process has no UIAbility, and this API cannot be called. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: Fail to connect system service. |

## enableDelayedProcessExit

```TypeScript
enableDelayedProcessExit(): Promise<void>
```

Enable delayed exit for the current process. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. <br>Under normal circumstances, the process exits after the last UIAbility within the application process has exited. After calling this interface, the process will delay its exit for 10 seconds after the last UIAbility exits. If a new Ability is started within the 10 seconds in the current process, the process no longer exits.&lt;/p&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-enableDelayedProcessExit(): Promise<void>--><!--Device-ApplicationContext-enableDelayedProcessExit(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 16000150 | The current process has no UIAbility, and this API cannot be called. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: Fail to connect system service. |

## getAllRunningInstanceKeys

```TypeScript
getAllRunningInstanceKeys(): Promise<Array<string>>
```

Obtains the unique instance IDs of all multi-instances of this application. This API uses a promise to return the result. It can be called only on the main thread.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getAllRunningInstanceKeys(): Promise<Array<string>>--><!--Device-ApplicationContext-getAllRunningInstanceKeys(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;string&gt;&gt; | Promise used to return the unique instance IDs of all multi-instances of the application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000078](../errorcode-ability.md#16000078-multi-instance-mode-is-not-supported) | The multi-instance is not supported. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.getAllRunningInstanceKeys();
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`getAllRunningInstanceKeys fail, code: ${code}, msg: ${message}`);
    }
  }
}
```

## getAllWindowStages

```TypeScript
getAllWindowStages(): Promise<Array<window.WindowStage>>
```

Obtains all WindowStage objects in the current application process. This API uses a promise to return the result. It can be called only on the main thread. This API is used to manage multiple windows in an application that contains several UIAbility components, for example, managing the states of different WindowStage objects, or synchronizing state or data between multiple windows within the same application.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationContext-getAllWindowStages(): Promise<Array<window.WindowStage>>--><!--Device-ApplicationContext-getAllWindowStages(): Promise<Array<window.WindowStage>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;window.WindowStage&gt;&gt; | Promise used to return all WindowStage objects in the current application process. |

**Examples**

```TypeScript
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.getAllWindowStages().then((data: window.WindowStage[]) => {
        let windowStage: window.WindowStage[] = data;
        console.info(`WindowStages size ${windowStage.length}`);
      }).catch((error: BusinessError) => {
        console.error(`getAllWindowStages error, code: ${error.code}, error msg: ${error.message}`);
      });
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`getAllWindowStages fail, code: ${code}, msg: ${message}`);
    }
  }
}
```

## getCurrentAppCloneIndex

```TypeScript
getCurrentAppCloneIndex(): int
```

Obtains the index of the current application clone.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationContext-getCurrentAppCloneIndex(): int--><!--Device-ApplicationContext-getCurrentAppCloneIndex(): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Index of the current application clone. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) | The MultiAppMode is not App_CLONE. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    try {
      let appCloneIndex = applicationContext.getCurrentAppCloneIndex();
    } catch (error) {
      console.error(`getCurrentAppCloneIndex fail, error: ${JSON.stringify(error)}`);
    }
  }
}
```

## getCurrentInstanceKey

```TypeScript
getCurrentInstanceKey(): string
```

Obtains the unique instance ID of this application. This API can be called only on the main thread. This API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000078 is returned.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getCurrentInstanceKey(): string--><!--Device-ApplicationContext-getCurrentInstanceKey(): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Unique instance ID of the application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000078](../errorcode-ability.md#16000078-multi-instance-mode-is-not-supported) | The multi-instance is not supported. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    let applicationContext = this.context.getApplicationContext();
    let currentInstanceKey = '';
    try {
      currentInstanceKey = applicationContext.getCurrentInstanceKey();
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`getCurrentInstanceKey fail, code: ${code}, msg: ${message}`);
    }
    console.info(`currentInstanceKey: ${currentInstanceKey}`);
  }
}
```

## getRunningProcessInformation

```TypeScript
getRunningProcessInformation(): Promise<Array<ProcessInformation>>
```

Obtains the information about running processes. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-getRunningProcessInformation(): Promise<Array<ProcessInformation>>--><!--Device-ApplicationContext-getRunningProcessInformation(): Promise<Array<ProcessInformation>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[ProcessInformation](arkts-ability-processinformation-i.md)&gt;&gt; | Promise used to return the API call result and the process running information. You can perform error handling or custom processing in this callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbility extends UIAbility {
  onForeground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.getRunningProcessInformation().then((data) => {
      console.info(`The process running information is: ${JSON.stringify(data)}`);
    }).catch((error: BusinessError) => {
      console.error(`error code: ${error.code}, error msg: ${error.message}`);
    });
  }
}
```

## getRunningProcessInformation

```TypeScript
getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void
```

Obtains the information about running processes. This API uses an asynchronous callback to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void--><!--Device-ApplicationContext-getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[ProcessInformation](arkts-ability-processinformation-i.md)&gt;&gt; | Yes | Callback used to return the information about the running processes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onForeground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.getRunningProcessInformation((err, data) => {
      if (err) {
        console.error(`getRunningProcessInformation failed, err: ${JSON.stringify(err)}`);
      } else {
        console.info(`The process running information is: ${JSON.stringify(data)}`);
      }
    })
  }
}
```

## getUIAbilityByInstanceId

```TypeScript
getUIAbilityByInstanceId(instanceId: string): UIAbility
```

Get the UIAbility instance by the instance Id. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-getUIAbilityByInstanceId(instanceId: string): UIAbility--><!--Device-ApplicationContext-getUIAbilityByInstanceId(instanceId: string): UIAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instanceId | string | Yes | The instanceId of the UIAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | The UIAbility instance. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. System service failed to communicate with dependency module. |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) | The id does not exist. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

## killAllProcesses

```TypeScript
killAllProcesses(): Promise<void>
```

Kills all processes of this application. The application will not execute the normal lifecycle when exiting. This API uses a promise to return the result. It can be called only on the main thread. > **NOTE：**> > This API is used to forcibly exit an application in abnormal scenarios. To exit an application properly, call > [terminateSelf()](arkts-ability-uiabilitycontext-c.md#terminateself).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-killAllProcesses(): Promise<void>--><!--Device-ApplicationContext-killAllProcesses(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.killAllProcesses();
  }
}
```

## killAllProcesses

```TypeScript
killAllProcesses(clearPageStack: boolean): Promise<void>
```

Kills all processes of this application. The application will not execute the normal lifecycle when exiting. This API uses a promise to return the result. It can be called only on the main thread. > **NOTE：**> > This API is used to forcibly exit an application in abnormal scenarios. To exit an application properly, call > [terminateSelf()](arkts-ability-uiabilitycontext-c.md#terminateself).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationContext-killAllProcesses(clearPageStack: boolean): Promise<void>--><!--Device-ApplicationContext-killAllProcesses(clearPageStack: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clearPageStack | boolean | Yes | Whether to clear the page stack. **true** to clear, **false** otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | If the input parameter is not valid parameter. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

let isClearPageStack = false;

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.killAllProcesses(isClearPageStack);
  }
}
```

## killAllProcesses

```TypeScript
killAllProcesses(callback: AsyncCallback<void>): void
```

Kills all processes of this application. The application will not execute the normal lifecycle when exiting. This API uses an asynchronous callback to return the result. It can be called only on the main thread. > **NOTE：**> > This API is used to forcibly exit an application in abnormal scenarios. To exit an application properly, call > [terminateSelf()](arkts-ability-uiabilitycontext-c.md#terminateself).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-killAllProcesses(callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-killAllProcesses(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If all the processes are killed, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onBackground() {
    let applicationContext = this.context.getApplicationContext();
    applicationContext.killAllProcesses(error => {
      if (error) {
        console.error(`killAllProcesses fail, error: ${JSON.stringify(error)}`);
      }
    });
  }
}
```

## offAbilityLifecycle

```TypeScript
offAbilityLifecycle(callbackId: int, callback: AsyncCallback<void>): void
```

Unregisters the listener that monitors the ability lifecycle of the application. This API uses an asynchronous callback to return the result. It can be called only by the main thread.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-offAbilityLifecycle(callbackId: int, callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-offAbilityLifecycle(callbackId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackId | int | Yes | ID of the listener to unregister. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | ID returned when the [ApplicationContext.on('abilityLifecycle')](#on_abilitylifecycleabilitylifecycle) API is called to register a listener for the lifecycle of a UIAbility within the application. |

## offAbilityLifecycle

```TypeScript
offAbilityLifecycle(callbackId: int): Promise<void>
```

Unregisters the listener that monitors the ability lifecycle of the application. This API uses a promise to return the result. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-offAbilityLifecycle(callbackId: int): Promise<void>--><!--Device-ApplicationContext-offAbilityLifecycle(callbackId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackId | int | Yes | Indicates the number code of the callback. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | ThePromise returned by the function. |

## offApplicationStateChange

```TypeScript
offApplicationStateChange(callback?: ApplicationStateChangeCallback): void
```

Unregister applicationStateChange callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-offApplicationStateChange(callback?: ApplicationStateChangeCallback): void--><!--Device-ApplicationContext-offApplicationStateChange(callback?: ApplicationStateChangeCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ApplicationStateChangeCallback](arkts-ability-app-ability-applicationstatechangecallback-applicationstatechangecallback-c.md) | No | The applicationStateChange callback. |

## offEnvironment

```TypeScript
offEnvironment(callbackId: int, callback: AsyncCallback<void>): void
```

Unregister environment callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-offEnvironment(callbackId: int, callback: AsyncCallback<void>): void--><!--Device-ApplicationContext-offEnvironment(callbackId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackId | int | Yes | Indicates the number code of the callback. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | The callback of unregisterEnvironmentCallback. |

## offEnvironment

```TypeScript
offEnvironment(callbackId: int): Promise<void>
```

Unregister environment callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-offEnvironment(callbackId: int): Promise<void>--><!--Device-ApplicationContext-offEnvironment(callbackId: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackId | int | Yes | Indicates the number code of the callback. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

## offInteropAbilityLifecycle

```TypeScript
offInteropAbilityLifecycle(callback?: InteropAbilityLifecycleCallback): void
```

Unregisters the listener that monitors the ability lifecycle of the application for interoperability. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-offInteropAbilityLifecycle(callback?: InteropAbilityLifecycleCallback): void--><!--Device-ApplicationContext-offInteropAbilityLifecycle(callback?: InteropAbilityLifecycleCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [InteropAbilityLifecycleCallback](arkts-ability-app-ability-interopabilitylifecyclecallback-interopabilitylifecyclecallback-i.md) | No | Callback used to be unregistered. |

## offSystemConfigurationUpdated

```TypeScript
offSystemConfigurationUpdated(callback?: systemConfiguration.UpdatedCallback): void
```

unregisters a listener for system configuration updated. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ApplicationContext-offSystemConfigurationUpdated(callback?: systemConfiguration.UpdatedCallback): void--><!--Device-ApplicationContext-offSystemConfigurationUpdated(callback?: systemConfiguration.UpdatedCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | systemConfiguration.UpdatedCallback | No | The system configuration updated callback. If a defined callback is passed in, the listener for that callback is unregistered. If no value is passed in, all the listeners for the corresponding event are unregistered. |

## off_abilityLifecycle('abilityLifecycle')

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'abilityLifecycle' | Yes | Lifecycle of the UIAbility within the application. The value is fixed at **'abilityLifecycle'**. |
| callbackId | number | Yes | ID returned when the [ApplicationContext.on('abilityLifecycle')](#on_abilitylifecycleabilitylifecycle) API is called to register a listener for the lifecycle of a UIAbility within the application. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the deregistration is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let lifecycleId: number;

export default class EntryAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    console.info(`stage applicationContext: ${applicationContext}`);
    try {
      applicationContext.off('abilityLifecycle', lifecycleId, (error, data) => {
        if (error) {
          console.error(`unregisterAbilityLifecycleCallback fail, err: ${JSON.stringify(error)}`);
        } else {
          console.info(`unregisterAbilityLifecycleCallback success, data: ${JSON.stringify(data)}`);
        }
      });
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error code: ${(paramError as BusinessError).message}`);
    }
  }
}
```

## off_abilityLifecycle('abilityLifecycle')

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'abilityLifecycle' | Yes | Lifecycle of the UIAbility within the application. The value is fixed at **'abilityLifecycle'**. |
| callbackId | number | Yes | ID returned when the [ApplicationContext.on('abilityLifecycle')](#on_abilitylifecycleabilitylifecycle) API is called to register a listener for the lifecycle of a UIAbility within the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let lifecycleId: number;

export default class MyAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    console.info(`stage applicationContext: ${applicationContext}`);
    try {
      applicationContext.off('abilityLifecycle', lifecycleId);
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
  }
}
```

## off_applicationStateChange('applicationStateChange')

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'applicationStateChange' | Yes | Application process state change. The value is fixed at **'applicationStateChange'**. |
| callback | [ApplicationStateChangeCallback](arkts-ability-app-ability-applicationstatechangecallback-applicationstatechangecallback-c.md) | No | Callback used to return the result. The value can be a callback defined by [ApplicationContext.on('applicationStateChange')](#on_abilitylifecycleabilitylifecycle) or empty.<br>- If a defined callback is passed in, the listener for that callback is unregistered.<br>- If no value is passed in, all the listeners for the corresponding event are unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Examples**

Assume that [ApplicationContext.on('applicationStateChange')](#onapplicationstatechange) is used to register a callback named applicationStateChangeCallback. The following example shows how to unregister the corresponding listener.

```TypeScript
import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let applicationStateChangeCallback: ApplicationStateChangeCallback = {
  onApplicationForeground() {
    console.info('applicationStateChangeCallback onApplicationForeground');
  },
  onApplicationBackground() {
    console.info('applicationStateChangeCallback onApplicationBackground');
  }
};

export default class MyAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      // In this example, the callback field is set to applicationStateChangeCallback.
      // If no value is passed in, all the listeners for the corresponding event are unregistered.
      applicationContext.off('applicationStateChange', applicationStateChangeCallback);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
  }
}
```

## off_environment('environment')

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'environment' | Yes | System environment change, for example, system dark/light color mode change. The value is fixed at **'environment'**. |
| callbackId | number | Yes | ID returned when the [ApplicationContext.on('environment')](#on_abilitylifecycleabilitylifecycle) API is called to register a listener for system environment changes. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the deregistration is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2 .Incorrect parameter types. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackId: number;

export default class EntryAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.off('environment', callbackId, (error, data) => {
        if (error) {
          console.error(`unregisterEnvironmentCallback fail, err: ${JSON.stringify(error)}`);
        } else {
          console.info(`unregisterEnvironmentCallback success, data: ${JSON.stringify(data)}`);
        }
      });
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
  }
}
```

## off_environment('environment')

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'environment' | Yes | System environment change, for example, system dark/light color mode change. The value is fixed at **'environment'**. |
| callbackId | number | Yes | ID returned when the [ApplicationContext.on('environment')](#on_abilitylifecycleabilitylifecycle) API is called to register a listener for system environment changes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2 .Incorrect parameter types. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackId: number;

export default class MyAbility extends UIAbility {
  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.off('environment', callbackId);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
  }
}
```

## onAbilityLifecycle

```TypeScript
onAbilityLifecycle(callback: AbilityLifecycleCallback): int
```

Registers a listener to monitor the ability lifecycle of the application. This API uses an asynchronous callback to return the result. It can be called only by the main thread.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-onAbilityLifecycle(callback: AbilityLifecycleCallback): int--><!--Device-ApplicationContext-onAbilityLifecycle(callback: AbilityLifecycleCallback): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AbilityLifecycleCallback](arkts-ability-app-ability-abilitylifecyclecallback-abilitylifecyclecallback-c.md) | Yes | Callback triggered when the UIAbility lifecycle changes. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number code of the callback. |

## onApplicationStateChange

```TypeScript
onApplicationStateChange(callback: ApplicationStateChangeCallback): void
```

Register applicationStateChange callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-onApplicationStateChange(callback: ApplicationStateChangeCallback): void--><!--Device-ApplicationContext-onApplicationStateChange(callback: ApplicationStateChangeCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ApplicationStateChangeCallback](arkts-ability-app-ability-applicationstatechangecallback-applicationstatechangecallback-c.md) | Yes | The applicationStateChange callback. |

## onEnvironment

```TypeScript
onEnvironment(callback: EnvironmentCallback): int
```

Register environment callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-onEnvironment(callback: EnvironmentCallback): int--><!--Device-ApplicationContext-onEnvironment(callback: EnvironmentCallback): int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [EnvironmentCallback](../../apis-na/arkts-apis/arkts-na-app-ability-environmentcallback-environmentcallback-i.md) | Yes | The environment callback. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the number code of the callback. |

## onInteropAbilityLifecycle

```TypeScript
onInteropAbilityLifecycle(callback: InteropAbilityLifecycleCallback): void
```

Registers a listener to monitor the ability lifecycle of the application for interoperability. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-onInteropAbilityLifecycle(callback: InteropAbilityLifecycleCallback): void--><!--Device-ApplicationContext-onInteropAbilityLifecycle(callback: InteropAbilityLifecycleCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [InteropAbilityLifecycleCallback](arkts-ability-app-ability-interopabilitylifecyclecallback-interopabilitylifecyclecallback-i.md) | Yes | Callback used to be registered as the listener. |

## onSystemConfigurationUpdated

```TypeScript
onSystemConfigurationUpdated(callback: systemConfiguration.UpdatedCallback): void
```

Registers a listener for system configuration updated. &lt;p&gt;**NOTE：**: <br>It can be called only by the main thread. &lt;/p&gt;

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ApplicationContext-onSystemConfigurationUpdated(callback: systemConfiguration.UpdatedCallback): void--><!--Device-ApplicationContext-onSystemConfigurationUpdated(callback: systemConfiguration.UpdatedCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | systemConfiguration.UpdatedCallback | Yes | The system configuration updated callback. |

## on_abilityLifecycle('abilityLifecycle')

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'abilityLifecycle' | Yes | Lifecycle of the UIAbility within the application. The value is fixed at **'abilityLifecycle'**. |
| callback | [AbilityLifecycleCallback](arkts-ability-app-ability-abilitylifecyclecallback-abilitylifecyclecallback-c.md) | Yes | Callback triggered when the UIAbility lifecycle changes. |

**Return value:**

| Type | Description |
| --- | --- |
| number | ID of the callback registered. This ID is used to unregister the corresponding callback in [ApplicationContext.off('abilityLifecycle')]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Examples**

```TypeScript
import { UIAbility, AbilityLifecycleCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let lifecycleId: number;

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let AbilityLifecycleCallback: AbilityLifecycleCallback = {
      onAbilityCreate(ability) {
        console.info(`AbilityLifecycleCallback onAbilityCreate ability: ${ability}`);
      },
      onWindowStageCreate(ability, windowStage) {
        console.info(`AbilityLifecycleCallback onWindowStageCreate ability: ${ability}`);
        console.info(`AbilityLifecycleCallback onWindowStageCreate windowStage: ${windowStage}`);
      },
      onWindowStageActive(ability, windowStage) {
        console.info(`AbilityLifecycleCallback onWindowStageActive ability: ${ability}`);
        console.info(`AbilityLifecycleCallback onWindowStageActive windowStage: ${windowStage}`);
      },
      onWindowStageInactive(ability, windowStage) {
        console.info(`AbilityLifecycleCallback onWindowStageInactive ability: ${ability}`);
        console.info(`AbilityLifecycleCallback onWindowStageInactive windowStage: ${windowStage}`);
      },
      onWindowStageDestroy(ability, windowStage) {
        console.info(`AbilityLifecycleCallback onWindowStageDestroy ability: ${ability}`);
        console.info(`AbilityLifecycleCallback onWindowStageDestroy windowStage: ${windowStage}`);
      },
      onAbilityDestroy(ability) {
        console.info(`AbilityLifecycleCallback onAbilityDestroy ability: ${ability}`);
      },
      onAbilityForeground(ability) {
        console.info(`AbilityLifecycleCallback onAbilityForeground ability: ${ability}`);
      },
      onAbilityBackground(ability) {
        console.info(`AbilityLifecycleCallback onAbilityBackground ability: ${ability}`);
      },
      onAbilityContinue(ability) {
        console.info(`AbilityLifecycleCallback onAbilityContinue ability: ${ability}`);
      }
    }
    // 1. Obtain applicationContext through the context property.
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2. Register a listener for application lifecycle changes through applicationContext.
      lifecycleId = applicationContext.on('abilityLifecycle', AbilityLifecycleCallback);
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
    console.info(`registerAbilityLifecycleCallback lifecycleId: ${lifecycleId}`);
  }
}
```

## on_applicationStateChange('applicationStateChange')

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'applicationStateChange' | Yes | Application process state change. The value is fixed at **'applicationStateChange'**. |
| callback | [ApplicationStateChangeCallback](arkts-ability-app-ability-applicationstatechangecallback-applicationstatechangecallback-c.md) | Yes | Callback triggered when the application process state is changed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Examples**

```TypeScript
import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let applicationStateChangeCallback: ApplicationStateChangeCallback = {
      onApplicationForeground() {
        console.info('applicationStateChangeCallback onApplicationForeground');
      },
      onApplicationBackground() {
        console.info('applicationStateChangeCallback onApplicationBackground');
      }
    }

    // 1. Obtain an applicationContext object.
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2. Register a listener for application process state changes through applicationContext.
      applicationContext.on('applicationStateChange', applicationStateChangeCallback);
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
    console.info('Register applicationStateChangeCallback');
  }
}
```

## on_environment('environment')

```TypeScript
on(type: 'environment', callback: EnvironmentCallback): number
```

Registers a listener for system environment changes. This API uses an asynchronous callback to return the result. It can be called only on the main thread. > **NOTE：**> > - You can also use [onConfigurationUpdate](arkts-ability-app-ability-ability-ability-c.md#onconfigurationupdate) to > listen for system environment changes. Unlike > [onConfigurationUpdate](arkts-ability-app-ability-ability-ability-c.md#onconfigurationupdate) of **Ability**, this > API offers greater flexibility. It can be used both within application components and pages. However, the > environment variables that can be subscribed to are different from those of > [onConfigurationUpdate](arkts-ability-app-ability-ability-ability-c.md#onconfigurationupdate). For example, this > API cannot be used to subscribe to direction, screen density, and display ID changes. For details, see the > description of each environment variable in > [Configuration](arkts-ability-app-ability-configuration-configuration-i.md). > > - There are certain restrictions when this API is triggered. For example, if you set the application language by > calling [setLanguage](#setlanguage), the system does not trigger the > callback for the current API even if the system language changes. For details, see > [When to Use](../../../application-models/subscribe-system-environment-variable-changes.md#when-to-use).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationContext-on(type: 'environment', callback: EnvironmentCallback): number--><!--Device-ApplicationContext-on(type: 'environment', callback: EnvironmentCallback): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'environment' | Yes | System environment change, for example, system dark/light color mode change. The value is fixed at **'environment'**. |
| callback | [EnvironmentCallback](../../apis-na/arkts-apis/arkts-na-app-ability-environmentcallback-environmentcallback-i.md) | Yes | Callback triggered when the system environment changes. |

**Return value:**

| Type | Description |
| --- | --- |
| number | ID of the callback registered. This ID is used to unregister the corresponding callback in [ApplicationContext.off('environment')]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2 .Incorrect parameter types. |

**Examples**

```TypeScript
import { UIAbility, EnvironmentCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackId: number;

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate')
    let environmentCallback: EnvironmentCallback = {
      onConfigurationUpdated(config) {
        console.info(`onConfigurationUpdated config: ${JSON.stringify(config)}`);
      },
      onMemoryLevel(level) {
        console.info(`onMemoryLevel level: ${level}`);
      }
    };
    // 1. Obtain an applicationContext object.
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2. Register a listener for system environment changes through applicationContext.
      callbackId = applicationContext.on('environment', environmentCallback);
    } catch (paramError) {
      console.error(`error code: ${(paramError as BusinessError).code}, error msg: ${(paramError as BusinessError).message}`);
    }
    console.info(`registerEnvironmentCallback callbackId: ${callbackId}`);
  }
}
```

## restartApp

```TypeScript
restartApp(want: Want): void
```

Restarts the application and starts the specified UIAbility. This API can be called only by the main thread, and the application to restart must be active. > **NOTE：**> > When this API is called to restart the application, the **onDestroy** lifecycle callback of the ability in the > application is not triggered. > > If an atomic service calls this API, > [restartSelfAtomicService()](arkts-ability-abilitymanager-restartselfatomicservice-f.md) > , or [UIAbilityContext.restartApp()](arkts-ability-uiabilitycontext-c.md#restartapp) within 3 seconds after a > successful call to this API, the system returns error code 16000064. > > If an application calls this API or > [UIAbilityContext.restartApp()](arkts-ability-uiabilitycontext-c.md#restartapp) within 3 seconds after a > successful call to this API, the system returns error code 16000064.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationContext-restartApp(want: Want): void--><!--Device-ApplicationContext-restartApp(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Want information about the UIAbility to start. No verification is performed on the bundle name passed in. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) | The ability is not on the top of the UI. |
| [16000064](../errorcode-ability.md#16000064-frequent-application-restart) | Restart too frequently. Try again at least 3s later. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000063](../errorcode-ability.md#16000063-invalid-ability-during-application-restart) | The target to restart does not belong to the current application or is not a UIAbility. |

**Examples**

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'restartApp';
  private context = this.getUIContext().getHostContext()?.getApplicationContext() as common.ApplicationContext;

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let want: Want = {
            bundleName: 'com.example.myapplication',
            abilityName: 'EntryAbility'
          };
          if (this.context) {
            try {
              this.context.restartApp(want);
            } catch (err) {
              hilog.error(0x0000, 'testTag', `restart failed: ${err.code}, ${err.message}`);
            }
          } else {
            hilog.error(0x0000, 'testTag', "%{public}s", 'AppContext is null');
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## setColorMode

```TypeScript
setColorMode(colorMode: ConfigurationConstant.ColorMode): void
```

Sets the dark/light color mode for the application. This API can be called only on the main thread. > **NOTE：**> > Before calling this API, ensure that the window has been created and the page corresponding to the UIAbility has > been loaded (using the > [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9) API in the > [onWindowStageCreate()](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate) lifecycle).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void--><!--Device-ApplicationContext-setColorMode(colorMode: ConfigurationConstant.ColorMode): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colorMode | ConfigurationConstant.ColorMode | Yes | Dark/light color mode, which can be dark mode, light mode, or follow-system mode (default). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility, ConfigurationConstant } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info("Ability onWindowStageCreate");
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
      let applicationContext = this.context.getApplicationContext();
      applicationContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
    });
  }
}
```

## setFont

```TypeScript
setFont(font: string): void
```

Sets the font for this application. This API can be called only on the main thread. > **NOTE：**> > Before calling this API, ensure that the window has been created and the page corresponding to the UIAbility has > been loaded (using the > [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9) API in the > [onWindowStageCreate()](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate) lifecycle).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-setFont(font: string): void--><!--Device-ApplicationContext-setFont(font: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | string | Yes | Font, which can be registered by calling [UIContext.registerFont](../../../reference/apis-arkui/arkts-apis-uicontext-font.md#registerfont). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear() {
    this.getUIContext().getFont().registerFont({
      familyName: 'fontName',
      familySrc: $rawfile('font/medium.ttf')  // 'font/medium.ttf' is used only as an example. Replace it with the actual font resource file.
    });

    this.context.getApplicationContext().setFont('fontName');
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(50)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## setFontSizeScale

```TypeScript
setFontSizeScale(fontSizeScale: double): void
```

Sets the scale ratio for the font size of this application. This API can be called only on the main thread.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationContext-setFontSizeScale(fontSizeScale: double): void--><!--Device-ApplicationContext-setFontSizeScale(fontSizeScale: double): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontSizeScale | double | Yes | Font scale ratio. The value is a non-negative number. When the application's [fontSizeScale](../../../quick-start/app-configuration-file.md#configuration) is set to **followSystem** and the value set here exceeds the value of [fontSizeMaxScale](../../../quick-start/app-configuration-file.md#configuration), the value of [fontSizeMaxScale](../../../quick-start/app-configuration-file.md#configuration) takes effect. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        return;
      }
      let applicationContext = this.context.getApplicationContext();
      applicationContext.setFontSizeScale(2);
    });
  }
}
```

## setLanguage

```TypeScript
setLanguage(language: string): void
```

Sets the language for the application. This API can be called only on the main thread. > **NOTE：**> > Before calling this API, ensure that the window has been created and the page corresponding to the UIAbility has > been loaded (using the > [loadContent](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#loadcontent9) API in the > [onWindowStageCreate()](arkts-ability-app-ability-uiability-uiability-c.md#onwindowstagecreate) lifecycle).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationContext-setLanguage(language: string): void--><!--Device-ApplicationContext-setLanguage(language: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | Target language. The list of supported languages can be obtained by calling [getSystemLanguages()](../../apis-na/arkts-apis/arkts-na-i18n-system-c.md#getsystemlanguages). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    console.info("Ability onWindowStageCreate");
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        console.error(`Failed to load the content. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info(`Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
    });
    let applicationContext = this.context.getApplicationContext();
    applicationContext.setLanguage('zh-cn');
  }
}
```

## setSupportedProcessCache

```TypeScript
setSupportedProcessCache(isSupported : boolean): void
```

Sets whether the current application's process supports resource caching, so that the cached process resources can be reused when the application is started again. This API can be called only on the main thread. This setting applies only to the current process instance and does not affect others. If the application process instance is terminated, the previously set state will not be preserved and must be reset. This API can be properly called only on phones and 2-in-1 devices. If it is called on other device types, error code 801 is returned. > **NOTE：**> > - This API only sets the application to be ready for quick startup after caching. It does not mean that quick > startup will be triggered. Other conditions must be considered to determine whether to trigger quick startup. > > - To ensure that this API is effective before the process exits, it should be called as soon as possible. You are > advised to call this API within the **onCreate()** callback of the > [AbilityStage](arkts-ability-app-ability-abilitystage-abilitystage-c.md). > > - If this API is called multiple times within the same process, the outcome of the final call is used. In cases > where there are multiple AbilityStage instances, to achieve the desired result, this API must be called and > configured with the same value in each AbilityStage.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-ApplicationContext-setSupportedProcessCache(isSupported : boolean): void--><!--Device-ApplicationContext-setSupportedProcessCache(isSupported : boolean): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSupported | boolean | Yes | Whether process cache is supported. The value &lt;code&gt;true&lt;/code&gt; means that process cache is supported, and &lt;code&gt;false&lt;/code&gt; means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

```TypeScript
import { AbilityStage, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbilityStage extends AbilityStage {
  onCreate() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.setSupportedProcessCache(true);
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(`setSupportedProcessCache fail, code: ${code}, msg: ${message}`);
    }
  }
}
```

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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Indicates the UIAbility to start. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| 16000161 | Delayed process exit is not pending in the current process, and this API cannot be called. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: Fail to connect system service. |
| [16000130](../errorcode-ability.md#16000130-uiability-does-not-belong-to-the-caller) | The UIAbility does not belong to the caller. |
| 16000162 | The current process still has another UIAbility, and this API cannot be called. |
| [16000124](../errorcode-ability.md#16000124-starting-a-distributed-uiability-is-not-supported) | Starting a remote UIAbility is not supported. |
| [16000125](../errorcode-ability.md#16000125-starting-a-plugin-is-not-supported) | Starting a plugin UIAbility is not supported. |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) | An ability cannot be started or stopped in Wukong mode. |
| [16000122](../errorcode-ability.md#16000122-target-component-is-intercepted-by-the-system-control-module) | The target component is blocked by the system module and does not support startup. |
| [16000123](../errorcode-ability.md#16000123-implicit-startup-is-not-supported) | Implicit startup is not supported. |

