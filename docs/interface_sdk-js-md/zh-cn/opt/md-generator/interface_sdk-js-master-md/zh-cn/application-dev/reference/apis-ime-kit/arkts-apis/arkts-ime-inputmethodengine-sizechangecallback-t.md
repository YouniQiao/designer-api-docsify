# SizeChangeCallback

```TypeScript
export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void
```

当输入法面板大小变化时触发的回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputMethodEngine-export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void--><!--Device-inputMethodEngine-export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | window.Size | 是 |
| keyboardArea | [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) | 否 |
