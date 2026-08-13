# startAVPlayback（系统接口）

## startAVPlayback

```TypeScript
function startAVPlayback(bundleName: string, assetId: string): Promise<void>
```

启动媒体播放应用程序。结果通过Promise异步回调方式返回。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function startAVPlayback(bundleName: string, assetId: string): Promise<void>--><!--Device-avSession-function startAVPlayback(bundleName: string, assetId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| assetId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { audio } from '@kit.AudioKit';

avSession.startAVPlayback("com.example.myapplication", "121278").then(() => {
  console.info('Succeeded in starting AV playback.');
});
```


## startAVPlayback

```TypeScript
function startAVPlayback(bundleName: string, assetId: string, info: CommandInfo): Promise<void>
```

携带启动参数的冷启动应用播放接口

**起始版本：** 24

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function startAVPlayback(bundleName: string, assetId: string, info: CommandInfo): Promise<void>--><!--Device-avSession-function startAVPlayback(bundleName: string, assetId: string, info: CommandInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| assetId | string | 是 |
| info | [CommandInfo](arkts-avsession-avsession-commandinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
