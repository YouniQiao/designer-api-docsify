# OnMessageCallback

```TypeScript
type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void
```

当输入法框架需要显示预览文本时触发的回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputMethodEngine-type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void--><!--Device-inputMethodEngine-type OnMessageCallback = (msgId: string, msgParam?: ArrayBuffer) => void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| msgId | string | 是 |
| msgParam | ArrayBuffer | 否 |
