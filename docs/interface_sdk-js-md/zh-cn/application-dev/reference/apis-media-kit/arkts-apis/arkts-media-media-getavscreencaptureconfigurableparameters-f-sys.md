# getAVScreenCaptureConfigurableParameters（系统接口）

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getAVScreenCaptureConfigurableParameters

```TypeScript
function getAVScreenCaptureConfigurableParameters(sessionId: number): Promise<string>
```

get Configurations which user can changes from AVScreenCapture server

**起始版本：** 20

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400109](../errorcode-media.md#5400109-会话id不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
