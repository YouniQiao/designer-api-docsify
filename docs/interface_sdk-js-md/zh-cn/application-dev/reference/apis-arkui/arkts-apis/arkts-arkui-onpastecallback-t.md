# OnPasteCallback

```TypeScript
declare type OnPasteCallback = (pasteValue: string, event: PasteEvent) => void
```

进行粘贴操作时，触发该回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pasteValue | string | 是 |
| event | [PasteEvent](../arkts-components/arkts-arkui-pasteevent-i.md) | 是 |
