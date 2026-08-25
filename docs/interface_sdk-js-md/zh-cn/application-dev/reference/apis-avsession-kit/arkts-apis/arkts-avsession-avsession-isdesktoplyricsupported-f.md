# isDesktopLyricSupported

## 导入模块

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## isDesktopLyricSupported

```TypeScript
function isDesktopLyricSupported(): Promise<boolean>
```

设备是否支持桌面歌词功能。使用Promise异步回调。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |

**示例**

```TypeScript
import { avSession } from '@kit.AVSessionKit';

avSession.isDesktopLyricSupported().then((isSupported: boolean) => {
  console.info(`isDesktopLyricSupported : SUCCESS : isSupported : ${isSupported}`);
});
```
