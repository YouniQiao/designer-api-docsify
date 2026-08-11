# startDeviceLogging（系统接口）

## startDeviceLogging

```TypeScript
function startDeviceLogging(url: string, maxSize?: number): Promise<void>
```

开始将设备日志写入文件。结果通过Promise异步回调方式返回。

**起始版本：** 13

<!--Device-avSession-function startDeviceLogging(url: string, maxSize?: int): Promise<void>--><!--Device-avSession-function startDeviceLogging(url: string, maxSize?: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| maxSize | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { fileIo } from '@kit.CoreFileKit';

let file = await fileIo.open("filePath");
let url = file.fd.toString();
avSession.startDeviceLogging(url, 2048).then(() => {
  console.info('Succeeded in starting device logging.');
})
```
