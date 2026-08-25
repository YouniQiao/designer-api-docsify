# onChange

## 导入模块

```TypeScript
import { display } from '@kit.ArkUI';
```

## onChange

```TypeScript
function onChange(callback: Callback<long>): void
```

Register the callback for display changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 |

**示例**

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<long> = (data: long) => {
  console.info(`Listening enabled. Data: ${data}`);
};

display.onChange(callback);
```
