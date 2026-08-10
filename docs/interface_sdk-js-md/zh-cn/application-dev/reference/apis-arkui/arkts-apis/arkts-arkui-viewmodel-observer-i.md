# observer

Defines the observer interface.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export interface observer--><!--Device-unnamed-export interface observer-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## observe

```TypeScript
observe(callback: string): void
```

Turn on the listener.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-observer-observe(callback: string): void--><!--Device-observer-observe(callback: string): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | string | 是 |  |

## unobserve

```TypeScript
unobserve(): void
```

Turn off the listener.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-observer-unobserve(): void--><!--Device-observer-unobserve(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

