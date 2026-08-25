# AudioDeviceEnhanceManager

音频设备增强管理功能，用于应用级音频设备选择及流维度音频设备选择。 在使用AudioDeviceEnhanceManager的接口之前，需要先通过getDeviceEnhanceManager获取AudioDeviceEnhanceManager实例。

> **说明：**&gt;
> 应用在使用前应先调用isEnhancedRoutingSupported，确认系统是否支持音频设备增强管理功能。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

## 导入模块

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## isEnhancedRoutingSupported

```TypeScript
isEnhancedRoutingSupported(): boolean
```

查询系统是否支持当前管理器提供的增强路由能力。

> **说明：**&gt;
> - 增强路由能力包括为应用或音频流选择输入输出设备。&gt;
> - 应用在调用增强路由相关接口前，先调用本接口确认系统是否支持。即使是同一类型设备，不同机型也会因硬件限制而支持情况不同。&gt;
> - 当系统不支持增强路由能力时，调用相关接口不会生效，并会为应用或音频流选择默认的输入输出设备。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

**返回值：**

| 类型 |
| --- |
| boolean |

## selectInputDevice

```TypeScript
selectInputDevice(inputDevice: AudioDeviceDescriptor): Promise<void>
```

为应用选择输入设备。使用Promise异步回调。

> **说明：**&gt;
> - 此设置对应用下创建的所有录音流生效，除非特定流已经通过selectInputDeviceForAudioCapturer
> 指定了专属输入设备。&gt;
> - 当应用实现输入设备选择功能时，可以通过
> [AudioRoutingManager.getAvailableDevices](arkts-audio-audio-audioroutingmanager-i.md#getavailabledevices)
> 获取可用输入设备列表，并通过
> [AudioRoutingManager.getPreferredInputDeviceForCapturerInfo](arkts-audio-audio-audioroutingmanager-i.md#getpreferredinputdeviceforcapturerinfo)
> 获取当前首选输入设备。&gt;
> - 当应用退出或所选设备离线时，此选择将失效。应用重启或设备重新上线后，需要重新设置才会生效。&gt;
> - 当系统不支持此功能时，会为应用选择默认输入设备。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## selectInputDeviceForAudioCapturer

```TypeScript
selectInputDeviceForAudioCapturer(capturer: AudioCapturer, inputDevice: AudioDeviceDescriptor): Promise<void>
```

为指定音频录制流设置首选输入设备。使用Promise异步回调。

> **说明：**&gt;
> - 应用需要确保指定的AudioCapturer实例有效。&gt;
> - 此选择仅对指定音频流生效，应用内其他录音流会继续使用应用级选择的设备或系统默认输入设备。&gt;
> - 当应用退出或所选设备离线时，此选择将失效。应用重启或设备重新上线后，需要重新设置才会生效。&gt;
> - 当系统不支持此功能时，会为该音频录制流选择默认输入设备。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capturer | [AudioCapturer](arkts-audio-audio-audiocapturer-i.md) | 是 |
| inputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## selectOutputDevice

```TypeScript
selectOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<void>
```

为应用选择输出设备。使用Promise异步回调。

> **说明：**&gt;
> - 此设置对应用下创建的所有播放流生效，除非特定流已经通过selectOutputDeviceForAudioRenderer
> 指定了专属输出设备。&gt;
> - 当应用实现输出设备选择功能时，可以通过
> [AudioRoutingManager.getAvailableDevices](arkts-audio-audio-audioroutingmanager-i.md#getavailabledevices)
> 获取可用输出设备列表，并通过
> [AudioRoutingManager.getPreferOutputDeviceForRendererInfo](arkts-audio-audio-audioroutingmanager-i.md#getpreferoutputdeviceforrendererinfo)
> 获取当前首选输出设备。&gt;
> - 当应用退出或所选设备离线时，此选择将失效。应用重启或设备重新上线后，需要重新设置才会生效。&gt;
> - 当系统不支持此功能时，会为应用选择默认输出设备。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| outputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |

## selectOutputDeviceForAudioRenderer

```TypeScript
selectOutputDeviceForAudioRenderer(renderer: AudioRenderer, outputDevice: AudioDeviceDescriptor): Promise<void>
```

为指定音频播放流设置首选输出设备。使用Promise异步回调。

> **说明：**&gt;
> - 应用需要确保指定的AudioRenderer实例有效。&gt;
> - 此选择仅对指定音频流生效，应用内其他播放流会继续使用应用级选择的设备或系统默认输出设备。&gt;
> - 当应用退出或所选设备离线时，此选择将失效。应用重启或设备重新上线后，需要重新设置才会生效。&gt;
> - 当系统不支持此功能时，会为该音频播放流选择默认输出设备。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.DeviceEnhance

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| renderer | [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) | 是 |
| outputDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-无效入参) |
| [6800301](../errorcode-audio.md#6800301-系统处理异常) |
