# AVCastPickerHelper

A helper to enable a picker to select output devices

**Since:** 23

<!--Device-avSession-class AVCastPickerHelper--><!--Device-avSession-class AVCastPickerHelper-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## constructor

```TypeScript
constructor(context: Context)
```

The constructor used to create a AVCastPickerHelper object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVCastPickerHelper-constructor(context: Context)--><!--Device-AVCastPickerHelper-constructor(context: Context)-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | represents the context. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

**Examples**

```TypeScript
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as Context;
            let avCastPicker = new avSession.AVCastPickerHelper(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## off('pickerStateChange')

```TypeScript
off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void
```

Unregister picker state change callback.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AVCastPickerHelper-off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void--><!--Device-AVCastPickerHelper-off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'pickerStateChange' | Yes | 'pickerStateChange' |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCastPickerState](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstate-e.md)&gt; | No | The callback used to handle picker state changed event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

## offPickerStateChange

```TypeScript
offPickerStateChange(callback?: Callback<AVCastPickerState>) : void
```

Unregister picker state change callback.

**Since:** 23

<!--Device-AVCastPickerHelper-offPickerStateChange(callback?: Callback<AVCastPickerState>) : void--><!--Device-AVCastPickerHelper-offPickerStateChange(callback?: Callback<AVCastPickerState>) : void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCastPickerState](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstate-e.md)&gt; | No | The callback used to handle picker state changed event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

## on('pickerStateChange')

```TypeScript
on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void
```

Register picker state change callback.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AVCastPickerHelper-on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void--><!--Device-AVCastPickerHelper-on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'pickerStateChange' | Yes | 'pickerStateChange' |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCastPickerState](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstate-e.md)&gt; | Yes | The callback used to handle picker state changed event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

## onPickerStateChange

```TypeScript
onPickerStateChange(callback: Callback<AVCastPickerState>) : void
```

Register picker state change callback.

**Since:** 23

<!--Device-AVCastPickerHelper-onPickerStateChange(callback: Callback<AVCastPickerState>) : void--><!--Device-AVCastPickerHelper-onPickerStateChange(callback: Callback<AVCastPickerState>) : void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCastPickerState](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstate-e.md)&gt; | Yes | The callback used to handle picker state changed event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

## resetCommunicationDevice

```TypeScript
resetCommunicationDevice(): Promise<void>
```

Reset audio device to be default set by the platform which is used for communication use cases including voice or video calls. For example, the audio output device will be switched to earpiece for voice call and to speaker for video call on phone.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AVCastPickerHelper-resetCommunicationDevice(): Promise<void>--><!--Device-AVCastPickerHelper-resetCommunicationDevice(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Examples**

```TypeScript
import { common } from '@kit.AbilityKit';
import { avSession } from '@kit.AVSessionKit';

async function avCastPicker(context: common.Context) {
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.resetCommunicationDevice().then(() => {
    console.info('resetCommunicationDevice successfully');
  });
}
```

## select

```TypeScript
select(options?: AVCastPickerOptions): Promise<void>
```

Pull up the avcastpicker based on the options.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AVCastPickerHelper-select(options?: AVCastPickerOptions): Promise<void>--><!--Device-AVCastPickerHelper-select(options?: AVCastPickerOptions): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [AVCastPickerOptions](arkts-avsession-avsession-avcastpickeroptions-i.md) | No | represents the options provided to the picker. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | void promise when executed successfully |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**Examples**

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

async function avCastPicker(context: common.Context) {
  let avCastPickerOptions : avSession.AVCastPickerOptions = {
    sessionType : 'video',
  }
  let avCastPicker = new avSession.AVCastPickerHelper(context);
  avCastPicker.select(avCastPickerOptions).then(() => {
    console.info('select successfully');
  }).catch((err: BusinessError) => {
    console.error(`AVCastPicker.select failed with err: ${err.code}, ${err.message}`);
  });
}
```

