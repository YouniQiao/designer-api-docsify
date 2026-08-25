# AVDataSrcDescriptor

Defines the descriptor of an audio and video file, which is used in DataSource playback mode. Use scenario: An application can create a playback instance and start playback before it finishes downloading the audio and video resources.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

## 导入模块

```TypeScript
import { media } from '@kit.MediaKit';
```

## callback

ArkTS-Dyn:
```TypeScript
callback: (buffer: ArrayBuffer, length: number, pos?: number) => number
```

ArkTS-Sta:
```TypeScript
callback: (buffer: ArrayBuffer, length: long, pos?: long) => int
```

Callback function implemented by users, which is used to fill data. buffer - The buffer need to fill. length - The stream length player want to get. pos - The stream position player want get start, and is an optional parameter. When fileSize set to -1, this parameter is not used. Returns length of the data to be filled, Return -1 to indicate that the end of the stream is reached, Return -2 to indicate that an unrecoverable error has been encountered.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| buffer | ArrayBuffer | 是 |
| length | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| pos | ArkTS-Dyn: number<br>ArkTS-Sta：long | 否 |

## fileSize

```TypeScript
fileSize: long
```

Size of the file, -1 means the file size is unknown, in this case, seek and setSpeed can't be executed, loop can't be set, and can't replay.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer
