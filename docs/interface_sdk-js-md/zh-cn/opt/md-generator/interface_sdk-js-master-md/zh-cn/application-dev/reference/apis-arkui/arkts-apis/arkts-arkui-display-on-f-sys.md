# on（系统接口）

## on('privateModeChange')

```TypeScript
function on(type: 'privateModeChange', callback: Callback<boolean>): void
```

开启屏幕隐私模式变化的监听。当屏幕前台有隐私窗口，则屏幕处于隐私模式，屏幕中的隐私窗口内容无法被截屏或录屏。

**起始版本：** 10

<!--Device-display-function on(type: 'privateModeChange', callback: Callback<boolean>): void--><!--Device-display-function on(type: 'privateModeChange', callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'privateModeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<boolean> = (data: boolean) => {
  console.info(`Listening enabled. Data: ${data}`);
};
try {
  // 注册隐私模式变化监听
  display.on('privateModeChange', callback);
} catch (exception) {
  console.error(`Failed to register callback. Code: ${exception.code}, message: ${exception.message}`);
}
```
