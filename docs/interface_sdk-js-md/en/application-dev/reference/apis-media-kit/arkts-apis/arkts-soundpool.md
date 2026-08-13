# soundPool

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ErrorInfo](arkts-media-soundpool-errorinfo-i.md) | Describes the error information. |
| [PlayParameters](arkts-media-soundpool-playparameters-i.md) | Describes the playback parameters of the sound pool. These parameters are used to control the playback volume, number of loops, and priority. |
| [SoundPool](arkts-media-soundpool-soundpool-i.md) | Implements a sound pool that provides APIs for loading, unloading, playing, and stopping playing system sounds, setting the volume, and setting the number of loops. Before using these APIs, you must call [media.createSoundPool](../../../reference/apis-media-kit/arkts-apis-media-f.md) to create a SoundPool instance. > **NOTE：**> > - When using the SoundPool instance, you are advised to register the following callbacks to proactively obtain > status changes: > > - [on('loadComplete')](arkts-media-soundpool-soundpool-i.md#on_loadComplete): listens for the > event indicating that the resource loading is finished. You are advised to listen for this callback to ensure that > the audio is played after being loaded. > > - > [on('playFinishedWithStreamId')](arkts-media-soundpool-soundpool-i.md#on_loadComplete): > listens for the event indicating that the playback is finished and returns the stream ID of the audio that finishes > playing. > > - [on('playFinished')](arkts-media-soundpool-soundpool-i.md#on_loadComplete): listens > for the event indicating that the playback is finished. > > - [on('error')](arkts-media-soundpool-soundpool-i.md#on_loadComplete): listens for error events. > > - [on('errorOccurred')](arkts-media-soundpool-soundpool-i.md#on_loadComplete): listens for > error events and returns [errorInfo](arkts-media-soundpool-errorinfo-i.md#ErrorInfo). > > - Currently, SoundPool does not support audio focus policies such as background playback and audio interruption, or > skipping the silent frames at the beginning and end of an audio file. For details about low-latency playback using > SoundPool, see > [Using SoundPool to Play Short Sounds (ArkTS)](../../../media/media/using-soundpool-for-playback.md). |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [PlayParameters](arkts-media-soundpool-playparameters-i-sys.md) | Describes the playback parameters of the sound pool. These parameters are used to control the playback volume, number of loops, and priority. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ErrorType](arkts-media-soundpool-errortype-e.md) | Enumerates the error types (used to distinguish error stages). |

