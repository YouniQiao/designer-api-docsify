# createAudioRenderer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## createAudioRenderer

```TypeScript
function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void
```

Obtains an [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) instance. This method uses a promise to return the renderer instance.The AudioRenderer instance is used to play streaming audio data. When using AudioRenderer apis, there are many instructions for application to achieve better performance and lower power consumption: In music or audiobook background playback situation, you can have low power consumption by following this best practices document **Low-Power Rules in Music Playback Scenarios**. And for navigation situation, you can follow **Low-Power Rules in Navigation and Positioning Scenarios**.Application developer should also be careful when app goes to background, please check if your audio playback is still needed, see **Audio Resources** in best practices document. And avoiding to send silence audio data continuously to waste system resources, otherwise system will take control measures when this behavior is detected, see **Audio Playback** in best practices document.If you want to use AudioRenderer api to implement a music playback application, there are also many interactive scenes to consider, see **Developing an Audio Application** in best practices document.

**Since:** 8

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[AudioRenderer](arkts-audio-audio-audiorenderer-i.md)&gt; | Yes |


## createAudioRenderer

```TypeScript
function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>
```

Obtains an [AudioRenderer](arkts-audio-audio-audiorenderer-i.md) instance. This method uses a promise to return the renderer instance.The AudioRenderer instance is used to play streaming audio data. When using AudioRenderer apis, there are many instructions for application to achieve better performance and lower power consumption: In music or audiobook background playback situation, you can have low power consumption by following this best practices document **Low-Power Rules in Music Playback Scenarios**. And for navigation situation, you can follow **Low-Power Rules in Navigation and Positioning Scenarios**.Application developer should also be careful when app goes to background, please check if your audio playback is still needed, see **Audio Resources** in best practices document. And avoiding to send silence audio data continuously to waste system resources, otherwise system will take control measures when this behavior is detected, see **Audio Playback** in best practices document.If you want to use AudioRenderer api to implement a music playback application, there are also many interactive scenes to consider, see **Developing an Audio Application** in best practices document.

**Since:** 8

**System capability:** SystemCapability.Multimedia.Audio.Renderer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [AudioRendererOptions](arkts-audio-audio-audiorendereroptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AudioRenderer](arkts-audio-audio-audiorenderer-i.md)&gt; |
