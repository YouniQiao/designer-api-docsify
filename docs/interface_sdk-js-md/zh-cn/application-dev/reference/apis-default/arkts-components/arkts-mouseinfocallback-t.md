# MouseInfoCallback

```TypeScript
export type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void
```

The callback when mouse event is triggered in native embed area

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void--><!--Device-unnamed-export type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [NativeEmbedMouseInfo](arkts-web-nativeembedmouseinfo-i.md) | 是 | callback information of mouse event in native embed area. |

**示例**

完整示例代码参考[onNativeEmbedMouseEvent](./arkts-basic-components-web-events.md#onnativeembedmouseevent20)。

