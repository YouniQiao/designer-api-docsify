# requestAnimationFrame

## requestAnimationFrame

```TypeScript
export declare function requestAnimationFrame(handler: Function): number
```

Sets a vsync after which a function will be executed.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**模型约束：** 此接口仅可在FA模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-export declare function requestAnimationFrame(handler: Function): number--><!--Device-unnamed-export declare function requestAnimationFrame(handler: Function): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Function | 是 | Indicates the function to be called when the vsync trigger. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

