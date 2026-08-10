# TTS

Provides methods for setting information about text-to-speech (TTS) conversion, including the pitch, speech rate,engine, and plug-ins.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-settings-namespace TTS--><!--Device-settings-namespace TTS-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 常量

| 名称 | 说明 |
| --- | --- |
| [DEFAULT_TTS_PITCH](arkts-basicservices-tts-con.md#default_tts_pitch) | Indicates the default pitch of the text-to-speech (TTS) engine.  &lt;p&gt;100 = 1x. If the value is set to {@code 200}, the frequency is twice the normal sound frequency. |
| [DEFAULT_TTS_RATE](arkts-basicservices-tts-con.md#default_tts_rate) | Indicates the default speech rate of the TTS engine. 100 = 1x. |
| [DEFAULT_TTS_SYNTH](arkts-basicservices-tts-con.md#default_tts_synth) | Indicates the default TTS engine. |
| [ENABLED_TTS_PLUGINS](arkts-basicservices-tts-con.md#enabled_tts_plugins) | Indicates the list of activated plug-in packages used for TTS. Multiple plug-in packages are separated by spaces. |

