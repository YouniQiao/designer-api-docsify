# createXComponentNodeWithNativeParameters

## createXComponentNodeWithNativeParameters

```TypeScript
export function createXComponentNodeWithNativeParameters(
    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent
```

创建 XComponent 类型的 FrameNode（支持原生开发参数）

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | 是 |
| parameters | [NativeXComponentParameters](arkts-arkui-xcomponent-nativexcomponentparameters-i.md) | 是 |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) |
