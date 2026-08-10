# cancelAnimationFrame

## cancelAnimationFrame

```TypeScript
export declare function cancelAnimationFrame(requestId: number): void
```

Cancels the vsync callback set by "requestAnimationFrame()".

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在FA模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export declare function cancelAnimationFrame(requestId: number): void--><!--Device-unnamed-export declare function cancelAnimationFrame(requestId: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestId | number | 是 | Indicates the vsync callback ID returned by "requestAnimationFrame()". |

