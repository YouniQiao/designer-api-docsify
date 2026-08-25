# sendImage（系统接口）

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## sendImage

```TypeScript
function sendImage(sessionId: number, image: image.PixelMap, quality?: number): Promise<void>
```

应用连接成功并创建传输流后，设备A或设备B可向对端设备发送图片。 图片会根据指定的压缩质量进行编码后，通过传输流通道发送至对端设备。 发送成功后，对端设备可通过注册的回调接收图片，使用Promise异步回调。 业务结束后应及时销毁传输流，否则会增加系统功耗，使用场景包括跨设备视频通话中发送视频帧、 远程协作时发送截图、跨设备图片共享等需要向对端发送图片数据的场景。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |
| [image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md) | image.PixelMap | 是 |
| quality | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
