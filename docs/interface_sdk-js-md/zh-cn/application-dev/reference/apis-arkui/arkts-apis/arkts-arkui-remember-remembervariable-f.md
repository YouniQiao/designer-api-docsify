# rememberVariable

## rememberVariable

```TypeScript
export declare function rememberVariable<T>(initialValue: RememberInitialType<T>): MutableVariable<T>
```

创建状态变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| initialValue | [RememberInitialType](arkts-arkui-rememberinitialtype-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [MutableVariable](arkts-arkui-remember-mutablevariable-i.md)&lt;T&gt; |
