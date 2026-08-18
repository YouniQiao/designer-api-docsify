# AVCastPickerHelper

A helper to enable a picker to select output devices

**Since:** 23

<!--Device-avSession-class AVCastPickerHelper--><!--Device-avSession-class AVCastPickerHelper-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## Modules to Import

```TypeScript
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## offPickerStateChange

```TypeScript
offPickerStateChange(callback?: Callback<AVCastPickerState>) : void
```

Unregister picker state change callback.

**Since:** 23

<!--Device-AVCastPickerHelper-offPickerStateChange(callback?: Callback<AVCastPickerState>) : void--><!--Device-AVCastPickerHelper-offPickerStateChange(callback?: Callback<AVCastPickerState>) : void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCastPickerState](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstate-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## off_pickerStateChange

```TypeScript
off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void
```

Unregister picker state change callback.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AVCastPickerHelper-off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void--><!--Device-AVCastPickerHelper-off(type: 'pickerStateChange', callback?: Callback<AVCastPickerState>) : void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'pickerStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCastPickerState](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstate-e.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## onPickerStateChange

```TypeScript
onPickerStateChange(callback: Callback<AVCastPickerState>) : void
```

Register picker state change callback.

**Since:** 23

<!--Device-AVCastPickerHelper-onPickerStateChange(callback: Callback<AVCastPickerState>) : void--><!--Device-AVCastPickerHelper-onPickerStateChange(callback: Callback<AVCastPickerState>) : void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCastPickerState](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstate-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

## on_pickerStateChange

```TypeScript
on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void
```

Register picker state change callback.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AVCastPickerHelper-on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void--><!--Device-AVCastPickerHelper-on(type: 'pickerStateChange', callback: Callback<AVCastPickerState>) : void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'pickerStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AVCastPickerState](arkts-avsession-multimedia-avcastpickerparam-avcastpickerstate-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AVCastPickerOptions](arkts-avsession-avsession-avcastpickeroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
