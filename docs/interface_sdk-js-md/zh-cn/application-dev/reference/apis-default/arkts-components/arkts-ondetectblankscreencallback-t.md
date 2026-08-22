# OnDetectBlankScreenCallback

```TypeScript
export type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void
```

The callback when web engine detects current page is blank or nearly blank.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void--><!--Device-unnamed-export type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [BlankScreenDetectionEventInfo](arkts-web-blankscreendetectioneventinfo-i.md) | 是 | the detection event info. |

**示例**

完整示例代码参考[onDetectedBlankScreen](./arkts-basic-components-web-events.md#ondetectedblankscreen22)。

