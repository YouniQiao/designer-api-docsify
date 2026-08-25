# animateToImmediately

## animateToImmediately

```TypeScript
export declare function animateToImmediately(value: AnimateParam, processor: VoidCallback): void
```

Define animation functions for immediate distribution. This interface depends on the UI context and cannot be used when the UI context is unclear. It is recommended to use animateToImmediately to explicitly specify the UI context.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [AnimateParam](arkts-arkui-common-animateparam-i.md) | 是 |
| processor | [VoidCallback](arkts-arkui-voidcallback-t.md) | 是 |
