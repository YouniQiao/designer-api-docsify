# OnDetectBlankScreenCallback

```TypeScript
export type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void
```

The callback when web engine detects current page is blank or nearly blank.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [BlankScreenDetectionEventInfo](arkts-arkweb-web-blankscreendetectioneventinfo-i.md) | 是 |

**示例**

完整示例代码参考[onDetectedBlankScreen](./arkts-basic-components-web-events.md#ondetectedblankscreen22)。
