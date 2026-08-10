# onWaterMarkFlagChange（系统接口）

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## onWaterMarkFlagChange

```TypeScript
function onWaterMarkFlagChange(callback: Callback<boolean>): void
```

添加水印启用状态变化的监听。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-window-function onWaterMarkFlagChange(callback: Callback<boolean>): void--><!--Device-window-function onWaterMarkFlagChange(callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | 是 | 回调函数。返回当前水印的启用状态。true表示当前已启用水印；false表示当前未启用水印。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1300003 | This window manager service works abnormally. |
| 1300002 | This window state is abnormal. |
| 202 | Permission verification failed. A non-system application calls a system API. |

