# OnVerifyPinCallback

```TypeScript
type OnVerifyPinCallback = (verifyPinEvent: VerifyPinEvent) => void
```

需要用户进行PIN码认证时触发的回调。

**起始版本：** 22

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为22。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| verifyPinEvent | [VerifyPinEvent](arkts-arkweb-verifypinevent-i.md) | 是 |
