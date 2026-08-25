# sendControlEvent（系统接口）

## 导入模块

```TypeScript
import { onScreen } from '@kit.MultimodalAwarenessKit';
```

## sendControlEvent

```TypeScript
function sendControlEvent(event: ControlEvent): Promise<void>
```

在需要控制的窗口在桌面上时，在调用[onScreen.getPageContent](arkts-multimodalawareness-onscreen-getpagecontent-f-sys.md)后，根据其返回的段落信息，调用该接口发送屏上控制事件。

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.SIMULATE_USER_INPUT

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [ControlEvent](arkts-multimodalawareness-onscreen-controlevent-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [34000001](../errorcode-carAwareness.md#34000001-服务异常) |
| [34000005](../errorcode-onScreen.md#34000005-目标未找到) |

**示例**

ArkTS-Dyn示例:

```TypeScript
import { onScreen } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let options: onScreen.ContentOptions = {
   contentUnderstand: true,
   textOnly: true
};
let event: onScreen.ControlEvent | undefined = undefined;
try {
   onScreen.getPageContent(options).then((pageContent: onScreen.PageContent) => {
      if (pageContent.paragraphs != undefined && pageContent.paragraphs.length > 0 &&
         pageContent.paragraphs[0].hookId != undefined) {
         event = {
            windowId: pageContent.windowId,
            sessionId: pageContent.sessionId,
            hookId: pageContent.paragraphs[0].hookId,
            eventType: onScreen.EventType.SCROLL_TO_HOOK
         };
      }
   }).catch((err: BusinessError) => {
      console.error(`get page content failed, Code: ${err.code}, message: ${err.message}`);
   });
} catch (err) {
   console.error(`invoke failed, Code: ${err.code}, message: ${err.message}`);
}
if (event != undefined) {
   try {
      onScreen.sendControlEvent(event).catch((err: BusinessError) => {
         console.error(`send control event failed, Code: ${err.code}, message: ${err.message}`);
      })
   } catch (err) {
      console.error(`invoke failed, Code: ${err.code}, message: ${err.message}`);
   }
}
```

ArkTS-Sta示例:

```TypeScript
import { onScreen } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let controlEvent: onScreen.ControlEvent = {
   windowId:1,
   sessionId:1,
   eventType:onScreen.EventType.SCROLL_TO_HOOK,
   hookId:1
}
onScreen.sendControlEvent(controlEvent).then(() => {
   console.info("屏上感知发送成功");
});
```
