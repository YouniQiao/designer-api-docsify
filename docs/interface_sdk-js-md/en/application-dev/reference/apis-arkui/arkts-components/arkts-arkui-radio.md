# Radio

单选框，提供单选类型的用户交互选择项。

> **说明：**
>
> - API version 12开始，Radio选中默认样式由RadioIndicatorType.DOT变为RadioIndicatorType.TICK。

> - 该组件默认有[margin]{@link CommonMethod#margin}间距，默认值为：{&nbsp;top: '14px',&nbsp;right: '14px',&nbsp;bottom: '14px',&
> nbsp;left: '14px' }。

## 子组件

无

## Radio

```TypeScript
Radio(options: RadioOptions)
```

创建单选框组件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RadioInterface-(options: RadioOptions): RadioAttribute--><!--Device-RadioInterface-(options: RadioOptions): RadioAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RadioOptions](../arkts-apis/arkts-arkui-radio-radiooptions-i.md) | Yes | 配置单选框的参数。 |

## Summary

- [RadioConfiguration](arkts-arkui-radio-radioconfiguration-i.md)
- [RadioOptions](arkts-arkui-radio-radiooptions-i.md)
- [RadioStyle](arkts-arkui-radio-radiostyle-i.md)
- [OnRadioChangeCallback](arkts-arkui-radio-onradiochangecallback-t.md)
- [RadioIndicatorType](arkts-arkui-radio-radioindicatortype-e.md)
