# offConnect（系统接口）

## 导入模块

```TypeScript
import { screen } from '@kit.ArkUI';
```

## offConnect

```TypeScript
function offConnect(callback?: Callback<long>): void
```

Unregister the callback for screen connection events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
let callback: Callback<long> = (data: long) => {
  console.info(`Succeeded in unregistering the callback for screen changes. Data: ${data}`)
};
screen.offConnect(callback);
screen.offConnect();
```
