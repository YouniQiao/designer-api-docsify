# OnPasteCallback

```TypeScript
export type OnPasteCallback = (content: string, event: PasteEvent) => void
```

粘贴回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | string | 是 |
| event | [PasteEvent](arkts-arkui-richeditor-pasteevent-i.md) | 是 |
