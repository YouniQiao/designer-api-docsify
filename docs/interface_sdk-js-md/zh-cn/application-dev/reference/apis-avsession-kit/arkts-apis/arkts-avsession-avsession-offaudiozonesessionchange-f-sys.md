# offAudioZoneSessionChange（系统接口）

## 导入模块

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## offAudioZoneSessionChange

```TypeScript
function offAudioZoneSessionChange(userId: int, callback?: Callback<AVSessionDescriptor>): void
```

取消注册音区对应的会话变化监听

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avSession-function offAudioZoneSessionChange(userId: int, callback?: Callback<AVSessionDescriptor>): void--><!--Device-avSession-function offAudioZoneSessionChange(userId: int, callback?: Callback<AVSessionDescriptor>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 用户id，归属某个音区 &lt;br&gt;用户userId 所归属的音区 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AVSessionDescriptor&gt; | 否 | 返回对应音区的会话列表 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 202 | Not System App. |

