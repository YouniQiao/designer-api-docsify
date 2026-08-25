# transferCompatibleUpdatableBuilder

## transferCompatibleUpdatableBuilder

```TypeScript
export declare function transferCompatibleUpdatableBuilder<T extends Object>(
    builder: CompatibleUpdatableBuilder<T>
): ESValue
```

在ArkTS-Sta中给ArkTS-Dyn的@BuilderParam传递@Builder函数（适用于字面量更新场景）。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [CompatibleUpdatableBuilder](arkts-arkui-compatibleupdatablebuilder-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| ESValue |
