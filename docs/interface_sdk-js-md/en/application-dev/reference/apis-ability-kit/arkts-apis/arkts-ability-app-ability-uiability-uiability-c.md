# UIAbility

Application component that has the UI. It provides lifecycle callbacks such as component creation, destruction, and foreground/background switching, and supports background communication.

**Inheritance/Implementation:** UIAbility extends [Ability](arkts-ability-app-ability-ability-ability-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { UIAbility, Callee, CalleeCallback, Caller, OnReleaseCallback, OnRemoteStateChangeCallback } from '@kit.AbilityKit';
```

## onBackground

```TypeScript
onBackground(): void
```

Called when the application transitions from the foreground to the background. You can release resources when the UI is no longer visible, for example, stopping location services, within this callback.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onBackground() {
    // The UIAbility transitions to the background.
    hilog.info(0x0000, 'testTag', `onBackground`);
  }
}
```

## onBackPressed

```TypeScript
onBackPressed(): boolean
```

Called when an operation of going back to the previous page is triggered on this UIAbility. The return value determines whether to destroy the UIAbility instance.  
- When the target SDK version is earlier than 12, the default return value is **false**, indicating that the UIAbility will be destroyed. - When the target SDK version is 12 or later, the default return value is **true**, indicating that the UIAbility will be moved to the background and will not be destroyed.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onBackPressed() {
    return true;
  }
}
```

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

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

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

**Examples**

```TypeScript
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyAbility extends UIAbility {
  onCollaborate(wantParam: Record<string, Object>) {
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
}
```

## onCollaborate

```TypeScript
onCollaborate(wantParam: Record<string, RecordData>): AbilityConstant.CollaborateResult
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

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wantParam | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| AbilityConstant.CollaborateResult |

**Examples**

See [onCollaborate](#oncollaborate)

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

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

**Examples**

The following is an example of saving data using a synchronous API during application migration:

```TypeScript
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onContinue(wantParams: Record<string, Object>) {
    console.info('onContinue');
    wantParams['myData'] = 'my1234567';
    return AbilityConstant.OnContinueResult.AGREE;
  }
}
```

The following is an example of saving data using an asynchronous API during application migration:

```TypeScript
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  async setWant(wantParams: Record<string, Object>) {
    console.info('setWant start');
    for (let time = 0; time < 1000; ++time) {
      wantParams[time] = time;
    }
    console.info('setWant end');
  }

  async onContinue(wantParams: Record<string, Object>) {
    console.info('onContinue');
    return this.setWant(wantParams).then(() => {
      return AbilityConstant.OnContinueResult.AGREE;
    });
  }
}
```

## onCreate

```TypeScript
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
```

Called when a UIAbility instance is created. You can execute initialization logic (such as defining variables and loading resources) in this callback. This callback is invoked during a [cold start](../../../application-models/uiability-intra-device-interaction.md#cold-starting-uiability) of the UIAbility.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| launchParam | AbilityConstant.LaunchParam | Yes |

**Examples**

```TypeScript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // Execute an asynchronous task.
    hilog.info(0x0000, 'testTag',
      `onCreate, want: ${want.abilityName}, the launchReason is ${launchParam.launchReason}, the lastExitReason is ${launchParam.lastExitReason}`);
  }
}
```

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

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Examples**

A synchronous callback example is as follows:

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onDestroy() {
    hilog.info(0x0000, 'testTag', `onDestroy`);
    // Call the synchronous function.
  }
}
```

A promise asynchronous callback example is as follows:

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  async onDestroy() {
    hilog.info(0x0000, 'testTag', `onDestroy`);
    // Call the asynchronous function.
  }
}
```

## onDestroy

```TypeScript
onDestroy(): Promise<void> | undefined
```

Called when the UIAbility is destroyed (for example, when the UIAbility is terminated using the [terminateSelf](arkts-ability-uiabilitycontext-c.md#terminateself) API). You can clear resources and save data during this lifecycle.This API returns the result synchronously or uses a promise to return the result.

> **NOTE：**&gt;
> - Once the **onDestroy** lifecycle callback completes, the application may exit. This can interrupt any pending
> asynchronous operations (such as asynchronously writing data to a database), preventing them from finishing
> successfully. In this case, you are advised to use a promise to return the result.&gt;
> - The callback is invoked only when the UIAbility exits gracefully. It is not invoked in cases of abnormal exits
> (for example, process termination due to low memory conditions).

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; \ | undefined |

**Examples**

See [onDestroy](#ondestroy)

## onDidBackground

```TypeScript
onDidBackground(): void
```

Called after the application has transitioned to the background. It is called after [onBackground](#onbackground). It can be used to release resources after the application has entered the background, for example, stopping audio playback.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { audio } from '@kit.AudioKit';

export default class MyUIAbility extends UIAbility {
  static audioRenderer: audio.AudioRenderer;

  // ...
  onForeground(): void {
    let audioStreamInfo: audio.AudioStreamInfo = {
      samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // Sampling rate.
      channels: audio.AudioChannel.CHANNEL_2, // Channel.
      sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // Sampling format.
      encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // Encoding format.
    };

    let audioRendererInfo: audio.AudioRendererInfo = {
      usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
      rendererFlags: 0 // AudioRenderer flag.
    };

    let audioRendererOptions: audio.AudioRendererOptions = {
      streamInfo: audioStreamInfo,
      rendererInfo: audioRendererInfo
    };

    // Request an AudioRenderer in the foreground to play Pulse Code Modulation (PCM) audio data.
    audio.createAudioRenderer(audioRendererOptions).then((data) => {
      MyUIAbility.audioRenderer = data;
      hilog.info(0x0000, 'testTag', `AudioRenderer Created : Success : Stream Type: SUCCESS.`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `AudioRenderer Created : F : ${JSON.stringify(err)}.`);
    });
  }

  onDidBackground() {
    // Release the AudioRenderer after transitioning to the background.
    MyUIAbility.audioRenderer.release((err: BusinessError) => {
      if (err) {
        hilog.error(0x0000, 'testTag', `AudioRenderer release failed, error: ${JSON.stringify(err)}.`);
      } else {
        hilog.info(0x0000, 'testTag', `AudioRenderer released.`);
      }
    });
  }
}
```

## onDidForeground

```TypeScript
onDidForeground(): void
```

Called after the application has transitioned to the foreground. It is called after [onForeground](#onforeground). It can be used to capture the moment when the application fully transitions to the foreground. When paired with [onWillForeground](#onwillforeground), it can also measure the duration from the application's initial foreground entry to its full transition into the foreground state.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Examples**

For details, see [onWillForeground](#onwillforeground).

## onDump

```TypeScript
onDump(params: Array<string>): Array<string>
```

Called when UIAbility data is dumped by running the dump command during application debugging. You can return non- sensitive information to be dumped by the UIAbility in this callback.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onDump(params: Array<string>) {
    console.info(`dump, params: ${JSON.stringify(params)}`);
    return ['params'];
  }
}
```

## onForeground

```TypeScript
onForeground(): void
```

Called when the application is initially launched into the foreground or transitions from the background to the foreground. You can request necessary system resources, for example, requesting location services when the application transitions to the foreground, within this callback.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onForeground() {
    hilog.info(0x0000, 'testTag', `onForeground`);
  }
}
```

## onNewWant

```TypeScript
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void
```

Called when a started UIAbility instance is brought up again. If there are specific scenarios where you do not want this lifecycle callback to be triggered, you can use [setOnNewWantSkipScenarios](arkts-ability-uiabilitycontext-c.md#setonnewwantskipscenarios) to set those [scenarios](arkts-ability-contextconstant-scenarios-e.md).This API returns the result synchronously and does not support asynchronous callback.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| launchParam | AbilityConstant.LaunchParam | Yes |

**Examples**

```TypeScript
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info(`onNewWant, want: ${want.abilityName}`);
    console.info(`onNewWant, launchParam: ${JSON.stringify(launchParam)}`);
  }
}
```

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
> [window.WindowStage.on('windowStageClose')](../../../reference/apis-arkui/arkts-apis-window-WindowStage.md#onwindowstageclose)
> , this callback function is not executed.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PREPARE_APP_TERMINATE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onPrepareToTerminate() {
    // Define a pre-termination operation,
    // for example, starting another UIAbility and performing asynchronous termination based on the startup result.
    let want: Want = {
      bundleName: "com.example.myapplication",
      moduleName: "entry",
      abilityName: "SecondAbility"
    }
    this.context.startAbilityForResult(want)
      .then((result) => {
        // Obtain the startup result and terminate the current UIAbility when resultCode in the return value is 0.
        console.info('startAbilityForResult success, resultCode is ' + result.resultCode);
        if (result.resultCode === 0) {
          this.context.terminateSelf();
        }
      }).catch((err: BusinessError) => {
      // Exception handling.
      console.error('startAbilityForResult failed, err:' + JSON.stringify(err));
      this.context.terminateSelf();
    })

    return true; // The pre-termination operation is defined. The value true means that the UIAbility termination process is canceled.
  }
}
```

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

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PREPARE_APP_TERMINATE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  async onPrepareToTerminateAsync(): Promise<boolean> {
    await new Promise<boolean>((res, rej) => {
      setTimeout (res, 2000); // Execute the operation 2 seconds later.
    });
    return true; // The pre-termination operation is defined. The value true means that the UIAbility termination process is canceled.
  }
}
```

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

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

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

**Examples**

```TypeScript
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
    console.info('onSaveState');
    wantParam['myData'] = 'my1234567';
    return AbilityConstant.OnSaveResult.RECOVERY_AGREE;
  }
}
```

## onSaveState

```TypeScript
onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, RecordData>): AbilityConstant.OnSaveResult
```

This API must be used with [appRecovery](arkts-app-ability-apprecovery.md). When the application has enabled the fault recovery feature (with the **saveOccasion** parameter in [enableAppRecovery](arkts-ability-apprecovery-enableapprecovery-f.md) set to **SAVE_WHEN_ERROR**), this callback is invoked to save the UIAbility data in the case of an application fault.

> **NOTE：**&gt;
> Starting from API version 20, this callback is not executed when
> [onSaveStateAsync](#onsavestateasync)
> is implemented.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | AbilityConstant.StateType | Yes |
| wantParam | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| AbilityConstant.OnSaveResult |

**Examples**

See [onSaveState](#onsavestate)

## onSaveStateAsync

```TypeScript
onSaveStateAsync(stateType: AbilityConstant.StateType, wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult>
```

This API must be used with [appRecovery](arkts-app-ability-apprecovery.md). When the application has enabled the fault recovery feature (with the **saveOccasion** parameter in [enableAppRecovery](arkts-ability-apprecovery-enableapprecovery-f.md) set to **SAVE_WHEN_ERROR**), this callback is invoked to save the UIAbility data in the case of an application fault. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

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

**Examples**

```TypeScript
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  async onSaveStateAsync(reason: AbilityConstant.StateType,
    wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult> {
    await new Promise<string>((res, rej) => {
      setTimeout(res, 1000); // Execute the operation after 1 second.
    });
    return AbilityConstant.OnSaveResult.RECOVERY_AGREE;
  }
}
```

## onSaveStateAsync

```TypeScript
onSaveStateAsync(stateType: AbilityConstant.StateType, wantParam: Record<string, RecordData>): Promise<AbilityConstant.OnSaveResult>
```

This API must be used with [appRecovery](arkts-app-ability-apprecovery.md). When the application has enabled the fault recovery feature (with the **saveOccasion** parameter in [enableAppRecovery](arkts-ability-apprecovery-enableapprecovery-f.md) set to **SAVE_WHEN_ERROR**), this callback is invoked to save the UIAbility data in the case of an application fault. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [stateType](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-bundlestate-bundleactivestate-i.md) | AbilityConstant.StateType | Yes |
| wantParam | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;AbilityConstant.OnSaveResult & gt; |

**Examples**

See [onSaveStateAsync](#onsavestateasync)

## onShare

```TypeScript
onShare(wantParam: Record<string, Object>): void
```

Called when an atomic service is shared across devices. You can set the title, abstract, and URL of the atomic service to be shared in this callback.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wantParam | Record & lt;string, Object & gt; | Yes |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';

export default class MyUIAbility extends UIAbility {
  onShare(wantParams: Record<string, Object>) {
    console.info('onShare');
    wantParams['ohos.extra.param.key.shareUrl'] = 'example.com';
  }
}
```

## onShare

```TypeScript
onShare(wantParam: Record<string, RecordData>): void
```

Called when an atomic service is shared across devices. You can set the title, abstract, and URL of the atomic service to be shared in this callback.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| wantParam | Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes |

**Examples**

See [onShare](#onshare)

## onWillBackground

```TypeScript
onWillBackground(): void
```

Called just when the application transitions to the background. It is called before [onBackground](#onbackground). It can be used to log various types of data, such as faults, statistics, security information, and user behavior that occur during application running.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyUIAbility extends UIAbility {
  onWillBackground(): void {
    let eventParams: Record<string, number | string> = {
      "int_data": 100,
      "str_data": "strValue",
    };
    // Record the application fault information.
    hiAppEvent.write({
      domain: "test_domain",
      name: "test_event",
      eventType: hiAppEvent.EventType.FAULT,
      params: eventParams,
    }, (err: BusinessError) => {
      if (err) {
        hilog.error(0x0000, 'testTag', `hiAppEvent code: ${err.code}, message: ${err.message}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `hiAppEvent success to write event`);
    });
  }
}
```

## onWillForeground

```TypeScript
onWillForeground(): void
```

Called just before the application transitions to the foreground. It is called before [onForeground](#onforeground). It can be used to capture the moment when the application starts to transition to the foreground. When paired with [onDidForeground](#ondidforeground), it can also measure the duration from the application's initial foreground entry to its full transition into the foreground state.This API returns the result synchronously and does not support asynchronous callback.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  // ...

  onWillForeground(): void {
    // Start to log the event that the application starts moving to the foreground.
    let eventParams: Record<string, number> = { 'xxxx': 100 };
    let eventInfo: hiAppEvent.AppEventInfo = {
      // Define the event domain.
      domain: "lifecycle",
      // Define the event name.
      name: "onwillforeground",
      // Define the event type.
      eventType: hiAppEvent.EventType.BEHAVIOR,
      // Define the event parameters.
      params: eventParams,
    };
    hiAppEvent.write(eventInfo).then(() => {
      hilog.info(0x0000, 'testTag', `HiAppEvent success to write event`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`);
    });
  }

  // ...

  onDidForeground(): void {
    // Start to log the event that the application fully transitions to the foreground.
    let eventParams: Record<string, number> = { 'xxxx': 100 };
    let eventInfo: hiAppEvent.AppEventInfo = {
      // Define the event domain.
      domain: "lifecycle",
      // Define the event name.
      name: "ondidforeground",
      // Define the event type.
      eventType: hiAppEvent.EventType.BEHAVIOR,
      // Define the event parameters.
      params: eventParams,
    };
    hiAppEvent.write(eventInfo).then(() => {
      hilog.info(0x0000, 'testTag', `HiAppEvent success to write event`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`);
    });
  }
}
```

## onWindowStageCreate

```TypeScript
onWindowStageCreate(windowStage: window.WindowStage): void
```

Called when a [WindowStage](../../apis-arkui/arkts-apis/arkts-arkui-window-n.md) instance is created. You can load a page through the WindowStage instance in this callback.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowStage | window.WindowStage | Yes |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  // The main window has been created. Set the main page for the UIAbility.
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err)}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
    });
  }
}
```

## onWindowStageDestroy

```TypeScript
onWindowStageDestroy(): void
```

Called when the WindowStage instance has been destroyed. It informs applications that the WindowStage instance is no longer available for use.The callback is invoked only when the UIAbility exits gracefully. It is not invoked in cases of abnormal exits (for example, process termination due to low memory conditions).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class MyUIAbility extends UIAbility {
  onWindowStageDestroy() {
    // The main window is destroyed. It is time to release UI resources.
    hilog.info(0x0000, 'testTag', `onWindowStageDestroy`);
  }
}
```

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

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowStage | window.WindowStage | Yes |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  onWindowStageRestore(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', `onWindowStageRestore`);
  }
}
```

## onWindowStageWillDestroy

```TypeScript
onWindowStageWillDestroy(windowStage: window.WindowStage): void
```

Called when the WindowStage instance is about to be destroyed. You can cancel the listening of WindowStage events in this lifecycle.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowStage | window.WindowStage | Yes |

**Examples**

```TypeScript
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class MyUIAbility extends UIAbility {
  onWindowStageWillDestroy(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', `onWindowStageWillDestroy`);
  }
}
```

## callee

```TypeScript
callee: Callee
```

Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee), which is capable of receiving data sent from the Caller object.

**Type:** [Callee](arkts-ability-app-ability-uiability-callee-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## context

```TypeScript
context: UIAbilityContext
```

Context of the UIAbility.

**Type:** [UIAbilityContext](arkts-ability-uiabilitycontext-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## lastRequestWant

```TypeScript
lastRequestWant: Want
```

Want in the most recent request to launch the UIAbility.  
- On the first launch of a UIAbility, it is the Want parameter received in [onCreate](#oncreate). - On subsequent launches, it is the most recent Want received in [onNewWant](#onnewwant).

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore
