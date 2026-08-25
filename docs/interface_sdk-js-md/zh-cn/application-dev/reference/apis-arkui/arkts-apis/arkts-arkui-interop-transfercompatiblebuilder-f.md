# transferCompatibleBuilder

## transferCompatibleBuilder

```TypeScript
export declare function transferCompatibleBuilder<T extends Function>(@Builder builder: T): ESValue
```

在ArkTS-Sta中给ArkTS-Dyn的@BuilderParam传递@Builder函数（适用于非字面量更新场景）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | T | 是 |

**返回值：**

| 类型 |
| --- |
| ESValue |
