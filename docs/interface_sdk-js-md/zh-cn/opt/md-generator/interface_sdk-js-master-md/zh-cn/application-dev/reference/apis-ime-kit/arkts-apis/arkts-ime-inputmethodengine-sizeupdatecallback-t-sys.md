# SizeUpdateCallback（系统接口）

```TypeScript
export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void
```

当输入法面板大小变化时触发的回调。

**起始版本：** 14

<!--Device-inputMethodEngine-export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void--><!--Device-inputMethodEngine-export type SizeUpdateCallback = (size: window.Size, keyboardArea: KeyboardArea) => void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | window.Size | 是 |
| keyboardArea | [KeyboardArea](arkts-ime-inputmethodengine-keyboardarea-i.md) | 是 |
