# onDisconnect（系统接口）

## 导入模块

```TypeScript
import { screen } from '@kit.ArkUI';
```

## onDisconnect

```TypeScript
function onDisconnect(callback: Callback<long>): void
```

Register the callback for screen disconnection events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
let callback: Callback<long> = (data: long) => {
  console.info(`Succeeded in registering the callback for screen disconnect. Data: ${data}`)
};
screen.onDisconnect(callback);
```
