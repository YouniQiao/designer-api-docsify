# KeyCommandCallback（系统接口）

```TypeScript
type KeyCommandCallback = (keyOptions: KeyOptions, keyEvent: KeyEvent) => void
```

按键命令回调函数类型，当快捷键注册条件满足时触发的回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-inputConsumer-type KeyCommandCallback = (keyOptions: KeyOptions, keyEvent: KeyEvent) => void--><!--Device-inputConsumer-type KeyCommandCallback = (keyOptions: KeyOptions, keyEvent: KeyEvent) => void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyOptions | [KeyOptions](../../apis-test-kit/arkts-apis/arkts-test-uitest-keyoptions-i.md) | 是 |
| [keyEvent](arkts-input-inputeventclient-keyeventdata-i-sys.md) | [KeyEvent](arkts-input-multimodalinput-keyevent-keyevent-i.md) | 是 |
