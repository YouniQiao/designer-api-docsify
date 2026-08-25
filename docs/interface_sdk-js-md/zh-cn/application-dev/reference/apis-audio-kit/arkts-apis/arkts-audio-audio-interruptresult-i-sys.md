# InterruptResult（系统接口）

音频中断结果。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { audio } from '@kit.AudioKit';
```

## interruptNode

```TypeScript
interruptNode: int
```

音频请求中断的节点。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**系统接口：** 此接口为系统接口。

## requestResult

```TypeScript
requestResult: InterruptRequestResultType
```

表示音频请求中断类型。

**类型：** [InterruptRequestResultType](arkts-audio-audio-interruptrequestresulttype-e-sys.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**系统接口：** 此接口为系统接口。
