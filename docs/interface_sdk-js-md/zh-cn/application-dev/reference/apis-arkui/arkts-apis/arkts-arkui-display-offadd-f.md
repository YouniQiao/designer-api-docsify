# offAdd

## 导入模块

```TypeScript
import { display } from '@kit.ArkUI';
```

## offAdd

```TypeScript
function offAdd(callback?: Callback<long>): void
```

Unregister the callback for display add events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 |

**示例**

```TypeScript
// 如果通过on注册多个callback，同时关闭所有callback监听
display.offAdd();

let callback: Callback<long> = (data: long) => {
  console.info(`Succeeded in unregistering the callback for display remove. Data: ${data}`)
};
// 关闭传入的callback监听
display.offAdd(callback);
```
